from fastapi import FastAPI
from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO

from models import ActionResponse, ObservationModel

repo_id = "Bebrus/ppo-LunarLander-v2"
filename = "ppo-LunarLander-v2.zip"

custom_objects = {
    "learning_rate": 0.0,
    "lr_schedule": lambda _: 0.0,
    "clip_range": lambda _: 0.0,
}

point = load_from_hub(repo_id, filename)
model = PPO.load(point, custom_objects=custom_objects, print_system_info=True)

app = FastAPI()


@app.post("/api/inference", response_model=ActionResponse)
async def predict(data: ObservationModel):
    prediction, _ = model.predict(data.to_numpy())
    return {"action": int(prediction)}
