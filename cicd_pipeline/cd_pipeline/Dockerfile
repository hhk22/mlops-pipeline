FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

WORKDIR /app

COPY requirements.txt ./ 
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "cicd_pipeline/cicd_pipeline/mnist_trainer.py"]