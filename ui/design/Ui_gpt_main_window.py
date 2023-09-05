# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpt_main_window.ui'
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
    QLayout, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_gpt_chat_widget(object):
    def setupUi(self, gpt_chat_widget):
        if not gpt_chat_widget.objectName():
            gpt_chat_widget.setObjectName(u"gpt_chat_widget")
        gpt_chat_widget.resize(546, 502)
        self.verticalLayout_4 = QVBoxLayout(gpt_chat_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tab1_select_input_label_2 = QLabel(gpt_chat_widget)
        self.tab1_select_input_label_2.setObjectName(u"tab1_select_input_label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_select_input_label_2.sizePolicy().hasHeightForWidth())
        self.tab1_select_input_label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tab1_select_input_label_2)

        self.tab1_select_output_label_2 = QLabel(gpt_chat_widget)
        self.tab1_select_output_label_2.setObjectName(u"tab1_select_output_label_2")
        sizePolicy.setHeightForWidth(self.tab1_select_output_label_2.sizePolicy().hasHeightForWidth())
        self.tab1_select_output_label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tab1_select_output_label_2)

        self.label = QLabel(gpt_chat_widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, -1, 2, -1)
        self.tab1_select_input_combo = QComboBox(gpt_chat_widget)
        self.tab1_select_input_combo.setObjectName(u"tab1_select_input_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab1_select_input_combo.sizePolicy().hasHeightForWidth())
        self.tab1_select_input_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.tab1_select_input_combo)

        self.tab1_select_outpt_combo = QComboBox(gpt_chat_widget)
        self.tab1_select_outpt_combo.setObjectName(u"tab1_select_outpt_combo")
        sizePolicy1.setHeightForWidth(self.tab1_select_outpt_combo.sizePolicy().hasHeightForWidth())
        self.tab1_select_outpt_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.tab1_select_outpt_combo)

        self.tab1_select_correct_s2t_combo = QComboBox(gpt_chat_widget)
        self.tab1_select_correct_s2t_combo.addItem("")
        self.tab1_select_correct_s2t_combo.addItem("")
        self.tab1_select_correct_s2t_combo.setObjectName(u"tab1_select_correct_s2t_combo")
        sizePolicy1.setHeightForWidth(self.tab1_select_correct_s2t_combo.sizePolicy().hasHeightForWidth())
        self.tab1_select_correct_s2t_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.tab1_select_correct_s2t_combo)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tab1_start_btn = QPushButton(gpt_chat_widget)
        self.tab1_start_btn.setObjectName(u"tab1_start_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab1_start_btn.sizePolicy().hasHeightForWidth())
        self.tab1_start_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.tab1_start_btn)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tab1_load_session_btn = QPushButton(gpt_chat_widget)
        self.tab1_load_session_btn.setObjectName(u"tab1_load_session_btn")

        self.horizontalLayout_3.addWidget(self.tab1_load_session_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tab1_correct_s2t_editor = QPlainTextEdit(gpt_chat_widget)
        self.tab1_correct_s2t_editor.setObjectName(u"tab1_correct_s2t_editor")

        self.horizontalLayout_2.addWidget(self.tab1_correct_s2t_editor)

        self.tab1_send_corrected_text_btn = QPushButton(gpt_chat_widget)
        self.tab1_send_corrected_text_btn.setObjectName(u"tab1_send_corrected_text_btn")
        sizePolicy2.setHeightForWidth(self.tab1_send_corrected_text_btn.sizePolicy().hasHeightForWidth())
        self.tab1_send_corrected_text_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.tab1_send_corrected_text_btn)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab1_pause_speaker_btn = QPushButton(gpt_chat_widget)
        self.tab1_pause_speaker_btn.setObjectName(u"tab1_pause_speaker_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.tab1_pause_speaker_btn.sizePolicy().hasHeightForWidth())
        self.tab1_pause_speaker_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.tab1_pause_speaker_btn)

        self.tab1_speak_again_btn = QPushButton(gpt_chat_widget)
        self.tab1_speak_again_btn.setObjectName(u"tab1_speak_again_btn")
        sizePolicy3.setHeightForWidth(self.tab1_speak_again_btn.sizePolicy().hasHeightForWidth())
        self.tab1_speak_again_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.tab1_speak_again_btn)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textBrowser = QTextBrowser(gpt_chat_widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 8)

        self.retranslateUi(gpt_chat_widget)

        QMetaObject.connectSlotsByName(gpt_chat_widget)
    # setupUi

    def retranslateUi(self, gpt_chat_widget):
        gpt_chat_widget.setWindowTitle(QCoreApplication.translate("gpt_chat_widget", u"gpt\u804a\u5929", None))
        self.tab1_select_input_label_2.setText(QCoreApplication.translate("gpt_chat_widget", u"\u9009\u62e9\u8f93\u5165\u8bbe\u5907", None))
        self.tab1_select_output_label_2.setText(QCoreApplication.translate("gpt_chat_widget", u"\u9009\u62e9gpt\u8f93\u51fa\u8bbe\u5907", None))
        self.label.setText(QCoreApplication.translate("gpt_chat_widget", u"\u4fee\u6b63\u8bed\u97f3\u8bc6\u522b", None))
        self.tab1_select_correct_s2t_combo.setItemText(0, QCoreApplication.translate("gpt_chat_widget", u"\u5426", None))
        self.tab1_select_correct_s2t_combo.setItemText(1, QCoreApplication.translate("gpt_chat_widget", u"\u662f", None))

        self.tab1_start_btn.setText(QCoreApplication.translate("gpt_chat_widget", u"\u5f00\u59cb\u8bf4\u8bdd", None))
        self.tab1_load_session_btn.setText(QCoreApplication.translate("gpt_chat_widget", u"\u8f7d\u5165\u4f1a\u8bdd", None))
        self.tab1_send_corrected_text_btn.setText(QCoreApplication.translate("gpt_chat_widget", u"\u53d1\u9001", None))
        self.tab1_pause_speaker_btn.setText(QCoreApplication.translate("gpt_chat_widget", u"\u6682\u505c", None))
        self.tab1_speak_again_btn.setText(QCoreApplication.translate("gpt_chat_widget", u"\u91cd\u64ad", None))
    # retranslateUi

