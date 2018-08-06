from random import randint

def mixup(image1, image2, gt1, gt2):
    cols = image1.shape[1]
    pixel_border = randint(int(0.33*cols), int(0.66*cols))
    image1[ : , : , pixel_border : ] = image2[ : , : , pixel_border : ]
    gt1[ : , : , pixel_border : ] = gt2[ : , : , pixel_border : ]
    return image1, gt1


def mixup_prob(image1, image2, gt1, gt2):
    dim, rows, cols = image1.shpae
    while(1):
        x1 = randint(int(0.33*cols), int(0.66*cols))
        x2 = randint(int(0.33*cols), int(0.66*cols))
        y1 = randint(int(0.33*rows), int(0.66*rows))
        y2 = randint(int(0.33*rows), int(0.66*rows))
        if len(set([x1, x2, y1, y2])) == 4:
            a = float(y1-y2)/(x1-x2)
            b = y1 - a*x1
            if a!=1.0:
                break
    if abs(a)<1.0:
        for x in range(cols):
            image1[:, :int(a*x+b), x] = image2[:, :int(a*x+b), x]
            gt1[:, :int(a*x+b), x] = gt2[:, int(a*x+b), x]
    else:
        for y in range(rows):
            image1[:, y, :int((y-b)/a)] = image2[:, y, :int((y-b)/a)]
            gt1[:, y, :int((y-b)/a)] = gt2[:, y, :int((y-b)/a)]

    return image1, gt1
