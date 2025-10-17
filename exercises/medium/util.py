import cv2

def imread_rgb(path):
    img_bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

def imread_gray(path):
    img_bgr = cv2.imread(path)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    return img_gray