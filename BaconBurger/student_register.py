num_students = int(input("How many students are registering? "))
with open("reg_form.txt", "w") as file:
    for i in range(num_students):
        student_id = input(f"Enter Student ID for student {i + 1}: ")
        file.write(student_id + " ......................................\n")