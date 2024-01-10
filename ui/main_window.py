import PySide6.QtCore
from const import Mode
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self, mode) -> None:
        super().__init__()

        
            
    def closeEvent(self, event) -> None:
        self.gpt_chat_main.release_resource()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
