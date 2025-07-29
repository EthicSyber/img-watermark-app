import os, sys
from PIL import Image

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#cutting-pasting-and-merging-images
# GOTOs 
# open() uses the Image module to read files from disk; library auto-determines image format
# save() uses the Image module to save files

# Load an image with the open() function from the Image Module; if successful, returns an Image object
# img = Image.open("./Test/images/red_star_city.jpeg")
# img.show() # will display the image from a temporary file and calls a utility to display the image












# A file convertion function that takes two parameters to run and two arguments to pass it -f is specifying a file and -e the files new extention
# def convert_img_file_type(img_path:str, ext:str):
#         f, e = os.path.splitext(img_path)
#         print(f)
#         outfile = f + f"{ext}"
#         try:
#             with Image.open(img_path) as img:
#                 print("file:", outfile)
#                 img.save(outfile)
#         except OSError:
#             print("cannot convert", img_path)

# file_path = "-f"
# extention = "-e"
# image = sys.argv[2]
# file_ext = sys.argv[4]

# if sys.argv[1] == file_path and sys.argv[3] == extention:
#     convert_img_file_type(image, file_ext)
