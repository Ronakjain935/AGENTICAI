from textwrap import dedent
import os

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")


def build_youtube_agent():
    """
    Returns a configured YouTube Analysis Agent.
    """

    return Agent(
        name="YouTube Agent",

        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY,
        ),

        tools=[
            YouTubeTools()
        ],

        instructions=dedent("""
        You are an expert YouTube Video Analyzer.

        Analyze the video and provide:

        ## 📌 Video Overview
        - Title
        - Video Type
        - Duration (if available)

        ## 📚 Main Topics

        ## ⏱ Important Timestamps

        ## 💡 Key Learnings

        ## 🎯 Final Summary

        Rules:
        - Never hallucinate timestamps.
        - Keep answers concise.
        - Use Markdown formatting.
        """),

        markdown=True,
        add_datetime_to_context=True,
    )


# Run directly
if __name__ == "__main__":

    agent = build_youtube_agent()

    agent.print_response(
        "Analyze this video: https://www.youtube.com/watch?v=zjkBMFhNj_g",
        stream=True,
    )