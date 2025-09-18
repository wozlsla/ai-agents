## News Reader Agent

`CrewAI`

<img width="630" height="588" alt="Image" src="https://github.com/user-attachments/assets/0285d855-1ac0-448f-897a-c12e98e74601" />

<br>

### 목표

특정 뉴스 주제를 입력받아, 바로 발행 가능한 수준의 뉴스 보고서를 생성합니다.

<br>

### 협업 에이전트

- **뉴스 헌터 에이전트**  
  Google 검색과 웹사이트 스크래핑을 통해 주제와 관련된 기사를 수집합니다. 이후, 품질이 낮은 정보를 걸러내고 신뢰도와 관련성을 기준으로 각 기사에 점수를 매깁니다.

- **요약 에이전트**  
  '뉴스 헌터 에이전트'가 선별한 기사들에서 핵심 주제와 통계 데이터를 추출하여 상세 요약본을 만듭니다.

- **큐레이터 에이전트**  
  '요약 에이전트'가 만든 요약본을 바탕으로 주요 기사, 속보, 편집자 분석, 관련 읽을거리, 정확한 인용 정보를 포함한 최종 보고서를 완성합니다.

<br>

### 구조

```
./news-reader-agent
├── config
│   ├── agents.yaml
│   └── tasks.yaml
├── output
│   ├── content_harvest.md
│   ├── final_report.md
│   └── summary.md
├── main.py
└── pyproject.toml
```
