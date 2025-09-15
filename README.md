# AI-agents

- **Basic**
  - [x] First Agent
- **CREWAI**
  - [x] 뉴스 리더 에이전트
  - [x] 잡 헌터 에이전트
  - [ ] 콘텐츠 파이프라인 에이전트
- **AUTOGEN**
  - [ ] Grok 답 리서치 클론
- **OpenAI SDK**
  - [ ] ChatGPT 클론
  - [ ] 고객 지원 에이전트
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
