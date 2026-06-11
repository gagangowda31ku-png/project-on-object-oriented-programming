class Movie:
    def __init__(self, movie_id, name, price):
        self.movie_id = movie_id
        self.name = name
        self.price = price

    def display_movie(self):
        print(f"{self.movie_id}. {self.name} - ₹{self.price}")


class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name


class Ticket:
    def __init__(self, customer, movie, seats):
        self.customer = customer
        self.movie = movie
        self.seats = seats
        self.total_amount = movie.price * len(seats)

    def generate_bill(self):
        print("\n===== MOVIE TICKET =====")
        print("Customer Name :", self.customer.customer_name)
        print("Movie Name    :", self.movie.name)
        print("Seats Booked  :", ", ".join(self.seats))
        print("Ticket Price  : ₹", self.movie.price)
        print("Total Amount  : ₹", self.total_amount)
        print("========================")


class Theatre:
    def __init__(self, theatre_name):
        self.theatre_name = theatre_name
        self.movies = []
        self.available_seats = [
            "A1", "A2", "A3", "A4", "A5",
            "B1", "B2", "B3", "B4", "B5"
        ]

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nAvailable Movies")
        print("----------------")
        for movie in self.movies:
            movie.display_movie()

    def display_seats(self):
        print("\nAvailable Seats:")
        print(" ".join(self.available_seats))

    def book_seats(self, seats):
        for seat in seats:
            if seat not in self.available_seats:
                return False

        for seat in seats:
            self.available_seats.remove(seat)

        return True


# Main Program
theatre = Theatre("PVR Cinemas")

theatre.add_movie(Movie(1, "Leo", 200))
theatre.add_movie(Movie(2, "Kantara", 180))
theatre.add_movie(Movie(3, "KGF Chapter 2", 250))
theatre.add_movie(Movie(4, "Salaar", 220))

print("Welcome to", theatre.theatre_name)

customer_name = input("Enter Customer Name: ")
customer = Customer(customer_name)

theatre.display_movies()

movie_choice = int(input("\nSelect Movie ID: "))

selected_movie = None
for movie in theatre.movies:
    if movie.movie_id == movie_choice:
        selected_movie = movie
        break

if selected_movie:
    theatre.display_seats()

    seat_input = input(
        "\nEnter seat numbers separated by commas (Example: A1,A2): "
    )

    seats = [seat.strip().upper() for seat in seat_input.split(",")]

    if theatre.book_seats(seats):
        ticket = Ticket(customer, selected_movie, seats)
        ticket.generate_bill()
    else:
        print("Some selected seats are not available.")
else:
    print("Invalid Movie Selection!")