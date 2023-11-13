import tkinter as tk
import subprocess
from pacman import GhostRules
def open_level_selection():
    # Tạo cửa sổ mới cho việc chọn mức độ
    level_window = tk.Toplevel()
    level_window.title("Chọn mức độ")

    # Đặt vị trí cửa sổ mới giữa màn hình
    window_width = 300
    window_height = 200
    screen_width = level_window.winfo_screenwidth()
    screen_height = level_window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    level_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Tạo tiêu đề cho mức độ
    level_label = tk.Label(level_window, text="LEVEL", font=("Arial", 20))
    level_label.pack(pady=20)

    # Tạo các nút mức độ và hình ảnh
    easy_button = tk.Button(level_window, text="Easy", command=easyLevelforHuman)
    easy_button.pack(pady=10)

    medium_button = tk.Button(level_window, text="Medium",command=mediumLevelforHuman)
    medium_button.pack(pady=10)

    hard_button = tk.Button(level_window, text="Hard", command=hardLevelforHuman)
    hard_button.pack(pady=10)

def easyLevelforHuman():
    command = "python pacman.py -l easyMapHuman"
    subprocess.run(command, shell=True)

def mediumLevelforHuman():
    command = "python pacman.py -l mediumMapHuman"
    subprocess.run(command, shell=True)

def hardLevelforHuman():
    command = "python pacman.py -l hardMapHuman"
    subprocess.run(command, shell=True)
