import keyboard
import tkinter as tk

root = tk.Tk()
root.geometry("380x670")
root.title("Calculator")
root.resizable(False, False)

textFrame = tk.Frame(root)
textFrame.pack(fill="x")

t = tk.Frame(textFrame)
t.pack(fill="x")
text_field = tk.Label(t, text="0", height=5, font=("Arial", 20, "bold"))
text_field.pack(side="right")

text_field_result = tk.Label(textFrame, text="0", font=("Arial", 50, "bold"))
text_field_result.pack(side="right")

main_frame = tk.Frame(root)
main_frame.pack(pady=10)

operands = []
operators = []
current_value = ""


def appendToField(value):
    global current_value
    if len(text_field["text"]) == 1 and text_field["text"] == "0":
        text_field.config(text=str(value))
    else:
        text_field.config(text=text_field["text"] + str(value))

    current_value += str(value)


counter = 9
width = 13
height = 5
span_width = 26

for i in range(0, 5):
    for j in range(0, 3):
        if counter >= 0:
            button = tk.Button(main_frame, text=f"{counter}", font=("Arial", 16),
                               command=lambda b=counter: appendToField(b), width=width,
                               height=height)
            button.grid(row=i, column=j)
            counter -= 1
    if counter < 0:
        break


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
        result = float(operands[index]) + float(operands[index + 1])

    else:
        result = float(operands[index]) - float(operands[index + 1])

    string_result = str(result)

    if len(operators) == 1:
        current_value = string_result
        text_field.config(text=string_result)
        text_field_result.config(text=string_result)
        operators.clear()
        operands.clear()

    else:
        operands[index] = string_result
        operands.remove(index+1)
        operators.remove(index)


def getText(value):
    global current_value
    if value == "Clear":
        text_field.config(text="0")
        current_value = ""

    elif value == "=":
        if len(operands) > 0 and len(operators) > 0 and current_value != "":
            operands.append(current_value)
            print(operands)
            print(operators)
            calculate()
        else:
            return
    else:
        return


def operation(value):
    global current_value
    if current_value == "":
        return

    elif len(operators) > 0 and operators[len(operators) - 1] == value and current_value == "":
        return

    else:
        operands.append(current_value)
        operators.append(value)
        appendToField(value)
        current_value = ""


clear = tk.Button(main_frame, text="Clear", font=("Arial", 16), command=lambda: getText(clear["text"]), width=span_width,
                  height=height, padx=3)
clear.grid(row=3, column=1, columnspan=2)

plus = tk.Button(main_frame, text="+", font=("Arial", 16), command=lambda: operation(plus["text"]), width=width,
                 height=height)
plus.grid(row=4, column=0)

equal = tk.Button(main_frame, text="=", font=("Arial", 16), command=lambda: getText(equal["text"]), width=span_width,
                  height=height, padx=3)
equal.grid(row=4, column=1, columnspan=2)


def func(event):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for i in range(0, len(numbers)):
        if numbers[i] == event.char:
            appendToField(numbers[i])
            break


root.bind("<Key>", func)

root.mainloop()
