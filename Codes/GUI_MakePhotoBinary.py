"""_summary_
A simple program that serves as an front-end to the 
MakePhotoBinary.py file
"""

# Importing librabries 
import tkinter              # Base tkinter
import customtkinter        # Update customtkinter
from tkinter import messagebox

import MakePhotoBinary      # From the back-end file

"""_summary_
Initialize the setting for the GUI:
- Set to dark mode and blue color button
"""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the outer (base) windows:
console = customtkinter.CTk()

# Set the size and title of the window
console.geometry("860x480")
console.title("IPR_Assignment 1_Binary Photo")

# Add text above the box to enter the threshold value
# .pack is required to actually "pack" the element into the window
title = customtkinter.CTkLabel(console, text="Enter a threshold value between 0 and 255")
title.pack(ipadx = 10, ipady = 10)

"""_summary_
Codes for accepting inputed threshold value from user:
"""
# Initalize a thereshold size variable
# Set as string to avoid error:
threshold_from_user = tkinter.StringVar()

# Set and pack the area to eneter value
threshold = customtkinter.CTkEntry(console, width = 100, height = 50, border_color = "#d6e9ff",placeholder_text="Enter threshold value")
threshold.pack(padx=15, pady=15)



"""_summary_
A function to handle the set threshold and display the 

"""

def handle_threshold_value():
    # Accept input from the entry box
    input_threshold = int(threshold.get())
    
    # Raising exception if the number is smaller than 0
    if (input_threshold < 0):
        messagebox.showerror('Python Error', "Threshold value can not be negative!")
        
    # Raising another exception if the number is bigger than 255
    if (input_threshold > 255):
        messagebox.showerror('Python Error', "Threshold value is larger than 255")
        
    # Call function from back end:
    # Args accepted (in order of agrs: original image, threshold )
    MakePhotoBinary.make_photo_binary(input_threshold, filepath)

def handle_path_input():
    # TODO: THIS FUNCTION
    from customtkinter import filedialog
    
    # Set to global (in lieu of .get() from box input)
    global filepath
    
    
    # Specify what kind of file is accepted
    filepath = filedialog.askopenfilename(
    title="Please select an image file",
    filetypes=[
        (("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif"))
    ]
)
    
"""_summary
A button to display both the original image
and the greyscale binary image
"""
button = customtkinter.CTkButton(master=console, text="Display Binary Image", command=handle_threshold_value)
button.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

# Sample code to add another button to select file:
button = customtkinter.CTkButton(master=console, text="Select Image", command = handle_path_input)
button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

# Add a button call back to handle input:
console.mainloop()









