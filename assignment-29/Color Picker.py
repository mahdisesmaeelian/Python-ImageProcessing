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

def red_slider_changed(_,rcode):
    ui.lableR.setText(f"{rcode}")
    rcode = ui.redSlider.value()
    gcode = ui.greenSlider.value()
    bcode = ui.blueSlider.value()
    ui.labelColor.setText(f"rgb({rcode} , {gcode} , {bcode})")
    ui.labelColor.setStyleSheet(f"background-color: red")
    ui.labelColor.setStyleSheet(f"background-color: rgb({rcode},{gcode},{bcode});")

def green_slider_changed(_,gcode):
    ui.lableG.setText(f"{gcode}")
    rcode = ui.redSlider.value()
    gcode = ui.greenSlider.value()
    bcode = ui.blueSlider.value()
    ui.labelColor.setText(f"rgb({rcode} , {gcode} , {bcode})")
    ui.labelColor.setStyleSheet(f"background-color: rgb({rcode},{gcode},{bcode});")

def blue_slider_changed(_,bcode):
    ui.lableB.setText(f"{bcode}")
    rcode = ui.redSlider.value()
    gcode = ui.greenSlider.value()
    bcode = ui.blueSlider.value()
    ui.labelColor.setText(f"rgb({rcode} , {gcode} , {bcode})")
    ui.labelColor.setStyleSheet(f"background-color: blue")
    ui.labelColor.setStyleSheet(f"background-color: rgb({rcode},{gcode},{bcode});")
    

ui.redSlider.valueChanged.connect(partial(red_slider_changed,rcode))
ui.greenSlider.valueChanged.connect(partial(green_slider_changed,gcode))
ui.blueSlider.valueChanged.connect(partial(blue_slider_changed,bcode))

ui.show()
app.exec_()