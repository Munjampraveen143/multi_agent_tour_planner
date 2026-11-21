from llm import ask_llm


def supervisor_agent(state):

    prompt = f"""
You are the Supervisor Agent of a Multi-Agent AI Tour Planner.

Analyze the user's travel requirements and prepare
a coordination plan for the specialist agents.

TRAVEL DETAILS:

Destination: {state['destination']}
Days: {state['days']}
Travelers: {state['travelers']}
Budget: INR {state['budget']}
Interests: {state['interests']}
Travel month: {state['travel_month']}

Specialist agents:

1. Destination Agent
2. Hotel Agent
3. Food Agent
4. Transport Agent

Explain what each agent should focus on.

Make sure all recommendations consider the user's
budget, trip duration and interests.

Do not claim to have checked live prices or bookings.
"""

    result = ask_llm(prompt)

    return {
        "supervisor_plan": result
    }