#Create a dictionary of five countries and their capitals.
#Add a new country to the dictionary.
#Update the capital of one country.
#Delete one country.
#Check if a country exists using the in operator.
#Write a program that hashes the numbers [11, 23, 35, 47, 59] using number % 10 and prints the resulting table.

countries = {
    "USA": "Washington D.C.",
    "Canada": "Ottawa",
    "UK": "London",
    "France": "Paris",
    "Japan": "Tokyo"
}

print(countries)

countries["Pakistan"] = "Islamabad"

countries["Canada"]= "Ottawa City"

del countries["Canada"]

print(countries)


table_size = 10

numbers = [11, 23, 35, 47, 59]

for num in numbers:
    index = num % table_size
    print(f"{num} goes to index {index}")




print("---------------------")

table_size = 10

hash_table = [[] for _ in range(table_size)]

numbers = [11, 23, 35, 47, 59]

for num in numbers:
    index = num % table_size
    hash_table[index].append(num)

print(hash_table)

print("---------------------")

table_size = 10
hash_table = [None] * table_size

numbers = [15, 25, 35]

for num in numbers:
    index = num % table_size

    while hash_table[index] is not None:
        index = (index + 1) % table_size

    hash_table[index] = num

print(hash_table)

print("-----------------------")




# Train Reservation System
# - Reserve a seat for a passenger.
# - Cancel an existing reservation.
# - Search passenger records efficiently.
# - Automatically add passengers to the waiting list if all seats are occupied.
# - Automatically assign a freed seat to the first passenger in the waiting list.
# - Prevent duplicate reservations for the same passenger.

from collections import deque


class TrainReservationSystem:

    def __init__(self, total_seats):

        self.available_seats = deque(range(1, total_seats + 1))

        self.reserved_seats = {}      

        self.passengers = {}          

        self.registered_ids = set()   

        self.waiting_list = deque()


    def reserve(self, passenger_id, name):

        if passenger_id in self.registered_ids:
            print("Passenger already has a reservation or is waiting.")
            return

        self.registered_ids.add(passenger_id)

        if self.available_seats:

            seat = self.available_seats.popleft()

            self.reserved_seats[seat] = passenger_id

            self.passengers[passenger_id] = name

            print(f"{name} reserved Seat {seat}")

        else:

            self.waiting_list.append((passenger_id, name))

            print(f"No seat available.")
            print(f"{name} added to waiting list.")

    def cancel(self, passenger_id):

        seat_found = None

        for seat, pid in self.reserved_seats.items():

            if pid == passenger_id:
                seat_found = seat
                break

        if seat_found is None:
            print("Reservation not found.")
            return

        passenger_name = self.passengers[passenger_id]

        del self.reserved_seats[seat_found]
        del self.passengers[passenger_id]
        self.registered_ids.remove(passenger_id)

        print(f"{passenger_name}'s reservation cancelled.")

        # Give seat to first waiting passenger
        if self.waiting_list:

            new_id, new_name = self.waiting_list.popleft()

            self.reserved_seats[seat_found] = new_id
            self.passengers[new_id] = new_name

            print(f"{new_name} moved from waiting list to Seat {seat_found}")

        else:

            self.available_seats.appendleft(seat_found)


    def search(self, passenger_id):

        if passenger_id not in self.passengers:
            print("Passenger not found.")
            return

        for seat, pid in self.reserved_seats.items():

            if pid == passenger_id:

                print(f"""
Passenger Found

Name : {self.passengers[passenger_id]}
ID   : {passenger_id}
Seat : {seat}
""")
                return


    def display(self):

        print("\nReserved Seats")

        for seat in sorted(self.reserved_seats):
            pid = self.reserved_seats[seat]
            print(f"Seat {seat} -> {self.passengers[pid]}")

        print("\nWaiting List")

        for pid, name in self.waiting_list:
            print(name)

        print("-" * 30)




train = TrainReservationSystem(3)

train.reserve(101, "Ali")
train.reserve(102, "Sara")
train.reserve(103, "Ahmed")

# Train Full
train.reserve(104, "Hamza")
train.reserve(105, "Ayesha")

train.display()

train.cancel(102)

train.display()

train.search(104)        