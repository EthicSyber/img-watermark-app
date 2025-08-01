from PIL import Image
from colors import COLORS
from watermark_functions import text_watermark_image

redcity = "Test/images/red_star_city.jpeg"
redvalley = "./Test/images/red_star_valley.jpeg"
img = Image.open(redcity).convert("RGBA")
text_watermark_image(img=img, thickness=0.1, alpha=50)
img.show()
img.close()