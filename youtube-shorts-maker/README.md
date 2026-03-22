## Youtube Shorts Maker Agent

`Google ADK`

<br>

<img width="407" height="619" alt="Image" src="https://github.com/user-attachments/assets/bf4da40a-34e9-4894-837e-512659fbfefd" />

<br>

### 목표

주제를 입력하면 유튜브 쇼츠 영상을 자동으로 제작해 주는 시스템을 구축합니다.

<br>

### 협업 에이전트

- **데이터 분석가 에이전트**  
  yfinance를 활용해 실시간 시세, 기업 정보, 재무 지표 등 핵심 데이터를 수집합니다.

- **콘텐츠 기획 에이전트**  
   주제를 분석해 나레이션 대본, 비주얼 콘셉트, 텍스트 오버레이까지, 초 단위로 구성된 정교한 영상 시나리오를 기획합니다.

- **에셋 생성 에이전트**  
   기획된 시나리오에 맞춰, 필요한 이미지와 나레이션을 병렬로 생성합니다. 이미지 에이전트는 OpenAI의 DALL-E 모델을, 음성 에이전트는 TTS 모델을 사용합니다.

- **영상 편집 에이전트**  
   생성된 이미지와 음성 파일을 시나리오의 타임라인에 맞춰 결합한 후, FFmpeg을 통해 1080x1920 해상도의 최종 쇼츠 영상(MP4)을 완성합니다.

- **이미지 제작 에이전트**  
   프롬프트 작성 에이전트를 통해 최적화된 프롬프트를 생성한 후 GPT-Image-1 모델로 9:16 비율의 세로 이미지를 제작합니다.

- **프롬프트 작성 에이전트**  
   장면 설명을 바탕으로 이미지 생성 AI가 이해할 수 있는 최적화된 프롬프트를 작성하여 이미지 제작 에이전트에 전달합니다.

- **음성 생성 에이전트**  
   텍스트-음성 변환 스크립트를 GPT4o Mini TTS 모델로 처리하여 고품질 나레이션 오디오 파일을 생성합니다.

<br>

### 구조

```
./youtube-shorts-maker
├── youtube_shorts_maker # required
│   ├── __init__.py   # "
│   └── agent.py      # "
```

```
$ uv run adk web

# or
$ source .venv/bin/activate
$ adk web

# api (http://127.0.0.1:8000/docs)
$ adk api_server
```

<br>

### 참고

[Google ADK](https://github.com/google/adk-python?tab=readme-ov-file)

- [Artifacts](https://google.github.io/adk-docs/artifacts)
- [Workflow Agents](https://google.github.io/adk-docs/agents/workflow-agents)