from PIL import Image

def toPDF():
    image_1 = Image.open("./src/temp/result.jpg")
    im_1 = image_1.convert('RGB')
    im_1.save("./src/temp/result.pdf")