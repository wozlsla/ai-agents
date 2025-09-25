## ChatGPT Clone

`OpenAI Agents SDK`

<img width="630" height="588" alt="Image" src="https://github.com/user-attachments/assets/50471de3-4982-46ec-a96e-a504e8d78f4a" />

<br>

### 목표

OpenAI의 Agents SDK와 Streamlit을 사용하여 한층 더 강화된 버전의 ChatGPT를 구축합니다. 이 에이전트는 웹 검색, 코드 실행, 이미지 생성 같은 핵심 기능은 물론, MCP를 통해 Yahoo Finance 데이터 조회나 환율 변환 같은 여러 외부 도구를 동시에 활용하는 강력한 기능까지 포함합니다.

<br>

### 구조

```
./chatgpt-clone
├── chat-gpt-clone-memory.db
├── facts.txt (sample)
├── international.png (sample)
├── main.py
└── pyproject.toml


# (learn openai-agents-sdk)
./chatgpt-clone
├── ai-memory.db
├── ai-memory.db-shm
├── ai-memory.db-wal
└── dummy-agent.ipynb


# Run Streamlit
$ uv run streamlit run main.py
```

<br>

### 참고

- Tracing: [Logs](https://platform.openai.com/logs)

- OpenAI Agents SDK: [Tools](https://openai.github.io/openai-agents-python/tools)
  - Hosted tools
    - WebSearchTool
    - FileSearchTool, [vector store](https://platform.openai.com/storage/vector_stores)
    - ImageGenerationTool, [create image](https://platform.openai.com/docs/api-reference/images/create)
    - HostedMCPTool, [context7](https://context7.com)
  - Local MCP Server
    - [MCP Yahoo Finance](https://github.com/leoncuhk/mcp-yahoo-finance)
    - [Time MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/time)
