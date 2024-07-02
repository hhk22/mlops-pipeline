
## DataFlow Job

- 데이터 수집 및 모델 훈련 후 배포 과정
- Path: dataflow_job/*

## Log Pipeline

- Application에서 로그를 수집해, gcs로 최종 쌓는 파이프라인
- Path: log_pipeline/*

## CICD Pipeline

- ci : black, isort, mypy, pytest 를 통한 코드 검수. 
- cd : 해당 모델을 vertext ai training job을 통해 모델을 훈련시키고 gcs에 저장. 

- ci Path: cicd_pipeline/ci_pipeline/*
- cd Path: cicd_pipeline/cd_pipeline/*

Notion

- https://www.notion.so/MLOps-a1bc4fd039ef40fa88b414772337abc2?pvs=3&qid=
