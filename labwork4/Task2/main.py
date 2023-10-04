from random import randint


class Ticket:
    ticket_id = 0

    def __init__(self, price, ticket_type):
        Ticket.ticket_id += 1
        self.ticket_type = ticket_type
        self.ticket_number = f"T-{Ticket.ticket_id:04d}"
        self.price = price

    def print_ticket(self):
        print("=============================")
        print("Ticket Number:", self.ticket_number)
        print("Ticket Type:", self.ticket_type)
        print("Price:", self.price)
        print("=============================")


class RegularTicket(Ticket):
    def __init__(self, price):
        ticket_type = "Regular ticket (Not discount or increase)"
        super().__init__(price, ticket_type)


class EarlyTicket(Ticket):
    def __init__(self, price):
        discounted_price = price * 0.7  # 30% discount
        ticket_type = "Early ticket (30% discount)"
        super().__init__(discounted_price, ticket_type)


class StudentTicket(Ticket):
    def __init__(self, price):
        discounted_price = price * 0.5  # 50% discount
        ticket_type = "Student ticket (50% discount)"
        super().__init__(discounted_price, ticket_type)


class LastMinuteTicket(Ticket):
    def __init__(self, price):
        increased_price = price * 1.2  # 20% increase
        ticket_type = "Last minute ticket (20% increase)"
        super().__init__(increased_price, ticket_type)


class TicketSystem:
    def __init__(self):
        self.tickets = []

    def order_ticket(self, ticket_type):
        price = randint(100, 500)  # generate random price
        if ticket_type == "1":
            ticket = RegularTicket(price)
        elif ticket_type == "2":
            ticket = EarlyTicket(price)
        elif ticket_type == "3":
            ticket = StudentTicket(price)
        elif ticket_type == "4":
            ticket = LastMinuteTicket(price)
        else:
            print("Invalid ticket type")
            return

        self.tickets.append(ticket)
        print("Ticket ordered successfully!")
        ticket.print_ticket()

    def search_ticket(self, number):
        for ticket in self.tickets:
            if ticket.ticket_number == number:
                ticket.print_ticket()
                return
        print("Ticket not found")


def main():
    tickets_system = TicketSystem()

    while True:
        print("\n1. Order a ticket")
        print("2. Search for a ticket")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\t1. Regular Ticket")
            print("\t2. Early Ticket")
            print("\t3. Student Ticket")
            print("\t4. Last Minute Ticket")

            ticket_type = input("Enter ticket type: ")
            tickets_system.order_ticket(ticket_type)

        elif choice == "2":
            number = (input("Enter ticket number: "))
            tickets_system.search_ticket(number)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
