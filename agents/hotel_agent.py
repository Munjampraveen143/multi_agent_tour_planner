from llm import ask_llm


def hotel_agent(state):

    prompt = f"""
    You are a Hotel Recommendation Agent.

    Recommend suitable accommodation options.

    Destination: {state['destination']}
    Travelers: {state['travelers']}
    Duration: {state['days']} days
    Total budget: INR {state['budget']}

    Provide:

    1. Budget accommodation suggestions.
    2. Mid-range accommodation suggestions.
    3. Premium accommodation suggestions.
    4. Recommended areas to stay.
    5. Estimated accommodation cost per night.
    6. Best option for this budget.

    Consider the entire trip budget.

    These are AI-generated suggestions.
    Do not claim that hotel availability or reservations
    have been verified.
    Clearly label estimated costs.
    """

    result = ask_llm(prompt)

    return {
        "hotel_recommendations": result
    }