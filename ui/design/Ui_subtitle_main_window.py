# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subtitle_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_subtitle_main(object):
    def setupUi(self, subtitle_main):
        if not subtitle_main.objectName():
            subtitle_main.setObjectName(u"subtitle_main")
        subtitle_main.resize(400, 300)
        self.verticalLayout = QVBoxLayout(subtitle_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(subtitle_main)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.subtitle_input_select_combo = QComboBox(subtitle_main)
        self.subtitle_input_select_combo.setObjectName(u"subtitle_input_select_combo")

        self.horizontalLayout.addWidget(self.subtitle_input_select_combo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(subtitle_main)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.subtitle_model_select_combo = QComboBox(subtitle_main)
        self.subtitle_model_select_combo.setObjectName(u"subtitle_model_select_combo")

        self.horizontalLayout_2.addWidget(self.subtitle_model_select_combo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(subtitle_main)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.subtitle_language_select_combo = QComboBox(subtitle_main)
        self.subtitle_language_select_combo.setObjectName(u"subtitle_language_select_combo")

        self.horizontalLayout_3.addWidget(self.subtitle_language_select_combo)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_env_btn = QPushButton(subtitle_main)
        self.check_env_btn.setObjectName(u"check_env_btn")

        self.horizontalLayout_4.addWidget(self.check_env_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_btn = QPushButton(subtitle_main)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_5.addWidget(self.start_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(subtitle_main)

        QMetaObject.connectSlotsByName(subtitle_main)
    # setupUi

    def retranslateUi(self, subtitle_main):
        subtitle_main.setWindowTitle(QCoreApplication.translate("subtitle_main", u"horn", None))
        self.label.setText(QCoreApplication.translate("subtitle_main", u"\u9009\u62e9\u8f93\u5165\u8bbe\u5907", None))
        self.label_2.setText(QCoreApplication.translate("subtitle_main", u"\u6a21\u578b\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("subtitle_main", u"\u8bed\u8a00", None))
        self.check_env_btn.setText(QCoreApplication.translate("subtitle_main", u"\u73af\u5883\u68c0\u6d4b", None))
        self.start_btn.setText(QCoreApplication.translate("subtitle_main", u"\u542f\u52a8", None))
    # retranslateUi

