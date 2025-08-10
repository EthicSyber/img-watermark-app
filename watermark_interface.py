from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk
from watermark import Watermark
import sys, os

APP_WIDTH, APP_HEIGHT = 550,600
APP_W_OFFSET, APP_H_OFFSET = 6, 35
PADX, PADY = 20, 20
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
IMG_COORD = (0, 0)
NSEW = 'nsew'
DARK_GRAY = "#2d2d2d"
MEDIUM_GRAY = "#727272"
WHITE = "#ffffff"
VIOLET = "#4c4eb2"
BLUE_GRAY = "#3e4a7c"

class WatermarkUI:
    def __init__(self):
        self.filepath = ''
        self.filename = ''
        root = Tk()
        root.title('Watermark App')
        root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        root.minsize(width=APP_WIDTH-APP_W_OFFSET, height=APP_HEIGHT+APP_H_OFFSET)
        root.maxsize(width=APP_WIDTH-APP_W_OFFSET, height=APP_HEIGHT+APP_H_OFFSET)
        mainframe = Frame(root, padx=PADX, pady=PADY)
        mainframe.configure(background=DARK_GRAY)
        mainframe.grid(column=0, row=0, sticky='nsew')
        style_widgets = ttk.Style(mainframe) # in order to style your widgets ttk use this
        style_widgets.theme_use('clam') # to override style themes to get the bg or fg for a button use this method
        style_widgets.configure(style="Primary.TButton", background=BLUE_GRAY, foreground=WHITE)
        style_widgets.map("Primary.TButton", background=[('pressed', 'blue'), ('active', VIOLET)])
        self.path = StringVar()
        ttk.Label(mainframe, text='Filepath:', foreground=WHITE, background=DARK_GRAY).grid(column=0, row=0, sticky=W)
        ttk.Label(mainframe, textvariable=self.path, background=DARK_GRAY, foreground=WHITE).grid(column=0, row=0, sticky=W, padx=60)
        ttk.Button(mainframe, text="Select", style="Primary.TButton", command=self.select_image).grid(column=0, row=2, sticky=W, pady=PADY)
        ttk.Button(mainframe, text="Watermark", style="Primary.TButton", command=self.watermark_image).grid(column=0, row=2, sticky=W, padx=120)
        ttk.Button(mainframe, text="Save", style="Primary.TButton", command=self.save_file).grid(column=0, row=2, sticky=E)
        self.canvas = Canvas(mainframe, width=500, height=500, borderwidth=1, background=MEDIUM_GRAY, highlightthickness=1, relief=SOLID)
        self.canvas.grid(column=0, row=3)
        root.mainloop()

    def select_image(self):
        self.filepath = filedialog.askopenfilename() 
        self.filename = self.filepath.split('/')[-1]
        if len(self.filename) > 30:
            self.filename = f"default.{self.filepath.split(".")[-1]}" 
        self.path.set(self.filename)
 
    def watermark_image(self):
        if self.filepath:
            self.watermark = Watermark(self.filepath)
            self.watermark.text_watermark_image(img=self.watermark.image, thickness=0.2, alpha=50)
            self.preview_watermark(watermark_image=self.watermark.image)
        else:
            messagebox.showinfo(title="Invalid File", message="File not found!", icon='warning')
        
    def save_file(self):
        is_save = messagebox.askquestion(title="Save File", message="Would you like to save your new image?")
        if is_save.startswith('y'):
            self.watermark.image.save(fp=f"./images/{self.filename}", format='png')
        else:
            messagebox.showinfo(title="Invalid File", message="File not found!", icon='warning')
    
    def preview_watermark(self, watermark_image):
        temp = watermark_image.resize((500, 500))
        self.image = ImageTk.PhotoImage(image=temp)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

