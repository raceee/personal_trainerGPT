import openai
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
import yaml

with open("config.yaml") as creds:
    keys = yaml.safe_load(creds)

###############################
### Apple Watch data parse  ###
### Goes here               ###
###############################
json_file = {'vo2': [68,29,70,68,71]}

chat_model = ChatOpenAI(openai_api_key=keys["chatgpt"])
template = f"""
I am trying to get healthier, I would like suggestions of activity that I can do based on some of the biometric data my Apple Watch is producing. Here is a json file of the health data that was produced this week:
{json_file}
"""

print(chat_model.predict(template))


