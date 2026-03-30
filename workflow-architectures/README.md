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
    - 각 LLM 호출을 "더 쉬운 작업"으로 만들수록, 결과물의 품질이 올라감.
    - Trade Off: 속도를 조금 희생하고, 정확도를 높인다.  

- **Examples where prompt chaining is useful**
    - 마케팅 카피 작성카피 생성 → 다른 언어로 번역
    - 문서 작성목차 작성 → gate(기준 충족 여부 검사) → 본문 작성  
    - 앞 단계의 결과가 뒷 단계의 입력이 되고, 각 단계는 한 가지 일만 한다. 

</br>

> [!NOTE]  
> LLM은 한 번에 너무 많은 걸 요구받으면 품질이 떨어짐. 반면 범위가 좁고 명확한 작업은 훨씬 잘 수행.   
이 특성을 의도적으로 활용하는 전략.

</br>

### Routing
입력을 분류(classify)하여, 그에 맞는 전문화된 후속 작업으로 연결하는 방식.
각 입력 유형마다 최적화된 프롬프트와 처리 경로를 분리할 수 있음.

- **When to use this workflow**
    - 입력의 종류가 명확히 구분되고, 각각 다르게 처리하는 것이 유리한 복잡한 작업에 적합
    - 분류(classification) 자체는 LLM이 해도 되고, 전통적인 분류 모델/알고리즘을 써도 됨
    - 하나의 프롬프트로 모든 입력을 처리하려 하면, 한 유형을 최적화할수록 다른 유형의 성능이 떨어짐

- **Examples where routing is useful**
    - 고객 서비스 쿼리 분류 → 일반 문의 / 환불 요청 / 기술 지원 각각 다른 프로세스·프롬프트·도구로 연결
    - 질문 난이도에 따라 라우팅 → 쉬운 질문은 Claude Haiku 4.5(저비용) → 어렵고 복잡한 질문은 Claude Sonnet 4.5(고성능)

</br>

> [!NOTE]  
> "모든 입력에 맞는 하나의 완벽한 프롬프트"를 만들려 하지 말 것.  
> 입력을 분류하고 경로를 나누는 것 자체가 성능과 비용 모두를 최적화하는 전략.

</br>

### Parallelization
### Orchestrator-workers
### Evaluator-optimizer