
import csv


def display_grades():
    # Open the CSV file and read its records.
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check whether the file contains data.
    if not rows:
        print("The grades.csv file is empty.")
        return

    # Calculate the width needed for each column.
    column_widths = []

    for column in range(len(rows[0])):
        width = max(len(row[column]) for row in rows)
        column_widths.append(width)

    # Display the header and student records.
    for row_number, row in enumerate(rows):
        formatted_row = " | ".join(
            row[column].ljust(column_widths[column])
            for column in range(len(row))
        )

        print(formatted_row)

        # Print a divider below the header.
        if row_number == 0:
            divider = "-+-".join(
                "-" * width for width in column_widths
            )
            print(divider)


# Run the program.
if __name__ == "__main__":
    display_grades()
