import math

import keyboard
from tkinter import PhotoImage
import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x760")
root.title("Calculator")
icon = PhotoImage(file="calculator.png")
root.iconphoto(False, icon)
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
    string_result = str(math.floor(result * 100000) / 100000)

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


# function for Clear and Equal button
def clearEqual(value):
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
            calculate()
    else:
        return


# function for the operators
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


# clear button [ Clear ]
clear = ctk.CTkButton(main_frame, text="Clear", font=("Arial", 16), fg_color="red", corner_radius=0,
                      command=lambda: clearEqual(clear.cget("text")),
                      width=span_width,
                      height=height)
clear.grid(row=3, column=1, padx=1, columnspan=2)

# the equal button [ = ]
equal = ctk.CTkButton(main_frame, text="=", font=("Arial", 16), fg_color="green", corner_radius=0,
                      command=lambda: clearEqual(equal.cget("text")), width=span_width, height=height)
equal.grid(row=4, column=1, padx=1, columnspan=2)


# function for the dot button
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


# the dot button [ . ]
dot = ctk.CTkButton(main_frame, text=".", font=("Arial", 45), fg_color="orange", corner_radius=0,
                    command=lambda: dotOperator(dot.cget("text")), width=width,
                    height=height)
dot.grid(row=4, column=0, pady=1)

# operator buttons [ / x + ]
operations = ["/", "x", "+", "-"]
for operation_index in range(len(operations) - 1):
    button = ctk.CTkButton(main_frame, text=operations[operation_index], font=("Arial", 16),
                           corner_radius=0,
                           command=lambda op=operations[operation_index]: operation(op), width=width,
                           height=height).grid(row=5, column=operation_index, pady=1)
# the subtraction button [ - ]
subtract = ctk.CTkButton(main_frame, text="-", font=("Arial", 16), corner_radius=0,
                         command=lambda: operation(subtract.cget("text")), width=width,
                         height=height)
subtract.grid(row=6, column=0, pady=1)

isTrig = True


# switch between trig and inverse trig
def trigSwitcher(value):
    global isTrig
    if value == "Trig":
        isTrig = True
        trig_sin.configure(text="Sin")
        trig_cos.configure(text="Cos")
        trig_tan.configure(text="Tan")
    else:
        isTrig = False
        trig_sin.configure(text="aSin")
        trig_cos.configure(text="aCos")
        trig_tan.configure(text="aTan")


# trig calculations
def TrigCalc(trig_operation):
    number = math.radians(float(current_value))
    if trig_operation == "Sin":
        result = (math.floor(math.sin(number) * 10)) / 10
        print(result)
        text_field_result.configure(text=str(result))
    elif trig_operation == "Cos":
        result = (math.floor(math.cos(number) * 10)) / 10
        text_field_result.configure(text=str(result))
    else:
        result = (math.floor(math.tan(number) * 10)) / 10
        text_field_result.configure(text=str(result))


# inverse trig calculations
def TrigInverseCalc(trig_operation):
    number = float(current_value)
    if trig_operation == "aSin":
        result = (math.floor(math.degrees(math.asin(number)) * 10)) / 10
        text_field_result.configure(text=str(result))
        pass
    elif trig_operation == "aCos":
        print(math.floor(math.degrees(math.acos(number)) * 10) / 10)
        result = math.floor(math.degrees(math.acos(number)) * 10) / 10
        text_field_result.configure(text=str(result))
        pass
    else:
        result = (math.floor(math.degrees(math.atan(number)) * 10)) / 10
        text_field_result.configure(text=str(result))
        pass


# function determines where to execute TrigCalc() or TrigInverseCalc()
def trigOperation(trig_operation):
    if current_value == "" or len(operators) > 0 or len(operands) > 0:
        return

    if isTrig:
        TrigCalc(trig_operation)
    else:
        TrigInverseCalc(trig_operation)


# switch between normal trig sin cos tan and inverse trig sin inverse etc ...
trig = ctk.CTkButton(main_frame, text="Trig", font=("Arial", 16), fg_color="gray", corner_radius=0,
                     command=lambda: trigSwitcher(trig.cget("text")), width=width,
                     height=height)
trig.grid(row=6, column=1, pady=1)
trig_inverse = ctk.CTkButton(main_frame, text="Trig Inverse", font=("Arial", 16), fg_color="transparent",
                             corner_radius=0,
                             command=lambda: trigSwitcher(trig_inverse.cget("text")), width=width,
                             height=height)
trig_inverse.grid(row=6, column=2, pady=1)

# trigonometry operator buttons
trig_sin = ctk.CTkButton(main_frame, text="Sin", font=("Arial", 16), fg_color="purple", corner_radius=0,
                         command=lambda: trigOperation(trig_sin.cget("text")), width=width,
                         height=height)
trig_sin.grid(row=7, column=0, pady=1)

trig_cos = ctk.CTkButton(main_frame, text="Cos", font=("Arial", 16), fg_color="purple", corner_radius=0,
                         command=lambda: trigOperation(trig_cos.cget("text")), width=width,
                         height=height)
trig_cos.grid(row=7, column=1, pady=1)

trig_tan = ctk.CTkButton(main_frame, text="Tan", font=("Arial", 16), fg_color="purple", corner_radius=0,
                         command=lambda: trigOperation(trig_tan.cget("text")), width=width,
                         height=height)
trig_tan.grid(row=7, column=2, pady=1)


def delete():
    global current_value
    if current_value != "":
        current_value = current_value[0:len(current_value) - 1]
        text_field.configure(text=text_field.cget("text")[0:len(text_field.cget("text")) - 1])
        if len(text_field.cget("text")) == 0:
            text_field.configure(text="0")
    elif len(operators) > 0:
        text_field.configure(text=text_field.cget("text")[0:len(text_field.cget("text")) - 1])
        operators.remove(operators[len(operators) - 1])
        current_value = operands[len(operands) - 1]
        operands.remove(operands[len(operands) - 1])
    else:
        return

    # keyboard input for 0-9 and .


def func(event):
    if event.char == "d":
        delete()

    if event.char == "/" or event.char == "x" or event.char == "-" or event.char == "+":
        operation(event.char)

    else:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "x", "+", "-"]
        for i in range(0, len(numbers)):
            if numbers[i] == "." and event.char == ".":
                dotOperator(numbers[i])
            else:
                if numbers[i] == event.char:
                    appendToField(numbers[i])
                    break


root.bind("<Key>", func)

root.mainloop()
