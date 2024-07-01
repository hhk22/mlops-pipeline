import torch
import torch.nn as nn
import torch.optim as optim
from ml_models.xor import XORModel

if __name__ == "__main__":
    X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
    Y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

    model = XORModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)

    for epoch in range(1000):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, Y)
        loss.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print(f"Epoch [{epoch+1}/1000] Loss: {loss.item():.4f}")

    model_name = "xor_model.pth"
    torch.save(model.state_dict(), model_name)
    print(f"Model saved to {model_name}")
