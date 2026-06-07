
import tkinter as tk
from tkinter import messagebox

# =========================
# STUDENT CLASS
# =========================

class Student:

    def __init__(self, name, roll, marks, fees_paid):

        self.name = name
        self.roll = roll
        self.marks = marks
        self.fees_paid = fees_paid

    def percentage(self):

        return self.marks

    def grade(self):

        if self.marks >= 90:
            return "Grade A"

        elif self.marks >= 75:
            return "Grade B"

        elif self.marks >= 60:
            return "Grade C"

        elif self.marks >= 50:
            return "Grade D"

        else:
            return "Fail"

    def remaining_fees(self):

        total_fees = 10000

        return total_fees - self.fees_paid


# =========================
# FILE NAME
# =========================

FILE_NAME = "student.txt"


# =========================
# ADD STUDENT
# =========================

def add_student():

    name = name_entry.get()
    roll = roll_entry.get()

    try:
        marks = int(marks_entry.get())
        fees_paid = int(fees_entry.get())

    except:
        messagebox.showerror("Error", "Marks and Fees must be numbers")
        return

    file = open(FILE_NAME, "a")

    file.write(
        name + "," +
        roll + "," +
        str(marks) + "," +
        str(fees_paid) +
        "\n"
    )

    file.close()

    messagebox.showinfo("Success", "Student Added Successfully")

    clear_fields()


# =========================
# SHOW STUDENTS
# =========================

def show_students():

    output_text.delete(1.0, tk.END)

    try:

        file = open(FILE_NAME, "r")

        data = file.readlines()

        file.close()

        if len(data) == 0:

            output_text.insert(tk.END, "No Student Found")

        else:

            for line in data:

                if line.strip() == "":
                    continue

                student_data = line.strip().split(",")

                name = student_data[0]
                roll = student_data[1]
                marks = int(student_data[2])
                fees_paid = int(student_data[3])

                s = Student(name, roll, marks, fees_paid)

                output_text.insert(
                    tk.END,
                    f"\nName : {s.name}\n"
                    f"Roll : {s.roll}\n"
                    f"Marks : {s.marks}\n"
                    f"Percentage : {s.percentage()}%\n"
                    f"Grade : {s.grade()}\n"
                    f"Fees Paid : {s.fees_paid}\n"
                    f"Remaining Fees : {s.remaining_fees()}\n"
                    f"-----------------------------\n"
                )

    except:
        output_text.insert(tk.END, "File Not Found")


# =========================
# SEARCH STUDENT
# =========================

def search_student():

    output_text.delete(1.0, tk.END)

    roll_search = roll_entry.get()

    found = False

    try:

        file = open(FILE_NAME, "r")

        data = file.readlines()

        file.close()

        for line in data:

            student_data = line.strip().split(",")

            name = student_data[0]
            roll = student_data[1]
            marks = int(student_data[2])
            fees_paid = int(student_data[3])

            if roll == roll_search:

                s = Student(name, roll, marks, fees_paid)

                output_text.insert(
                    tk.END,
                    f"\nStudent Found\n\n"
                    f"Name : {s.name}\n"
                    f"Roll : {s.roll}\n"
                    f"Marks : {s.marks}\n"
                    f"Percentage : {s.percentage()}%\n"
                    f"Grade : {s.grade()}\n"
                    f"Fees Paid : {s.fees_paid}\n"
                    f"Remaining Fees : {s.remaining_fees()}\n"
                )

                found = True

                break

        if found == False:

            output_text.insert(tk.END, "Student Not Found")

    except:

        output_text.insert(tk.END, "File Not Found")


# =========================
# DELETE STUDENT
# =========================

def delete_student():

    roll_delete = roll_entry.get()

    found = False

    try:

        file = open(FILE_NAME, "r")

        data = file.readlines()

        file.close()

        file = open(FILE_NAME, "w")

        for line in data:

            student_data = line.strip().split(",")

            roll = student_data[1]

            if roll != roll_delete:

                file.write(line)

            else:
                found = True

        file.close()

        if found:

            messagebox.showinfo(
                "Success",
                "Student Deleted Successfully"
            )

        else:

            messagebox.showerror(
                "Error",
                "Student Not Found"
            )

    except:

        messagebox.showerror(
            "Error",
            "File Not Found"
        )


