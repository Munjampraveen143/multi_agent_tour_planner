from llm import ask_llm


def transport_agent(state):

    prompt = f"""
You are a Travel Transportation Planning Agent.

Destination: {state['destination']}
Travelers: {state['travelers']}
Duration: {state['days']} days
Budget: INR {state['budget']}

Recommend:

1. Airport or railway station transfers.
2. Local transportation options.
3. Public transportation.
4. Taxi and cab options.
5. Intercity travel options, if relevant.
6. Estimated transportation expenses.

Suggest practical and budget-friendly arrangements.

Do not invent live traffic conditions,
exact route distances or confirmed fares.
Clearly label estimates.
"""

    result = ask_llm(prompt)

    return {
        "transport_plan": result
    }