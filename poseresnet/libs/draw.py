import cv2


def draw_bones(img, annotations):
    limbs = [
        [0, 1], [1, 2], [2, 3], [3, 4],
        [0, 5], [5, 6], [6, 7], [7, 8],
        [0, 9], [9, 10], [10, 11], [11, 12],
        [0, 13], [13, 14], [14, 15], [15, 16],
        [0, 17], [17, 18], [18, 19], [19, 20]
    ]

    colors = [
        (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255),
        (250, 250, 210), (250, 250, 210), (250, 250, 210), (250, 250, 210),
        (60, 179, 113), (60, 179, 113), (60, 179, 113), (60, 179, 113),
        (100, 149, 237), (100, 149, 237), (100, 149, 237), (100, 149, 237),
        (153, 50, 204), (153, 50, 204), (153, 50, 204), (153, 50, 204)
    ]

    for (l, c) in zip(limbs, colors):
        img = cv2.line(img, annotations[l[0]], annotations[l[1]], c, 2)
    
    return img


def draw_joints(img, annotations):
    for a in annotations:
        img = cv2.circle(img, a, 1, (0, 0, 0), 3)

    return img