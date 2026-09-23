from functools import reduce

def main():
    expenses = []

    print("Monthly Expense Tracker")
    print("-----------------------")

    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ")

        if expense_type.lower() == "done":
            break

        amount = float(input("Enter expense amount: $"))

        expenses.append([expense_type, amount])

    if len(expenses) == 0:
        print("No expenses were entered.")
        return

    # Find the total expense
    total = reduce(lambda x, y: x + y[1], expenses, 0)

    # Find the highest expense
    highest = reduce(lambda x, y: y if y[1] > x[1] else x, expenses)

    # Find the lowest expense
    lowest = reduce(lambda x, y: y if y[1] < x[1] else x, expenses)

    print()
    print("Monthly Expense Summary")
    print("-----------------------")
    print("Total Expense: $" + format(total, ".2f"))
    print("Highest Expense: " + highest[0] + " - $" + format(highest[1], ".2f"))
    print("Lowest Expense: " + lowest[0] + " - $" + format(lowest[1], ".2f"))


main()