# IPR Assignment 1

This GUI-based approach turns a normal, simple exercise about image resizing and binary image thresholding into a delightful interactive experience akin to playing with digital building blocks. Gone are the days of tediously typing commands into a terminal or wrestling with complicated software interfaces. With just a few clicks and drags, users can effortlessly manipulate images.

## Program structure:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/b024753e-24dd-4472-a72e-799733aa7f09)

There are 2 requirements for this prorgam: Resize photo and display binary image. For each task, there are 2 files (as shown on the figure above): A GUI file that create the GUI windows, accept user inputs and parse them to the back end files (ImgResize and MakePhotoBinary). The structure can be shown in the diagram below: 
```md
+-----------------------+           +-----------------------+            +-----------------------+
|        GUI File       |           |      Backend File      |            |      Application      |
+-----------------------+           +-----------------------+            +-----------------------+
| - title: customtkinter|           |                       |            |      - app: CTk       |
| - height_var: StringVar|           |                       |            +-----------------------+
| - width_var: StringVar|           |                       |
|                       |           |                       |
| + handle_resize()     |           | + image_resize()      |
| + handle_path_input() |           |                       |
+-----------------------+           +-----------------------+
                |                                |
                |                                |
                |                                |
                |                                |
                |                                |
                +--------------------------------+
                                   |
                                   |
                                   |
                                   |
                                   v
+-----------------------+
|      Libraries        |
+-----------------------+
| - OpenCV              |
| - Matplotlib          |
+-----------------------+
```
## Instruction
### Select the program
After downloading, your IDE will show 4 files: *GUI_ImgResize, GUI_MakePhotoBinary, ImgResize, MakePhotoBinary*. The program **wll only run from the appopriate GUI file.**

#### Resize image
First, run the `GUI_ImgResize` file. A window will pop up, like this:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/f2d6dff8-af2d-4d43-9fd8-b8651d8c4ccb)

Enter the height and the width (in pixel) of your photo that the resized image would be in. For example, if you want to resize the image to 1280x720, enter like this:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/5248312c-bc72-4808-9803-081ec28e117e)

Then select the image you want to resize:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/90510f28-382f-4120-978a-194460ea9d76)

Press "Resize Image", and the resized image will be displayed:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/b0a62203-4541-4bbb-8dc3-4126f7314523)

#### Display binary image:
First, run the `GUI_MakePhotoBinary` file. A window will pop up, like this:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/73cb80dd-7296-4ec9-a652-12387498b6d5)

Enter the binary threshold (must be between 0 and 255). For the best result, It's recommended set the binary value to 128:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/fe3eedf0-f3e7-459b-a33a-06a70702e341)

If you enter an out-of-bound binary threshold, a error message will pop up:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/bef48627-9c57-4fb8-b834-13d7c6db1b4e)

Then select the image you want to display binary image:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/90510f28-382f-4120-978a-194460ea9d76)

Press "Display Binary Image", and a Mathplotlib plot will show both the original (in RGB color, if selected) and the binary image:
![image](https://github.com/NotAProPilot/IPR_Assignment-1/assets/113848893/adf91ac0-26c7-44cf-8c2e-b9574e5b8994)

## Frequently Asked Questions (FAQs)
### Do i need to install any outside libraries?
Yes. You will need the following:
- tkinter (install by ``


## Acknowledgement:
This Assignment made extensive use of the [CustomTkinter library](https://github.com/TomSchimansky/CustomTkinter).

For debugging, I want to thanks the following StackOverflow thread for the following fixes:
- [Photo size might be read as empty by CV2](https://stackoverflow.com/questions/52162004/i-am-having-trouble-with-this-error-215assertion-failed-ssize-empty-in-fu)
- [Save filepath as an object, simillar to how to handle input from box](https://stackoverflow.com/questions/61312896/saving-file-path-in-a-variable-using-tkinter)
- [Select multiple file type as one](https://stackoverflow.com/questions/40292705/tkinter-file-pattern-set-in-a-file-dialog)
- [Displaying placeholder text properly](https://stackoverflow.com/questions/74973450/why-is-the-custom-tkinter-placeholder-text-for-an-entry-box-ignored)

[For general approach to GUI via CustomTkinter](https://www.youtube.com/watch?v=NI9LXzo0UY0&t=1028s)

