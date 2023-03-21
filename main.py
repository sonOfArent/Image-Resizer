from PIL import Image

img = Image.open("./images/bookshelf.png")

print(img.mode)
print(img.size)