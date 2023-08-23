class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result

    def search_by_source_destination(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    flight_table = FlightTable()

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("\nMenu:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            city_code = input("Enter city code: ")
            city_name = cities.get(city_code, "Unknown")
            city_flights = flight_table.search_by_city(city_code)
            print(f"Flights for {city_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, To: {cities[flight.destination]}, Price: {flight.price}")

        elif choice == "2":
            city_code = input("Enter city code: ")
            city_name = cities.get(city_code, "Unknown")
            city_flights = flight_table.search_by_city(city_code)
            print(f"Flights from {city_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, To: {cities[flight.destination]}, Price: {flight.price}")

        elif choice == "3":
            source = input("Enter source city code: ")
            destination = input("Enter destination city code: ")
            source_name = cities.get(source, "Unknown")
            destination_name = cities.get(destination, "Unknown")
            city_flights = flight_table.search_by_source_destination(source, destination)
            print(f"Flights from {source_name} to {destination_name}:")
            for flight in city_flights:
                print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
