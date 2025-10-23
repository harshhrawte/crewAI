from crewai import Agent, LLM
from tools import youtube_search
import google.generativeai as genai 

llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.3,
    max_tokens=2000,
    api_key=''  
)

blog_researcher = Agent(
    role='YouTube Video Researcher',
    goal='Search for videos about {topic} and provide summaries',
    backstory=(
        "You are a YouTube content researcher. When using tools, "
        "pass simple string queries. For example: use 'AI vs ML' not complex objects."
    ),
    tools=[youtube_search],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2,
    max_execution_time=120
)


blog_writer = Agent(
    role='Content Writer',
    goal='Write blog posts about {topic} based on research',
    backstory="You write engaging blog content based on video summaries.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2,
    max_execution_time=120
)