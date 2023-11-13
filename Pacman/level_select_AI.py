import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from pacman import GhostRules
def open_level_selection():
    # Tạo cửa sổ mới cho việc chọn mức độ
    level_window = tk.Toplevel()
    level_window.title("Chọn mức độ")

    # Tạo 2 frame
    level_frame = tk.Frame(level_window, relief="groove")
    algorithm_frame = tk.Frame(level_window, relief="groove")

    # Thêm các widget vào các frame
    level_frame.pack()
    algorithm_frame.pack()

    # Tạo tiêu đề cho mức độ
    level_label = tk.Label(level_frame, text="LEVEL", font=("Arial", 20))
    level_label.pack(pady=20)

    # Tạo tiêu đề cho thuật toán
    algorithm_label = tk.Label(algorithm_frame, text="ALGORITHM", font=("Arial", 20))
    algorithm_label.pack(pady=20)

    level_label.pack(pady=20)
    # Tạo các nút mức độ
    easy_button = tk.Button(level_frame, text="Easy", width=10, height=2)
    easy_button.pack(side=tk.LEFT, pady=10, padx=10)

    medium_button = tk.Button(level_frame, text="Medium", width=10, height=2)
    medium_button.pack(side=tk.LEFT, pady=10, padx=10)

    hard_button = tk.Button(level_frame, text="Hard", width=10, height=2)
    hard_button.pack(side=tk.LEFT, pady=10, padx=10)

    # Tạo các nút algorithm
    dfs_button = tk.Button(algorithm_frame, text="DFS", width=10, height=2)
    dfs_button.pack(side=tk.LEFT, pady=10, padx=10)

    bfs_button = tk.Button(algorithm_frame, text="BFS", width=10, height=2)
    bfs_button.pack(side=tk.LEFT, pady=10, padx=10)

    astar_button = tk.Button(algorithm_frame, text="A*", width=10, height=2)
    astar_button.pack(side=tk.LEFT, pady=10, padx=10)