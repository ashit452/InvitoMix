from PIL import Image
a = Image.open("E:\projectfiles\images\\template\\background\paper-2926300_1920.jpg")
b = Image.open("E:\projectfiles\images\\baby shower\\footprint-23991_1280.png")
c = Image.open("E:\projectfiles\images\\template\corner-47040_1280.png")
a.paste(a, (0,0))
a.paste(b, (300,300),mask=b)
a.paste(c, (50,50),mask=c)
a.save("123.jpg")
