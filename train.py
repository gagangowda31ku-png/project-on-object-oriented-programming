class Passenger:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age


class Train:
    def __init__(self, train_no, train_name, total_seats):
        self.train_no = train_no
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats


class Ticket:
    def __init__(self, pnr, passenger, train):
        self.pnr = pnr
        self.passenger = passenger
        self.train = train

    def display_ticket(self):
        print("\n========== TICKET ==========")
        print("PNR Number :", self.pnr)
        print("Passenger  :", self.passenger.name)
        print("Age        :", self.passenger.age)
        print("Train No   :", self.train.train_no)
        print("Train Name :", self.train.train_name)
        print("============================")


class Reservation:
    pnr_counter = 1001

    def __init__(self):
        self.bookings = {}

    def book_ticket(self, passenger, train):
        if train.available_seats > 0:
            pnr = Reservation.pnr_counter
            Reservation.pnr_counter += 1

            ticket = Ticket(pnr, passenger, train)

            self.bookings[pnr] = ticket
            train.available_seats -= 1

            print("\nTicket Booked Successfully!")
            ticket.display_ticket()

        else:
            print("\nNo Seats Available!")

    def cancel_ticket(self, pnr):
        if pnr in self.bookings:
            ticket = self.bookings[pnr]

            ticket.train.available_seats += 1

            del self.bookings[pnr]

            print("\nTicket Cancelled Successfully!")
        else:
            print("\nInvalid PNR Number!")

    def show_bookings(self):
        if not self.bookings:
            print("\nNo Reservations Found.")
        else:
            print("\nCurrent Reservations")
            for ticket in self.bookings.values():
                ticket.display_ticket()


# Main Program

train = Train(16535, "Gol Gumbaz Express", 5)

reservation = Reservation()

while True:
    print("\n===== Railway Reservation System =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Reservations")
    print("4. Train Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = input("Passenger ID: ")
        name = input("Passenger Name: ")
        age = int(input("Passenger Age: "))

        passenger = Passenger(pid, name, age)

        reservation.book_ticket(passenger, train)

    elif choice == 2:
        pnr = int(input("Enter PNR Number: "))
        reservation.cancel_ticket(pnr)

    elif choice == 3:
        reservation.show_bookings()

    elif choice == 4:
        print("\nTrain Number :", train.train_no)
        print("Train Name   :", train.train_name)
        print("Available Seats :", train.available_seats)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")