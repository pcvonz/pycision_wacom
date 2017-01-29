#!/usr/bin/env python2
import subprocess
from Xlib import display

#Grabs current stylus settings to check if it's in precision mode or not.
curr_stylus_settings = str(subprocess.check_output(["xinput", "list-props", "Wacom Intuos4 WL Pen stylus"]))
curr_stylus_settings = curr_stylus_settings.split("\n")[2].split("\t")[2].split(" ")[0].replace(",", "")

print(curr_stylus_settings)

xwininfo = str(subprocess.check_output(["xwininfo", "-root"]))
geometry = xwininfo.split("\n")
geometry = geometry[(len(geometry)-3)]
geometry = geometry.split(" ")[3]
geometry = geometry.split("+")[0]
geometry = geometry.split("x")

desktop_width = float(geometry[0])
desktop_height = float(geometry[1])

#for i in xwininfo:
    #print(i)
tablet_height = 495.0
tablet_width = 755.0

data = display.Display().screen().root.query_pointer()._data
x_pos = data["root_x"]-(tablet_width/2)
y_pos = data["root_y"]-(tablet_height/2)

tablet_width_over_desktop_width = tablet_width / desktop_width
tablet_height_over_desktop_height = tablet_height / desktop_height
tablet_x_over_desktop_width = x_pos / desktop_width
tablet_y_over_desktop_height = y_pos / desktop_height

test_string = "%f" % (tablet_width_over_desktop_width)

print(test_string)
print(curr_stylus_settings)

if(curr_stylus_settings != "0.567568"):
    subprocess.call(["xinput", "set-prop", "Wacom Intuos4 WL Pen stylus", "--type=float", "Coordinate Transformation Matrix", "0.567568", "0", ".432", "0", "1", "0", "0", "0", "1"])
else:
    subprocess.call(["xinput", "set-prop", "Wacom Intuos4 WL Pen stylus", "--type=float", "Coordinate Transformation Matrix", str(tablet_width_over_desktop_width), "0", str(tablet_x_over_desktop_width), "0", str(tablet_height_over_desktop_height), str(tablet_y_over_desktop_height), "0", "0", "1"])
