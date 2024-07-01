from contextlib import asynccontextmanager

import torch
from fastapi import FastAPI
from ml_models.xor import XORModel
from models.xor import XORInput

model: XORModel = XORModel()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model.load_state_dict(torch.load("xor_model.pth"))
    model.eval()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict/")
async def predict(data: XORInput):
    inputs = torch.tensor([[data.x1, data.x2]], dtype=torch.float32)
    with torch.no_grad():
        prediction = model(inputs)
    return {"prediction": prediction.item()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
