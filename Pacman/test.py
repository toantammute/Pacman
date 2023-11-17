###########################      IMPORT LIBRARY          ###########################
import tkinter as tk
import subprocess
import level_select_human
import level_select_AI
from PIL import Image, ImageTk, ImageFont
from tkmacosx import Button
###########################      END IMPORT LIBRARY          ###########################


###########################      FUNCTION FOR BUTTON          ###########################
def start_player_game():
    # Hành động khi nhấn nút "Người chơi"
    level_select_human.open_level_selection()
def start_ai_game():
    # Hành động khi nhấn nút "Máy chơi"
    level_select_AI.open_level_selection()
def exit_game():
    # Hành động khi nhấn nút "Exit"
    print("Thoát trò chơi")
    root.destroy()
###########################      END FUNCTION FOR BUTTON          ###########################


###########################      SET UP ROOT          ###########################
width_root = 850
height_root = 550
root = tk.Tk()
root.title("PACMAN GAME")
# Set size of root
root.geometry(f"{width_root}x{height_root}")

###########################      END SET UP ROOT          ###########################



###########################      DEFINE FONT          ###########################
Button_Font = ("PacFont", 15)
Member_Font = ("BlockKie",10)
###########################      END DEFINE FONT          ###########################



###########################      MEMBER IN GROUP          ###########################
# Tạo khung
frame = tk.Frame(root, borderwidth=5,relief='sunken')
frame.pack(anchor="nw")

# Tạo nhãn thành viên
member_label1 = tk.Label(frame, text="MEMBERS", font=Member_Font, justify=tk.CENTER)
member_label1.pack()

# Căn đều các label tên thành viên
for i, name in enumerate(["Pham Hoang Anh - 21110753", "Dang Hieu Anh - 21110751", "Le Nguyen Toan Tam - 21110797"]):
    member_label = tk.Label(frame, text=name, font=Member_Font)
    member_label.pack()

###########################      END MEMBER IN GROUP          ###########################

title_label = tk.Label(root, text="PACMAN GAME", font=("PacFont",35,"bold"))
title_label.pack( pady=40)
###########################      DEFINE BUTTON          ###########################
# Set the size of the buttons
button_width = 12
button_height = 3
# Create the buttons
player_button = tk.Button(root, text="HUMAN PLAY", command=start_player_game, font=Button_Font, width=button_width, height=button_height)
ai_button = tk.Button(root, text="AI PLAY",bg='black',fg='white', command=start_ai_game, font=Button_Font, width=button_width, height=button_height)
exit_button = tk.Button(root, text="Exit", command=exit_game, font=Button_Font, width=button_width, height=button_height)
# Pack the buttons
player_button.pack(pady=10)
ai_button.pack(pady=10)
exit_button.pack(pady=10)
###########################      END DEFINE BUTTON          ###########################


root.mainloop()