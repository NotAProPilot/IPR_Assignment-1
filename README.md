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




