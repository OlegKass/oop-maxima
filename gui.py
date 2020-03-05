"""import PyQt5 as pq"""
import PyQt5.QtWidgets  as pqs

if __name__ == '__main__':

    app = pqs.QApplication([])
    label = pqs.QLabel('Hello World!')
    label.show()
    app.exec()
