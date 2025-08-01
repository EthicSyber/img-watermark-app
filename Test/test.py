
 ###################
##     TESTING     ##
 ###################

 # draw = ImageDraw.Draw(im=img, mode="RGB")
# print(type(draw))
# draw.line(xy=(0, 0)+img.size, fill=COLORS['lightgray'])
# draw.line(xy=[(0, img.size[0]//2), (img.size[1]//2), img.size[1]//2], fill=COLORS['lightgray'])
# draw.circle(xy=(img.size[0]//2, img.size[1]//2), radius=30.0, fill=None, outline=COLORS['lightgray'], width=1)
        
# to get the center coordinate of a image
# image size width // 2 and the image size height // 2

# newimg = Image.new(mode="RGBA", size=img.size)

# sys.arg usage: https://docs.python.org/3/library/sys.html#sys.argv
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#cutting-pasting-and-merging-images
# GOTOs 
# open() uses the Image module to read files from disk; library auto-determines image format
# save() uses the Image module to save files

# Load an image with the open() function from the Image Module; if successful, returns an Image object
# img = Image.open("./Test/images/red_star_city.jpeg")
# img.show() # will display the image from a temporary file and calls a utility to display the image

# Merging Images
# img1 = Image.open("./Test/images/red_star_valley.png").resize((500, 500))
# img2 = Image.open("./Test/images/red_star_logo.png").resize((500, 500))
# img1.putalpha(255)
# width of image
# img = Image.new("RGBA", (500, 500))
# img1.show()
# print(img1.mode, img2.mode)
# nw_img = Image.blend(img1, img2, alpha=0.3)
# nw_img.show()
# paste() will paste an image over another one with the mode set
# img.paste(img1) # https://pillow.readthedocs.io/en/stable/reference/Image.html#:~:text=Image.paste

# Adds or replaces the alpha layer in this image
# img2.putalpha(25) # https://pillow.readthedocs.io/en/stable/reference/Image.html#:~:text=Image.putalpha
# alpha composite can place the image right over the other with specificity on the location via a passed tuple to the second parameter being the area of the img (top left = (0, 0) bottom right = (max width - 20, max height -20)).
# img.alpha_composite(img2, (400, 400))

# img.show()


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
# arial = ImageFont.truetype(font='/Library/Fonts/Arial Unicode.ttf')