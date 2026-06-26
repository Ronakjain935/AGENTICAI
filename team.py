from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team
load_dotenv()
eng_agent=Agent(name="English Agent",role="You answer question in English")
chinese_agent=Agent(name="Chinese Agent",role="You answer question in Chinese")
hindi_agent=Agent(name="Hindi Agent",role="You answer question in Hindi")
team_leader=Team(
    name="Answer in Translation Team",
    members=[eng_agent,chinese_agent,hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must respond to answer the query in their specific language. 
                       Do not route to just one agent.
                       output the reponse of all agents"""
)
team_leader.print_response("What is the capital of India")
