import tkinter
import customtkinter
import Codes.ImageResizeActivity.ImgResize as ImgResize  # Assuming "ImgResize" is a module containing your image processing logic

# Set custom Tkinter appearance and theme (optional)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
app = customtkinter.CTk()
app.geometry("860x480")
app.title("IPR_Assignment 1")

# Title label
title = customtkinter.CTkLabel(app, text="Pick between the following options")
title.pack(ipadx=10, ipady=10)

# Entry boxes for width and height (using StringVar for input handling)
height_var = tkinter.StringVar()
width_var = tkinter.StringVar()

height_entry = customtkinter.CTkEntry(
    app, width=500, height=50, border_color="red", textvariable=height_var
)
height_entry.pack(padx=10, pady=10)

width_entry = customtkinter.CTkEntry(
    app, width=500, height=50, border_color="blue", textvariable=width_var
)
width_entry.pack(padx=10, pady=10)

# Function to handle button click and call image resize
def handle_resize():
    try:
        desired_height = int(height_var.get())
        desired_width = int(width_var.get())
        ImgResize.image_resize(desired_height, desired_width)  # Call the image resize function
    except ValueError:
        print("Invalid input. Please enter integers for width and height.")

# Button with command linked to the handle_resize function
button = customtkinter.CTkButton(master=app, text="Resize Image", command=handle_resize)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Start the main event loop
app.mainloop()

