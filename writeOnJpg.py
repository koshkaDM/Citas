from PIL import Image, ImageFont, ImageDraw

image_path = "./src/img/cita.jpg"
font_path = './src/fonts/arial2.ttf'
arial = './src/fonts/arial.ttf'
size = 38
rgb = [0, 0, 0]

def writeOnJpg(name, date, agend, service, footer):
    my_image = Image.open(image_path)
    title_font = ImageFont.truetype(font_path, size)
    arial_bold = ImageFont.truetype(arial, size)
    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((376, 1092), name, tuple(rgb), font=title_font)
    image_editable.text((333, 1275), date, tuple(rgb), font=title_font)
    image_editable.text((357, 1340), agend, tuple(rgb), font=title_font)
    image_editable.text((368, 1405), service, tuple(rgb), font=title_font)

    image_editable.text((100, 1650), "Si desea", tuple(rgb), font=arial_bold)
    image_editable.text((268, 1650), "cancelar la cita", (200, 0, 0), font=arial_bold)
    image_editable.text((563, 1650), "creada el", tuple(rgb), font=arial_bold)
    image_editable.text((733, 1650), footer, tuple(rgb), font=arial_bold)
    image_editable.text((100, 1690), "deberá hacerlo al menos 3 días antes del día de visita", tuple(rgb), font=arial_bold)

    my_image.save("./src/temp/result.jpg")
