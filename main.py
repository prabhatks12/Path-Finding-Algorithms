import tkinter as tk
from PIL import Image, ImageTk
from algorithms import random_path
from util import Util

MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
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


        random_moves = random_path.RandomPath()
        self.next_moves = random_moves.get_next_moves()
        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.create_objects()
        self.multiple_moves(self.next_moves)

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
            print(error)
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

    def multiple_moves(self, list_of_moves):
        for moves in list_of_moves:
            self.after(1000, self.move_player(moves))


#  self.after(GAME_SPEED, self.perform_actions)



# creating instance of tk-inter
root = tk.Tk()
root.title('Path Fidning')

# creating instance of our Game class and launching it
path_find = PathFinding()
path_find.pack()

# looping scene to visualoze it untill we close it
root.mainloop()
