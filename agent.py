from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()
def build_agent():
    return Agent(
         model=Groq(id="llama-3.3-70b-versatile"),
         tools=[DuckDuckGoTools()],
         markdown=True,
         instructions="You are a helpful and expert travel agent",
         add_datetime_to_context=True
    )
groq_agent= build_agent()
groq_agent.print_response("Is is save to travel UAE today? ")
