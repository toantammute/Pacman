import tkinter as tk
import subprocess
import level_select_human
import level_select_AI
from PIL import Image, ImageTk, ImageFont
import pyglet, os

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

root = tk.Tk()
root.title("PACMAN GAME")

Font_tuple = ("PacFont", 20, "bold")
# Tạo một đối tượng PhotoImage từ file GIF
#gif = ImageTk.PhotoImage(Image.open("images/giphy.gif"))

# Đặt đối tượng PhotoImage làm background cho root
background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Tạo khung
frame = tk.Frame(root, borderwidth=1, relief="solid")
frame.pack(anchor="nw")

# Tạo nhãn thành viên
member_label1 = tk.Label(frame, text="MEMBERS :")
member_label1.pack(anchor="nw")
member_label2 = tk.Label(frame, text="Pham Hoang Anh - 21110753")
member_label2.pack(anchor="nw")
member_label3 = tk.Label(frame, text="Dang Hieu Anh - 21110751")
member_label3.pack(anchor="nw")
member_label4 = tk.Label(frame, text="Le Nguyen Toan Tam - 21110797")
member_label4.pack(anchor="nw")
# Tạo các nút và đặt chúng trong giao diện
# Set the size of the buttons
button_width = 40
button_height = 3

# Create the buttons
player_button = tk.Button(root, text="HUMAN PLAY",bg='blue', command=start_player_game, font=Font_tuple, width=button_width, height=button_height)
ai_button = tk.Button(root, text="AI PLAY", command=start_ai_game, font=Font_tuple, width=button_width, height=button_height)
exit_button = tk.Button(root, text="Exit", command=exit_game, font=Font_tuple, width=button_width, height=button_height)



# Pack the buttons
player_button.pack()
ai_button.pack()
exit_button.pack()



root.mainloop()