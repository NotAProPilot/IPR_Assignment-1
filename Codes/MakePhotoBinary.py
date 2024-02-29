import cv2
import matplotlib.pyplot as plt

def make_photo_binary(input_threshold, filepath):
    # Image path:
    img_path = filepath

    # Read the image in BGR format (unchanged)
    original_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Convert to RGB for Matplotlib display (optional)
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    # Create a grayscale copy
    grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    # Thresholding with a value of 128
    _, binary_img = cv2.threshold(grayscale_img, input_threshold, 255, cv2.THRESH_BINARY)

    
    # Create the figure with subplots
    rows = 1
    column = 2
    figure = plt.figure(figsize=(20, 10))

    figure.add_subplot(rows, column, 1)
    plt.imshow(original_img_rgb)
    plt.title("Original Image (Color)")

    figure.add_subplot(rows, column, 2)
    plt.imshow(binary_img, cmap="gray")  # Use "gray" colormap for grayscale display
    plt.title("Binary Image with Threshold = " + str(input_threshold))

    plt.tight_layout()  # Adjust layout for better visualization
    plt.show()
