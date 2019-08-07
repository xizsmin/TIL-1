#### 목적
- 클릭 예측

#### 사용 데이터
- 2013년 4분기 임의의 한 주 데이터
- 온라인 학습을 위한 데이터 (상세 설명 없음)


#### 평가지표
- 정확도
  - 수익이 제일 큰 이슈
  - 하지만 영향을 끼치는 요인을 찾는게 가장 중요하기 때문에 정확도 사용
- Normalized Entropy
- Calibration
  - 예상 클릭수 대비 실제 관찰된 클릭 수 비율
  - 1에 가까울수록 좋음


#### 모델 구성
- 개요
  - Decision Tree로 입력 데이터 피쳐 생성
  - Logistic Regression으로 학습
- Decision Tree
  - feature의 변환이 주 목적
    - 일반적인 피쳐 변환 방법
      - 범주형 피쳐를 모든 조합에 대해 사용
      - 연속적인 값은 K-D 트리 사용해서 분할
        - 그냥 K차원 데이터를 축에 따라 이진 분할했다고 생각하면 됨
    - 사용한 방법
      -  피쳐를 Boosting 된 트리로 만들어서 boost 결과의 leaf 출력값을 0, 1로 만들어 피쳐 벡터 생성
        - L2 TreeBoosting 썼다는데… L2로스로 결정 트리 기반 부스팅 하는 학습법인가??
      - 각 레벨은 decision tree로 구성됨
      - 바로 로지스틱 리그레션 했을때보다 엔트로피 기준 3% 성능 향상
      - 트리만 썼을때보단  엔트로피 기준 4% 향상
      - 트리는 배치 방식으로 학습
         
- Data freshness 유지를 위한 Online linear classifier
  - 단순히 뒤쪽 lr을 온라인 러닝으로 구성한단 이야기니 패스하겠음


#### 중요 요소
- 부스팅 트리 수 결정
  - 1개~2000개로 나누어 실험
  - 부스팅 트리의 수는 500개 이상일경우 성능 향상이 없었고 1000개를 넘어가면 성능 하락이 발생하는 경우도 존재
- 중요한 피쳐?
  - 피쳐수에 따른 중요도를 봤을때 상위 10개가 50%의 중요도, 마지막 300개가 1% 정도
  - 피쳐 10개만 사용시 기준으로
    - 20개 사용시 1% 성능 향상
    - 50개 사용시 2%
    - 100개 사용시 2.5%
    - 200개 사용시 2.75%
    - 400개 사용시 3%
  - 피쳐는 공개 안한대 이씨
    - 단 Historical, Contextual 피쳐로 구분한다고 함
    - Historical 피쳐: 사용자와 광고의 이전 활동
    - Contextual 피쳐: 사용자의 기기, 사용중인 페이지 등 현재 상태
  - Historical 피쳐만 사용시 Contextual 피쳐만 사용한 경우보다 4% 가량 성능 향상
    - 전체 사용시 Contextual 피쳐보단 5%, Historical 피쳐보단 1% 향상


#### 학습 데이터 감소
- subsampling: 10% 까지 성능 유지
- negative sampling: 2.5%까지 성능 유지