import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from pacman import GhostRules
def open_level_selection():
    # Tạo cửa sổ mới cho việc chọn mức độ
    level_window = tk.Toplevel()
    level_window.title("CHOOSE LEVEL & ALGORITHM")
    # Đặt vị trí cửa sổ mới giữa màn hình
    window_width = 850
    window_height = 500
    screen_width = level_window.winfo_screenwidth()
    screen_height = level_window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    level_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Tạo 2 frame
    level_frame = tk.Frame(level_window, relief="groove")
    algorithm_frame = tk.Frame(level_window, relief="groove")

    # Set the size of the buttons
    button_width = 12
    button_height = 3
    Button_Font = ("Gamer Station", 15)

    # Tạo biến level và algorithm
    level = tk.StringVar()
    algorithm = tk.StringVar()

    # Thêm các widget vào các frame
    level_frame.pack()
    algorithm_frame.pack()

    # Tạo tiêu đề cho mức độ
    level_label = tk.Label(level_frame, text="LEVEL", font=("PacFont", 20))
    level_label.pack(pady=20)

    # Tạo tiêu đề cho thuật toán
    algorithm_label = tk.Label(algorithm_frame, text="ALGORITHM", font=("PacFont", 20))
    algorithm_label.pack(pady=20)

    level_label.pack(pady=20)
    # Tạo các nút mức độ
    easy_button = tk.Button(level_frame, text="Easy", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_levelTextbox(level_textbox,level, "EASY"))
    easy_button.pack(side=tk.LEFT, pady=10, padx=10)

    medium_button = tk.Button(level_frame, text="Medium", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_levelTextbox(level_textbox,level, "MEDIUM"))
    medium_button.pack(side=tk.LEFT, pady=10, padx=10)

    hard_button = tk.Button(level_frame, text="Hard", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_levelTextbox(level_textbox,level, "HARD"))
    hard_button.pack(side=tk.LEFT, pady=10, padx=10)

    # Tạo các nút algorithm
    dfs_button = tk.Button(algorithm_frame, text="DFS", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_algorithmTextbox(algorithm_textbox,algorithm, "DFS"))
    dfs_button.pack(side=tk.LEFT, pady=10, padx=10)

    bfs_button = tk.Button(algorithm_frame, text="BFS", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_algorithmTextbox(algorithm_textbox,algorithm, "BFS"))
    bfs_button.pack(side=tk.LEFT, pady=10, padx=10)

    astar_button = tk.Button(algorithm_frame, text="A*", font=Button_Font, width=button_width,
                              height=button_height, command=lambda: update_algorithmTextbox(algorithm_textbox,algorithm, "AStar"))
    astar_button.pack(side=tk.LEFT, pady=10, padx=10)

    # Tạo nút Play
    play_button = tk.Button(level_window, text="Play", font=Button_Font, width=button_width,
                            height=button_height, command=lambda: play(level.get(), algorithm.get()))
    play_button.pack(pady=20)

    # Tạo ô văn bản cho Level và Algorithm
    level_textbox = tk.Text(level_frame, width=button_width, height=1, font=Button_Font)
    level_textbox.pack(side=tk.LEFT, pady=10, padx=10)
    level_textbox.insert(tk.END, level.get())

    algorithm_textbox = tk.Text(algorithm_frame, width=button_width, height=1, font=Button_Font)
    algorithm_textbox.pack(side=tk.LEFT, pady=10, padx=10)
    algorithm_textbox.insert(tk.END, algorithm.get())

def update_levelTextbox(level_textbox, level, value):
    # Thực hiện các hành động liên quan đến việc chơi game với level và algorithm đã chọn
    level_textbox.delete("1.0", tk.END)
    level.set(value)
    level_textbox.insert(tk.END, level.get())

def update_algorithmTextbox(algorithm_textbox, algorithm, value):
    # Thực hiện các hành động liên quan đến việc chơi game với level và algorithm đã chọn
    algorithm_textbox.delete("1.0", tk.END)
    algorithm.set(value)
    algorithm_textbox.insert(tk.END, algorithm.get())

def play(level, algorithm):
    level_string = level.lower() + 'MapAI'
    algorithm_string = algorithm + 'FoodSearchAgent'
    command = f"python pacman.py -l {level_string} -p {algorithm_string}"
    subprocess.run(command, shell=True)

def easyLevelAI(level, algorithm):
    level_string =level.lower() +'MapAI'
    algorithm_string = algorithm+'FoodSearchAgent'
    command = f"python pacman.py -l {level_string} -p {algorithm_string}"
    subprocess.run(command, shell=True)

