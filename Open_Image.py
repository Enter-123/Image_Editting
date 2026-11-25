from PySide6.QtWidgets import *
from PySide6.QtGui import *
import cv2
# from experiment_1 import window


def get_image(parent=None):
    name, _ = QFileDialog.getOpenFileName(
        parent,
        "Select a Image File",
        "",
        "Images (*.png *.jpg *.jpeg *.gif);;All Files (*)"
    )
    if name is None:
        return None, None
    
    image = cv2.imread(name)

    if image is None:
        return None, None

    return image, name

