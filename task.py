import re

class Tracker:
    def __init__(self):
        self.students = []
        print("Learning progress tracker")

    def match_name(self, name):
        if re.match("^(?!['-])([a-zA-Z]+[-']?)+([a-zA-Z]+['-]?[a-zA-Z]*[\s]?)+(?<!['-])$", name):
            return True
        else:
            return False

    def match_email(self, email):
        if re.match("[\w\.\-]+@{1}\w+[.]\w+", email):
            return True
        else:
            return False

    def add_student(self):
        student_batch = []
        print("Enter student credentials or 'back' to return")
        while True:
            student_data = input().split()
            if student_data and student_data[0] == "back":
                print(f"Total {len(student_batch)} students have been added.")
                break
            elif len(student_data) > 2:
                if self.match_name(student_data[0]):
                    #print(" ".join(student_data[1:-1]), student_data, student_data[1:-1])
                    if self.match_name(" ".join(student_data[1:-1])):
                        if self.match_email(student_data[-1]):
                            student_batch.append(" ".join(student_data))
                            print("The student has been added.")
                        else:
                            print("Incorrect email.")
                    else:
                        print("Incorrect last name.")
                else:
                    print("Incorrect first name.")
            else:
                print("Incorrect credentials.")

    def menu(self):
        while True:
            users_input = input()
            if not users_input.strip():
                print("No input.")
            elif users_input == "add students":
                self.add_student()
            elif users_input == "back":
                print("Enter 'exit' to exit the program")
            elif users_input == "exit":
                print("Bye!")
                break
            else:
                print("Unknown command!")


tracker = Tracker()
tracker.menu()