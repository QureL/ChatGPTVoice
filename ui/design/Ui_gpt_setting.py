# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpt_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_GPT_Setting(object):
    def setupUi(self, GPT_Setting):
        if not GPT_Setting.objectName():
            GPT_Setting.setObjectName(u"GPT_Setting")
        GPT_Setting.resize(385, 259)
        self.verticalLayout = QVBoxLayout(GPT_Setting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GPT_Setting)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox_context_cnt = QSpinBox(GPT_Setting)
        self.spinBox_context_cnt.setObjectName(u"spinBox_context_cnt")
        self.spinBox_context_cnt.setMinimum(0)
        self.spinBox_context_cnt.setValue(10)

        self.horizontalLayout.addWidget(self.spinBox_context_cnt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(GPT_Setting)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(GPT_Setting)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(GPT_Setting)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.textEdit_system_cmd = QTextEdit(GPT_Setting)
        self.textEdit_system_cmd.setObjectName(u"textEdit_system_cmd")

        self.horizontalLayout_3.addWidget(self.textEdit_system_cmd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(GPT_Setting)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.doubleSpinBox_speak_speed = QDoubleSpinBox(GPT_Setting)
        self.doubleSpinBox_speak_speed.setObjectName(u"doubleSpinBox_speak_speed")
        self.doubleSpinBox_speak_speed.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_speak_speed)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_confirm = QPushButton(GPT_Setting)
        self.btn_confirm.setObjectName(u"btn_confirm")

        self.horizontalLayout_4.addWidget(self.btn_confirm)

        self.btn_cancel = QPushButton(GPT_Setting)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(GPT_Setting)

        QMetaObject.connectSlotsByName(GPT_Setting)
    # setupUi

    def retranslateUi(self, GPT_Setting):
        GPT_Setting.setWindowTitle(QCoreApplication.translate("GPT_Setting", u"GPT\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("GPT_Setting", u"\u4e0a\u4e0b\u6587\u6570\u91cf", None))
        self.label_2.setText(QCoreApplication.translate("GPT_Setting", u"\u6a21\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("GPT_Setting", u"gpt-3.5-turbo", None))

        self.label_3.setText(QCoreApplication.translate("GPT_Setting", u"\u9884\u7f6e\u6307\u4ee4", None))
        self.label_4.setText(QCoreApplication.translate("GPT_Setting", u"AI\u8bed\u901f", None))
        self.btn_confirm.setText(QCoreApplication.translate("GPT_Setting", u"\u786e\u5b9a", None))
        self.btn_cancel.setText(QCoreApplication.translate("GPT_Setting", u"\u53d6\u6d88", None))
    # retranslateUi

