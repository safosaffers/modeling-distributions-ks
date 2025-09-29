# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_View.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(850, 550)
        View.setMinimumSize(QSize(850, 350))
        View.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: rgb(154, 219, 242);\n"
"}\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 20px 28px;\n"
"    margin-top: 19px;\n"
"    background-color: #edf9fd;\n"
"    border-radius: 15px;\n"
"}\n"
"QGroupBox {\n"
"    background-color: #def3fb;\n"
"    margin-top: 30px;\n"
"    margin-right: 3px;\n"
"	font: 800 20pt \"Segoe UI\";\n"
"    color: #464d55;\n"
"    font-weight: 600;\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"}\n"
"QToolTip {\n"
"    color: #464d55;\n"
"    background-color: #def3fb;\n"
"	font: 14pt \"Segoe UI\";\n"
"    font-weight: 600;\n"
"    margin: 1px;\n"
"    border: 3px solid #464d55;\n"
"    border-radius: 6px;\n"
"}\n"
"QLabel, QCheckBox{\n"
"    color: #464d55;\n"
"    background-color: #def3fb;\n"
"	font: 18pt \"Segoe UI\";\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2"
                        ":0,\n"
"                                stop:0 #106381, stop:1 #1683aa);\n"
"  font: 14pt \"Verdana\";\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #1683aa, stop:1 #b5ecff);\n"
"	text-decoration: underline;\n"
"  border: 3px solid #ECF0F4;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 3px 10px;\n"
"	font: 18pt \"Verdana\";\n"
"}\n"
"\n"
"#tb_sequence_representations QWidget{ \n"
"    background-color: #def3fb;\n"
"}\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: #f1f1f1;\n"
"    width: 12px; /* \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e */\n"
"    height: 12px; /* \u0434\u043b\u044f \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c"
                        "\u043d\u043e\u0433\u043e */\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #106381, stop:1 #1683aa);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"  color: #37475E;\n"
