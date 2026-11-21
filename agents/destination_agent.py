from llm import ask_llm


def destination_agent(state):

    prompt = f"""
You are a professional Destination Planning Agent.

Recommend tourist attractions for the user's trip.

Destination: {state['destination']}
Duration: {state['days']} days
Interests: {state['interests']}
Travel month: {state['travel_month']}

Provide:

1. Famous tourist attractions.
2. Nature and sightseeing locations.
3. Historical and cultural places.
4. Adventure activities.
5. Suggested visit duration.
6. Recommended places for each day.

Make recommendations suitable for the trip duration.

Do not invent live opening hours or ticket prices.
Clearly identify estimates.
"""

    result = ask_llm(prompt)

    return {
        "destination_recommendations": result
    }