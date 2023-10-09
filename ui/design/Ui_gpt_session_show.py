# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpt_session_show.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QWidget)

class Ui_gpt_show_session(object):
    def setupUi(self, gpt_show_session):
        if not gpt_show_session.objectName():
            gpt_show_session.setObjectName(u"gpt_show_session")
        gpt_show_session.resize(400, 333)
        self.textBrowser = QTextBrowser(gpt_show_session)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 381, 311))

        self.retranslateUi(gpt_show_session)

        QMetaObject.connectSlotsByName(gpt_show_session)
    # setupUi

    def retranslateUi(self, gpt_show_session):
        gpt_show_session.setWindowTitle(QCoreApplication.translate("gpt_show_session", u"Show Session", None))
    # retranslateUi

