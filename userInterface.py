import tkinter as tk

root = tk.Tk()
root.geometry("700x500")
root.title("GUI PYCHARM")

form_title = tk.Label(root, text="Log in Form", font=("Arial", 40), pady=30)
form_title.pack()

frame = tk.Frame(root)
frame.pack()
#
# tk.Label(frame, text="User name :", font=("Arial", 14)).grid(row=0, column=0)
# tk.Entry(frame).grid(row=0, column=1)
# # text_label.pack()
#
#
# tk.Label(frame, text="Password :", font=("Arial", 14)).grid(row=1, column=0)
# tk.Entry(frame).grid(row=1, column=1)
# # clicked = False
#
# tk.Button(frame, text="Submit").grid(row=2, column=1)

# def display(clicked):
#     if clicked:
#         text_label.config(text="Button unClicked")
#         clicked = False
#     else:
#         text_label.config(text="Button Clicked")
#         clicked = True


left_frame = tk.Frame(frame, height=100)
left_frame.pack(side="left")

name_label = tk.Label(left_frame, text="User name :", font=("Arial", 14))
passcode_label = tk.Label(left_frame, text="Password :", font=("Arial", 14))
name_label.pack()
passcode_label.pack()

right_frame = tk.Frame(frame, height=100)
right_frame.pack()

name = tk.Entry(right_frame)
passcode = tk.Entry(right_frame)
name.pack()
passcode.pack()


def getName():
    if len(name.get()) > 0 and len(passcode.get()) > 0:
        print(f"{name.get()} {passcode.get()}")
    else:
        return


button = tk.Button(root, text="Submit", command=getName)
button.pack()

root.mainloop()
