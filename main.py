import tkinter as tk
from PIL import Image, ImageTk


MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
GAME_SPEED = 1000 // MOVES_PER_SECOND


class PathFinding(tk.Canvas):

    def __init__(self):
        super().__init__(width = 800, height = 460, background = "black", highlightthickness = 0)

        # declaring all positions for: player, food, walls
        self.player_pos = [(40,60)]
        self.wall_pos = [(400,220),(380,220),(360,220),(340,220),(320,220),(420,220),(440,220),
                        (400,200),(380,200),(360,200),(340,200),(320,200),(420,200),(440,200),
                        (340,180),(320,180),(340,160),(320,160),(340,140),(320,140),(340,120),(320,120),
                        (420,240),(440,240),(420,260),(440,260),(420,280),(440,280),(420,300),(440,300),
                        (140,100),(140,120),(140,80),(140,200),(140,220),(140,180),(140,300),(140,320),(140,280),
                        (600,100),(600,120),(600,80),(600,200),(600,220),(600,180),(600,300),(600,320),(600,280)]
        self.food_pos = [(660,400)]
        self.num_moves = 0
        self.direction = "Right"

        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.create_objects()

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

    def check_collisions(self, new_position):
        (x_pos, y_pos) = new_position[0]

        return (
            x_pos in (20, 780)
            or y_pos in (40, 440)
            or (x_pos, y_pos) in self.wall_pos
        )

    def move_player(self, new_direction):
        (x_pos, y_pos) = self.player_pos[0]

        if new_direction == "Up":
            return [(x_pos, y_pos - MOVE_INCREMENT)]
        elif new_direction == "Right":
            return [(x_pos + MOVE_INCREMENT, y_pos)]
        elif new_direction == "Left":
            return [(x_pos - MOVE_INCREMENT, y_pos)]
        elif new_direction == "Down":
            return [(x_pos, y_pos + MOVE_INCREMENT)]

    def on_key_press(self, key):
        new_direction = key.keysym

        new_position = self.move_player(new_direction)

        if not self.check_collisions(new_position):
            self.player_pos = new_position
            self.coords(self.find_withtag("player"), *self.player_pos)

            self.num_moves += 1
            moves = self.find_withtag("moves")
            self.itemconfigure(moves, text=f"Moves: {self.num_moves}", tag="moves")




# creating instance of tk-inter
root = tk.Tk()
root.title('Path Fidning')

# creating instance of our Game class and launching it
pathFind = PathFinding()
pathFind.pack()

# looping scene to visualoze it untill we close it
root.mainloop()
