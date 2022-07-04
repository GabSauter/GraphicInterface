from asyncio.windows_events import NULL
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QBrush, QPen, QPainter, QPolygon, QColor, QPainterPath
from PyQt5.QtCore import QPoint, QRect, Qt
import math


class ViewPort(QWidget):
    hasPoint = False
    hasTriangle = False
    hasPolygon = False
    hasBezier = False

    pointCoords = []
    trianglesCoords = []
    bezierCoords = []

    polygonCoordsV = []
    polygonCoordsVLen = []

    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.fillRect(e.rect(), Qt.white)
        painter.setClipRect(e.rect())  # Faz o clipping

        # Faz com que a coordenada do meio fique no (0,0)
        painter.setWindow(QRect(-275, -275, 550, 550))

        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(254, 215, 102), Qt.SolidPattern))

        if(self.hasPoint):
            for i in self.pointCoords:
                painter.drawPoint(i)

        if(self.hasTriangle):
            for i in range(0, len(self.trianglesCoords), 6):
                painter.drawPolygon(QPolygon([QPoint(self.trianglesCoords[i], self.trianglesCoords[i+1]), QPoint(
                    self.trianglesCoords[i+2], self.trianglesCoords[i+3]), QPoint(self.trianglesCoords[i+4], self.trianglesCoords[i+5])]))

        if(self.hasPolygon):
            start = 0
            for i in range(0, len(self.polygonCoordsVLen)):
                polygon = QPolygon([])
                for j in range(start, self.polygonCoordsVLen[i]+start, 2):
                    polygon.append(
                        QPoint(self.polygonCoordsV[j], self.polygonCoordsV[j+1]))
                start += self.polygonCoordsVLen[i]
                painter.drawPolygon(polygon)

        if(self.hasBezier):
            for i in range(0,  len(self.bezierCoords), 6):
                path = QPainterPath(
                    QPoint(self.bezierCoords[i], self.bezierCoords[i+1]))

                path.cubicTo(self.bezierCoords[i], self.bezierCoords[i+1],  self.bezierCoords[i+2],
                             self.bezierCoords[i+3],  self.bezierCoords[i+4], self.bezierCoords[i+5])
                painter.drawPath(path)

    def hasPointFunc(self):
        self.hasPoint = True
        self.repaint()

    def hasTriangleFunc(self):
        self.hasTriangle = True
        self.repaint()

    def hasPolygonFunc(self):
        self.hasPolygon = True
        self.repaint()

    def hasBezierFunc(self):
        self.hasBezier = True
        self.repaint()

    def translateFunc(self, x, y):

        for i in self.pointCoords:
            i.setX(i.x() + x)
            i.setY(i.y() + y)

        for i in range(0, len(self.trianglesCoords), 6):
            self.trianglesCoords[i] += x
            self.trianglesCoords[i+2] += x
            self.trianglesCoords[i+4] += x

            self.trianglesCoords[i+1] += y
            self.trianglesCoords[i+3] += y
            self.trianglesCoords[i+5] += y

        for i in range(len(self.polygonCoordsV)):
            if i % 2 == 0:
                self.polygonCoordsV[i] += x
            else:
                self.polygonCoordsV[i] += y

        for i in range(0, len(self.bezierCoords), 6):
            self.bezierCoords[i] += x
            self.bezierCoords[i+2] += x
            self.bezierCoords[i+4] += x

            self.bezierCoords[i+1] += y
            self.bezierCoords[i+3] += y
            self.bezierCoords[i+5] += y
        self.repaint()

    def rotate(self, angle):

        def rotationX(px, py):
            return int(0 + math.cos(angle) * (px - 0) -
                       math.sin(angle) * (py - 0))

        def rotationY(px, py):
            return int(0 + math.sin(angle) * (px - 0) +
                       math.cos(angle) * (py - 0))

        for i in self.pointCoords:
            pointX = rotationX(i.x(), i.y())
            pointY = rotationY(i.x(), i.y())
            i.setX(pointX)
            i.setY(pointY)

        for i in range(0, len(self.trianglesCoords), 2):

            pointX = rotationX(
                self.trianglesCoords[i], self.trianglesCoords[i+1])
            pointY = rotationY(
                self.trianglesCoords[i], self.trianglesCoords[i+1])
            self.trianglesCoords[i] = pointX
            self.trianglesCoords[i+1] = pointY

        for i in range(0, len(self.polygonCoordsV), 2):
            pointX = rotationX(
                self.polygonCoordsV[i], self.polygonCoordsV[i+1])
            pointY = rotationY(
                self.polygonCoordsV[i], self.polygonCoordsV[i+1])

            self.polygonCoordsV[i] = pointX
            self.polygonCoordsV[i+1] = pointY

        for i in range(0, len(self.bezierCoords), 2):
            pointX = rotationX(
                self.bezierCoords[i], self.bezierCoords[i+1])
            pointY = rotationY(
                self.bezierCoords[i], self.bezierCoords[i+1])

            self.bezierCoords[i] = pointX
            self.bezierCoords[i+1] = pointY

        self.repaint()

    def scale(self, scaleValue):

        for point in self.pointCoords:
            point *= scaleValue

        for i in range(0, len(self.trianglesCoords)):
            self.trianglesCoords[i] = int(self.trianglesCoords[i] * scaleValue)

        for i in range(0, len(self.polygonCoordsV)):
            self.polygonCoordsV[i] = int(self.polygonCoordsV[i]*scaleValue)

        for i in range(0, len(self.bezierCoords)):
            self.bezierCoords[i] = int(self.bezierCoords[i]*scaleValue)

        self.repaint()
