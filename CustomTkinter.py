import math

import customtkinter as ctk

root = ctk.CTk()
root.geometry("470x470")
root.title("Learning Custom Tkinter")
root.resizable(False, False)

heading = ctk.CTkLabel(root, text="This is our practice Arena", font=("Arial", 30, "bold"), pady=20)
heading.pack()

list_button = ["Create new Account / Register", "Sign in"]

gender_variable = ctk.StringVar(value="none selected")

gender_frame = ctk.CTkFrame(root, fg_color="transparent")
male = ctk.CTkRadioButton(gender_frame, text="Male", value="Male", variable=gender_variable, state="normal")
female = ctk.CTkRadioButton(gender_frame, text="Female", value="Female", variable=gender_variable, state="normal")

Age = 25


def segment(value):
    if value == list_button[1]:
        gender_variable.set("none selected")
        male.configure(state="disabled")
        female.configure(state="disabled")
        age_label.configure(text="")
        age_slider.configure(state="disabled")
    else:
        male.configure(state="normal")
        female.configure(state="normal")
        age_label.configure(text=f"Age {Age}")
        age_slider.configure(state="normal")


controls = ctk.CTkSegmentedButton(root, values=list_button, command=segment)
controls.pack(pady=8)
# controls.set(list_button[0])

fill_frame = ctk.CTkFrame(root)
fill_frame.pack(pady=30)

name_label = ctk.CTkLabel(fill_frame, text="Enter name :", pady=5).grid(row=0, column=0, padx=5)
name_entry = ctk.CTkEntry(fill_frame, placeholder_text="Name")
name_entry.grid(row=0, column=1, pady=5)

email_label = ctk.CTkLabel(fill_frame, text="Enter Email :", pady=5).grid(row=1, column=0, padx=5)
email_entry = ctk.CTkEntry(fill_frame, placeholder_text="Email")
email_entry.grid(row=1, column=1, pady=5)

password_label = ctk.CTkLabel(fill_frame, text="Enter Password :", pady=5).grid(row=2, column=0, padx=5)
password_entry = ctk.CTkEntry(fill_frame, placeholder_text="Password")
password_entry.grid(row=2, column=1, pady=5)

age_label = ctk.CTkLabel(root, text=f"Age :{Age}")
age_label.pack()


def showAge(value):
    global Age
    Age = math.floor(value)
    age_label.configure(text=f"Age :{Age}")


age_slider = ctk.CTkSlider(root, from_=18, to=90, command=lambda value: showAge(value))
age_slider.set(25)
age_slider.pack()
gender_frame.pack(pady="15")

male.pack(side="left", padx=5)
female.pack()


def display():
    if len(name_entry.get()) > 0 and len(email_entry.get()) > 0 and len(password_entry.get()) > 0:
        print(f"Welcome {name_entry.get()}")
        print(gender_variable.get())
    else:
        print("All fields required")


clickMeButton = ctk.CTkButton(root, text="Submit", command=lambda: display(), width=70)
clickMeButton.pack(pady=25)

root.mainloop()
