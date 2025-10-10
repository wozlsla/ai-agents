import dotenv

dotenv.load_dotenv()
import re
import os
import yfinance as yf
from datetime import datetime, timedelta
from typing import List, Dict, Any

# 기존 Firecrawl 관련 코드 (현재 rate limit으로 인해 사용하지 않음)
"""
from firecrawl import FirecrawlApp, ScrapeOptions

def _firecrawl_search(query: str):
    
    # Web Search Tool.
    # Args:
    #     query: str
    #         The query to search the web for.
    # Returns
    #     A list of search results with the website content in Markdown format.
    
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    response = app.search(
        query=query,
        limit=5,
        scrape_options=ScrapeOptions(
            formats=["markdown"],
        ),
    )

    if not response.success:
        return "Error using tool."

    cleaned_chunks = []

    for result in response.data:
        # 필요한 키가 있는지 확인
        if not all(key in result for key in ["title", "url", "content"]):
            continue

        title = result["title"]
        url = result["url"]
        content = result.get("markdown") or result.get("content", "")

        markdown_text = result.get("markdown", "").strip()
        content_text = result.get("content", "").strip()
        content = markdown_text or content_text or ""

        cleaned = re.sub(r"\\+|\n+", "", content)
        cleaned = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://[^\s]+", "", cleaned)

        cleaned_result = {
            "title": title,
            "url": url,
            "markdown": cleaned,
        }

        cleaned_chunks.append(cleaned_result)

    return cleaned_chunks
"""


def web_search_tool(query: str) -> List[Dict[str, Any]]:
    """
    Web Search Tool using yfinance news API.
    Args:
        query: str
            The stock symbol to search news for (e.g. "AAPL", "MSFT")
    Returns
        A list of news results with title, url, and content.
    """
    try:
        # yfinance Ticker 객체 생성
        ticker = yf.Ticker(query)

        # 뉴스 데이터 가져오기
        news_data = ticker.news

        if not news_data:
            return []

        cleaned_chunks = []

        for news in news_data:
            # 필수 필드 확인
            if not all(key in news for key in ["title", "link"]):
                continue

            title = news["title"]
            url = news["link"]

            # 뉴스 내용 추출 (publisher, providerPublishTime 등이 있는 경우 활용)
            content_parts = []

            if "publisher" in news:
                content_parts.append(f"Publisher: {news['publisher']}")

            if "providerPublishTime" in news:
                timestamp = news["providerPublishTime"]
                date = datetime.fromtimestamp(timestamp)
                content_parts.append(f"Published: {date.strftime('%Y-%m-%d %H:%M:%S')}")

            if "type" in news:
                content_parts.append(f"Type: {news['type']}")

            content = " | ".join(content_parts)

            cleaned_result = {"title": title, "url": url, "markdown": content}

            cleaned_chunks.append(cleaned_result)

        return cleaned_chunks

    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        return []
