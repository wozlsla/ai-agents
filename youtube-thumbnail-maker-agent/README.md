## Youtube Thumbnail Maker Agent

`LangGraph`

<br>

<img width="407" height="619" alt="Image" src="https://github.com/user-attachments/assets/483f741c-4c5d-4d31-919f-70a6504bd0ae" />

<br>

### 목표

영상 파일을 분석하여 조회수를 높일 만한 썸네일 시안을 자동으로 생성한 후, 유저의 선택과 피드백을 반영한 최종본을 완성하는 시스템을 구축합니다.

<br>

### 협업 에이전트

- **오디오 추출 및 스크립트 변환 에이전트**  
  영상 파일에서 오디오를 추출한 뒤, OpenAI의 Whisper 모델을 사용해 텍스트 스크립트로 변환합니다.

- **콘텐츠 요약 에이전트**  
   긴 스크립트를 여러 부분으로 나눠 병렬로 요약하고, 그 결과들을 다시 종합하여 영상의 핵심 주제를 파악합니다.

- **썸네일 스케쳐 에이전트**  
   영상 핵심 주제를 바탕으로, 클릭을 유도할 만한 독창적인 썸네일 컨셉(시안)을 동시에 생성합니다.

- **최종 썸네일 생성 에이전트**  
   생성된 시안들을 유저에게 보여주어 직접 선택하게 하고, 피드백을 반영하여 선택된 시안을 고품질의 썸네일 이미지로 최종 완성합니다.

<br>

### 구조

```
./youtube-thumbnail-maker-agent
├── langgraph.json # for langsmith
└── graph.py
```

```
# langsmith 서버 실행
$ langgraph dev
```