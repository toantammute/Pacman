import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import random
'''
def run_pacman_AStar():
    command = "python pacman.py -l mediumScaryMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic"
    subprocess.run(command, shell=True)
def run_pacman_BFS():
    command = "python pacman.py -l mediumScaryMaze -p SearchAgent -a fn=bfs"
    subprocess.run(command, shell=True)
def run_pacman_DFS():
    command = "python pacman.py -l mediumScaryMaze -p SearchAgent -a fn=dfs"
    subprocess.run(command, shell=True)
def play():
    command = "python pacman.py"
    subprocess.run(command, shell=True)
# Tạo cửa sổ giao diện
window = tk.Tk()
font_game = ("Arcade", 20, "bold")
# Tạo hình ảnh background
background_image = Image.open("images/background.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
background_image = background_image.resize((screen_width, screen_height))
# Hiển thị hình ảnh background
background_label = tk.Label(window, image=background_photo)
background_label.pack()
# Tạo nút A*
button = tk.Button(window, text="Play", command=play, font=font_game)
button.pack()
button = tk.Button(window, text="A*", command=run_pacman_AStar)
button.pack()
button = tk.Button(window, text="BFS", command=run_pacman_BFS)
button.pack()
button = tk.Button(window, text="DFS", command=run_pacman_DFS)
button.pack()

# Chạy vòng lặp giao diện
window.mainloop()
'''
def generateRandomMap(width, height):
    # Tạo 1 map hcn rỗng bên trong
    map = [['%' for _ in range(width)] for _ in range(height)]
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            map[i][j] = ' '
    # end
    # gắn vị trí mặc định của P
    map[1][1] = 'P'
    # random các phần tử bên trong
    count_G = 2;
    count_walls = 250;
    count_dot = 5;
    for i in range(0, count_G):
        row = random.randint(2, 17)
        col = random.randint(2, 37)
        if (map[row][col] == 'G'): i = i-1
        else: map[row][col] = 'G'
    for i in range(0, count_walls):
        row = random.randint(2, 17)
        col = random.randint(2, 37)
        if(map[row][col] != 'G'): map[row][col] = '%'
    for i in range(0, count_dot):
        row = random.randint(2, 17)
        col = random.randint(2, 37)
        if(map[row][col] != 'G'): map[row][col] = '.'
    with open('layouts/random.lay', 'w') as f:
        for row in map:
            f.write(''.join(row) + '\n')
    # Return the map
    return map
map = generateRandomMap(38, 18)

'''
def read_layout(filename):
    with open(filename, 'r') as f:
        layout = []
        for line in f:
            layout.append([c for c in line])
    return layout

def count_percentage(layout):
    count = 0
    for row in layout:
        for c in row:
            if c == '%':
                count += 1
    return count

layout = read_layout('layouts/random.lay')
count = count_percentage(layout)
print(count)
'''