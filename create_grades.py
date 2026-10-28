
import csv


def create_grades_file():
    # Ask how many students the instructor wants to enter.
    student_count = int(input("How many students do you want to enter? "))

    # Open the CSV file and write the header.
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "First Name",
            "Last Name",
            "Exam 1",
            "Exam 2",
            "Exam3"
        ])

        # Collect information for each student.
        for student in range(student_count):
            print(f"\nStudent {student + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            # Collect the three exam grades.
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student's information to the file.
            writer.writerow([
                first_name,
                last_name,
                exam1,
                exam2,
                exam3
            ])

    print("\nGrades saved to grades.csv successfully.")


# Run the program.
if __name__ == "__main__":
    create_grades_file()
