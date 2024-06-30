## Airflow (데이터 수집)

DataFlow(Apache-beam)를 이용해 gcs에 있는 데이터를 bigquery로 옮기는 작업.  
Airflow(gcp-composer) 에서 작업했으며, 실행파일들의 일부분을 아래 경로에 저장.
- Dags: ~/dataflow_job/dags/dataflow.py
- Scripts: ~/dataflow_job/scripts/dataflow_gcs_to_bigquery.py

## Model Piepline (모델 훈련 및 배포)

VertexAI에서 모델 훈련 및 배포하는 파이프라인 구조.  
Bigquery -> GCS -> Model Training -> Endpoint(Vertex AI) 로 이루어진 파이프라인.  
실행을 위해서는 package 설치와, 각 resource에 대한 접근권한을 가진 google credential json 파일이 필요하다. 

- Pipeline: ~/dataflow_job/VertexAI_pipeline.ipynb

