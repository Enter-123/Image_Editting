from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys 
from image_processor import convert_CVT, convert_to_pixmap, save_image, open_image


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Getting Started with OpenCV")
        self.resize(1000, 550)

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.original_image = None
        self.current_image = None

        self.image = QLabel("Select a Image to Display")   # Objects are mutable
        self.image_name = QLineEdit("Enter Image Name")   # Objects are mutable


        self.open_image_button = QPushButton("Open Image")
        self.close_image = QPushButton("Close Image")
        self.gray_convert_button = QPushButton("Convert to Gray Scale")
        self.save_image_button = QPushButton("Save Image")
        self.undo_button = QPushButton("Undo")

        
        self.save_image_button.clicked.connect(lambda : save_image(self.image_name.text(), self.current_image))
        self.open_image_button.clicked.connect(self.display_image)
        self.close_image.clicked.connect(self.clear_buttonImage)
        self.gray_convert_button.clicked.connect(self.gray_conversion)
        self.undo_button.clicked.connect(lambda : self.image.setPixmap(convert_to_pixmap(self.original_image).scaled(
            650,
            650,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )))


        self.close_image.setEnabled(False)
        self.gray_convert_button.setEnabled(False)
        self.save_image_button.setEnabled(False)


        self.main_layout = QHBoxLayout()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.v3_layout = QVBoxLayout()
        self.setCentralWidget(self.container)

        self.v2_layout.addWidget(QLabel("Image Processing Application"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addStretch()    
        self.v2_layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v2_layout.addStretch()

        self.v1_layout.addWidget(self.open_image_button)
        self.v1_layout.addWidget(self.gray_convert_button)
        self.v1_layout.addWidget(self.undo_button)
        self.v3_layout.addWidget(self.close_image)
        self.v3_layout.addWidget(self.save_image_button)
        self.v3_layout.addWidget(self.image_name)
        self.v3_layout.addWidget(QPushButton("Button 6"))

        self.main_layout.addLayout(self.v1_layout, 1)
        self.main_layout.addLayout(self.v2_layout, 6)
        self.main_layout.addLayout(self.v3_layout, 1)

        self.container.setLayout(self.main_layout)

    def gray_conversion(self):
        self.current_image = convert_CVT(self.current_image)

        pixmap = convert_to_pixmap(self.current_image)
        self.image.setPixmap(
            pixmap.scaled(
                650,
                650,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )       


    def clear_buttonImage(self):
        self.image.setText("Select a Image to Display")
        self.close_image.setEnabled(False)
        self.gray_convert_button.setEnabled(False)
        self.save_image_button.setEnabled(False)
         

    def display_image(self):
        pixmap, loc = open_image(self)
        if pixmap is None:
            return None

        self.original_image = pixmap.copy()
        self.current_image = pixmap.copy()
        self.image_path = loc

        pixmap = convert_to_pixmap(self.current_image)

        self.image.setPixmap(
            pixmap.scaled(
                650,
                650,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.close_image.setEnabled(True)
        self.gray_convert_button.setEnabled(True)
        self.save_image_button.setEnabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()