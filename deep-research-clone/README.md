## Grok Deep Research Clone

`Autogen`

<img width="630" height="588" alt="Image" src="https://github.com/user-attachments/assets/aeead274-a6da-418b-b73e-c38412577ae0" />

<br>

### 목표

복잡한 질문에 대해 여러 에이전트가 협력하여 다각도로 심층 리서치를 수행하고, 그 결과를 종합하여 Grok 모델에 버금가는 수준 높은 분석 보고서를 생성하는 멀티 에이전트 시스템을 구축합니다.

<br>

### 협업 에이전트

- **리서치 플래너 에이전트**  
  복잡한 질문을 분석하여, 8~12개의 세부적인 연구 계획으로 나누어 리서치 전략을 수립합니다.

- **검색 에이전트**  
  Firecrawl API를 사용해 뉴스, 논문, 보고서 등 15~25개의 신뢰도 높은 자료를 체계적으로 수집합니다.

- **페이지 리더 & 리서치 강화 에이전트**  
  각 자료에서 핵심 내용을 추출하는 동시에, 리서치의 빈틈이나 논리적 허점을 파악하여 보강이 필요한 부분을 제시합니다.

- **리서치 분석가 에이전트**  
  수집된 모든 정보를 종합 분석하여, 핵심 요약, 배경 분석, 미래 전망 등을 모두 담은 5,000단어 이상의 상세 보고서를 작성합니다.

- **품질 검토자 에이전트**  
  보고서의 논리적 완성도와 정보의 정확성을 최종 검수하여, Grok과 견주어도 손색없을 정도의 최종 보고서를 완성시킵니다.

<br>

### 구조

```
./deep-research-clone
├── deep-research-team.ipynb
├── email-optimizer-team.ipynb
├── main.py
├── pyproject.toml
├── report.md
└── tools.py

```

firecrawl : searching & scrapping
