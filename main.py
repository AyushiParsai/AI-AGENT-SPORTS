from crew_setup import sports_crew

topic = input("Enter your sports planning request: ")

result = sports_crew.kickoff(
    inputs={"sport_topic": topic}
)

print("\nFINAL RESULT\n")
print(result)