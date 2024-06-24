1. 전체적인 파이프라인 그림

2. Spec

3. Issues

4. TroubleShooting

5. References


## Airflow (데이터 수집)
DataFlow(Apache-beam)를 이용해 gcs에 있는 데이터를 bigquery로 옮기는 작업.  
Airflow(gcp-composer) 에서 작업했으며, 실행파일들의 일부분을 아래 경로에 저장.
- Dags: ~/dags/dataflow.py
- Scripts: ~/scripts/dataflow_gcs_to_bigquery.py

## Model Piepline (모델 훈련 및 배포)



