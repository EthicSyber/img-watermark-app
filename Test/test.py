
 ###################
##     TESTING     ##
 ###################

############
## PILLOW ##
############

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



###############################
#### BELOW IS TESTING CODE ####
###############################





# # from colors import COLORS
# from watermark_functions import text_watermark_image, get_image_object
# from tkinter import *
# from tkinter import ttk, filedialog, messagebox
# # from style import *

# APP_WIDTH, APP_HEIGHT = 550,650
# PADX, PADY = 20, 45
# CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
# IMG_COORD = (0, 0)


# # redcity = "Test/images/red_star_city.jpeg"
# # redvalley = "./Test/images/red_star_valley.jpeg"
# # text_watermark_image(img=img, thickness=0.1, alpha=50)
# # img.show()
# # img.close()


# # Need a good review on TK
# # Follow along this first: https://tkdocs.com/tutorial/firstexample.html

# filepath = ''

# def select_image():
#     global filepath
#     filepath = filedialog.askopenfilename() 
#     filename = filepath.split('/')[-1]
#     if len(filename) > 30:
#         filename = f"default.{filepath.split(".")[-1]}" 
#     path.set(filename)
 
# def watermark_image():
#     if filepath:
#         image = get_image_object(filepath)
#         text_watermark_image(img=image, thickness=0.2, alpha=50)
#         image.show()
#     else:
#         messagebox.showinfo(title="Invalid File", message="File not found!", icon='warning')


# # Creating Application Window
# root = Tk()
# root.title("Watermark App")
# root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
# root.minsize(width=APP_WIDTH, height=APP_HEIGHT)


# mainframe = Frame(root) # padding="left top right bottom"
# mainframe.configure(background="#2d2d2d", padx=20, pady=20)
# mainframe.grid(column=0, row=0, sticky="nsew")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)




# style_widgets = ttk.Style(mainframe) # in order to style your widgets ttk use this
# style_widgets.theme_use('clam') # to override style themes to get the bg or fg for a button use this method
# style_widgets.configure(style="Primary.TButton", background="#4144ff", foreground="#ffffff", borderwidth=0, relief=SOLID)
# style_widgets.map("Primary.TButton", background=[('pressed', 'blue'), ('active', 'violet')])

# # btn_primary()
# # Create Entry Widget for Image path
# path = StringVar()
# ttk.Label(mainframe, textvariable=path, background="#2d2d2d", foreground='#ffffff').grid(column=0, row=0, sticky=(W, E), pady=10)
# ttk.Button(mainframe, text="Select", style="Primary.TButton", command=select_image).place(x=0, y=30)
# ttk.Button(mainframe, text="Watermark", style="Primary.TButton", command=watermark_image).place(x=120, y=30)

# canvas = Canvas(mainframe, width=500, height=500, borderwidth=1, background="#727272", highlightthickness=1, relief=SOLID)
# canvas.place(x=0, y=70)




# root.mainloop()




# def btn_primary():
#     primary_style = ttk.Style()
#     primary_style.theme_use('clam')
#     primary_style.configure('Primary.TButton', background='#ccccff')
#     primary_style.map('Primary.TButton',
#                     background=[('pressed', 'purple'), ('active', 'lightblue')],
#                     foreground=[('active', 'white')]
#     )


####
# TEST TK
####

# APP_WIDTH, APP_HEIGHT = 550,600
# PADX, PADY = 20, 45
# CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
# IMG_COORD = (0, 0)



# root = Tk()

# # .geometry will give the application width and height
# root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
# # to give the application some padding use the .config(padx=?, pady=?)
# root.config(padx=PADX, pady=PADY)
# image = img.open("Test/watermarked_images/red_star_city.png").resize((CANVAS_WIDTH, CANVAS_HEIGHT))
# tk_img = ImageTk.PhotoImage(image=image)
# canvas = Canvas(root, width=tk_img.width(), height=tk_img.height(), border=1, relief=SOLID, highlightthickness=0)
# canvas.create_image((canvas.size()[0]+1 / 2), (canvas.size()[1]+1 / 2), image=tk_img, anchor="nw")
# canvas.grid(column=0, row=0)

# root.mainloop()


# def preview_watermark(img):
#     image = img.resize()










# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 5)/10000.0)
#     except ValueError:
#         pass

# # Setting up the main application window
# root = Tk()
# root.title("Watermark")


# # Setting up the frame for the content
# mainframe = ttk.Frame(root, padding="5 5 12 12") # padding="left top right bottom"
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


# # Creating the Entry Widget
# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, stick=(W, E))


# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# # polishing user interface

# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)


# # Keep application window running
# root.mainloop()


