from PyQt4 import QtCore, QtGui


class DigitalClock(QtGui.QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__()

        self.setSegmentStyle(QtGui.QLCDNumber.Flat)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(300,60)

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
##        if (time.second()% 2) == 0:
##            text = text[:2] + ' ' + text[3:]

        nDigits = 8
        self.setNumDigits(nDigits)
        self.display(text)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())    
