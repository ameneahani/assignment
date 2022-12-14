import os
import imageio
IMAGES = []
image_list = sorted(os.listdir("Assignment8\images"))

for image_name in image_list:
    image_path = "Assignment8/images/" + image_name
    image = imageio.imread(image_path)
    IMAGES.append(image)
imageio.mimsave("Assignment8/my.gif",IMAGES)