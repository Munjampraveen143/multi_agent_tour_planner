from llm import ask_llm


def itinerary_agent(state):

    prompt = f"""
You are an Expert AI Travel Itinerary Agent.

Create a complete, personalized travel itinerary.

USER DETAILS:

Destination: {state['destination']}
Duration: {state['days']} days
Travelers: {state['travelers']}
Budget: INR {state['budget']}
Interests: {state['interests']}
Travel month: {state['travel_month']}

DESTINATION RECOMMENDATIONS:
{state['destination_recommendations']}

HOTEL RECOMMENDATIONS:
{state['hotel_recommendations']}

FOOD RECOMMENDATIONS:
{state['food_recommendations']}

TRANSPORT PLAN:
{state['transport_plan']}

BUDGET ANALYSIS:
{state['budget_plan']}

Create the final travel plan with:

1. Trip overview.
2. Day-wise itinerary.
3. Morning activities.
4. Afternoon activities.
5. Evening activities.
6. Food recommendations.
7. Accommodation suggestions.
8. Transportation suggestions.
9. Estimated total budget.
10. Important travel tips.

Keep the schedule realistic.
Avoid visiting too many distant locations on one day.
Respect the user's budget.

Use clear headings and bullet points.

Do not claim that any hotel, restaurant or activity
has been booked or verified live.
"""

    result = ask_llm(prompt)

    return {
        "final_itinerary": result
    }