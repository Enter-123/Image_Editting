import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog
import numpy as np
from Open_Image import get_image


def convert_CVT():
    img = picture
    new_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_pixmap = convert_to_pixmap(image=new_image)
    return show_image(gray_pixmap)
    

def show_image(image=None) -> QPixmap:
    if not isinstance(image, QPixmap):
        return
    return image.scaled(
        650,
        650,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation
    )


def get_imageFromLabel(parent=None, label=None):
    return label, parent


def save_image(picture1, parent=None):
    if not picture1:
        return 
    pixmap = picture1
    if not isinstance(pixmap, QPixmap):
        return 
    file_name, _ = QFileDialog.getSaveFileName(
        parent,
        "Save your Image",
        "",
        "Images (*.png *.jpeg *.jpg);;All Files (*)"
    )
    if file_name:
        pixmap.save(file_name)



def convert_to_pixmap(image = None):
    if isinstance(image, np.ndarray):
        img = image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape

        qimage = QImage(
            img.data,
            w,
            h,
            ch * w,
            QImage.Format.Format_RGB888
        )
        pixmap = QPixmap.fromImage(qimage)
        return pixmap



def open_image(parent=None):
    global path 
    global picture
    img, loc = get_image(parent)
    picture = img       # Image Matrix in ndarray
    path = loc          # Image Path
    return show_image(convert_to_pixmap(picture))
