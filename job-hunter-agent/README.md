## Job Hunter Agent

`CrewAI`

<img width="407" height="619" alt="Image" src="https://github.com/user-attachments/assets/e9e26876-cdaa-408b-8fa3-5c6676834bca" />

<br>

### 목표

유저의 이력서와 목표 직무 정보를 바탕으로 채용 공고 검색부터 면접 준비까지, 구직의 전 과정을 자동화하여 최적의 입사 지원 자료를 제공합니다.

<br>

### 협업 에이전트

- **채용 공고 검색 에이전트**  
  주요 채용 사이트를 스크래핑하여 유저의 조건에 맞는 채용 공고를 찾습니다.

- **직무 매칭 에이전트**  
  검색된 공고들을 유저의 경력 및 기술과 비교 분석하여 직무 적합도에 따라 점수를 매깁니다.

- **이력서 최적화 에이전트**  
  가장 적합하다고 판단되는 직무에 맞춰 이력서 내용을 수정 및 최적화합니다.

- **기업 조사 에이전트**  
  목표 기업에 대한 심층 조사를 통해 전략적인 정보를 수집합니다.

- **면접 준비 에이전트**  
  수집된 정보를 바탕으로 예상 면접 질문과 학습 계획 등 종합적인 면접 대비 자료를 생성합니다.

<br>

### 구조

```
./job-hunter-agent
├── config
│   ├── agents.yaml
│   └── tasks.yaml
├── knowledge
│   └── resume.txt
├── output
│   ├── company_research.md
│   ├── interview_prep.md
│   └── rewritten_resume.md
├── main.py
├── models.py
├── pyproject.toml
└── tools.py
```

firecrawl : searching & scrapping
