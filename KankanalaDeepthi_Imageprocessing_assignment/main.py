import cv2
import numpy as np
import os

# Function to count rice grains
def count_rice_grains(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define blue color range
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a mask for blue background
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Invert the mask to get rice grains
    rice_grains = cv2.bitwise_not(mask)


    _, thresh = cv2.threshold(rice_grains, 0, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_rice_grains = len(contours)

    # Find broken grains and full grains
    total_broken_grains = 0
    total_full_grains = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:  # You may need to adjust this threshold based on your images
            total_broken_grains += 1
        else:
            total_full_grains += 1

    return total_rice_grains, total_broken_grains, total_full_grains

# Paths
train_folder =r"C:\Users\dell\Desktop\DeepthiKankanala_OpenCv_assiggnment\train"
test_folder = r"C:\Users\dell\Desktop\DeepthiKankanala_OpenCv_assiggnment\test"
submission_file = "submission.csv"

# Process images in the test folder and create a submission file
with open(submission_file, "w") as f:
    f.write("file_name,total_rice_grain,Total_Broken_Grain,Total_Full_Grain\n")
    for image_name in os.listdir(test_folder):
        image_path = os.path.join(test_folder, image_name)
        total_rice, total_broken, total_full = count_rice_grains(image_path)
        f.write(f"{image_name},{total_rice},{total_broken},{total_full}\n")

print("Submission file created successfully.")
