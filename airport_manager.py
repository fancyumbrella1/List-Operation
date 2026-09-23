"""Airport data and operations for the list exercise."""

airport_info = ("OUL", 1, "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki", "departure": "08:30", "gate": "A2",
        "capacity": 5, "passengers": ["Alice Wong", "David Kim", "Fatima Ali"],
    },
    "SK271": {
        "destination": "Stockholm", "departure": "10:15", "gate": "B1",
        "capacity": 4, "passengers": ["Chen Wei", "George Smith"],
    },
    "LH2491": {
        "destination": "Munich", "departure": "12:40", "gate": "A4",
        "capacity": 5, "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"],
    },
}


def find_flight(flights, flight_number):
    requested = flight_number.strip().casefold()
    for key in flights:
        if key.casefold() == requested:
            return key
    return None


def passenger_exists(passengers, passenger_name):
    requested = passenger_name.strip().casefold()
    for name in passengers:
        if name.strip().casefold() == requested:
            return True
    return False


def check_in_passenger(flights, flight_number, passenger_name, restricted_destinations):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"
    name = passenger_name.strip()
    if not name:
        return "EMPTY_NAME"
    flight = flights[key]
    if flight["destination"].casefold() in {
        destination.casefold() for destination in restricted_destinations
    }:
        return "RESTRICTED"
    if passenger_exists(flight["passengers"], name):
        return "DUPLICATE"
    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"
    flight["passengers"].append(name.title())
    return "OK"


def remove_passenger(flights, flight_number, passenger_name):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"
    for name in flights[key]["passengers"]:
        if name.strip().casefold() == passenger_name.strip().casefold():
            flights[key]["passengers"].remove(name)
            return "OK"
    return "PASSENGER_NOT_FOUND"


def change_gate(flights, flight_number, new_gate, allowed_gates):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"
    requested = new_gate.strip().casefold()
    for gate in allowed_gates:
        if gate.casefold() == requested:
            flights[key]["gate"] = gate
            return "OK"
    return "INVALID_GATE"


def flight_status(flight):
    count = len(flight["passengers"])
    capacity = flight["capacity"]
    if count >= capacity:
        return "FULL"
    if count / capacity >= 0.75:
        return "ALMOST FULL"
    return "AVAILABLE"


def sorted_manifest(flights, flight_number):
    key = find_flight(flights, flight_number)
    if key is None:
        return None
    return sorted(flights[key]["passengers"])


def total_passengers(flights):
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total


def any_full_flight(flights):
    return any(flight_status(flight) == "FULL" for flight in flights.values())


def all_flights_have_passengers(flights):
    return all(len(flight["passengers"]) > 0 for flight in flights.values())
