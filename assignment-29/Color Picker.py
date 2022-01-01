import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

loader = QUiLoader()
app = QApplication(sys.argv)
ui = loader.load("Input\color picker.ui", None)
ui.setWindowTitle("Color Picker")

v_r = 0
v_g = 0
v_b = 0

def red_slider_changed(_,value):
    value += 1
    ui.lableR.setText(f"{value}")
    return value

def green_slider_changed(_,value):
    value += 1
    ui.lableG.setText(f"{value}")
    return value

def blue_slider_changed(_,value):
    value += 1
    ui.lableB.setText(f"{value}")
    return value

# def label_Color(value1,value2,value3):
#     ui.labelColor.setText(f"rgb({value1} , {value2} , {value3})")

# value1 = red_slider_changed(v_r,v_r)
# value2 = green_slider_changed(v_g,v_g)
# value3 = blue_slider_changed(v_b,v_b)
# label_Color(value1,value2,value3)

ui.redSlider.valueChanged.connect(partial(red_slider_changed,v_r))
ui.greenSlider.valueChanged.connect(partial(green_slider_changed,v_g))
ui.blueSlider.valueChanged.connect(partial(blue_slider_changed,v_b))

ui.show()
app.exec_()
