# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
    QLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_setting_window(object):
    def setupUi(self, setting_window):
        if not setting_window.objectName():
            setting_window.setObjectName(u"setting_window")
        setting_window.resize(358, 547)
        self.verticalLayout = QVBoxLayout(setting_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gpt_setting = QTabWidget(setting_window)
        self.gpt_setting.setObjectName(u"gpt_setting")
        self.subtitle_set = QWidget()
        self.subtitle_set.setObjectName(u"subtitle_set")
        self.verticalLayout_2 = QVBoxLayout(self.subtitle_set)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.subtitle_set)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 312, 447))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.subtitle_sample_time = QSpinBox(self.scrollAreaWidgetContents)
        self.subtitle_sample_time.setObjectName(u"subtitle_sample_time")
        self.subtitle_sample_time.setValue(10)

        self.horizontalLayout_4.addWidget(self.subtitle_sample_time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.subtitle_mode_select_combo = QComboBox(self.scrollAreaWidgetContents)
        self.subtitle_mode_select_combo.addItem("")
        self.subtitle_mode_select_combo.addItem("")
        self.subtitle_mode_select_combo.setObjectName(u"subtitle_mode_select_combo")

        self.horizontalLayout_5.addWidget(self.subtitle_mode_select_combo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.subtitle_confirm = QPushButton(self.subtitle_set)
        self.subtitle_confirm.setObjectName(u"subtitle_confirm")

        self.horizontalLayout_3.addWidget(self.subtitle_confirm)

        self.subtitle_setting_cancel = QPushButton(self.subtitle_set)
        self.subtitle_setting_cancel.setObjectName(u"subtitle_setting_cancel")

        self.horizontalLayout_3.addWidget(self.subtitle_setting_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gpt_setting.addTab(self.subtitle_set, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gpt_setting.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.gpt_setting)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(setting_window)

        self.gpt_setting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(setting_window)
    # setupUi

    def retranslateUi(self, setting_window):
        setting_window.setWindowTitle(QCoreApplication.translate("setting_window", u"Setting", None))
        self.label.setText(QCoreApplication.translate("setting_window", u"\u91c7\u6837\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("setting_window", u"\u6a21\u5f0f", None))
        self.subtitle_mode_select_combo.setItemText(0, QCoreApplication.translate("setting_window", u"\u672c\u5730", None))
        self.subtitle_mode_select_combo.setItemText(1, QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b", None))

        self.label_3.setText(QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b\u5730\u5740", None))
        self.subtitle_confirm.setText(QCoreApplication.translate("setting_window", u"\u786e\u5b9a", None))
        self.subtitle_setting_cancel.setText(QCoreApplication.translate("setting_window", u"\u53d6\u6d88", None))
        self.gpt_setting.setTabText(self.gpt_setting.indexOf(self.subtitle_set), QCoreApplication.translate("setting_window", u"\u5b9e\u65f6\u5b57\u5e55", None))
        self.gpt_setting.setTabText(self.gpt_setting.indexOf(self.tab_2), QCoreApplication.translate("setting_window", u"gpt\u8bed\u97f3", None))
    # retranslateUi

