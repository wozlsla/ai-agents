# AI-agents

- **Basic**
  - [x] First Agent
- **CREWAI**
  - [x] 뉴스 리더 에이전트
  - [x] 잡 헌터 에이전트
  - [x] 콘텐츠 파이프라인 에이전트
- **AUTOGEN**
  - [x] (이메일 최적화 에이전트)
  - [x] Grok 딥 리서치 클론
- **OpenAI SDK**
  - [x] ChatGPT 클론
  - [x] 고객 지원 에이전트
- **Google ADK**
  - [ ] 투자 전략 에이전트
  - [ ] 유튜브 쇼츠 메이커 에이전트
- **LangGraph**
  - [ ] 유튜브 썸네일 크리에이터 에이전트
  - [ ] AI 튜터 에이전트

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

##

Nomad Coders, [AI Agents 마스터클래스](https://nomadcoders.co/ai-agents-masterclass "AI Agents 마스터클래스")

<br>

**Learn**

- Autogen

  - group chat

- OpenAI SDK

  - agents, runner, stream event, memory, schema
  - tools, vector store, multi-modal(image), MCP
  - context management, dynamic instructions, guardrails, handoffs, hooks, voice agent

<br>

**Docs**

[CrewAI Agents](https://docs.crewai.com/ko/concepts/agents)  
[Streamlit](https://docs.streamlit.io)  
[OpenAI Agents SDK](https://openai.github.io/openai-agents-python)

[Serper](https://serper.dev)  
[Firecrawl](https://docs.firecrawl.dev/introduction)
