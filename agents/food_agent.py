from llm import ask_llm


def food_agent(state):

    prompt = f"""
You are a Local Food Recommendation Agent.

Recommend local food experiences.

Destination: {state['destination']}
Travelers: {state['travelers']}
Budget: INR {state['budget']}
Interests: {state['interests']}

Provide:

1. Famous local dishes.
2. Street food recommendations.
3. Local restaurant suggestions.
4. Vegetarian options.
5. Popular food areas.
6. Estimated daily food expenses.

Focus on authentic local cuisine.

Do not claim that restaurant hours or table
availability have been verified.
"""

    result = ask_llm(prompt)

    return {
        "food_recommendations": result
    }