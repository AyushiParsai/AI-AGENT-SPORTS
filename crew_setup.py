from crewai import Crew
from tasks import planning_task, analysis_task, strategy_task, summary_task
from agents import planner_agent, analysis_agent, strategy_agent, summary_agent


sports_crew = Crew(
    agents=[
        planner_agent,
        analysis_agent,
        strategy_agent,
        summary_agent
    ],

    tasks=[
        planning_task,
        analysis_task,
        strategy_task,
        summary_task
    ],

    verbose=True
)