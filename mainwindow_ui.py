# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.mix_video_path = QLineEdit(self.tab)
        self.mix_video_path.setObjectName(u"mix_video_path")

        self.horizontalLayout.addWidget(self.mix_video_path)

        self.mix_video_button = QPushButton(self.tab)
        self.mix_video_button.setObjectName(u"mix_video_button")

        self.horizontalLayout.addWidget(self.mix_video_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.mix_audio_path = QLineEdit(self.tab)
        self.mix_audio_path.setObjectName(u"mix_audio_path")

        self.horizontalLayout_2.addWidget(self.mix_audio_path)

        self.mix_audio_button = QPushButton(self.tab)
        self.mix_audio_button.setObjectName(u"mix_audio_button")

        self.horizontalLayout_2.addWidget(self.mix_audio_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.mix_output_path = QLineEdit(self.tab)
        self.mix_output_path.setObjectName(u"mix_output_path")

        self.horizontalLayout_3.addWidget(self.mix_output_path)

        self.mix_output_button = QPushButton(self.tab)
        self.mix_output_button.setObjectName(u"mix_output_button")

        self.horizontalLayout_3.addWidget(self.mix_output_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.mix_button = QPushButton(self.tab)
        self.mix_button.setObjectName(u"mix_button")

        self.verticalLayout_2.addWidget(self.mix_button)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.mux_src_path = QLineEdit(self.tab)
        self.mux_src_path.setObjectName(u"mux_src_path")

        self.horizontalLayout_4.addWidget(self.mux_src_path)

        self.mux_src_button = QPushButton(self.tab)
        self.mux_src_button.setObjectName(u"mux_src_button")

        self.horizontalLayout_4.addWidget(self.mux_src_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.mux_output_path = QLineEdit(self.tab)
        self.mux_output_path.setObjectName(u"mux_output_path")

        self.horizontalLayout_5.addWidget(self.mux_output_path)

        self.mux_output_button = QPushButton(self.tab)
        self.mux_output_button.setObjectName(u"mux_output_button")

        self.horizontalLayout_5.addWidget(self.mux_output_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.mux_button = QPushButton(self.tab)
        self.mux_button.setObjectName(u"mux_button")

        self.verticalLayout_2.addWidget(self.mux_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e03\u7ef4\u5de5\u5177\u7bb1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u89c6\u9891\u6df7\u6d41", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u6587\u4ef6", None))
        self.mix_video_button.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u6587\u4ef6", None))
        self.mix_audio_button.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.mix_output_button.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.mix_button.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"flv mkv \u8f6c\u5c01\u88c5\u4e3a mp4\uff08\u53ef\u80fd\u4f1a\u5931\u8d25\uff09", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u539f\u6587\u4ef6", None))
        self.mux_src_button.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.mux_output_button.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.mux_button.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5c01\u88c5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5e38\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u9884\u7559", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u9884\u75592", None))
    # retranslateUi

