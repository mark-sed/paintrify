import generator as generator
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QAction,
                             QPushButton,
                             QFileDialog,
                             QLabel,
                             QLineEdit,
                             QFormLayout,
                             QSlider, 
                             QCheckBox,
                             QProgressBar,
                             QComboBox,
                             QWidgetAction,
                             QSizePolicy,
                             QTextBrowser,
                             QMessageBox)
import numpy
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import (QPixmap,
                         QIntValidator)


class GUI(QMainWindow):
    """
    Main Paintrify windows
    """

    def __init__(self, config, argparser, info_method):
        """
        Constructor
        :param config Configuration class
        :param argparser Argument parser class
        """
        super(GUI, self).__init__()
        self.config = config
        self.argparser = argparser
        self.info = info_method

        # Window
        self.setWindowTitle("Paintrify")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)

        # Input form
        self.form_layout = QFormLayout()

        # Generate button
        self.randomize_button = QPushButton("Randomize 🎲", self)
        self.randomize_button.pressed.connect(self.randomize)
        self.form_layout.addRow(self.randomize_button)

        # Generate button
        self.generate_button = QPushButton("Generate", self)
        self.generate_button.pressed.connect(self.generate)
        self.form_layout.addRow(self.generate_button)

        # Apply layout
        widg = QtWidgets.QWidget(self)
        self.setCentralWidget(widg)
        widg.setLayout(self.form_layout)
        self.update()
        self.show()

    def randomize(self):
        """
        Randomization
        """

    def generate(self):
        """
        Image generation
        """
        self.info("Image generation started")
        self.gen = generator.Generator(self.config, self.info)
        img = self.gen.generate()
        self.editor = Editor(self, img, self.config, self.info)

class Editor(QMainWindow):
    """
    Editor window
    """

    def __init__(self, parent, image, config, info_method):
        """
        Constructor
        :param config Configuration class
        :param argparser Argument parser class
        """
        super(Editor, self).__init__(parent)
        self.config = config
        self.info = info_method
        self.image = image

        # Window
        self.setWindowTitle("Paintrify Editor")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        
        # Convert numpy array to image and display it
        qim = ImageQt(Image.fromarray(image, 'RGBA'))
        pix = QtGui.QPixmap.fromImage(qim)

        self.img_label = QLabel(self)
        self.img_label.setPixmap(pix)
        self.img_label.adjustSize()

        self.resize(self.config.width, self.config.height)
        self.update()

        self.show()


