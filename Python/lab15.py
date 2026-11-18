students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:
    print("\n" + "=" * 55)
    print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 55)

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\n--- Enrolled Student Records ---")

        for roll, student in students.items():
            print(
                f"Roll No: {roll} | Name: {student['Name']} "
                f"| Branch: {student['Branch']} "
                f"| Sem: {student['Semester']} "
                f"| Marks: {student['Marks']}"
            )

        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)

        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print("Name     :", student["Name"])
            print("Branch   :", student["Branch"])
            print("Semester :", student["Semester"])
            print("Marks    :", student["Marks"])
        else:
            print("[ERROR] Student record not found.")

    elif choice == "3":
        print("\n--- Register New Student ---")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("[ERROR] Roll Number already exists.")
            continue

        name = input("Enter Student Name: ")
        branch = input("Enter Branch (e.g. BCA AI): ")
        semester = input("Enter Semester: ")

        marks = []

        print("Enter marks obtained in 3 subjects:")

        valid = True

        for i in range(1, 4):
            mark = int(input(f"  Subject {i}: "))

            if mark < 0 or mark > 100:
                print("[ERROR] Marks must be between 0 and 100.")
                valid = False
                break

            marks.append(mark)

        if valid:
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        student = students.get(roll)

        if student:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print("1. Branch:", student["Branch"],
                  "| 2. Semester:", student["Semester"])

            field = input("Choose field to update (1 for Branch, 2 for Semester): ")

            if field == "1":
                new_branch = input("Enter new branch: ")
                student["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")

            elif field == "2":
                new_semester = input("Enter new semester: ")
                student["Semester"] = new_semester
                print(f"[SUCCESS] Semester updated to '{new_semester}'.")

            else:
                print("[ERROR] Invalid field choice.")

        else:
            print("[ERROR] Student record not found.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)

        if student:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])

            result = "PASS" if all(mark >= 40 for mark in student["Marks"]) else "FAIL"

            print("\n" + "=" * 50)
            print("             ACADEMIC REPORT")
            print("=" * 50)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print("Subject Marks:", student["Marks"])
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print("Final Result :", result)
            print("=" * 50)

        else:
            print("[ERROR] Student record not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        student = students.pop(roll, None)

        if student:
            print(f"\n[SUCCESS] Record for '{student['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print("[ERROR] Student record not found.")

    elif choice == "7":
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice. Please enter a number from 1 to 7.")