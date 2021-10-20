from tkinter import *
from tkinter import font
import math
from fractions import Fraction

expression = ""


def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)


def clear_input_field(equation):
    global expression
    expression = ""
    equation.set(expression)


def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = equation.get()
    except ZeroDivisionError:
        equation.set("Cannot be divided by zero")
        expression = ""
    except SyntaxError:
        equation.set("Invalid Input/Operation")
        expression = ""


def back(equation):
    global expression
    if len(expression) > 0:
        result = expression[:-1]
        equation.set(result)
        expression = equation.get()
    else:
        expression = ""


def sin(equation):
    global expression
    try:
        result = math.sin(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def cos(equation):
    global expression
    try:
        result = math.cos(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def tan(equation):
    global expression
    try:
        result = math.tan(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def sinh(equation):
    global expression
    try:
        result = math.sinh(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def cosh(equation):
    global expression
    try:
        result = math.cosh(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def tanh(equation):
    global expression
    try:
        result = math.tanh(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter a value first")
        expression = ""


def log(equation):
    global expression
    try:
        result = math.log(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Cannot find log of blank/negative numbers")
        expression = ""


def log2(equation):
    global expression
    try:
        result = math.log2(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Cannot find log2 of blank/negative numbers")
        expression = ""


def log10(equation):
    global expression
    try:
        result = math.log10(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Cannot find log10 of blank/negative numbers")
        expression = ""


def factorial(equation):
    global expression
    try:
        result = str(math.factorial(int(expression)))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Cannot find factorial of blank/negative integers")
        expression = ""


def reciprocal(equation):
    global expression
    try:
        result = 1/float(expression)
        equation.set(result)
        expression = equation.get()
    except ZeroDivisionError:
        equation.set("Cannot divide by 0")
        expression = ""
    except ValueError:
        equation.set("Enter a value first to find the reciprocal")
        expression = ""


def root(equation):
    global expression
    try:
        result = math.sqrt(float(expression))
        equation.set(result)
    except ValueError:
        equation.set("Please enter a positive number")
        expression = ""


def exponential(equation):
    global expression
    try:
        result = math.exp(float(expression))
        equation.set(result)
        expression = equation.get()
    except ValueError:
        equation.set("Enter value before finding exponential")
        expression = ""


def degree2fraction(equation):
    global expression
    result = Fraction(expression)
    equation.set(result)
    expression = equation.get()


def radian(equation):
    global expression
    result = math.radians(float(expression))
    equation.set(result)
    expression = equation.get()


def degree(equation):
    global expression
    result = math.degrees(float(expression))
    equation.set(result)
    expression = equation.get()

# creating the GUI


def main():
    window = Tk()
    window.title("Sci-Calc")
    window.iconbitmap(
        "C:\\Users\\varma\\Desktop\\py Programs\\tkinter\\calculator\\calc.ico")
    window.geometry("560x300")
    # window.resizable(width=0, height=0)   # Make window fixed/unresizable
    n_rows = 6
    n_columns = 8
    for i in range(n_rows):
        window.grid_rowconfigure(i,  weight=1)
    for i in range(n_columns):
        window.grid_columnconfigure(i,  weight=1)

    button_font = font.Font(family='Verdana', weight=font.BOLD)

    equation = StringVar()

    input_field = Entry(window, textvariable=equation,
                        relief=RIDGE, bd=10, font=("Verdana", 20))
    # NSEW: stretch items inside a grid in all 4 directions
    input_field.grid(row=0, columnspan=8, ipadx=15, ipady=15, sticky=NSEW)
    equation.set("Enter the expression")

    sin_button = Button(window, text="sin", fg="white", bg="green", command=lambda: sin(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    sin_button.grid(row=1, column=0, sticky=NSEW)
    cos_button = Button(window, text="cos", fg="white", bg="green", command=lambda: cos(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    cos_button.grid(row=1, column=1, sticky=NSEW)
    tan_button = Button(window, text="tan", fg="white", bg="green", command=lambda: tan(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    tan_button.grid(row=1, column=2, sticky=NSEW)
    back_button = Button(window, text="Back", fg="white", bg="dark orange", command=lambda: back(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    back_button.grid(row=1, column=3, sticky=NSEW)
    button_7 = Button(window, text="7", fg="white", bg="black", command=lambda: input_number(
        7, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_7.grid(row=1, column=4, sticky=NSEW)
    button_8 = Button(window, text="8", fg="white", bg="black", command=lambda: input_number(
        8, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_8.grid(row=1, column=5, sticky=NSEW)
    button_9 = Button(window, text="9", fg="white", bg="black", command=lambda: input_number(
        9, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_9.grid(row=1, column=6, sticky=NSEW)
    divide_button = Button(window, text="/", fg="white", bg="purple", command=lambda: input_number(
        "/", equation), height=3, width=6, borderwidth=10, font=button_font)
    divide_button.grid(row=1, column=7, sticky=NSEW)

    sinh_button = Button(window, text="sinh", fg="white", bg="lime green", command=lambda: sinh(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    sinh_button.grid(row=2, column=0, sticky=NSEW)
    cosh_button = Button(window, text="cosh", fg="white", bg="lime green", command=lambda: cosh(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    cosh_button.grid(row=2, column=1, sticky=NSEW)
    tanh_button = Button(window, text="tanh", fg="white", bg="lime green", command=lambda: tanh(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    tanh_button.grid(row=2, column=2, sticky=NSEW)
    clear_button = Button(window, text="C", fg="white", bg="red", command=lambda: clear_input_field(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    clear_button.grid(row=2, column=3, sticky=NSEW)
    button_4 = Button(window, text="4", fg="white", bg="black", command=lambda: input_number(
        4, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_4.grid(row=2, column=4, sticky=NSEW)
    button_5 = Button(window, text="5", fg="white", bg="black", command=lambda: input_number(
        5, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_5.grid(row=2, column=5, sticky=NSEW)
    button_6 = Button(window, text="6", fg="white", bg="black", command=lambda: input_number(
        6, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_6.grid(row=2, column=6, sticky=NSEW)
    multiply_button = Button(window, text="*", fg="white", bg="purple", command=lambda:  input_number(
        "*", equation), height=3, width=6, borderwidth=10, font=button_font)
    multiply_button.grid(row=2, column=7, sticky=NSEW)

    log_base_e_button = Button(window, text="log", fg="white", bg="sienna", command=lambda: log(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    log_base_e_button.grid(row=3, column=0, sticky=NSEW)
    log_base_2_button = Button(window, text="log2", fg="white", bg="sienna", command=lambda: log2(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    log_base_2_button.grid(row=3, column=1, sticky=NSEW)
    log_base_10_button = Button(window, text="log10", fg="white", bg="sienna", command=lambda: log10(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    log_base_10_button.grid(row=3, column=2, sticky=NSEW)
    factorial_button = Button(window, text="x !", fg="white", bg="deep pink", command=lambda: factorial(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    factorial_button.grid(row=3, column=3, sticky=NSEW)
    button_1 = Button(window, text="1", fg="white", bg="black", command=lambda: input_number(
        1, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_1.grid(row=3, column=4, sticky=NSEW)
    button_2 = Button(window, text="2", fg="white", bg="black", command=lambda: input_number(
        2, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_2.grid(row=3, column=5, sticky=NSEW)
    button_3 = Button(window, text="3", fg="white", bg="black", command=lambda: input_number(
        3, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_3.grid(row=3, column=6, sticky=NSEW)
    minus_button = Button(window, text="-", fg="white", bg="purple", command=lambda: input_number(
        "-", equation), height=3, width=6, borderwidth=10, font=button_font)
    minus_button.grid(row=3, column=7, sticky=NSEW)

    reciprocal_button = Button(window, text="1/x", fg="white", bg="darkgoldenrod",
                               command=lambda: reciprocal(equation), height=3, width=6, borderwidth=10, font=button_font)
    reciprocal_button.grid(row=4, column=0, sticky=NSEW)
    root_button = Button(window, text="√x", fg="white", bg="darkgoldenrod", command=lambda: root(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    root_button.grid(row=4, column=1, sticky=NSEW)
    square_button = Button(window, text="x\u00b2", fg="white", bg="darkgoldenrod", command=lambda: input_number(
        "**2", equation), height=3, width=6,    borderwidth=10, font=button_font)
    square_button.grid(row=4, column=2, sticky=NSEW)
    x_power_y_button = Button(window, text="x^y", fg="white", bg="darkgoldenrod", command=lambda: input_number(
        "**", equation), height=3, width=6,  borderwidth=10, font=button_font)
    x_power_y_button.grid(row=4, column=3, sticky=NSEW)
    button_00 = Button(window, text="00", fg="white", bg="black", command=lambda: input_number(
        "00", equation), height=3, width=6, borderwidth=10, font=button_font)
    button_00.grid(row=4, column=4, sticky=NSEW)
    button_0 = Button(window, text="0", fg="white", bg="black", command=lambda: input_number(
        0, equation), height=3, width=6, borderwidth=10, font=button_font)
    button_0.grid(row=4, column=5, sticky=NSEW)
    dot_button = Button(window, text=".", fg="white", bg="black", command=lambda: input_number(
        ".", equation), height=3, width=6, borderwidth=10, font=button_font)
    dot_button.grid(row=4, column=6, sticky=NSEW)
    plus_button = Button(window, text="+", fg="white", bg="purple", command=lambda: input_number(
        "+", equation), height=3, width=6, borderwidth=10, font=button_font)
    plus_button.grid(row=4, column=7, sticky=NSEW)

    e_button = Button(window, text="e", fg="white", bg="midnightblue", command=lambda: input_number(
        math.e, equation), height=3, width=6, borderwidth=10, font=button_font)
    e_button.grid(row=5, column=0, sticky=NSEW)
    exponential_of_x_button = Button(window, text="e^x", fg="white", bg="midnightblue", command=lambda: exponential(
        equation), height=3, width=6,  borderwidth=10, font=button_font)
    exponential_of_x_button.grid(row=5, column=1, sticky=NSEW)
    pi_button = Button(window, text="π", fg="white", bg="mediumblue", command=lambda: input_number(
        math.pi, equation), height=3, width=6, borderwidth=10, font=button_font)
    pi_button.grid(row=5, column=2, sticky=NSEW)
    decimal_to_fraction_button = Button(window, text="S<>D", fg="white", bg="mediumblue", command=lambda: degree2fraction(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    decimal_to_fraction_button.grid(row=5, column=3, sticky=NSEW)
    rad_button = Button(window, text="RAD", fg="white", bg="darkorchid", command=lambda: radian(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    rad_button.grid(row=5, column=4, sticky=NSEW)
    deg_button = Button(window, text="DEG", fg="white", bg="darkorchid", command=lambda: degree(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    deg_button.grid(row=5, column=5, sticky=NSEW)
    modulus_button = Button(window, text="%", fg="white", bg="purple", command=lambda: input_number(
        "%", equation), height=3, width=6, borderwidth=10, font=button_font)
    modulus_button.grid(row=5, column=6, sticky=NSEW)
    equal_button = Button(window, text="=", fg="white", bg="purple", command=lambda: evaluate(
        equation), height=3, width=6, borderwidth=10, font=button_font)
    equal_button.grid(row=5, column=7, sticky=NSEW)

    window.mainloop()


if __name__ == "__main__":
    main()