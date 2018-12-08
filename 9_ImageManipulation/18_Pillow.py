# Install pip from here: https://pip.pypa.io/en/stable/installing/
# pip is a package manager. if you want to install library in Python, just run pip install <name-of-library>
# Install Pillow from here: https://pillow.readthedocs.io/en/latest/installation.html

from PIL import Image

im = Image.open("image1.jpg")
im.show()

im2 = Image.open("scooter.jpeg")
im2.show()
im2 = im2.rotate(55)  # rotate the image by 55 degrees


# Now, let us resize the images.

def resize(image_names, new_size=(256, 256)):
    for im_name in image_names:
        img = Image.open(im_name)
        img = img.resize(new_size)
        img.save("rsz_" + im_name)


images = ['image1.jpg', 'scooter.jpeg']
resize(images)

# convert image to greyscale
colour_img = Image.open('colourful.jpg')
colour_img.show()
grayscale = colour_img.convert('L')
grayscale.show()
