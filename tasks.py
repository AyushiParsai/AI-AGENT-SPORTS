from crewai import Task
from agents import planner_agent, analysis_agent, strategy_agent, summary_agent


planning_task = Task(
    description="""
    Based on the user sports request: {sport_topic}

    Create a detailed sports training plan including:
    - Training schedule
    - Fitness preparation
    - Skill development
    """,
    expected_output="Detailed sports training plan",
    agent=planner_agent
)


analysis_task = Task(
    description="""
    Analyze the training plan and identify
    improvements for better performance.
    """,
    expected_output="Performance analysis report",
    agent=analysis_agent
)


strategy_task = Task(
    description="""
Based on the training plan and performance analysis, create match-winning strategies.

Include:
1. Batting strategy
2. Bowling strategy
3. Field placement strategy
4. Powerplay strategy
5. Death overs strategy

Focus on practical cricket match tactics.
""",
    expected_output="Detailed match strategies and tactics",
    agent=strategy_agent 
)


summary_task = Task(
    description="""
    Combine planning, analysis and strategy
    into a final sports planning assistant report.
    """,
    expected_output="Final sports planning assistant report",
    agent=summary_agent
)