# Jevaughn Morris
# Assignment 6 Course Selection
# COP2500
# July 26, 2022

# create list for courses

course_code = []

#print the content needed after each course is added

print("Welcome to class registration!")

course1 = input("Enter a course code:\n")

while (course1 != "DONE"):

    course_code.append(course1)

    print("You have registered in the following courses:")

    for num in range(len(course_code)):
        print(str(num+1) + "." + course_code[num])

#Delete a course if more than 6 are entered

    if(len(course_code) > 5):

        print("You have registered for too many courses. Please pick one to delete.")

        delete = int(input("What course code would you like to delete? (1-6)"))

        while (delete < 1 or delete > 6):
            delete = int(input("What course code would you like to delete? (1-6)"))

        delete = delete - 1

        course_code.pop(delete)

    course1 = input("Enter a course code:\n")

print("Goodbye")
