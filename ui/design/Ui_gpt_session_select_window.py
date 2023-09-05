# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpt_session_select_window.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_gpt_session_select(object):
    def setupUi(self, gpt_session_select):
        if not gpt_session_select.objectName():
            gpt_session_select.setObjectName(u"gpt_session_select")
        gpt_session_select.resize(402, 339)
        self.listWidget = QListWidget(gpt_session_select)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 20, 241, 301))
        self.widget = QWidget(gpt_session_select)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 60, 77, 86))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.view_btn = QPushButton(self.widget)
        self.view_btn.setObjectName(u"view_btn")

        self.verticalLayout.addWidget(self.view_btn)

        self.confirm_btn = QPushButton(self.widget)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.verticalLayout.addWidget(self.confirm_btn)

        self.cancel_btn = QPushButton(self.widget)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.verticalLayout.addWidget(self.cancel_btn)


        self.retranslateUi(gpt_session_select)

        QMetaObject.connectSlotsByName(gpt_session_select)
    # setupUi

    def retranslateUi(self, gpt_session_select):
        gpt_session_select.setWindowTitle(QCoreApplication.translate("gpt_session_select", u"\u9009\u62e9GPT\u4f1a\u8bdd", None))
        self.view_btn.setText(QCoreApplication.translate("gpt_session_select", u"\u67e5\u770b", None))
        self.confirm_btn.setText(QCoreApplication.translate("gpt_session_select", u"\u786e\u8ba4", None))
        self.cancel_btn.setText(QCoreApplication.translate("gpt_session_select", u"\u53d6\u6d88", None))
    # retranslateUi

