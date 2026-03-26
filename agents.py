from crewai import Agent, LLM
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# define LLM with token limit
llm_model = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=500
)

planner_agent = Agent(
    role="Sports Planner",
    goal="Create structured sports training plans",
    backstory="Expert sports coach who creates training programs.",
    verbose=True,
    allow_delegation=False,
    llm=llm_model
)

analysis_agent = Agent(
    role="Sports Analyst",
    goal="Analyze sports performance and improve strategies",
    backstory="Sports data analyst with expertise in performance metrics.",
    verbose=True,
    llm=llm_model
)

strategy_agent = Agent(
    role="Strategy Expert",
    goal="Develop winning sports strategies",
    backstory="Expert in sports tactics and match strategies.",
    verbose=True,
    llm=llm_model
)

summary_agent = Agent(
    role="Report Generator",
    goal="Generate the final sports planning report",
    backstory="Combines insights into a final structured report.",
    verbose=True,
    llm=llm_model
)