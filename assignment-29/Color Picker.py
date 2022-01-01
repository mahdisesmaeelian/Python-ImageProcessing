import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

loader = QUiLoader()
app = QApplication(sys.argv)
ui = loader.load("Input\color picker.ui", None)
ui.setWindowTitle("Color Picker")

rcode = ui.redSlider.value()
gcode = ui.greenSlider.value()
bcode = ui.blueSlider.value()

def red_slider_changed(_,value):
    ui.lableR.setText(f"{value}")
    # rcode = ui.redSlider.value()

def green_slider_changed(_,value):
    ui.lableG.setText(f"{value}")

def blue_slider_changed(_,value):
    ui.lableB.setText(f"{value}")
    

ui.redSlider.valueChanged.connect(partial(red_slider_changed,rcode))
ui.greenSlider.valueChanged.connect(partial(green_slider_changed,gcode))
ui.blueSlider.valueChanged.connect(partial(blue_slider_changed,bcode))

ui.labelColor.setText(f"rgb({rcode} , {gcode} , {bcode })")

ui.show()
app.exec_()
