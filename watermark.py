from PIL import Image, ImageDraw

class Watermark:
    def __init__(self, image:str, mode="RGBA"):
        self.image = self.get_image_object(path=image, mode=mode)

    def get_image_object(self, path:str, mode:str) -> Image.Image:
        file = Image.open(path).convert(mode)
        return file


    def text_watermark_image(self, img:Image.Image, text:str="© CYBER-SAIYAN", xy:tuple[int]=(100, 60), x_offset:int=35, thickness:float=0.5, color:str|tuple='white', hv_len:tuple=(100, 50), mode='RGBA', alpha:int=25, show_image=False):
        """Draws text over the image in a sequence
        
        :params Image img: takes Image object to draw text on.
        :params tuple [int] xy: a tuple of the x and y coordinate values for starting placement of the text on the image (e.g., (0, 0) is top-left).
        :params int x_offset: the space (i.e., offset) between each text placement (otherwise with none it will overlay/overlap)
        :params str text: te text you want to have as a repeated pattern across the image
        :params float thickness: the desired thickness of the text.
        :params str | tuple color: the desired color (can be repsented as str e.g., 'lightgray' or 'red'; Or can be like an rgb/hsl value rgb(255, 0, 0) or (100%, 0%, 0%))
        :params tuple hv_len: the amount of text placed horizonatal and vertacally on the image

        :returns: None
        """
        watermark = self.create_new_image(img=img, mode=mode)
        v_len, h_len = self.get_watermark_area(watermark, hv_len)
        self.create_watermark(watermark, mode, h_len, v_len, xy, x_offset, text, thickness, color)
        self.apply_transparency(img=watermark, alpha=alpha)
        self.apply_watermark(img, watermark)

        if show_image == True:
            img.show()


    def apply_watermark(self, img:Image.Image, watermark:Image.Image):
        img.alpha_composite(im=watermark)

    def create_watermark(self, img:Image.Image, mode:str, h_len, v_len, xy, x_offset, text, thickness, color):
        draw = ImageDraw.Draw(im=img, mode=mode)
        for v in range(v_len):
            for h in range(h_len):
                draw.text(
                    xy=((xy[0]*h) + x_offset, xy[1] * v), 
                    text=text, 
                    stroke_width=thickness, 
                    fill=color,
                )

    def get_watermark_area(self, img:Image.Image, hv_len:tuple):
        v_len = img.size[1]//hv_len[1]
        h_len = img.size[0]//hv_len[0]
        return v_len, h_len

    def create_new_image(self, img:Image.Image, mode="RGBA"):
        """Creates a new image with a specified mode based on the given Image.Image objects size"""
        new_image = Image.new(mode, img.size)
        return new_image


    def apply_transparency(self, img:Image.Image, alpha:int):
        img.putalpha(alpha)

