import sys
import argparse
import subprocess
from importlib.metadata import version
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt

class CountdownWindow(QMainWindow):
    def __init__(self, count, command, label_font, label_size, label_x, label_y, label_width, label_height,
                 button_text, button_x, button_y, button_width, button_height, button_font, button_size, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ctndrun")
        self.setGeometry(0, 0, 250, 150)
        self.setStyleSheet(
            "border: 1px solid green; color: green; background-color: black;"
        )
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        screen = QApplication.desktop().screenGeometry()
        x = int((screen.width() - self.width()) / 2)
        y = int((screen.height() - self.height()) / 2)
        self.move(x, y)

        self.countdown_label = QLabel(self)
        self.countdown_label.setFont(QFont(label_font, label_size))
        self.countdown_label.setGeometry(label_x, label_y, label_width, label_height)
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet("border: 1px solid black;")

        self.close_button = QPushButton(button_text, self)
        self.close_button.setFont(QFont(button_font, button_size))
        self.close_button.setGeometry(button_x, button_y, button_width, button_height)
        self.close_button.clicked.connect(self.close)

        self.countdown = count
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)
        self.command = command
        self.countdown_label.setText(str(self.countdown))

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
    parser.add_argument('--version', action='version', version=version("cntdrun"))
    
    # Arguments for customization
    parser.add_argument("--label-font", type=str, default="Arial", help="Font for countdown label")
    parser.add_argument("--label-size", type=int, default=32, help="Font size for countdown label")
    parser.add_argument("--label-x", type=int, default=50, help="X position of countdown label")
    parser.add_argument("--label-y", type=int, default=20, help="Y position of countdown label")
    parser.add_argument("--label-width", type=int, default=150, help="Width of countdown label")
    parser.add_argument("--label-height", type=int, default=50, help="Height of countdown label")
    parser.add_argument("--button-text", type=str, default="close", help="Text for close button")
    parser.add_argument("--button-x", type=int, default=100, help="X position of close button")
    parser.add_argument("--button-y", type=int, default=100, help="Y position of close button")
    parser.add_argument("--button-width", type=int, default=50, help="Width of close button")
    parser.add_argument("--button-height", type=int, default=30, help="Height of close button")
    parser.add_argument("--button-font", type=str, default="Arial", help="Font for close button")
    parser.add_argument("--button-size", type=int, default=10, help="Font size for close button")

    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = CountdownWindow(
        args.count, args.command,
        args.label_font, args.label_size, args.label_x, args.label_y, args.label_width, args.label_height,
        args.button_text, args.button_x, args.button_y, args.button_width, args.button_height,
        args.button_font, args.button_size
    )
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
