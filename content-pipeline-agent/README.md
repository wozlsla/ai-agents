## Job Hunter Agent

`CrewAI`

<img width="630" height="588" alt="Image" src="https://github.com/user-attachments/assets/7a37c2fe-bd1e-4d21-88db-41f623523133" />

<br>

### 목표

특정 주제와 콘텐츠 유형(블로그, 트윗 등)을 입력받아, 여러 플랫폼에 최적화된 콘텐츠를 자동으로 생성합니다.

<br>

### 협업 에이전트

- **리서치 크루**  
  웹 검색과 전문가 분석을 통해 주제에 대한 구조화된 정보를 수집하여 콘텐츠 제작의 기반을 마련합니다.

- **작가 에이전트**  
  '리서치 크루'가 수집한 정보를 바탕으로 콘텐츠 초안을 작성합니다.

- **SEO 및 바이럴 평가 에이전트**  
  작성된 초안을 분석하여 검색 결과 상위 노출(SEO)과 콘텐츠 확산을 극대화하도록 최적화합니다. 최종적으로 성과 분석 리포트와 함께 바로 게시 가능한 완성본을 전달합니다.

<br>

### 구조

```
./content-pipeline-agent
├── crewai_flow.html
├── main.py
├── pyproject.toml
├── seo_crew.py
├── tools.py
└── virality_crew.py
```

firecrawl : searching & scrapping