"	font: 700 16pt \"Verdana\";\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"\n"
"/* --------QTABLEWIDGET-------- */ \n"
"QTableWidget {\n"
"    gridline-color: #1683aa;\n"
"	font: 18pt \"Segoe UI\";\n"
"    background-color: #def3fb; /* \u0444\u043e\u043d \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"    outline: 0px; /* \u0443\u0431\u0438\u0440\u0430\u0435\u0442 \u043f\u0443\u043d\u043a\u0442\u0438\u0440 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	font: 18pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    border: 1px solid #1683aa;\n"
"    padding: 5px;\n"
"    "
                        "background-color: #fdfeff; /* \u0444\u043e\u043d \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"    color: #464d55; /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #e0f0ff;\n"
"    padding: 4px;\n"
"    border: 1px solid #1683aa;\n"
"	font: 16pt \"Segoe UI\";\n"
"}\n"
"QHeaderView {\n"
"    background-color: #def3fb;\n"
"    border: none;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #b3d7ff;\n"
"    color: black;\n"
"}\n"
"/* --------QTABLEWIDGET (END) -------- */ \n"
"\n"
"/* LINE*/\n"
"Line {\n"
"    background-color: #edf9fd;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 15px;\n"
"}")
        self.verticalLayout = QVBoxLayout(View)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(View)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(690, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 3, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.f_menu = QFrame(self.frame_2)
        self.f_menu.setObjectName(u"f_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_menu.sizePolicy().hasHeightForWidth())
        self.f_menu.setSizePolicy(sizePolicy)
        self.f_menu.setMaximumSize(QSize(500, 16777215))
        self.f_menu.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(199, 218, 225);\n"
"}\n"
"QLabel {\n"
"    color: rgb(30, 30, 30);\n"
"    background-color: rgba(128, 128, 128, 0.0);\n"
"	font: 14pt \"Segoe UI\";\n"
"    font-weight: 600;\n"
"    margin: 5px;\n"
"    margin-left: 0px;\n"
"    margin-right: 0px;\n"
"}\n"
"QPushButton {\n"
"    background: rgba(253, 253, 253, 0.-5);\n"
"    min-height: 50px;\n"
"  font: 12pt \"Verdana\";\n"
"  color: rgb(0, 0, 0);\n"
"  font-weight: 600;\n"
"  color: rgb(30, 30, 30);\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(193, 193, 193);\n"
"	text-decoration: none;\n"
"    border: none;\n"
"}")
        self.f_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.f_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.f_menu)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(15, 15, 15, -1)
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.pb_page_0 = QPushButton(self.f_menu)
        self.pb_page_0.setObjectName(u"pb_page_0")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pb_page_0.setFont(font)
        self.pb_page_0.setStyleSheet(u"QPushButton{    background: rgba(253, 253, 253, 0.95);}")

        self.verticalLayout_42.addWidget(self.pb_page_0)

        self.pb_page_1 = QPushButton(self.f_menu)
        self.pb_page_1.setObjectName(u"pb_page_1")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.pb_page_1.setFont(font1)

        self.verticalLayout_42.addWidget(self.pb_page_1)

        self.pb_page_2 = QPushButton(self.f_menu)
        self.pb_page_2.setObjectName(u"pb_page_2")

        self.verticalLayout_42.addWidget(self.pb_page_2)

        self.pb_page_3 = QPushButton(self.f_menu)
        self.pb_page_3.setObjectName(u"pb_page_3")
        self.pb_page_3.setFont(font1)

        self.verticalLayout_42.addWidget(self.pb_page_3)

        self.verticalSpacer_65 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_65)

        self.layout_language = QHBoxLayout()
        self.layout_language.setObjectName(u"layout_language")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_language.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.f_menu)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setStyleSheet(u"")

        self.layout_language.addWidget(self.label)

        self.layout_language.setStretch(0, 1)
        self.layout_language.setStretch(1, 3)

        self.verticalLayout_42.addLayout(self.layout_language)

        self.layout_theme = QHBoxLayout()
        self.layout_theme.setObjectName(u"layout_theme")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_theme.addItem(self.horizontalSpacer_15)

        self.label_2 = QLabel(self.f_menu)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.layout_theme.addWidget(self.label_2)

        self.layout_theme.setStretch(0, 1)
        self.layout_theme.setStretch(1, 3)

        self.verticalLayout_42.addLayout(self.layout_theme)

        self.verticalSpacer_68 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer_68)


        self.verticalLayout_43.addLayout(self.verticalLayout_42)


        self.horizontalLayout_23.addWidget(self.f_menu)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.sw_pages = QStackedWidget(self.frame_2)
        self.sw_pages.setObjectName(u"sw_pages")
        self.sw_pages.setStyleSheet(u"")
        self.sw_pages.setLineWidth(0)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_3 = QVBoxLayout(self.page_0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.page_0_vl_content = QVBoxLayout()
        self.page_0_vl_content.setObjectName(u"page_0_vl_content")
        self.label_3 = QLabel(self.page_0)
        self.label_3.setObjectName(u"label_3")

        self.page_0_vl_content.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.page_0)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.le_uniform_distribution_a_parameter = QLineEdit(self.page_0)
        self.le_uniform_distribution_a_parameter.setObjectName(u"le_uniform_distribution_a_parameter")
        self.le_uniform_distribution_a_parameter.setFrame(True)

        self.horizontalLayout_3.addWidget(self.le_uniform_distribution_a_parameter)

        self.label_7 = QLabel(self.page_0)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.le_uniform_distribution_b_parameter = QLineEdit(self.page_0)
        self.le_uniform_distribution_b_parameter.setObjectName(u"le_uniform_distribution_b_parameter")

        self.horizontalLayout_3.addWidget(self.le_uniform_distribution_b_parameter)

        self.label_8 = QLabel(self.page_0)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.le_uniform_distribution_N_parameter = QLineEdit(self.page_0)
        self.le_uniform_distribution_N_parameter.setObjectName(u"le_uniform_distribution_N_parameter")

        self.horizontalLayout_3.addWidget(self.le_uniform_distribution_N_parameter)


        self.page_0_vl_content.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pb_uniform_distribution_calculate = QPushButton(self.page_0)
        self.pb_uniform_distribution_calculate.setObjectName(u"pb_uniform_distribution_calculate")

        self.horizontalLayout_2.addWidget(self.pb_uniform_distribution_calculate)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.cb_uniform_distribution_draw = QCheckBox(self.page_0)
        self.cb_uniform_distribution_draw.setObjectName(u"cb_uniform_distribution_draw")

        self.horizontalLayout_2.addWidget(self.cb_uniform_distribution_draw)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.page_0_vl_content.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_22 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content.addItem(self.verticalSpacer_22)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.page_0)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.le_uniform_distribution_delta_1 = QLineEdit(self.page_0)
        self.le_uniform_distribution_delta_1.setObjectName(u"le_uniform_distribution_delta_1")
        self.le_uniform_distribution_delta_1.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.le_uniform_distribution_delta_1)

        self.label_10 = QLabel(self.page_0)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.le_uniform_distribution_delta_2 = QLineEdit(self.page_0)
        self.le_uniform_distribution_delta_2.setObjectName(u"le_uniform_distribution_delta_2")
        self.le_uniform_distribution_delta_2.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.le_uniform_distribution_delta_2)


        self.page_0_vl_content.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tw_uniform_distribution_result = QTableWidget(self.page_0)
        self.tw_uniform_distribution_result.setObjectName(u"tw_uniform_distribution_result")

        self.horizontalLayout.addWidget(self.tw_uniform_distribution_result)


        self.page_0_vl_content.addLayout(self.horizontalLayout)

        self.verticalSpacer_26 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content.addItem(self.verticalSpacer_26)

        self.page_0_vl_content.setStretch(0, 1)
        self.page_0_vl_content.setStretch(2, 1)
        self.page_0_vl_content.setStretch(6, 1)
        self.page_0_vl_content.setStretch(8, 8)

        self.verticalLayout_3.addLayout(self.page_0_vl_content)

        self.sw_pages.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_4 = QVBoxLayout(self.page_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.page_0_vl_content_6 = QVBoxLayout()
        self.page_0_vl_content_6.setObjectName(u"page_0_vl_content_6")
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")

        self.page_0_vl_content_6.addWidget(self.label_4)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_6.addItem(self.verticalSpacer_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_35 = QLabel(self.page_1)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_21.addWidget(self.label_35)

        self.le_exponential_distribution_lamda_parameter = QLineEdit(self.page_1)
        self.le_exponential_distribution_lamda_parameter.setObjectName(u"le_exponential_distribution_lamda_parameter")

        self.horizontalLayout_21.addWidget(self.le_exponential_distribution_lamda_parameter)

        self.label_37 = QLabel(self.page_1)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_21.addWidget(self.label_37)

        self.le_exponential_distribution_N_parameter = QLineEdit(self.page_1)
        self.le_exponential_distribution_N_parameter.setObjectName(u"le_exponential_distribution_N_parameter")

        self.horizontalLayout_21.addWidget(self.le_exponential_distribution_N_parameter)


        self.page_0_vl_content_6.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_17 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_6.addItem(self.verticalSpacer_17)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_12)

        self.pb_exponential_distribution_calculate = QPushButton(self.page_1)
        self.pb_exponential_distribution_calculate.setObjectName(u"pb_exponential_distribution_calculate")

        self.horizontalLayout_22.addWidget(self.pb_exponential_distribution_calculate)

        self.horizontalSpacer_4 = QSpacerItem(12, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_4)

        self.cb_exponential_distribution_draw = QCheckBox(self.page_1)
        self.cb_exponential_distribution_draw.setObjectName(u"cb_exponential_distribution_draw")

        self.horizontalLayout_22.addWidget(self.cb_exponential_distribution_draw)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_13)


        self.page_0_vl_content_6.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_23 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_6.addItem(self.verticalSpacer_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_38 = QLabel(self.page_1)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_25.addWidget(self.label_38)

        self.le_exponential_distribution_delta_1 = QLineEdit(self.page_1)
        self.le_exponential_distribution_delta_1.setObjectName(u"le_exponential_distribution_delta_1")
        self.le_exponential_distribution_delta_1.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.le_exponential_distribution_delta_1)

        self.label_39 = QLabel(self.page_1)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_25.addWidget(self.label_39)

        self.le_exponential_distribution_delta_2 = QLineEdit(self.page_1)
        self.le_exponential_distribution_delta_2.setObjectName(u"le_exponential_distribution_delta_2")
        self.le_exponential_distribution_delta_2.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.le_exponential_distribution_delta_2)


        self.page_0_vl_content_6.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_6.addItem(self.verticalSpacer_18)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.tw_exponential_distribution_result = QTableWidget(self.page_1)
        self.tw_exponential_distribution_result.setObjectName(u"tw_exponential_distribution_result")

        self.horizontalLayout_26.addWidget(self.tw_exponential_distribution_result)


        self.page_0_vl_content_6.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_6.addItem(self.verticalSpacer_25)

        self.page_0_vl_content_6.setStretch(2, 1)
        self.page_0_vl_content_6.setStretch(6, 1)
        self.page_0_vl_content_6.setStretch(8, 8)

        self.verticalLayout_2.addLayout(self.page_0_vl_content_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.sw_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.page_0_vl_content_7 = QVBoxLayout()
        self.page_0_vl_content_7.setObjectName(u"page_0_vl_content_7")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.page_0_vl_content_7.addWidget(self.label_5)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_7.addItem(self.verticalSpacer_19)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_40 = QLabel(self.page_2)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_27.addWidget(self.label_40)

        self.le_normal_distribution_a_parameter = QLineEdit(self.page_2)
        self.le_normal_distribution_a_parameter.setObjectName(u"le_normal_distribution_a_parameter")

        self.horizontalLayout_27.addWidget(self.le_normal_distribution_a_parameter)

        self.label_41 = QLabel(self.page_2)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_27.addWidget(self.label_41)

        self.le_normal_distribution_sigma_square_parameter = QLineEdit(self.page_2)
        self.le_normal_distribution_sigma_square_parameter.setObjectName(u"le_normal_distribution_sigma_square_parameter")

        self.horizontalLayout_27.addWidget(self.le_normal_distribution_sigma_square_parameter)

        self.label_42 = QLabel(self.page_2)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_27.addWidget(self.label_42)

        self.le_normal_distribution_N_parameter = QLineEdit(self.page_2)
        self.le_normal_distribution_N_parameter.setObjectName(u"le_normal_distribution_N_parameter")

        self.horizontalLayout_27.addWidget(self.le_normal_distribution_N_parameter)


        self.page_0_vl_content_7.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_20 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_7.addItem(self.verticalSpacer_20)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_14)

        self.pb_normal_distribution_calculate = QPushButton(self.page_2)
        self.pb_normal_distribution_calculate.setObjectName(u"pb_normal_distribution_calculate")

        self.horizontalLayout_28.addWidget(self.pb_normal_distribution_calculate)

        self.horizontalSpacer_6 = QSpacerItem(12, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_6)

        self.cb_normal_distribution_draw = QCheckBox(self.page_2)
        self.cb_normal_distribution_draw.setObjectName(u"cb_normal_distribution_draw")

        self.horizontalLayout_28.addWidget(self.cb_normal_distribution_draw)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_16)


        self.page_0_vl_content_7.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_7.addItem(self.verticalSpacer_24)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_43 = QLabel(self.page_2)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_29.addWidget(self.label_43)

        self.le_normal_distribution_delta_1 = QLineEdit(self.page_2)
        self.le_normal_distribution_delta_1.setObjectName(u"le_normal_distribution_delta_1")
        self.le_normal_distribution_delta_1.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.le_normal_distribution_delta_1)

        self.label_44 = QLabel(self.page_2)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_29.addWidget(self.label_44)

        self.le_normal_distribution_delta_2 = QLineEdit(self.page_2)
        self.le_normal_distribution_delta_2.setObjectName(u"le_normal_distribution_delta_2")
        self.le_normal_distribution_delta_2.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.le_normal_distribution_delta_2)


        self.page_0_vl_content_7.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_7.addItem(self.verticalSpacer_21)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.tw_normal_distribution_result = QTableWidget(self.page_2)
        self.tw_normal_distribution_result.setObjectName(u"tw_normal_distribution_result")

        self.horizontalLayout_30.addWidget(self.tw_normal_distribution_result)


        self.page_0_vl_content_7.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_27 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.page_0_vl_content_7.addItem(self.verticalSpacer_27)

        self.page_0_vl_content_7.setStretch(2, 1)
        self.page_0_vl_content_7.setStretch(6, 1)
        self.page_0_vl_content_7.setStretch(8, 8)

        self.verticalLayout_9.addLayout(self.page_0_vl_content_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.sw_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 484, 1076))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.page_about = QVBoxLayout()
        self.page_about.setObjectName(u"page_about")
        self.gb_about = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_about.setObjectName(u"gb_about")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.gb_about.setFont(font2)
        self.gb_about.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"padding-right: 20px;\n"
