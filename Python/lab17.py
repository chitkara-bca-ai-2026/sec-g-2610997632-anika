def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}%")


def add_student(records, roll, name, marks):
    if roll in records:
        print("[ERROR] Roll Number already exists.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]}
}

while True:
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    if choice == "1":
        print("\n--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print("Total Students:", len(students))

    elif choice == "2":
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks = []
        print("Enter marks for 3 subjects:")
        for i in range(3):
            mark = int(input(f"Subject {i+1}: "))
            marks.append(mark)

        add_student(students, roll, name, marks)

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            print("\n[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":
        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter 1-4.")