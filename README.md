# AI Agents

- **Basic**
  - [x] First Agent
- **CREWAI**
  - [x] 뉴스 리더 에이전트
  - [x] 잡 헌터 에이전트
  - [x] 콘텐츠 파이프라인 에이전트
- **AUTOGEN**
  - [x] (이메일 최적화 에이전트)
  - [x] Grok 딥 리서치 클론
- **OpenAI Agents SDK**
  - [x] ChatGPT 클론
  - [x] 고객 지원 에이전트
- **Google ADK**
  - [x] 투자 전략 에이전트
  - [ ] 유튜브 쇼츠 메이커 에이전트
- **LangGraph**
  - [x] 유튜브 썸네일 크리에이터 에이전트
  - [ ] AI 튜터 에이전트  
</br>  

>[!IMPORTANT]  
> [Workflow Architectures](https://github.com/wozlsla/ai-agents/tree/main/workflow-architectures)

<br>

## Setup

Uses **`uv`** for Python environment & package management.

```
$ brew install uv
```

<br>

**1. Initialize a new agent**

```
$ uv init first-agent
```

<br>

**2. Sync dependencies**

check files: `.python-version`, `pyproject.toml`

```
$ cd first-agent
$ uv sync
```

<br>

## Notes

### Learned

- AUTOGEN

  - group chat

- OpenAI Agents SDK

  - agents, runner, stream event, memory, schema
  - tools, vector store, multi-modal(image), MCP
  - context management, dynamic instructions, guardrails, handoffs, hooks, voice agent

- Google ADK

  - agent, subagents, state, artifacts
  - workflow agents

- LangGraph

  - graph, state, nodes, edges
  - multiple schemas, reducer functions, node caching
  - conditional edge, send api, command(handoff)
  - tools, memory, human feedback, tracing(langsmith)  
  </br>
  
  - testing agents

<br>

### Docs

[CrewAI Agents](https://docs.crewai.com/ko/concepts/agents)  
[OpenAI Agents SDK](https://openai.github.io/openai-agents-python)  
[Google ADK](https://github.com/google/adk-python?tab=readme-ov-file)

[Streamlit](https://docs.streamlit.io)  
[Serper](https://serper.dev)  
[Firecrawl](https://docs.firecrawl.dev/introduction)  
[Yahoo Finance's API](https://github.com/ranaroussi/yfinance)

<br>

---

Nomad Coders, [AI Agents 마스터클래스](https://nomadcoders.co/ai-agents-masterclass "AI Agents 마스터클래스")
