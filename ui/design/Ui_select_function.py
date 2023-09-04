# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_function.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 151)
        self.select_funcion_combo = QComboBox(Form)
        self.select_funcion_combo.addItem("")
        self.select_funcion_combo.addItem("")
        self.select_funcion_combo.setObjectName(u"select_funcion_combo")
        self.select_funcion_combo.setGeometry(QRect(130, 40, 141, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 71, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 90, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"OfflineSubtitle", None))
        self.select_funcion_combo.setItemText(0, QCoreApplication.translate("Form", u"gpt\u8bed\u97f3\u804a\u5929", None))
        self.select_funcion_combo.setItemText(1, QCoreApplication.translate("Form", u"\u7cfb\u7edf\u58f0\u97f3\u79bb\u7ebf\u5b57\u5e55", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u529f\u80fd", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

