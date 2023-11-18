import tkinter as tk
import subprocess
from PIL import ImageTk, Image
from pacman import GhostRules
def open_level_selection():
    # Tạo cửa sổ mới cho việc chọn mức độ
    level_window = tk.Toplevel()
    level_window.title("CHOOSE LEVEL")
    # Đặt vị trí cửa sổ mới giữa màn hình
    window_width = 850
    window_height = 500
    screen_width = level_window.winfo_screenwidth()
    screen_height = level_window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    level_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Tạo tiêu đề cho mức độ
    level_label = tk.Label(level_window, text="LEVEL", font=("PacFont",35,"bold"))
    level_label.pack(pady=30)

    # Set the size of the buttons
    button_width = 12
    button_height = 3
    Button_Font = ("PacFont", 15)
    # Tạo một khung để chứa các nút
    button_frame = tk.Frame(level_window)
    button_frame.pack(pady=10)

    # Tạo các nút trong khung
    easy_button = tk.Button(button_frame, text="Easy", command=easyLevelforHuman, font=Button_Font, width=button_width,
                              height=button_height)
    easy_button.pack(side=tk.LEFT, padx=10)

    medium_button = tk.Button(button_frame, text="Medium", command=mediumLevelforHuman, font=Button_Font,
                          width=button_width, height=button_height)
    medium_button.pack(side=tk.LEFT, padx=10)

    hard_button = tk.Button(button_frame, text="Hard", command=hardLevelforHuman, font=Button_Font, width=button_width,
                            height=button_height)
    hard_button.pack(side=tk.LEFT, padx=10)



def easyLevelforHuman():
    command = "python pacman.py -l easyMapHuman"
    subprocess.run(command, shell=True)

def mediumLevelforHuman():
    command = "python pacman.py -l mediumMapHuman"
    subprocess.run(command, shell=True)

def hardLevelforHuman():
    command = "python pacman.py -l hardMapHuman"
    subprocess.run(command, shell=True)
