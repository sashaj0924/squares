def setup():
    size(800, 600)
    noStroke()
    background (255, 51, 228)
    img= loadImage("emoji.jpg")
    image (img, 0, 0)
    x=0
    while x < 800:
        y=0
        while y < 600:
            
            if x % 200== 0:
                fill (random(255), random(255), random(255))
            else:
                fill (0, 0, 0)
            image (img, x, y, 100, 100)
            if y% 300==0:
                fill (255, 255, 255)
                image (img, x, y, 10, 10)
            y= y+ 100
        x= x+ 100
            
