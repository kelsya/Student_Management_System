import json  # used for saving and loading student data to/from files in structured format

# Global dictionary to store students
students = {}
Student_Info_File = "students.json"


# Auto-save function
def auto_save():
    try:
        with open(Student_Info_File, 'w') as f: #use with for file handling, which it automatically handle file closure
            json.dump(students, f, indent=4)
        print("Records auto-saved successfully!")
    except Exception as e:
        print(f"Error auto-saving records: {e}") #will give feedback of what went wrong


# 2.1 add student
def add_student():
    try:
        print("\nAdding new student:")
        print("Note: Student ID must be exactly 10 digits (e.g., 1002371471)")

        # Student ID validation
        while True: #infinite loop, will keep on repeating until specific condition is met
            student_id = input("Enter student ID: ")
            # Remove any spaces in the ID during validation
            cleaned_id = student_id.replace(" ", "")
            if not cleaned_id.isdigit():
                print("Error: Student ID must contain only numbers")
                continue
            if len(cleaned_id) != 10:
                print("Error: Student ID must be exactly 10 digits")
                continue
            if cleaned_id in students:
                print("Error: Student ID already exists")
                continue
            student_id = cleaned_id  # Use the cleaned ID
            break

        # Name validation
        while True:
            name = input("Enter student name: ")
            # Remove extra spaces between words and at ends
            cleaned_name = " ".join(word for word in name.split() if word)
            #split breaks the string into a list of words
            #if word filters remove empty string
            #" ".join reconnects the words with a single space
            if not cleaned_name:  # Check if name is empty after cleaning
                print("Error: Name cannot be empty")
                continue
            if not all(c.isalpha() or c.isspace() or c == '-' for c in cleaned_name):
                print("Error: Name must contain only letters, spaces, and hyphens")
                continue
            if len(cleaned_name) < 2 or len(cleaned_name) > 50:
                print("Error: Name must be between 2 and 50 characters")
                continue
            name = cleaned_name.title()  # Use the cleaned name
            break

        # Age validation
        while True:
            try:
                age_input = input("Enter student age: ")
                # Remove any spaces in the age during validation
                age = int(age_input.replace(" ", ""))
                if not (16 <= age <= 80):
                    print("Error: Age must be between 16 and 80")
                    continue #will restart input process
                break #exit the loop completely when valid input is recieved
            except ValueError:
                print("Error: Please enter a valid number for age")

        # Course input with basic cleaning
        course_input = input("Enter course name: ")
        course = " ".join(word for word in course_input.split() if word)

        # GPA validation
        while True:
            try:
                gpa_input = input("Enter GPA (0.0-4.0): ")
                # Remove any spaces in the GPA during validation
                gpa = float(gpa_input.replace(" ", ""))
                if not (0.0 <= gpa <= 4.0):
                    print("Error: GPA must be between 0.0 and 4.0")
                    continue
                gpa = round(gpa, 2)
                break
            except ValueError:
                print("Error: Please enter a valid number for GPA")

        # Add student to dictionary
        students[student_id] = {        #student_id serves as a unique key
            'student_id': student_id,
            'name': name,
            'age': age,
            'course': course,
            'gpa': gpa
        }
        print("\nStudent added successfully!")

        # Auto-save after adding student
        auto_save()

    except Exception as e:
        print(f"\nError occurred: {e}")


# 2.2 update student records
def update_student():
    try:
        # Student ID validation
        while True:
            student_id = input("\nEnter student ID to update: ")
            cleaned_id = student_id.replace(" ", "")
            if cleaned_id not in students:
                print("Error: Student ID not found")
                return
            student_id = cleaned_id
            break

        update_made = False
        while True:
            print("\nUpdate Options:")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. GPA")
            print("5. Done")

            choice = input("\nEnter choice (1-5): ")

            if choice == "1":
                while True:
                    name = input("Enter new name: ")
                    cleaned_name = " ".join(word for word in name.split() if word)
                    if not cleaned_name:
                        print("Error: Name cannot be empty")
                        continue
                    if not all(c.isalpha() or c.isspace() or c == '-' for c in cleaned_name):
                        print("Error: Name must contain only letters, spaces, and hyphens")
                        continue
                    if len(cleaned_name) < 2 or len(cleaned_name) > 50:
                        print("Error: Name must be between 2 and 50 characters")
                        continue
                    students[student_id]['name'] = cleaned_name.title()
                    update_made = True
                    break

            elif choice == "2":
                while True:
                    try:
                        age_input = input("Enter new age: ")
                        age = int(age_input.replace(" ", ""))
                        if not (16 <= age <= 99):
                            print("Error: Age must be between 16 and 99")
                            continue
                        students[student_id]['age'] = age
                        update_made = True
                        break
                    except ValueError:
                        print("Error: Please enter a valid number for age")

            elif choice == "3":
                course_input = input("Enter new course: ")
                course = " ".join(word for word in course_input.split() if word)
                students[student_id]['course'] = course
                update_made = True

            elif choice == "4":
                while True:
                    try:
                        gpa_input = input("Enter new GPA: ")
                        gpa = float(gpa_input.replace(" ", ""))
                        if not (0.0 <= gpa <= 4.0):
                            print("Error: GPA must be between 0.0 and 4.0")
                            continue
                        students[student_id]['gpa'] = round(gpa, 2)
                        update_made = True
                        break
                    except ValueError:
                        print("Error: Please enter a valid number for GPA")

            elif choice == "5":
                break
            else:
                print("Invalid choice")
                continue

            print("Update successful!")

        # Auto-save if any updates were made
        if update_made:
            auto_save()

    except Exception as e:
        print(f"\nError occurred: {e}")


