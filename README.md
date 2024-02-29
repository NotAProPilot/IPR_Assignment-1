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




