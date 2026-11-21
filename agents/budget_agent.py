from llm import ask_llm


def budget_agent(state):

    prompt = f"""
You are an expert Travel Budget Analysis Agent.

Calculate an estimated budget for the trip.

Destination: {state['destination']}
Travelers: {state['travelers']}
Duration: {state['days']} days
Available budget: INR {state['budget']}

DESTINATION RECOMMENDATIONS:
{state['destination_recommendations']}

HOTEL RECOMMENDATIONS:
{state['hotel_recommendations']}

FOOD RECOMMENDATIONS:
{state['food_recommendations']}

TRANSPORT RECOMMENDATIONS:
{state['transport_plan']}

Prepare an expense breakdown:

1. Accommodation.
2. Food.
3. Transportation.
4. Sightseeing and activities.
5. Miscellaneous expenses.

Calculate:

- Estimated total cost.
- Cost per traveler.
- Remaining budget or budget deficit.
- Suggestions to reduce expenses.

Ensure that costs are not counted twice.
Use INR and label all figures as estimates.

Do not invent confirmed prices.
"""

    result = ask_llm(prompt)

    return {
        "budget_plan": result
    }