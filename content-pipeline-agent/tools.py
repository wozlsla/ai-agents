import os, re, requests

from crewai.tools import tool


@tool
def web_search_tool(query: str) -> str:
    """
    Web Search Tool. (Firecrawl Code Snippets)
    Args:
        query: str
            The query to search the web for.
    Returns
        A list of search results with the website content in Markdown format.
    """
    url = "https://api.firecrawl.dev/v2/search"

    payload = {
        "query": query,
        "sources": ["web"],
        "categories": [],
        "limit": 5,
        "scrapeOptions": {
            "onlyMainContent": True,
            "maxAge": 172800000,
            # "parsers": ["pdf"],
            "formats": ["markdown"],
        },
    }

    headers = {
        "Authorization": f"Bearer {os.getenv('FIRECRAWL_API_KEY')}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    response = response.json()

    # 후처리
    if response["success"] is not True:
        return "Error using tool."

    cleaned_chunks = []

    for result in response["data"]["web"]:
        title = result["title"]
        url = result["url"]
        markdown = result["markdown"] if "markdown" in result else ""

        cleaned = re.sub(r"\\+|\n+", "", markdown).strip()
        cleaned = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://[^\s]+", "", cleaned)

        cleaned_result = {
            "title": title,
            "url": url,
            "markdown": cleaned,
        }

        cleaned_chunks.append(cleaned_result)

    return cleaned_chunks


# print(web_search_tool("ai engineer jobs in south korea"))
