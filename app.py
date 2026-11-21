
import streamlit as st

from graph import generate_tour

from tools.travel_tools import (
    validate_trip_details,
    create_map_link
)


st.set_page_config(
    page_title="Multi-Agent AI Tour Planner",
    page_icon="🌍",
    layout="wide"
)


# Application heading
st.title("🌍 Multi-Agent AI Tour Planner")

st.markdown(
    """
    Plan personalized trips using multiple AI agents,
    LangGraph and your local Ollama model.
    """
)

st.divider()


# Sidebar
st.sidebar.title("About Project")

st.sidebar.info(
    """
    AI-powered travel planning application.

    Powered by:
    - Ollama
    - Qwen 2.5
    - LangGraph
    - Python
    - Streamlit
    - OpenStreetMap
    """
)


# User input
st.header("✈️ Plan Your Trip")

with st.form("travel_form"):

    destination = st.text_input(
        "Destination",
        placeholder="Example: Kerala"
    )

    col1, col2 = st.columns(2)

    with col1:

        days = st.number_input(
            "Number of days",
            min_value=1,
            max_value=30,
            value=5
        )

        travelers = st.number_input(
            "Number of travelers",
            min_value=1,
            max_value=20,
            value=2
        )

    with col2:

        budget = st.number_input(
            "Total budget (INR)",
            min_value=1000,
            max_value=10000000,
            value=30000,
            step=1000
        )

        travel_month = st.text_input(
            "Travel month",
            placeholder="Example: December"
        )

    interests = st.multiselect(
        "Select your interests",
        [
            "Nature",
            "Beaches",
            "Adventure",
            "Historical places",
            "Shopping",
            "Food",
            "Culture",
            "Wildlife",
            "Photography"
        ],
        default=["Nature", "Food"]
    )

    submitted = st.form_submit_button(
        "🚀 Generate My Tour Plan",
        use_container_width=True
    )


# Generate travel plan
if submitted:

    try:

        validate_trip_details(
            destination,
            days,
            travelers,
            budget
        )

        if not interests:
            st.warning(
                "Please select at least one interest."
            )

        else:

            with st.spinner(
                "🤖 AI agents are working on your tour plan..."
            ):

                result = generate_tour(
                    destination=destination,
                    days=days,
                    travelers=travelers,
                    budget=budget,
                    interests=", ".join(interests),
                    travel_month=travel_month or "Not specified"
                )

            st.success(
                "Your personalized tour plan is ready!"
            )

            # Final itinerary
            st.header("🗺️ Your Complete Travel Itinerary")

            st.markdown(
                result.get(
                    "final_itinerary",
                    "No itinerary generated."
                )
            )

            st.divider()

            # Destination
            with st.expander(
                "📍 Destination Agent Results"
            ):
                st.markdown(
                    result.get(
                        "destination_recommendations",
                        "No results."
                    )
                )

            # Hotels
            with st.expander(
                "🏨 Hotel Agent Results"
            ):
                st.markdown(
                    result.get(
                        "hotel_recommendations",
                        "No results."
                    )
                )

            # Food
            with st.expander(
                "🍽️ Food Agent Results"
            ):
                st.markdown(
                    result.get(
                        "food_recommendations",
                        "No results."
                    )
                )

            # Transport
            with st.expander(
                "🚗 Transport Agent Results"
            ):
                st.markdown(
                    result.get(
                        "transport_plan",
                        "No results."
                    )
                )

            # Budget
            with st.expander(
                "💰 Budget Agent Results"
            ):
                st.markdown(
                    result.get(
                        "budget_plan",
                        "No results."
                    )
                )

            # Supervisor
            with st.expander(
                "🧠 Supervisor Agent Results"
            ):
                st.markdown(
                    result.get(
                        "supervisor_plan",
                        "No results."
                    )
                )

            # Map
            st.divider()

            st.subheader("🗺️ Explore Your Destination")

            map_link = create_map_link(destination)

            st.markdown(
                f"[Open {destination} in OpenStreetMap]({map_link})"
            )

    except ValueError as error:

        st.error(str(error))

    except Exception as error:

        st.error(
            "Unable to generate your tour plan. "
            "Check that Ollama is running and the model is available."
        )

        with st.expander("Technical error details"):
            st.exception(error)
