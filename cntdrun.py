import sys
import argparse
import subprocess
from importlib.metadata import version
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt, QSize

class CountdownWindow(QMainWindow):
    def __init__(self, count, command, window_width, window_height,
                 label_font, label_size, button_text, button_font, button_size,
                 window_x, window_y, command_label_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ctndrun")
        self.setStyleSheet(
            "QMainWindow {border: 1px solid green; background-color: black;}"
            "QLabel { background-color: black; }"
            "QLabel {border: 1px solid black; color: green;}"
            "QPushButton {background-color: black; color: green; border: 1px solid green;}"
        )
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.resize(window_width, window_height)
        if window_x is not None and window_y is not None:
            self.move(window_x, window_y)
        else:
            self.center()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)


        self.command_label = QLabel(command_label_text if command_label_text else f"Command: {command}")
        self.command_label.setFont(QFont(label_font, label_size // 2))
        self.command_label.setAlignment(Qt.AlignCenter)
        self.command_label.setWordWrap(True)
        main_layout.addWidget(self.command_label)

        self.countdown_label = QLabel(str(count))
        self.countdown_label.setFont(QFont(label_font, label_size))
        self.countdown_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.countdown_label, 1)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.close_button = QPushButton(button_text)
        self.close_button.setFont(QFont(button_font, button_size))
        self.close_button.clicked.connect(self.close)
        self.close_button.setFixedSize(QSize(80, 30))
        button_layout.addStretch(1)
        button_layout.addWidget(self.close_button)
        button_layout.addStretch(1)

        self.countdown = count
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)
        self.command = command

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_countdown(self):
        if self.countdown > 0:
            self.countdown -= 1
            self.countdown_label.setText(str(self.countdown))
        if self.countdown == 0:
            self.countdown_label.setText("0")
            self.timer.stop()
            QTimer.singleShot(100, self.execute_command)

    def execute_command(self):
        if self.command:
            print("Executing command:", self.command)
            try:
                result = subprocess.run(
                    self.command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                if result.returncode == 0:
                    print(f"Command executed successfully. Output: {result.stdout.strip()}")
                    self.countdown_label.setText("Over")
                else:
                    print(f"Command execution failed. Error: {result.stderr.strip()}")
                    self.countdown_label.setText("Error")
            except Exception as e:
                print("Error occurred while executing command:", e)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.close_button.click()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="Countdown time in seconds")
    parser.add_argument("command", type=str, help="Command to execute after countdown")
    
    parser.add_argument("--command-label", type=str, default=None, help="Custom text for command label")
    parser.add_argument('--version', action='version', version=version("cntdrun"))

    parser.add_argument("--window-width", type=int, default=250, help="Width of the window")
    parser.add_argument("--window-height", type=int, default=150, help="Height of the window")
    parser.add_argument("--window-x", type=int, default=None, help="X position of the window")
    parser.add_argument("--window-y", type=int, default=None, help="Y position of the window")
    
    parser.add_argument("--label-font", type=str, default="Arial", help="Font for countdown label")
    parser.add_argument("--label-size", type=int, default=32, help="Font size for countdown label")
    parser.add_argument("--button-text", type=str, default="close", help="Text for close button")
    parser.add_argument("--button-font", type=str, default="Arial", help="Font for close button")
    parser.add_argument("--button-size", type=int, default=10, help="Font size for close button")

    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = CountdownWindow(
        args.count, args.command,
        args.window_width, args.window_height,
        args.label_font, args.label_size,
        args.button_text, args.button_font, args.button_size,
        args.window_x, args.window_y,
        args.command_label
    )
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
