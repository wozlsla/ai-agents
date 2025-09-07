import time
from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

search_tool = SerperDevTool()
# search_tool = SerperDevTool(n_results=30)

# print(search_tool.run(search_query="World War 2"))


@tool
def scrape_tool(url: str):
    """
    Use this when you need to read the content of a website.
    Returns the content of a website, in case the website is not available, it returns 'No content'.
    Input should be a `url` string. for example (https://www.reuters.com/world/asia-pacific/cambodia-thailand-begin-talks-malaysia-amid-fragile-ceasefire-2025-08-04/)
    """

    print(f"Scrapping URL: {url}")

    # Playwright를 동기 모드로 초기화
    with sync_playwright() as p:

        # Chromium 브라우저를 백그라운드에서 실행
        browser = p.chromium.launch(headless=True)

        # 새 웹 페이지(탭) 열기
        page = browser.new_page()

        # 지정된 URL로 이동
        page.goto(url)

        # 페이지 로드, 5초 대기
        time.sleep(5)

        # 현재 페이지의 HTML 콘텐츠 가져오기
        html = page.content()

        # 브라우저 닫기
        browser.close()

        # HTML 콘텐츠를 BeautifulSoup으로 파싱
        soup = BeautifulSoup(html, "html.parser")

        unwanted_tags = [
            "header",
            "footer",
            "nav",
            "aside",
            "script",
            "style",
            "noscript",
            "iframe",
            "form",
            "button",
            "input",
            "select",
            "textarea",
            "img",
            "svg",
            "canvas",
            "audio",
            "video",
            "embed",
            "object",
        ]

        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        content = soup.get_text(separator=" ")

        return content if content != "" else "No content"
