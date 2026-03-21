# agent.py
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os
from src.tools import weather_api
from src.tools import get_crop_price

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)

tools = [weather_api, get_crop_price]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
