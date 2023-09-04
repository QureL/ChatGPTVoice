from PySide6.QtGui import QGuiApplication
from ui.design.Ui_system_subtitle import Ui_Subtitle
from PySide6.QtWidgets import QLabel, QVBoxLayout, QMainWindow, QSizePolicy, QWidget
from PySide6.QtCore import Qt
import logging

class SystemSubtitle(QMainWindow, Ui_Subtitle):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 创建一个 QLabel 并设置初始文本内容
        self.label = QLabel(".....")
        self.label.setAlignment(Qt.AlignCenter)  # 文本居中显示

        # 设置 QLabel 的大小策略为 Expanding
        self.label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # 创建一个垂直布局管理器，并将 QLabel 添加进去
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # 创建一个 QWidget，并将布局管理器设置为窗体的主部件
        widget = QWidget()
        widget.setLayout(layout)

        # 将主部件设置为 QMainWindow 的中心部件
        self.setCentralWidget(widget)
        self.setWindowOpacity(0.8)
        desktop = QGuiApplication.primaryScreen().geometry()
        x = (desktop.width() - self.width()) // 2
        y = desktop.height() * 0.9 - self.height()
        self.move(x, y)

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def update(self, str):
        logging.debug("update str=%s", str)
        self.label.setText(str)
        self.adjustSize()

    def mousePressEvent(self, event):
        # 捕获鼠标按下事件，并记录鼠标点击点相对于窗体左上角的偏移量
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        # 捕获鼠标移动事件，并在窗体可移动时更新窗体的位置
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        # 捕获鼠标释放事件，表示窗体不可移动
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False

    def mouseDoubleClickEvent(self, event):
        # 捕获鼠标双击事件，关闭窗体
        self.close()