"""_summary_
A simple program to demo how to run GUI
"""
# Importing librabries 
import tkinter
import customtkinter
import ImgResize
from tkinter import messagebox

"""_summary_
Initializing system settings
"""
# Set to dark mode
customtkinter.set_appearance_mode("dark")

# Set deafult color for button
customtkinter.set_default_color_theme("dark-blue")

"""_summary_
Show the actual window
"""
app = customtkinter.CTk()

# Set the size and title of the window
app.geometry("860x480")
app.title("IPR_Assignment 1_Resize Image")

"""_summary_
Add UI elements
"""
title = customtkinter.CTkLabel(app,text="Pick between the following options")
title.pack(ipadx = 10, ipady = 10)



"""_summary_
Add two box to enter width and height
See image_resize() function
It is strongly recommend that StringVar is used, then use int(.get()) to convert to int instead of IntVar
"""
# Initialzing a height variable
height_var = tkinter.StringVar()
height = customtkinter.CTkEntry(app, width=500, height = 50, border_color="red", placeholder_text="Enter the height you want:",placeholder_text_color="red")
height.pack(padx=10,pady=10)

# Initalizing a width variable
width_var = tkinter.StringVar()
width = customtkinter.CTkEntry(app, width=500, height = 50, border_color="blue", placeholder_text="Enter the width you want: ", placeholder_text_color="blue")
width.pack(padx=10,pady=10)

# A function to handle the resize function (by calling )
def handle_resize():
    # Parse data from input and cast to integer
    desired_height = int(height.get())
    desired_width = int(width.get())
    
    # Raise exception if width or height is negative
    if desired_height < 0 or desired_width <0:
         messagebox.showerror('Python Error', "New image width or height can't be a negative number")
    path_from_user = filepath
    ImgResize.image_resize(desired_height, desired_width, path_from_user)

"""_summary_
Add a button to resize image
"""
button = customtkinter.CTkButton(master=app, text="Resize Image", command=handle_resize)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


# The function that handle path input
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
  
# Sample code to add another button:
button = customtkinter.CTkButton(master=app, text="Select Image", command = handle_path_input)
button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

# Code for displaying the GUI
app.mainloop()
