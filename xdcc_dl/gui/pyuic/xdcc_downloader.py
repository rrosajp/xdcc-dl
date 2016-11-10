# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xdcc_dl/gui/qt_designer/xdcc_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZDCCDownloaderWindow(object):
    def setupUi(self, ZDCCDownloaderWindow):
        ZDCCDownloaderWindow.setObjectName("ZDCCDownloaderWindow")
        ZDCCDownloaderWindow.resize(967, 515)
        self.centralwidget = QtWidgets.QWidget(ZDCCDownloaderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.download_button.setObjectName("download_button")
        self.gridLayout.addWidget(self.download_button, 10, 5, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 1)
        self.message_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.message_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.message_edit.setObjectName("message_edit")
        self.gridLayout.addWidget(self.message_edit, 1, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 0, 1, 8)
        self.down_arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_arrow_button.setObjectName("down_arrow_button")
        self.gridLayout.addWidget(self.down_arrow_button, 7, 7, 1, 1)
        self.left_arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_arrow_button.setObjectName("left_arrow_button")
        self.gridLayout.addWidget(self.left_arrow_button, 5, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 4)
        self.doqnload_queue_list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.doqnload_queue_list_widget.sizePolicy().hasHeightForWidth())
        self.doqnload_queue_list_widget.setSizePolicy(sizePolicy)
        self.doqnload_queue_list_widget.setMinimumSize(QtCore.QSize(350, 0))
        self.doqnload_queue_list_widget.setSizeIncrement(QtCore.QSize(0, 100))
        self.doqnload_queue_list_widget.setObjectName("doqnload_queue_list_widget")
        self.gridLayout.addWidget(self.doqnload_queue_list_widget, 3, 6, 4, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        self.server_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_edit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.server_edit.setObjectName("server_edit")
        self.gridLayout.addWidget(self.server_edit, 1, 3, 1, 4)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 7, 2, 1, 1)
        self.search_engine_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.search_engine_combo_box.setObjectName("search_engine_combo_box")
        self.gridLayout.addWidget(self.search_engine_combo_box, 7, 1, 1, 1)
        self.search_term_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_term_edit.setObjectName("search_term_edit")
        self.gridLayout.addWidget(self.search_term_edit, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.destination_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination_edit.sizePolicy().hasHeightForWidth())
        self.destination_edit.setSizePolicy(sizePolicy)
        self.destination_edit.setObjectName("destination_edit")
        self.gridLayout.addWidget(self.destination_edit, 10, 1, 1, 4)
        self.rigth_arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.rigth_arrow_button.setObjectName("rigth_arrow_button")
        self.gridLayout.addWidget(self.rigth_arrow_button, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 4, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 1, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem5, 8, 1, 1, 1)
        self.up_arrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_arrow_button.setObjectName("up_arrow_button")
        self.gridLayout.addWidget(self.up_arrow_button, 7, 6, 1, 1)
        self.search_result_tree_widget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.search_result_tree_widget.sizePolicy().hasHeightForWidth())
        self.search_result_tree_widget.setSizePolicy(sizePolicy)
        self.search_result_tree_widget.setMinimumSize(QtCore.QSize(455, 350))
        self.search_result_tree_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_result_tree_widget.setSizeIncrement(QtCore.QSize(0, 100))
        self.search_result_tree_widget.setObjectName("search_result_tree_widget")
        self.gridLayout.addWidget(self.search_result_tree_widget, 3, 0, 4, 3)
        ZDCCDownloaderWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ZDCCDownloaderWindow)
        self.statusbar.setObjectName("statusbar")
        ZDCCDownloaderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ZDCCDownloaderWindow)
        QtCore.QMetaObject.connectSlotsByName(ZDCCDownloaderWindow)

    def retranslateUi(self, ZDCCDownloaderWindow):
        _translate = QtCore.QCoreApplication.translate
        ZDCCDownloaderWindow.setWindowTitle(_translate("ZDCCDownloaderWindow", "XDCC Downloader"))
        self.download_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Start the download</p></body></html>"))
        self.download_button.setText(_translate("ZDCCDownloaderWindow", "Download"))
        self.down_arrow_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Move down</p></body></html>"))
        self.down_arrow_button.setText(_translate("ZDCCDownloaderWindow", "▼"))
        self.left_arrow_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Remove items from queue</p></body></html>"))
        self.left_arrow_button.setText(_translate("ZDCCDownloaderWindow", "◄"))
        self.label_2.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>The IRC Server to connect to</p></body></html>"))
        self.label_2.setText(_translate("ZDCCDownloaderWindow", "Server"))
        self.doqnload_queue_list_widget.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>This is the download queue.</p></body></html>"))
        self.search_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Start the search</p></body></html>"))
        self.search_button.setText(_translate("ZDCCDownloaderWindow", "Search"))
        self.search_engine_combo_box.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>The Search Engine(s) to use</p></body></html>"))
        self.search_term_edit.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Enter the search term here</p></body></html>"))
        self.label_3.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Specify the target directory for the downloaded files</p></body></html>"))
        self.label_3.setText(_translate("ZDCCDownloaderWindow", "Destination"))
        self.rigth_arrow_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Add packs to queue</p></body></html>"))
        self.rigth_arrow_button.setText(_translate("ZDCCDownloaderWindow", "►"))
        self.label.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>The XDCC Message copied from a packlist site</p></body></html>"))
        self.label.setText(_translate("ZDCCDownloaderWindow", "Message"))
        self.add_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Adds the Pack to the Queue</p></body></html>"))
        self.add_button.setText(_translate("ZDCCDownloaderWindow", "Add"))
        self.up_arrow_button.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>Move up</p></body></html>"))
        self.up_arrow_button.setText(_translate("ZDCCDownloaderWindow", "▲"))
        self.search_result_tree_widget.setToolTip(_translate("ZDCCDownloaderWindow", "<html><head/><body><p>The Search results are displayed here</p></body></html>"))
        self.search_result_tree_widget.headerItem().setText(0, _translate("ZDCCDownloaderWindow", "Bot"))
        self.search_result_tree_widget.headerItem().setText(1, _translate("ZDCCDownloaderWindow", "Pack"))
        self.search_result_tree_widget.headerItem().setText(2, _translate("ZDCCDownloaderWindow", "Size"))
        self.search_result_tree_widget.headerItem().setText(3, _translate("ZDCCDownloaderWindow", "Filename"))

