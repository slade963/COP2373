MAX_TICKETS = 10


def get_ticket_purchase(remaining):
    while True:
        tickets = int(input(f"How many tickets would you like to buy? (1-4): "))

        if tickets >= 1 and tickets <= 4 and tickets <= remaining:
            return tickets
        else:
            print("Invalid amount. Please enter 1-4 tickets.")


def sell_tickets():
    remaining = MAX_TICKETS
    buyers = 0

    while remaining > 0:
        tickets = get_ticket_purchase(remaining)

        remaining = remaining - tickets
        buyers = buyers + 1

        print("Purchase complete!")
        print("Tickets remaining:", remaining)

    print("All tickets have been sold!")
    print("Total number of buyers:", buyers)


sell_tickets()
