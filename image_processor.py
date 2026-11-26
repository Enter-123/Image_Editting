import cv2
from PySide6.QtGui import QImage, QPixmap
import numpy as np
from Open_Image import get_image


def convert_CVT(image=None):
    if image is None:
        return None

    if image.ndim == 2:     # This means the image is already in grayscale format. So, we don't need to convert it again.
        return image        # The return image will return the same image.
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



def save_image(image_name,image_tosave=None):
    if image_tosave is None:
        return 
    if not image_name.strip():
        image_name = "saved_image.png"
        
    if not image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        image_name += ".png"
    return cv2.imwrite(image_name, image_tosave)



def convert_to_pixmap(image = None):
    if image is None:
        return None

    if image.ndim == 2:
        h, w = image.shape

        qimage = QImage(
            image.data,
            w,
            h,
            image.strides[0],
            QImage.Format.Format_Grayscale8
        ).copy()
    else:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    # Here we are converting Opencv BGR image to RGB.
                                                        # Since PySide6 excepts RGB format for QImage. Also, we are converting the image to contiguous array to avoid memory issues.
                                                        # If used BGR to display the color will come out wrong. So, we need to convert it to RGB format.
        
        img = np.ascontiguousarray(img) # This will store the image in contiguous memory block. This is important for QImage to work properly. If we don't do this, we will get a segmentation fault error.
                                        # This will basically preserve the original image data in the memory in a contigous block. If the data is non-contigous then it will create one and copy the data to it.
        h, w, ch = img.shape
        qimage = QImage(
            img.data,
            w,
            h,
            ch * w,
            QImage.Format.Format_RGB888
        ).copy()

    return QPixmap.fromImage(qimage)



def open_image(parent=None):
    img, loc = get_image(parent)
    if img is None:
        return None, None
    return img, loc
