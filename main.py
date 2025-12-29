import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from bs4 import BeautifulSoup
import requests
import logging
import re
from fastmcp import FastMCP

mcp = FastMCP('Youtube Trancriber Server')
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

@mcp.tool
def get_api_transcript(url: str) -> dict:
    """
    Fetch the transcript of a YouTube video using the unofficial YouTube Transcript API.

    Args:
        url (str): The full URL of the YouTube video.

    Returns:
        dict: A dictionary containing the transcript text under the key 'transcript',
              or an error message under the key 'error'.
    """
    
    try:
        video_id = url.split("v=")[-1]
        logger.info(f"Extracted video ID: {video_id}")
        
        ytt_api = YouTubeTranscriptApi()
        transcript_obj = ytt_api.fetch(video_id, languages=['de', 'en', 'hi', 'ur'])
        transcript = " ".join(snippet.text for snippet in transcript_obj.snippets)
        
        logger.info("Transcript successfully fetched via YouTubeTranscriptApi")
        logger.debug(f"Transcript content: {transcript[:200]}...")  # log only first 200 chars
        return {"transcript": transcript}

    except TranscriptsDisabled:
        logger.warning("No captions available for this video")
        return {"error": "No captions available"}
    except Exception as e:
        logger.error(f"Error fetching transcript: {e}")
        return {"error": str(e)}
    
    
@mcp.tool
def get_tactiq_transcript(youtube_url: str) -> str:
    """
    Fetch the transcript of a YouTube video by scraping the Tactiq.io tool via Selenium.
    This serves as a fallback method when the primary API fails.

    Args:
        youtube_url (str): The full URL of the YouTube video.

    Returns:
        str: The extracted transcript text, or an error message if extraction fails.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--metrics-recording-only")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/120.0.0.0 Safari/537.36")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        logger.info("Navigating to Tactiq transcript tool")
        driver.get("https://tactiq.io/tools/youtube-transcript")

        wait = WebDriverWait(driver, 30)

        # Input YouTube URL
        input_field = wait.until(EC.presence_of_element_located((By.ID, "yt-2")))
        input_field.send_keys(youtube_url)
        logger.info(f"Entered YouTube URL: {youtube_url}")

        # Click Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='Get Video Transcript']")
        submit_button.click()
        logger.info("Submitted video URL")

        # Wait for Copy button to be clickable
        copy_btn = wait.until(EC.element_to_be_clickable((By.ID, "copy")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", copy_btn)
        logger.info("Scrolled to Copy button")

        # Click Copy button to trigger backend transcript fetch
        copy_btn.click()
        logger.info("Clicked Copy button to fetch transcript")

        # Wait for transcript to appear
        transcript_text = ""
        for attempt in range(10):
            try:
                # Look for transcript container with timestamp
                content_div = driver.find_element(By.XPATH, "//*[contains(text(), '00:00:00')]/parent::*")
                transcript_text = content_div.text.strip()
                if len(transcript_text.split('\n')) > 5:
                    logger.info("Transcript successfully extracted from timestamp container")
                    break
            except Exception:
                logger.debug(f"Attempt {attempt+1}: Transcript not ready yet")
            time.sleep(1)

        # Fallback extraction
        if not transcript_text or "No text" in transcript_text and len(transcript_text) < 50:
            logger.warning("Primary extraction failed, attempting fallback")
            elements = driver.find_elements(By.CSS_SELECTOR, "[data-astro-cid-puhxsgk4]")
            for el in elements:
                if len(el.text) > len(transcript_text):
                    transcript_text = el.text
            logger.info("Fallback extraction completed")

        logger.debug(f"Transcript preview: {transcript_text[:200]}...")
        return transcript_text

    except Exception as e:
        logger.error(f"Transcript extraction failed: {e}")
        return f"An error occurred: {e}"

    finally:
        driver.quit()
        logger.info("Driver closed")

@mcp.tool
def clean_transcript(raw_text: str) -> str:
    """
    Remove timestamp lines and inline timestamps from transcript text.
    """
    cleaned_lines = []
    for line in raw_text.splitlines():
        # Skip lines that are just timestamps
        if re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}$", line.strip()):
            continue
        # Remove inline timestamps if they appear before text
        line = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3}", "", line).strip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

if __name__ == "__main__":
    logger.info("Starting FastMCP server")
    mcp.run(transport="http", host="127.0.0.1", port=8000)
