import tkinter as tk
from PIL import Image, ImageTk
from algorithms import random_path, manhatten_and_euclidean
from util import Util
from time import sleep

MOVE_INCREMENT = 20
MOVES_PER_SECOND = 2
GAME_SPEED = 1000 // MOVES_PER_SECOND

utility = Util()
class PathFinding(tk.Canvas):

    def __init__(self):
        super().__init__(width = 800, height = 460, background = "black", highlightthickness = 0)

        # declaring all positions for: player, food, walls
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"

        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.create_objects()
        self.show_algorithms()

    # function to load images from assets folder
    def load_assets(self):
        try:
            self.player_img = Image.open("assets/player.png")
            self.player = ImageTk.PhotoImage(self.player_img)

            self.wall_img = Image.open("assets/wall.png")
            self.wall = ImageTk.PhotoImage(self.wall_img)

            self.food_img = Image.open("assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_img)

        except IOError as error:
            print("Error in loading assets : ", error)
            root.destroy()

    # function to create and display loaded images
    def create_objects(self):
        for x_pos, y_pos in self.wall_pos:
            self.create_image(x_pos, y_pos, image = self.wall, tag = "walls")

        self.create_image(*self.player_pos, image = self.player, tag = "player")
        self.create_image(*self.food_pos, image = self.food, tag = "food")
        self.create_rectangle(20, 40, 780, 440, outline="#525d69")

        self.create_text(
            40, 20, text=f"Moves: {self.num_moves}", tag="moves", fill="#fff", font=10
        )

    def show_algorithms(self):

        var_string = tk.StringVar(self, "random")
        self.create_text(200, 20, text=f"You have selected : ", tag="option", fill="#fff", font=10)

        self.frame = tk.Frame(left_pannal, borderwidth=3)

        self.radiobutton1 = tk.Radiobutton(self.frame, text='Random movement', variable=var_string, value='random', command = lambda: self.change_text(var_string.get()) )
        self.radiobutton1.pack(anchor=tk.W)

        self.radiobutton2 = tk.Radiobutton(self.frame, text='Closest using Manhatten', variable=var_string, value='manhatten', command = lambda: self.change_text(var_string.get()) )
        self.radiobutton2.pack(anchor=tk.W)

        self.radiobutton3 = tk.Radiobutton(self.frame, text='Closest using Euclidean', variable=var_string, value='euclidean', command = lambda: self.change_text(var_string.get()) )
        self.radiobutton3.pack(anchor=tk.W)

        self.frame.pack(side=tk.LEFT)

    def change_text(self, option_selected):
        print("Option selected : ", option_selected)
        options = self.find_withtag("option")
        self.itemconfigure(options, text="You have selected : " + option_selected, tag="option")
        self.activate_algorithm(option_selected)

    def activate_algorithm(self, algo_name):
        if algo_name == "random":
            self.run_random()

        elif algo_name == "manhatten":
            self.run_manh_euclidean(True)

        elif algo_name == "euclidean":
            self.run_manh_euclidean(False)

    def run_random(self):
        self.num_moves = 0
        random_algo = random_path.RandomPath()
        self.moves_list = random_algo.get_next_moves()
        self.moves_list = self.moves_list[::-1]
        self.after(GAME_SPEED, self.perform_actions)

    def run_manh_euclidean(self, run_manh):
        self.num_moves = 0
        manh_euclidean = manhatten_and_euclidean.ManhattenEuclidean()

        if run_manh:
            self.moves_list = manh_euclidean.get_next_moves_manhatten()
            self.moves_list = self.moves_list[::-1]
            self.after(GAME_SPEED, self.perform_actions)
        else:
            self.moves_list = manh_euclidean.get_next_moves_euclidean()
            self.moves_list = self.moves_list[::-1]
            self.after(GAME_SPEED, self.perform_actions)

    def on_key_press(self, key):
        new_direction = key.keysym
        new_position = utility.direction_to_loc(new_direction, self.player_pos)
        if not utility.check_collisions(new_position):
            self.move_player(new_position)

    def move_player(self, new_position):
        self.player_pos = new_position
        self.coords(self.find_withtag("player"), *self.player_pos)
        self.num_moves += 1
        moves = self.find_withtag("moves")
        self.itemconfigure(moves, text=f"Moves: {self.num_moves}", tag="moves")
        # print("Called")

    def perform_actions(self):
        if len(self.moves_list) == 0:
            return
        move = self.moves_list.pop()
        self.move_player(move)
        self.after(GAME_SPEED, self.perform_actions)


# creating instance of tk-inter
root = tk.Tk()
root.title('Path Fidning')
root.geometry("950x460+30+30")

left_pannal = tk.Label(root)
left_pannal.pack(side=tk.LEFT)

# creating instance of our Game class and launching it
path_find = PathFinding()
path_find.pack()

# looping scene to visualoze it untill we close it
root.mainloop()