# 2.3 Delete exist student records
def delete_student():
    while True:
        student_id = input("\nEnter student ID to delete: ")
        cleaned_id = student_id.replace(" ", "")
        if cleaned_id not in students:
            print("Error: Student ID not found")
            return
        student_id = cleaned_id
        break

    student = students[student_id]
    print(f"\nStudent to delete:")
    print(f"Name: {student['name']}")
    print(f"Course: {student['course']}")

    confirmation = input("\nAre you sure you want to delete this student? (yes/no): ").lower()
    if confirmation == "yes":
        del students[student_id]
        print("Student deleted successfully!")
        # Auto-save after deleting student
        auto_save()
    else:
        print("Deletion cancelled.")


# 2.4 viewing all student records
def view_students():
    if not students:
        print("\nNo students found in the records.")
        return      # exits the entire function immediately

    # Sort the student by GPA
    sorted_students = sorted(students.values(), key=lambda x: x['gpa'], reverse=False)

    print("\nStudent Records:")
    print("-" * 100)
    print(f"{'ID':<12} {'Name':<20} {'Age':<6} {'Course':<45} {'GPA':<6}")
    print("-" * 100)

    for student in students.values():
        print(f"{student['student_id']:<12} {student['name']:<20} {student['age']:<6} "
              f"{student['course']:<45} {student['gpa']:<6.2f}")
    print("-" * 100)


# 2.5 saving records (kept for compatibility, now uses auto_save)
def save_records():
    auto_save()


# 2.5 loading records
def load_records():
    global students
    try:
        with open(Student_Info_File, 'r') as f:
            students = json.load(f)
        print("Records loaded successfully!")
    except FileNotFoundError:
        print("No existing records found.")
        students = {}
    except Exception as e:
        print(f"Error loading records: {e}")

def search_student():
    if not students:
        print("\nNo students found in the records.")
        return

    # Search menu
    while True:
        print("\nSearch Students By:")
        print("1. Student ID")
        print("2. Name")
        print("3. Course")
        print("4. Return to Main Menu")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":
            # Search by Student ID
            search_id = input("Enter student ID (partial or full): ").replace(" ", "")
            results = [student for student_id, student in students.items()
                       if search_id in student_id]
            #.items() returns a view of BOTH keys and values as tuples (both keys and dictionary)
            #.values() returns a view of all the VALUES in a dictionary (just dictionary)

        elif search_choice == "2":
            # Search by Name (case-insensitive, partial match)
            search_name = input("Enter student name: ").lower()
            results = [student for student in students.values()
                       if search_name in student['name'].lower()]

        elif search_choice == "3":
            # Search by Course (case-insensitive, partial match)
            search_course = input("Enter course name: ").lower()
            results = [student for student in students.values()
                       if search_course in student['course'].lower()]

        elif search_choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        # Display results
        if results:
            print("\nSearch Results:")
            print("-" * 100)
            print(f"{'ID':<12} {'Name':<20} {'Age':<6} {'Course':<45} {'GPA':<6}")
            print("-" * 100)

            for student in results:
                print(f"{student['student_id']:<12} {student['name']:<20} {student['age']:<6} "
                      f"{student['course']:<45} {student['gpa']:<6.2f}")
            print("-" * 100)
            print(f"Total Results Found: {len(results)}")
        else:
            print("No matching students found.")

def main():
    # Load existing records when the program starts
    load_records()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Search Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            save_records()
        elif choice == "6":
            load_records()
        elif choice == "7":
            search_student()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()