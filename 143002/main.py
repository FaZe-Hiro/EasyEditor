#создай тут фоторедактор Easy Editor!
from PIL import Image,ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL.ImageFilter import SHARPEN
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QLabel,QListWidget,QFileDialog
app = QApplication([])
main_win = QWidget()
#интерфейс
ggg = QLabel('Картинка')
btn_p = QPushButton('Папка')
btn_l = QPushButton('Лево')
btn_r = QPushButton('Право')
btn_z = QPushButton('Зеркало')
btn_k = QPushButton('Размытие')
btn_m = QPushButton('Ч/Б')
btn_c = QPushButton('Контур')
list1 = QListWidget()
main_win.resize(1280,720)
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QHBoxLayout()
col4 = QHBoxLayout()
row = QHBoxLayout()
col1.addWidget(btn_p)
col1.addWidget(list1)
col2.addWidget(ggg)
col3.addWidget(btn_l)
col3.addWidget(btn_r)
col3.addWidget(btn_k)
col3.addWidget(btn_m)
col3.addWidget(btn_z)
col3.addWidget(btn_c)
col2.addLayout(col3)
col4.addLayout(col1)
col4.addLayout(col2)
main_win.setLayout(col4)
#для папки
workdir = ''
extentions = ['.jpeg','.jpg']

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files,extentions):
    m = []
    for file in files:
        for ext in extentions:
            if file.endswith(ext):
                m.append(file)
    return m
def showFilenameslist():
    extentions = ['.jpeg','.jpg']
    global workdir
    chooseWorkdir()
    filenames = os.listdir(workdir)
    names = filter(filenames,extentions)
    list1.clear()
    for name in names:
        list1.addItem(name)
btn_p.clicked.connect(showFilenameslist)
list1.clear()
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = 'modf/'
    def loadImage(self,filename):
        self.filename = filename
        image_path = os.path.join(workdir,filename)
        self.image = Image.open(image_path)
    def showImage(label,path):
        ggg.hide()
        pixmapimage = QPixmap(path)
        w, h = ggg.width(), ggg.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        ggg.setPixmap(pixmapimage)
        ggg.show()

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_transpose(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
def showChosenImage():
    if list1.currentRow() >= 0:
        filename = list1.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
workimage = ImageProcessor()
btn_m.clicked.connect(workimage.do_bw)
btn_k.clicked.connect(workimage.do_blur)
btn_l.clicked.connect(workimage.do_transpose)
btn_r.clicked.connect(workimage.do_right)
btn_z.clicked.connect(workimage.do_flip)
btn_c.clicked.connect(workimage.do_contour)
list1.currentRowChanged.connect(showChosenImage)
main_win.show()
app.exec_()         
