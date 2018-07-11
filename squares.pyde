def setup():
    size(800, 600)
    noStroke()
    x=0
    while x < 800:
        y=0
        while y < 600:
            if x % 200== 0:
                fill (random(255), random(255), random(255))
            else:
                fill (0, 0, 0)
            rect (x, y, 100, 100)
            if y% 300==0

    while pbj < 800:
        blt = 25
        while blt < 600:
            rect(pbj, blt, 50, 50)
            blt = blt+ 100
    pbj = pbj + 100
