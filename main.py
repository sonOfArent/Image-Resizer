from PIL import Image
import os

def increaseScale(folder_dir, filename, resizeNumber): # Folder_dir includes slashes.
  
  img = Image.open(f"{folder_dir}{filename}")
  newSize = (img.size[0] * resizeNumber, img.size[1] * resizeNumber)

  img = img.resize(newSize, resample=Image.NEAREST)
  img.save(f"{folder_dir}{filename}")

folder_dir = "./images/"
resizeNumber = 6

for image in os.listdir(folder_dir): increaseScale(folder_dir, image, resizeNumber)