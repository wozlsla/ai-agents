# Workflow Architectures 
`LangGraph`  
</br> 

Engineering at Anthropic, **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents "blogpost")**  

> **Workflows**: LLM과 도구들이 미리 정해진 코드 경로를 따라 움직이는 시스템  
**Agents**: LLM이 스스로 판단하며 프로세스와 도구 사용을 동적으로 결정하는 시스템  

</br>

## Workflow
### Prompt Chaining
하나의 큰 작업을 여러 단계로 쪼개서, 각 LLM 호출이 이전 결과를 받아 처리하는 방식.  
중간에 게이트(gate) 를 두어 "지금 방향이 맞는가?" 를 프로그래밍적으로 검증 가능.

- **When to use this workflow**
    - 작업이 고정된 하위 단계로 깔끔하게 분리되는 경우에 가장 적합
    - 각 LLM 호출을 '더 쉬운 작업'으로 만들수록, 결과물의 품질이 올라감.
    - Trade Off: 속도를 조금 희생하고, 정확도를 높인다.  

- Examples where prompt chaining is useful:
    - 마케팅 카피 작성카피 생성 → 다른 언어로 번역
    - 문서 작성목차 작성 → gate(기준 충족 여부 검사) → 본문 작성  
    - 앞 단계의 결과가 뒷 단계의 입력이 되고, 각 단계는 한 가지 일만 한다. 

</br>

> [!NOTE]  
> LLM은 한 번에 너무 많은 걸 요구받으면 품질이 떨어짐. 반면 범위가 좁고 명확한 작업은 훨씬 잘 수행.   
이 특성을 의도적으로 활용하는 전략.

</br>

### Routing
### Parallelization
### Orchestrator-workers
### Evaluator-optimizer