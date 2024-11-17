# Import the required Libraries
from tkinter import *


# Define the threshold heart rate for abnormality
def check_hr():
    heart_rate = int(a.get())
    abnormal_hr_threshold = 75

    # Ask user for heart rate input

    # Check if heart rate is abnormal
    if heart_rate < abnormal_hr_threshold:
        out = "Drowsy Status Detected."
    else:
        out = "Your heart rate is normal."

    label.config(text=out)


# Create an instance of Tkinter frame
win = Tk()

# Set the geometry of Tkinter frame
win.geometry("750x250")

# Create an Entry widget
Label(win, text="Enter Your Heart Rate", font='Calibre 10').pack()
a = Entry(win, width=35)
a.pack()

label = Label(win, text="Drowsiness Status", font='Calibre 15')
label.pack(pady=20)

Button(win, text="Detect Drowsiness", command=check_hr).pack()

win.mainloop()
