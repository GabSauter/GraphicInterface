import sys
from MainUi import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QPoint


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCreatePoint.clicked.connect(self.clickBtnPoint)
        self.ui.btnCreateTriangle.clicked.connect(self.clickBtnTriangle)
        self.ui.btnCreatePolygon.clicked.connect(self.clickBtnPolygon)
        self.ui.btnLeft.clicked.connect(self.clickBtnLeft)
        self.ui.btnRight.clicked.connect(self.clickBtnRight)
        self.ui.btnUp.clicked.connect(self.clickBtnUp)
        self.ui.btnDown.clicked.connect(self.clickBtnDown)
        self.ui.btnRotateLeft.clicked.connect(self.clickBtnRotateLeft)
        self.ui.btnRotateRight.clicked.connect(self.clickBtnRotateRight)
        self.ui.btnScaleMinus.clicked.connect(self.clickBtnScaleMinus)
        self.ui.btnScalePlus.clicked.connect(self.clickBtnScalePlus)

        self.ui.btnCreateBezierCurve.clicked.connect(self.clickBtnCreateBezier)

    def clickBtnPoint(self):
        try:
            x = int(float(self.ui.editX.text())*self.ui.viewPort.width()/2)
            y = int(float(self.ui.editY.text())*self.ui.viewPort.width()/2)

            self.ui.viewPort.pointCoords.append(QPoint(x, -y))

            self.ui.viewPort.hasPointFunc()

            self.ui.editY.setText("")
            self.ui.editX.setText("")
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada das coordenadas do ponto precisa de dois números.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnTriangle(self):
        try:
            x = int(float(self.ui.editTriangleX.text())
                    * self.ui.viewPort.width()/2)
            y = int(float(self.ui.editTriangleY.text())
                    * self.ui.viewPort.width()/2)
            x2 = int(float(self.ui.editTriangleX_2.text())
                     * self.ui.viewPort.width()/2)
            y2 = int(float(self.ui.editTriangleY_2.text())
                     * self.ui.viewPort.width()/2)
            x3 = int(float(self.ui.editTriangleX_3.text())
                     * self.ui.viewPort.width()/2)
            y3 = int(float(self.ui.editTriangleY_3.text())
                     * self.ui.viewPort.width()/2)

            self.ui.viewPort.trianglesCoords.append(x)
            self.ui.viewPort.trianglesCoords.append(-1*(y))
            self.ui.viewPort.trianglesCoords.append(x2)
            self.ui.viewPort.trianglesCoords.append(-1*(y2))
            self.ui.viewPort.trianglesCoords.append(x3)
            self.ui.viewPort.trianglesCoords.append(-1*(y3))

            self.ui.viewPort.hasTriangleFunc()

            self.ui.editTriangleY.setText("")
            self.ui.editTriangleY_2.setText("")
            self.ui.editTriangleY_3.setText("")
            self.ui.editTriangleX.setText("")
            self.ui.editTriangleX_2.setText("")
            self.ui.editTriangleX_3.setText("")
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada das coordenadas do triângulo precisa de seis números.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnPolygon(self):
        try:
            polygonString = str(self.ui.editPolygon.text())
            polygonCoords = polygonString.split(",")

            if(len(polygonCoords) % 2 == 0):
                polygonCoords = [float(x) for x in polygonCoords]

                for i in range(0, len(polygonCoords)):
                    if i % 2 == 0:
                        self.ui.viewPort.polygonCoordsV.append(
                            int((polygonCoords[i]*self.ui.viewPort.width()/2)))
                    else:
                        self.ui.viewPort.polygonCoordsV.append(
                            int(-1*(polygonCoords[i]*self.ui.viewPort.width()/2)))

                self.ui.viewPort.polygonCoordsVLen.append(len(polygonCoords))
                self.ui.viewPort.hasPolygonFunc()
            else:
                QMessageBox.about(
                    self, 'Erro', 'Está faltando coordenadas, "x1,y1,x2,y2,x3,y3,...,xn,yn"')
                pass
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada das coordenadas do polígono precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais\nE use vírgula "," para separar as coordenadas')
            pass
        self.ui.editPolygon.setText("")

    def clickBtnLeft(self):
        try:
            translateString = int(float(self.ui.editTranslation.text())
                                  * self.ui.viewPort.width()/2)
            self.ui.viewPort.translateFunc(-translateString, 0)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para translação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnRight(self):
        try:
            translateString = int(float(self.ui.editTranslation.text())
                                  * self.ui.viewPort.width()/2)
            self.ui.viewPort.translateFunc(translateString, 0)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para translação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnUp(self):
        try:
            translateString = int(float(self.ui.editTranslation.text())
                                  * self.ui.viewPort.width()/2)
            self.ui.viewPort.translateFunc(0, -translateString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para translação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnDown(self):
        try:
            translateString = int(float(self.ui.editTranslation.text())
                                  * self.ui.viewPort.width()/2)
            self.ui.viewPort.translateFunc(0, translateString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para translação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnRotateLeft(self):
        try:
            rotateString = float(self.ui.editRotate.text())
            self.ui.viewPort.rotate(-rotateString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para rotação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnRotateRight(self):
        try:
            rotateString = float(self.ui.editRotate.text())
            self.ui.viewPort.rotate(rotateString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para rotação precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnScaleMinus(self):
        try:
            scaleString = float(self.ui.editScale.text())
            self.ui.viewPort.scale(1/scaleString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para escala precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnScalePlus(self):
        try:
            scaleString = float(self.ui.editScale.text())
            self.ui.viewPort.scale(scaleString)
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para escala precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def clickBtnCreateBezier(self):
        try:
            bezierString = str(self.ui.editBezierCurve.text())
            bezierCoordsV = bezierString.split(",")
            if (len(bezierCoordsV) == 6):
                bezierCoordsV = [float(x) for x in bezierCoordsV]

                for i in range(0, len(bezierCoordsV)):
                    if i % 2 == 0:
                        self.ui.viewPort.bezierCoords.append(
                            int((bezierCoordsV[i]*self.ui.viewPort.width()/2)))
                    else:
                        self.ui.viewPort.bezierCoords.append(
                            int(-1*(bezierCoordsV[i]*self.ui.viewPort.width()/2)))

                self.ui.viewPort.hasBezierFunc()

            else:
                QMessageBox.about(
                    self, 'Erro', 'Coloque 3 coordenadas na curva de Bézier.\nExemplo: x1,y1,x2,y2,x3,y3')
                pass
        except Exception:
            self.createMessageBox(
                'Erro', 'Entrada da coordenada para a curva de Bezier precisa ser número.\nUse ponto "." em vez de vírgula "," para números decimais')
            pass

    def createMessageBox(self, title, description):
        QMessageBox.about(
            self, title, description)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
