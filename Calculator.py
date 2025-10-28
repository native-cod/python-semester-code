import keyboard
import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x760")
root.title("Calculator")
root.iconbitmap("calculator.ico")
root.resizable(False, False)

# main text container
textFrame = ctk.CTkFrame(root)
textFrame.pack(fill="x")

operand_frame = ctk.CTkFrame(textFrame, fg_color="transparent")
operand_frame.pack(fill="x")
text_field = ctk.CTkLabel(operand_frame, text="0", font=("Arial", 30), height=70)
text_field.pack(side="right", padx=5)

text_field_result = ctk.CTkLabel(textFrame, text="0", font=("Arial", 70, "bold"), height=110)
text_field_result.pack(side="right")

main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.pack(pady=10)

# main variables
operands = []
operators = []
current_value = ""
hasDot = False

counter = 9
width = 100
height = 65
span_width = 200

for i in range(0, 5):
    for j in range(0, 3):
        if counter >= 0:
            button = ctk.CTkButton(main_frame, text=f"{counter}", fg_color="transparent", font=("Arial", 16),
                                   command=lambda b=counter: appendToField(b), width=width,
                                   height=height, corner_radius=0)
            button.grid(row=i, column=j, pady=1, padx=1)
            counter -= 1
    if counter < 0:
        break


def appendToField(value):
    global current_value
    if len(text_field.cget("text")) == 1 and text_field.cget("text") == "0":
        text_field.configure(text=str(value))
    else:
        text_field.configure(text=text_field.cget("text") + str(value))

    current_value += str(value)


# main program function
def calculate():
    found = False
    while len(operators) > 0:
        order = ["/", "x", "+", "-"]
        for x in range(0, len(order)):
            for y in range(0, len(operators)):
                if order[x] == operators[y]:
                    calcHelper(operators[y], y)
                    found = True
                    break
            if found:
                found = False
                break


def calcHelper(active_operation, index):
    global current_value
    result = 0

    if active_operation == "/":
        result = float(operands[index]) / float(operands[index + 1])

    elif active_operation == "x":
        result = float(operands[index]) * float(operands[index + 1])

    elif active_operation == "+":
        print(operands)
        result = float(operands[index]) + float(operands[index + 1])

    else:
        result = float(operands[index]) - float(operands[index + 1])

    print(result)
    string_result = str(result)

    if len(operators) == 1:
        current_value = string_result
        text_field.configure(text=string_result)
        text_field_result.configure(text=string_result)
        operators.clear()
        operands.clear()

    else:
        operands[index] = string_result
        operands.remove(operands[index + 1])
        operators.remove(operators[index])


def getText(value):
    global current_value, hasDot
    if value == "Clear":
        text_field.configure(text="0")
        current_value = ""
        operands.clear()
        operators.clear()
        text_field_result.configure(text="0")
        hasDot = False

    elif value == "=":
        if len(operands) > 0 and len(operators) > 0 and current_value != "":
            operands.append(current_value)
            # print(operands)
            # print(operators)
            calculate()
        else:
            return
    else:
        return


def operation(value):
    global current_value, hasDot
    if current_value == "":
        return
    elif len(operators) > 0 and operators[len(operators) - 1] == value and current_value == "":
        return

    else:
        operands.append(current_value)
        operators.append(value)
        appendToField(value)
        current_value = ""
        hasDot = False


clear = ctk.CTkButton(main_frame, text="Clear", font=("Arial", 16), fg_color="red", corner_radius=0,
                      command=lambda: getText(clear.cget("text")),
                      width=span_width,
                      height=height)
clear.grid(row=3, column=1, padx=1, columnspan=2)


# change to .
def dotOperator(value):
    global hasDot, current_value
    if current_value == "":
        return
    elif hasDot:
        return
    else:
        hasDot = True
        current_value += value
        text_field.configure(text=text_field.cget("text") + value)


dot = ctk.CTkButton(main_frame, text=".", font=("Arial", 45), fg_color="orange", corner_radius=0,
                    command=lambda: dotOperator(dot.cget("text")), width=width,
                    height=height)
dot.grid(row=4, column=0, pady=1)

equal = ctk.CTkButton(main_frame, text="=", font=("Arial", 16), fg_color="green", corner_radius=0,
                      command=lambda: getText(equal.cget("text")), width=span_width, height=height)
equal.grid(row=4, column=1, padx=1, columnspan=2)

operations = ["/", "x", "+", "-"]
for operation_index in range(len(operations) - 1):
    button = ctk.CTkButton(main_frame, text=operations[operation_index], font=("Arial", 16),
                           corner_radius=0,
                           command=lambda op=operations[operation_index]: operation(op), width=width,
                           height=height).grid(row=5, column=operation_index, pady=1)

subtract = ctk.CTkButton(main_frame, text="-", font=("Arial", 16),  corner_radius=0,
                         command=lambda: operation(subtract.cget("text")), width=width,
                         height=height)
subtract.grid(row=6, column=0, pady=1)


# keyboard input for 0-9 and .
def func(event):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for i in range(0, len(numbers)):
        if numbers[i] == "." and event.char == ".":
            dotOperator(numbers[i])
        else:
            if numbers[i] == event.char:
                appendToField(numbers[i])
                break


root.bind("<Key>", func)

root.mainloop()
