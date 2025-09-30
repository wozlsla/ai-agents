## Financial Advisor Agent

`Google ADK`

> [!NOTE]  
> [Agent Development Kit (ADK)](https://google.github.io/adk-docs)  
> 에이전트 동작을 정밀하게 제어하는 동시에 정교한 멀티 에이전트 시스템을 빌드하는 프로세스를 간소화하는 오픈소스 프레임워크

<br>

<img width="630" height="588" alt="Image" src="https://github.com/user-attachments/assets/f776dfe6-9471-425e-8beb-c835f1e625d9" />

<br>

### 목표

실시간 시장 데이터와 뉴스를 종합 분석하여, 신뢰도 높은 투자 전략(매수/매도/보유)을 제시하는 전문 투자 분석 시스템을 구축합니다.

<br>

### 협업 에이전트

- **데이터 분석가 에이전트**  
  yfinance를 활용해 실시간 시세, 기업 정보, 재무 지표 등 핵심 데이터를 수집합니다.

- **뉴스 연구원 에이전트**  
  Firecrawl API로 최신 뉴스를 검색 및 스크래핑하여 시장의 전반적인 분위기와 투자 심리를 파악합니다.

- **재무 분석가 에이전트**  
  손익계산서, 대차대조표, 현금흐름표 등 기업의 재무제표를 심층 분석합니다.

- **최종 분석 및 추천**  
  3개의 에이전트 분석 결과를 종합하고 유저의 투자 성향(목표, 위험 선호도)까지 고려하여, 구체적인 목표 주가와 실행 전략을 담은 최종 투자 보고서를 생성합니다. 이 보고서는 ADK의 영속성(persistence) 기능을 통해 아티팩트로 저장됩니다.

<br>

### 구조

```
./financial-analyst
├── financial_advisor # required
│   ├── __init__.py   # "
│   └── agent.py      # "
```

```
$ uv run adk web

# or
$ source .venv/bin/activate
$ adk web
```

firecrawl

<br>

### 참고

[Google ADK](https://google.github.io/adk-docs)
