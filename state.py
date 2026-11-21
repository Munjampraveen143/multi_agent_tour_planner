from typing import TypedDict


class TravelState(TypedDict, total=False):

    destination: str
    days: int
    travelers: int
    budget: float
    interests: str
    travel_month: str

    supervisor_plan: str

    destination_recommendations: str
    hotel_recommendations: str
    food_recommendations: str
    transport_plan: str

    budget_plan: str
    final_itinerary: str

    errors: list[str]