# =========================
# CLEAR FIELDS
# =========================

def clear_fields():

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title("Student Management System")

root.geometry("1000x700")

root.config(bg="#1e1e2f")


# =========================
# TITLE
# =========================

title = tk.Label(

    root,

    text="STUDENT MANAGEMENT SYSTEM",

    font=("Arial", 24, "bold"),

    bg="#1e1e2f",

    fg="cyan"

)

title.pack(pady=20)


# =========================
# INPUT FRAME
# =========================

input_frame = tk.Frame(

    root,

    bg="#2c2c3e",

    bd=5,

    relief=tk.RIDGE

)

input_frame.pack(pady=10)


# =========================
# NAME
# =========================

name_label = tk.Label(

    input_frame,

    text="Name",

    font=("Arial", 14, "bold"),

    bg="#2c2c3e",

    fg="white"

)

name_label.grid(row=0, column=0, padx=20, pady=15)

name_entry = tk.Entry(

    input_frame,

    font=("Arial", 14),

    width=25

)

name_entry.grid(row=0, column=1, pady=15)


# =========================
# ROLL
# =========================

roll_label = tk.Label(

    input_frame,

    text="Roll Number",

    font=("Arial", 14, "bold"),

    bg="#2c2c3e",

    fg="white"

)

roll_label.grid(row=1, column=0, padx=20, pady=15)

roll_entry = tk.Entry(

    input_frame,

    font=("Arial", 14),

    width=25

)

roll_entry.grid(row=1, column=1, pady=15)


# =========================
# MARKS
# =========================

marks_label = tk.Label(

    input_frame,

    text="Marks",

    font=("Arial", 14, "bold"),

    bg="#2c2c3e",

    fg="white"

)

marks_label.grid(row=2, column=0, padx=20, pady=15)

marks_entry = tk.Entry(

    input_frame,

    font=("Arial", 14),

    width=25

)

marks_entry.grid(row=2, column=1, pady=15)


# =========================
# FEES
# =========================

fees_label = tk.Label(

    input_frame,

    text="Fees Paid",

    font=("Arial", 14, "bold"),

    bg="#2c2c3e",

    fg="white"

)

fees_label.grid(row=3, column=0, padx=20, pady=15)

fees_entry = tk.Entry(

    input_frame,

    font=("Arial", 14),

    width=25

)

fees_entry.grid(row=3, column=1, pady=15)


# =========================
# BUTTON FRAME
# =========================

button_frame = tk.Frame(

    root,

    bg="#1e1e2f"

)

button_frame.pack(pady=20)


button_style = {

    "font": ("Arial", 12, "bold"),

    "width": 16,

    "height": 2,

    "bd": 0
}


# ADD BUTTON

add_btn = tk.Button(

    button_frame,

    text="Add Student",

    bg="#00c853",

    fg="white",

    command=add_student,

    **button_style

)

add_btn.grid(row=0, column=0, padx=10, pady=10)


# SHOW BUTTON

show_btn = tk.Button(

    button_frame,

    text="Show Students",

    bg="#2962ff",

    fg="white",

    command=show_students,

    **button_style

)

show_btn.grid(row=0, column=1, padx=10, pady=10)


# SEARCH BUTTON

search_btn = tk.Button(

    button_frame,

    text="Search Student",

    bg="#ff6d00",

    fg="white",

    command=search_student,

    **button_style

)

search_btn.grid(row=0, column=2, padx=10, pady=10)


# DELETE BUTTON

delete_btn = tk.Button(

    button_frame,

    text="Delete Student",

    bg="#d50000",

    fg="white",

    command=delete_student,

    **button_style

)

delete_btn.grid(row=0, column=3, padx=10, pady=10)


# CLEAR BUTTON

clear_btn = tk.Button(

    button_frame,

    text="Clear",

    bg="#9c27b0",

    fg="white",

    command=clear_fields,

    **button_style

)

clear_btn.grid(row=0, column=4, padx=10, pady=10)


# =========================
# OUTPUT TEXT AREA
# =========================

output_text = tk.Text(

    root,

    width=110,

    height=20,

    font=("Consolas", 12),

    bg="#121212",

    fg="lime",

    bd=5

)

output_text.pack(pady=20)


# =========================
# RUN WINDOW
# =========================

root.mainloop()

