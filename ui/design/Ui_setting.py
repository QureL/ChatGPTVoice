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
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 312, 447))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.line_edit_api_base = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_api_base.setObjectName(u"line_edit_api_base")

        self.horizontalLayout_2.addWidget(self.line_edit_api_base)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.line_edit_api_key = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_api_key.setObjectName(u"line_edit_api_key")

        self.horizontalLayout_7.addWidget(self.line_edit_api_key)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.spin_box_context_cnt = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spin_box_context_cnt.setObjectName(u"spin_box_context_cnt")
        self.spin_box_context_cnt.setValue(20)

        self.horizontalLayout_8.addWidget(self.spin_box_context_cnt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.spin_box_speak_speed = QSpinBox(self.scrollAreaWidgetContents_2)
        self.spin_box_speak_speed.setObjectName(u"spin_box_speak_speed")
        self.spin_box_speak_speed.setValue(9)

        self.horizontalLayout_9.addWidget(self.spin_box_speak_speed)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.combo_box_s2t_mode = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_box_s2t_mode.addItem("")
        self.combo_box_s2t_mode.addItem("")
        self.combo_box_s2t_mode.setObjectName(u"combo_box_s2t_mode")

        self.horizontalLayout_11.addWidget(self.combo_box_s2t_mode)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.line_edit_s2t_remote_address = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_s2t_remote_address.setObjectName(u"line_edit_s2t_remote_address")

        self.horizontalLayout_12.addWidget(self.line_edit_s2t_remote_address)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.combox_box_t2s_mode = QComboBox(self.scrollAreaWidgetContents_2)
        self.combox_box_t2s_mode.addItem("")
        self.combox_box_t2s_mode.addItem("")
        self.combox_box_t2s_mode.setObjectName(u"combox_box_t2s_mode")

        self.horizontalLayout_13.addWidget(self.combox_box_t2s_mode)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.line_edit_t2s_remote_address = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_t2s_remote_address.setObjectName(u"line_edit_t2s_remote_address")

        self.horizontalLayout_14.addWidget(self.line_edit_t2s_remote_address)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_gpt_setting_confirm = QPushButton(self.tab_2)
        self.btn_gpt_setting_confirm.setObjectName(u"btn_gpt_setting_confirm")

        self.horizontalLayout_10.addWidget(self.btn_gpt_setting_confirm)

        self.btn_gpt_setting_cancel = QPushButton(self.tab_2)
        self.btn_gpt_setting_cancel.setObjectName(u"btn_gpt_setting_cancel")

        self.horizontalLayout_10.addWidget(self.btn_gpt_setting_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.gpt_setting.addTab(self.tab_2, "")
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

        self.subtitle_remote_address = QLineEdit(self.scrollAreaWidgetContents)
        self.subtitle_remote_address.setObjectName(u"subtitle_remote_address")

        self.horizontalLayout_6.addWidget(self.subtitle_remote_address)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.subtitle_confirm = QPushButton(self.subtitle_set)
        self.subtitle_confirm.setObjectName(u"subtitle_confirm")

        self.horizontalLayout_3.addWidget(self.subtitle_confirm)

        self.subtitle_setting_cancel = QPushButton(self.subtitle_set)
        self.subtitle_setting_cancel.setObjectName(u"subtitle_setting_cancel")

        self.horizontalLayout_3.addWidget(self.subtitle_setting_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gpt_setting.addTab(self.subtitle_set, "")

        self.horizontalLayout.addWidget(self.gpt_setting)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(setting_window)

        self.gpt_setting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(setting_window)
    # setupUi

    def retranslateUi(self, setting_window):
        setting_window.setWindowTitle(QCoreApplication.translate("setting_window", u"Setting", None))
        self.label_4.setText(QCoreApplication.translate("setting_window", u"API BASE", None))
        self.label_5.setText(QCoreApplication.translate("setting_window", u"API KEY", None))
        self.label_6.setText(QCoreApplication.translate("setting_window", u"\u4e0a\u4e0b\u6587\u6570\u91cf", None))
        self.label_7.setText(QCoreApplication.translate("setting_window", u"GPT\u8bed\u901f", None))
        self.label_8.setText(QCoreApplication.translate("setting_window", u"\u8bed\u97f3\u8f6c\u6587\u672c\u6a21\u5f0f", None))
        self.combo_box_s2t_mode.setItemText(0, QCoreApplication.translate("setting_window", u"\u672c\u5730", None))
        self.combo_box_s2t_mode.setItemText(1, QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b", None))

        self.label_9.setText(QCoreApplication.translate("setting_window", u"\u8bed\u97f3\u8f6c\u6587\u672c\u8fdc\u7a0b\u5730\u5740", None))
        self.label_10.setText(QCoreApplication.translate("setting_window", u"\u8bed\u97f3\u751f\u6210\u6a21\u5f0f", None))
        self.combox_box_t2s_mode.setItemText(0, QCoreApplication.translate("setting_window", u"\u672c\u5730", None))
        self.combox_box_t2s_mode.setItemText(1, QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b", None))

        self.label_11.setText(QCoreApplication.translate("setting_window", u"\u8bed\u97f3\u751f\u6210\u8fdc\u7a0b\u5730\u5740", None))
        self.btn_gpt_setting_confirm.setText(QCoreApplication.translate("setting_window", u"\u786e\u5b9a", None))
        self.btn_gpt_setting_cancel.setText(QCoreApplication.translate("setting_window", u"\u53d6\u6d88", None))
        self.gpt_setting.setTabText(self.gpt_setting.indexOf(self.tab_2), QCoreApplication.translate("setting_window", u"gpt\u8bed\u97f3", None))
        self.label.setText(QCoreApplication.translate("setting_window", u"\u91c7\u6837\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("setting_window", u"\u6a21\u5f0f", None))
        self.subtitle_mode_select_combo.setItemText(0, QCoreApplication.translate("setting_window", u"\u672c\u5730", None))
        self.subtitle_mode_select_combo.setItemText(1, QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b", None))

        self.label_3.setText(QCoreApplication.translate("setting_window", u"\u8fdc\u7a0b\u5730\u5740", None))
        self.subtitle_confirm.setText(QCoreApplication.translate("setting_window", u"\u786e\u5b9a", None))
        self.subtitle_setting_cancel.setText(QCoreApplication.translate("setting_window", u"\u53d6\u6d88", None))
        self.gpt_setting.setTabText(self.gpt_setting.indexOf(self.subtitle_set), QCoreApplication.translate("setting_window", u"\u5b9e\u65f6\u5b57\u5e55", None))
    # retranslateUi

