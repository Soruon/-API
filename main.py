from design import main_window as mw
from constants import *
import requests
import io
from PIL import Image
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QFileDialog, \
    QGraphicsView

scale = 12
delta = 0.005


class MainWindow(QMainWindow):
    def __init__(self):
        self.delta = delta
        self.scale = scale
        self.type_ = 'map'
        super().__init__()
        self.initUI()
        self.Search_btn.clicked.connect(self.btn_request)
        self.coords_btn.clicked.connect(self.coord_btn)
        self.type1_btn.clicked.connect(lambda x: self.btn_type_map('Схема'))
        self.type2_btn.clicked.connect(lambda x: self.btn_type_map('Спутник'))
        self.type3_btn.clicked.connect(lambda x: self.btn_type_map('Гибрид'))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            pass
        elif event.key() == Qt.Key_Down:
            pass
        elif event.key() == Qt.Key_Left:
            pass
        elif event.key() == Qt.Key_Right:
            pass
        elif event.key() == Qt.Key_PageDown:
            if self.delta < 1:
                self.delta += 0.005
                self.delta = round(self.delta, 3)
                if self.lineEdit.text():
                    # coords
                    map_params = {
                        "ll": self.lineEdit.text(),
                        "spn": ",".join([str(self.delta), str(self.delta)]),
                        "l": self.type_
                    }
                    response = requests.get(map_api_server, params=map_params)
                    with io.open('image.jpg', 'wb') as file:
                        file.write(response.content)
                    self.img_ = QPixmap('image.jpg')
                    self.label_3.setPixmap(self.img_)
                elif self.Place.text():
                    # place
                    geocoder_params = {
                        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                        "geocode": self.Place.text(),
                        "format": "json"}
                    response = requests.get(geocoder_api_server, params=geocoder_params)
                    if not response:
                        self.Place.setText('Ошибка запроса')
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"][
                        "featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"]
                    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
                    map_params = {
                        "ll": ",".join([toponym_longitude, toponym_lattitude]),
                        "spn": ",".join([str(self.delta), str(self.delta)]),
                        "l": self.type_,
                        "z": str(self.scale)
                    }
                    response = requests.get(map_api_server, params=map_params)
                    with io.open('image.jpg', 'wb') as file:
                        file.write(response.content)
                    self.img_ = QPixmap('image.jpg')
                    self.label_3.setPixmap(self.img_)
                else:
                    self.label_3.setText('Введите место или координаты')
            else:
                pass
        elif event.key() == Qt.Key_PageUp:
            if self.delta > 0:
                self.delta -= 0.005
                self.delta = round(self.delta, 3)
                if self.lineEdit.text():
                    # coords
                    map_params = {
                        "ll": self.lineEdit.text(),
                        "spn": ",".join([str(self.delta), str(self.delta)]),
                        "l": self.type_
                    }
                    response = requests.get(map_api_server, params=map_params)
                    with io.open('image.jpg', 'wb') as file:
                        file.write(response.content)
                    self.img_ = QPixmap('image.jpg')
                    self.label_3.setPixmap(self.img_)
                elif self.Place.text():
                    # place
                    geocoder_params = {
                        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                        "geocode": self.Place.text(),
                        "format": "json"}
                    response = requests.get(geocoder_api_server, params=geocoder_params)
                    if not response:
                        self.Place.setText('Ошибка запроса')
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"][
                        "featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"]
                    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
                    map_params = {
                        "ll": ",".join([toponym_longitude, toponym_lattitude]),
                        "spn": ",".join([str(self.delta), str(self.delta)]),
                        "l": self.type_
                    }
                    response = requests.get(map_api_server, params=map_params)
                    with io.open('image.jpg', 'wb') as file:
                        file.write(response.content)
                    self.img_ = QPixmap('image.jpg')
                    self.label_3.setPixmap(self.img_)
                else:
                    self.label_3.setText('Введите место или координаты')
            else:
                pass

    def btn_request(self):
        self.delta = 0.005
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.Place.text(),
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            self.Place.setText('Ошибка запроса')
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([str(self.delta), str(self.delta)]),
            "l": "map"
        }
        response = requests.get(map_api_server, params=map_params)
        with io.open('image.jpg', 'wb') as file:
            file.write(response.content)
        self.img_ = QPixmap('image.jpg')
        self.label_3.setPixmap(self.img_)

    def coord_btn(self):
        self.delta = 0.005
        map_params = {
            "ll": self.lineEdit.text(),
            "spn": ",".join([str(self.delta), str(self.delta)]),
            "l": "map"
        }
        response = requests.get(map_api_server, params=map_params)
        with io.open('image.jpg', 'wb') as file:
            file.write(response.content)
        self.img_ = QPixmap('image.jpg')
        self.label_3.setPixmap(self.img_)

    def btn_type_map(self, btn_text):
        if btn_text == 'Схема':
            self.type_of_data('map')
        elif btn_text == 'Спутник':
            self.type_of_data('sat')
        elif btn_text == 'Гибрид':
            self.type_of_data('sat,skl')

    def initUI(self):
        f = io.StringIO(mw)
        uic.loadUi(f, self)

    def type_of_data(self, type_):
        self.type_ = type_
        if self.lineEdit.text():
            # coords
            map_params = {
                "ll": self.lineEdit.text(),
                "spn": ",".join([str(self.delta), str(self.delta)]),
                "l": type_
            }
            response = requests.get(map_api_server, params=map_params)
            with io.open('image.jpg', 'wb') as file:
                file.write(response.content)
            self.img_ = QPixmap('image.jpg')
            self.label_3.setPixmap(self.img_)
        elif self.Place.text():
            # place
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": self.Place.text(),
                "format": "json"}
            response = requests.get(geocoder_api_server, params=geocoder_params)
            if not response:
                self.Place.setText('Ошибка запроса')
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
            map_params = {
                "ll": ",".join([toponym_longitude, toponym_lattitude]),
                "spn": ",".join([str(self.delta), str(self.delta)]),
                "l": type_
            }
            response = requests.get(map_api_server, params=map_params)
            with io.open('image.jpg', 'wb') as file:
                file.write(response.content)
            self.img_ = QPixmap('image.jpg')
            self.label_3.setPixmap(self.img_)
        else:
            self.label_3.setText('Введите место или координаты')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
