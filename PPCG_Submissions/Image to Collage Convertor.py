from PIL import Image,ImageDraw,ImageFont
im=Image.new("RGB",(1500,1125))
u=y=0
for i in ['Circle','Ellipse','Cross','Parabola','Elliptic Curve','Folium of Descartes','lemniscate','trifolium','astroid']:
    img=Image.open('/Users/Rohan/Pictures/%s.png'%i)
    img.thumbnail((500,500))
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype("/System/Library/Fonts/GillSans.ttc",20)
    draw.text((65,10),i.title(),(0,0,0),font=font)
    im.paste(img,(u,y))
    u+=500
    if u==1500:
        u=0
        y+=375
    im.save('Figures.png')
