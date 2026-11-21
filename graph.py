
from langgraph.graph import StateGraph, START, END

from state import TravelState

from agents.supervisor import supervisor_agent
from agents.destination_agent import destination_agent
from agents.hotel_agent import hotel_agent
from agents.food_agent import food_agent
from agents.transport_agent import transport_agent
from agents.budget_agent import budget_agent
from agents.itinerary_agent import itinerary_agent


def build_tour_graph():

    workflow = StateGraph(TravelState)

    # Register all agents
    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("destination", destination_agent)
    workflow.add_node("hotel", hotel_agent)
    workflow.add_node("food", food_agent)
    workflow.add_node("transport", transport_agent)
    workflow.add_node("budget", budget_agent)
    workflow.add_node("itinerary", itinerary_agent)

    # Starting point
    workflow.add_edge(START, "supervisor")

    # Supervisor delegates to specialist agents
    workflow.add_edge("supervisor", "destination")
    workflow.add_edge("supervisor", "hotel")
    workflow.add_edge("supervisor", "food")
    workflow.add_edge("supervisor", "transport")

    # Wait for specialist agents before budget analysis
    workflow.add_edge("destination", "budget")
    workflow.add_edge("hotel", "budget")
    workflow.add_edge("food", "budget")
    workflow.add_edge("transport", "budget")

    # Generate final itinerary
    workflow.add_edge("budget", "itinerary")

    workflow.add_edge("itinerary", END)

    return workflow.compile()


tour_graph = build_tour_graph()


def generate_tour(
    destination,
    days,
    travelers,
    budget,
    interests,
    travel_month
):

    initial_state = {
        "destination": destination,
        "days": int(days),
        "travelers": int(travelers),
        "budget": float(budget),
        "interests": interests,
        "travel_month": travel_month
    }

    result = tour_graph.invoke(initial_state)

    return result
