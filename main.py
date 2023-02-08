razlika = 0
ZBROJ = 0

def on_button_pressed_ab():
    global razlika, ZBROJ
    B = 0
    A = 0
    if A > B:
        razlika = A - B
        basic.show_number(razlika)
    else:
        ZBROJ = A + B
        basic.show_number(ZBROJ)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
