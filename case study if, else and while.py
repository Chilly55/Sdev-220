
# Header: 
# Parris Oliver 
# M02 Lab - Case Study: if...else and while
# Description:  a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
def main():
    student_records = []

    while True:
        #enter information name,gpa
        first_name = input("Enter the student's first name: ")
        if first_name == 'ZZZ':
            break
        last_name = input("Enter the student's last name (or ZZZ to quit): ")
        if last_name == 'ZZZ':
            break

        gpa = float(input("Enter the student's GPA: "))

        student_history = {'last_name': last_name, 'first_name': first_name, 'gpa': gpa}

        student_records.append(student_history)
        #checks gpa and prints what they qualify for

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"Sorry, {first_name} {last_name} has not made the Dean's List or Honor Roll.")

    #prints all info and what they qualify for
    print("\nStudent Records:")
    for student_history in student_records:
        print(f"{student_history['first_name']} {student_history['last_name']}: {student_history['gpa']}")


if __name__ == '__main__':
    main()