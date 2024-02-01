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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.Search_btn.clicked.connect(self.btn_request)

    def btn_request(self):
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
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        response = requests.get(map_api_server, params=map_params)
        with io.open('image.jpg', 'wb') as file:
            file.write(response.content)
        self.img_ = QPixmap('image.jpg')
        self.label_3.setPixmap(self.img_)

    def init(self):
        pass

    def initUI(self):
        f = io.StringIO(mw)
        uic.loadUi(f, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
