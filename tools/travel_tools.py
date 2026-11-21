from urllib.parse import quote


def validate_trip_details(
    destination,
    days,
    travelers,
    budget
):
    if not destination or not destination.strip():
        raise ValueError("Please enter a destination.")

    if not 1 <= int(days) <= 30:
        raise ValueError("Trip duration must be between 1 and 30 days.")

    if int(travelers) < 1:
        raise ValueError("At least one traveler is required.")

    if float(budget) <= 0:
        raise ValueError("Budget must be greater than zero.")

    return True


def create_map_link(destination):

    search = quote(destination)

    return (
        "https://www.openstreetmap.org/search"
        f"?query={search}"
    )