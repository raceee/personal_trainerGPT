from fastapi import FastAPI
import openai
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import yaml

app = FastAPI()

with open("config.yaml") as creds:
    keys = yaml.safe_load(creds)

class JsonIn(BaseModel):
    data: str

class PredictionOut(BaseModel):
    text: str

@app.get("/")
def home_page():
    return {"home_check": "OK", "home_type":"manual_uploads"}

@app.post("/send", response_model=PredictionOut)
def send(health_payload: JsonIn):
    text = chat_gpt(health_payload.data)
    print(text)
    return {"text":text}

def chat_gpt(text_input):
    chat_model = ChatOpenAI(openai_api_key=keys["chatgpt"])
    template = f"""
    I am trying to get healthier, I would like suggestions of activity that I can do based on some of the biometric data my Apple Watch is producing. Here is a json file of the health data that was produced this week:
    {text_input}
    """
    return chat_model.predict(template)
