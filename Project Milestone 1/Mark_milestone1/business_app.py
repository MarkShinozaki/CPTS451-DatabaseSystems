# Mark Shinozaki
# Milestone 1 

import psycopg2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QListWidget

class BusinessApp(QWidget):
    def __init__(self):
        super().__init__()

        self.conn = psycopg2.connect(
            dbname="milestone1DB",
            user="postgres",
            password="jn&!!8tCK6H",
            host="localhost"
        )
        self.cursor = self.conn.cursor()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.stateComboBox = QComboBox()
        self.stateComboBox.activated[str].connect(self.onStateChanged)
        layout.addWidget(self.stateComboBox)

        self.cityComboBox = QComboBox()
        self.cityComboBox.activated[str].connect(self.onCityChanged)
        layout.addWidget(self.cityComboBox)

        self.businessList = QListWidget()
        layout.addWidget(self.businessList)

        self.setLayout(layout)

        self.loadStates()

    def loadStates(self):
        self.cursor.execute("SELECT DISTINCT state FROM business ORDER BY state;")
        states = self.cursor.fetchall()
        self.stateComboBox.addItem("Select State")
        for state in states:
            self.stateComboBox.addItem(state[0])

    def onStateChanged(self, state):
        self.cityComboBox.clear()
        self.cursor.execute("SELECT DISTINCT city FROM business WHERE state=%s ORDER BY city;", (state,))
        cities = self.cursor.fetchall()
        self.cityComboBox.addItem("Select City")
        for city in cities:
            self.cityComboBox.addItem(city[0])

    def onCityChanged(self, city):
        self.businessList.clear()
        state = self.stateComboBox.currentText()
        self.cursor.execute("SELECT name, city, state FROM business WHERE city=%s AND state=%s ORDER BY name;", (city, state))
        businesses = self.cursor.fetchall()
        for business in businesses:
            self.businessList.addItem(f"{business[0]} - {business[1]}, {business[2]}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BusinessApp()
    ex.setWindowTitle('CptS 451 Milestone-1')
    ex.show()
    sys.exit(app.exec_())