"}")
        self.gb_about.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_46 = QVBoxLayout(self.gb_about)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalSpacer_76 = QSpacerItem(30, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_47.addItem(self.verticalSpacer_76)

        self.l_about = QLabel(self.gb_about)
        self.l_about.setObjectName(u"l_about")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.l_about.setFont(font3)
        self.l_about.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"padding-right: 20px;\n"
"}")
        self.l_about.setTextFormat(Qt.TextFormat.RichText)
        self.l_about.setScaledContents(False)
        self.l_about.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_about.setWordWrap(True)

        self.verticalLayout_47.addWidget(self.l_about)

        self.verticalSpacer_79 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_47.addItem(self.verticalSpacer_79)


        self.verticalLayout_46.addLayout(self.verticalLayout_47)


        self.page_about.addWidget(self.gb_about)


        self.verticalLayout_8.addLayout(self.page_about)

        self.verticalSpacer_80 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_80)

        self.gb_properties_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_properties_2.setObjectName(u"gb_properties_2")
        self.gb_properties_2.setFont(font2)
        self.gb_properties_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_50 = QVBoxLayout(self.gb_properties_2)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalSpacer_86 = QSpacerItem(30, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_51.addItem(self.verticalSpacer_86)

        self.l_technical_implementation = QLabel(self.gb_properties_2)
        self.l_technical_implementation.setObjectName(u"l_technical_implementation")
        self.l_technical_implementation.setFont(font3)
        self.l_technical_implementation.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"padding-right: 20px;\n"
"}")
        self.l_technical_implementation.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_technical_implementation.setWordWrap(True)

        self.verticalLayout_51.addWidget(self.l_technical_implementation)

        self.verticalSpacer_90 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_90)


        self.verticalLayout_50.addLayout(self.verticalLayout_51)


        self.verticalLayout_8.addWidget(self.gb_properties_2)

        self.verticalSpacer_89 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_89)

        self.gb_properties_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_properties_3.setObjectName(u"gb_properties_3")
        self.gb_properties_3.setFont(font2)
        self.gb_properties_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_52 = QVBoxLayout(self.gb_properties_3)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalSpacer_92 = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_53.addItem(self.verticalSpacer_92)

        self.l_features = QLabel(self.gb_properties_3)
        self.l_features.setObjectName(u"l_features")
        self.l_features.setFont(font3)
        self.l_features.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"padding-right: 20px;\n"
