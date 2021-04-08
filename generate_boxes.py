import random


def get_random_boxes(templates_size,image):
    points = []
    h = image.shape[0]
    w = image.shape[1]
    i = list(range(0,h,20))
    j = list(range(0,w,20))
    while len(points)<templates_size:
        x = random.choice(j)
        y = random.choice(i)
        if (x,y) in points:
            continue

        else:
            points.append((x,y))
    return points