"}")
        self.l_features.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.l_features.setWordWrap(True)

        self.verticalLayout_53.addWidget(self.l_features)

        self.verticalSpacer_95 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_95)


        self.verticalLayout_52.addLayout(self.verticalLayout_53)


        self.verticalLayout_8.addWidget(self.gb_properties_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.sw_pages.addWidget(self.page_3)

        self.horizontalLayout_24.addWidget(self.sw_pages)

        self.horizontalLayout_24.setStretch(0, 2)
        self.horizontalLayout_24.setStretch(1, 5)

        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 2)

        self.retranslateUi(View)

        self.sw_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(View)
    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"\u041a\u0430\u0440\u0438\u043c\u043e\u0432 \u0421\u0430\u0444\u043e 5095. \u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0432\u0438\u0434\u043e\u0432 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439", None))
        self.pb_page_0.setText(QCoreApplication.translate("View", u"\u0420\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u043e\u0435\n"
"\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.pb_page_1.setText(QCoreApplication.translate("View", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435\n"
"\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.pb_page_2.setText(QCoreApplication.translate("View", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0435\n"
"\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.pb_page_3.setText(QCoreApplication.translate("View", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("View", u"\u042f\u0437\u044b\u043a:", None))
        self.label_2.setText(QCoreApplication.translate("View", u"\u0422\u0435\u043c\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("View", u"\u0420\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u043e\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("View", u"a", None))
        self.label_7.setText(QCoreApplication.translate("View", u"b", None))
        self.label_8.setText(QCoreApplication.translate("View", u"N", None))
        self.pb_uniform_distribution_calculate.setText(QCoreApplication.translate("View", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0447\u0451\u0442", None))
        self.cb_uniform_distribution_draw.setText(QCoreApplication.translate("View", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.label_9.setText(QCoreApplication.translate("View", u"\u0394_1", None))
        self.label_10.setText(QCoreApplication.translate("View", u"\u0394_2", None))
        self.label_4.setText(QCoreApplication.translate("View", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_35.setText(QCoreApplication.translate("View", u"\u03bb", None))
        self.label_37.setText(QCoreApplication.translate("View", u"N", None))
        self.pb_exponential_distribution_calculate.setText(QCoreApplication.translate("View", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0447\u0451\u0442", None))
        self.cb_exponential_distribution_draw.setText(QCoreApplication.translate("View", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.label_38.setText(QCoreApplication.translate("View", u"\u0394_1", None))
        self.label_39.setText(QCoreApplication.translate("View", u"\u0394_2", None))
        self.label_5.setText(QCoreApplication.translate("View", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_40.setText(QCoreApplication.translate("View", u"a", None))
        self.label_41.setText(QCoreApplication.translate("View", u"\u03c3^2", None))
        self.label_42.setText(QCoreApplication.translate("View", u"N", None))
        self.pb_normal_distribution_calculate.setText(QCoreApplication.translate("View", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0447\u0451\u0442", None))
        self.cb_normal_distribution_draw.setText(QCoreApplication.translate("View", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.label_43.setText(QCoreApplication.translate("View", u"\u0394_1", None))
        self.label_44.setText(QCoreApplication.translate("View", u"\u0394_2", None))
        self.gb_about.setTitle(QCoreApplication.translate("View", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.l_about.setText(QCoreApplication.translate("View", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0431\u044b\u043b\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443 &quot;\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u0438 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u043b\u044c\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c&quot; \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u043c 1 \u043a\u0443\u0440\u0441\u0430 \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u044b<span style=\" font-weight:700;\"/>09.04.01 <span style=\" font-"
                        "weight:700;\">\u2014</span><span style=\" font-weight:700;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430, </span><span style=\" font-weight:700;\">\u041a\u0430\u0440\u0438\u043c\u043e\u0432\u044b\u043c \u0421\u0430\u0444\u043e</span>.</p></body></html>", None))
        self.gb_properties_2.setTitle(QCoreApplication.translate("View", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.l_technical_implementation.setText(QCoreApplication.translate("View", u"<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</span>:</li><p>Python 3.11 / PySide6</p><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0411\u0438\u0437\u043d\u0435\u0441-\u043b\u043e\u0433\u0438\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</span>:</li></ul><p>Python 3.11</p></body></html>", None))
        self.gb_properties_3.setTitle(QCoreApplication.translate("View", u"\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.l_features.setText(QCoreApplication.translate("View", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0441\u043b\u0443\u0447\u0430"
                        "\u0439\u043d\u043e\u0439 \u0432\u0435\u043b\u0438\u0447\u0438\u043d\u044b \u0434\u043b\u044f:</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">\u2014 \u0420\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u043e\u0433\u043e;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">\u2014 \u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">\u2014 \u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e;</p></body></html>", None))
    # retranslateUi

