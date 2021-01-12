import tkinter as tk
from PIL import Image, ImageTk
from algorithms import random_path, manhatten_and_euclidean, bfs_dfs, heuristic
from util import Util
from time import sleep

MOVE_INCREMENT = 20
EXPLORED_POS_SPEED = 10
CORRECT_PATH_SPEED = 50

utility = Util()

"""
PathFinding Class:
    Class for creating board and show player's movememt using Tkinter face
"""

class PathFinding(tk.Canvas):

    def __init__(self):
        super().__init__(width = 800, height = 460, background = "black", highlightthickness = 0)

        # declaring all positions for: player, food, walls
        self.player_pos = utility.get_player_pos()
        self.wall_pos = utility.get_walls_pos()
        self.food_pos = utility.get_food_pos()
        self.num_moves = 0
        self.direction = "Right"

        # calling functions to create the board
        self.bind_all("<Key>", self.on_key_press)
        self.load_assets()
        self.create_objects()
        self.show_algorithms()


    """
    Function to load images from assets folder
    """
    def load_assets(self):
        try:
            # loading player, wall, food and movement image
            self.player = ImageTk.PhotoImage(Image.open("assets/player.png"))
            self.wall = ImageTk.PhotoImage(Image.open("assets/wall.png"))
            self.food = ImageTk.PhotoImage(Image.open("assets/food.png"))
            self.movement = ImageTk.PhotoImage(Image.open("assets/movement.png"))

        except IOError as error:
            print("Error in loading assets : ", error)
            root.destroy()


    """
    Function to create and display loaded images
    """
    def create_objects(self):
         # displaying walls
        for x_pos, y_pos in self.wall_pos:
            self.create_image(x_pos, y_pos, image = self.wall, tag = "walls")

        # displaying player,food,boundary image and score
        self.create_image(*self.player_pos, image = self.player, tag = "player")
        self.create_image(*self.food_pos, image = self.food, tag = "food")
        self.create_rectangle(20, 40, 780, 440, outline="#525d69")
        self.create_text(40, 20, text=f"Moves: {self.num_moves}", tag="moves", fill="#fff", font=10)


    """
    Function to show all algorithms as option on left side of screen
    """
    def show_algorithms(self):
        # string to store option selected
        var_string = tk.StringVar(self, "random")
        self.create_text(200, 20, text=f"Select an option", tag="option", fill="#fff", font=10)

        text_value = {'Random movement' : 'random',
                     'Closest using Manhatten' : 'manhatten',
                     'Closest using Euclidean' : 'euclidean',
                     'Breath First Search' : 'bfs',
                     'Depth First Search' : 'dfs',
                     'Heuristic A*' : 'astar'
                    }

        # adding all radiobuttons to the frames
        self.frame = tk.Frame(left_pannal, borderwidth=3)

        # adding radiobuttons for all algorithms
        for text in text_value:
            tk.Radiobutton(self.frame, text=text, variable=var_string, value=text_value[text], command = lambda: self.call_algorithms(var_string.get()) ).pack(anchor=tk.W)

        self.frame.pack(side=tk.LEFT)


    """
    Function to call algorithms base on option selected and update the text on top
    """
    def call_algorithms(self, option_selected):
        # updating the text on top for selected option
        options = self.find_withtag("option")
        self.itemconfigure(options, text="You have selected : " + option_selected, tag="option")
        # reseting the board first to stop all ongoing activites
        self.reset_board()
        # calling the selected function
        if option_selected == "random":
            self.run_random()
        elif option_selected == "manhatten":
            self.run_manh_euclidean(True)
        elif option_selected == "euclidean":
            self.run_manh_euclidean(False)
        elif option_selected == "bfs":
            self.run_bfs_dfs(True)
        elif option_selected == "dfs":
            self.run_bfs_dfs(False)
        elif option_selected == "astar":
            self.run_astar()


    """
    Function to randomly move the player
    """
    def run_random(self):
        self.num_moves = 0
        random_algo = random_path.RandomPath()
        self.moves_list = random_algo.get_next_moves()
        self.moves_list = self.moves_list[::-1]
        self.perform_actions()
        return


    """
    Function to run player to positions closest to food based on manhatten or euclidean distance
    """
    def run_manh_euclidean(self, run_manh):
        self.num_moves = 0
        manh_euclidean = manhatten_and_euclidean.ManhattenEuclidean()

        if run_manh:
            self.player_path, self.visited_path = manh_euclidean.get_next_moves_manhatten()
        else:
            self.player_path, self.visited_path = manh_euclidean.get_next_moves_euclidean()

        self.visited_path, self.player_path = self.visited_path[::-1], self.player_path[::-1]
        self.show_visited_pos()
        return


    """
    Function to run player to positions based on BFS or DFS algorithm
    """
    def run_bfs_dfs(self, run_bfs):
        self.num_moves = 0
        bfsdfs_algo = bfs_dfs.BfsDfs()

        if run_bfs:
            self.player_path, self.visited_path = bfsdfs_algo.get_next_moves_bfs()
        else:
            self.player_path, self.visited_path = bfsdfs_algo.get_next_moves_dfs()
        self.visited_path, self.player_path = self.visited_path[::-1], self.player_path[::-1]
        self.show_visited_pos()
        return


    """
    Function to run A star algorithm on player
    """
    def run_astar(self):
        self.num_moves = 0
        astar_algo = heuristic.AStar()
        self.player_path, self.visited_path = astar_algo.get_next_moves()
        self.visited_path, self.player_path = self.visited_path[::-1], self.player_path[::-1]
        self.show_visited_pos()
        return


    """
    Function to move player based on key pressed on keyboard
    """
    def on_key_press(self, key):
        new_direction = key.keysym
        new_position = utility.direction_to_loc(new_direction, self.player_pos)
        if not utility.check_collisions(new_position):
            self.move_player(new_position)


    """
    Function to move player based on path stored in moves_list
    """
    def perform_actions(self):
        if len(self.moves_list) == 0:
            return
        move = self.moves_list.pop()
        self.move_player(move)
        self.after(CORRECT_PATH_SPEED, self.perform_actions)


    """
    Function to bring board on intial state
    """
    def reset_board(self):
        try:
            # clearing all the locations which are visited and player image
            self.delete("visited")
            self.delete("player")
            self.create_image(*self.player_pos, image = self.player, tag = "player")
        except IOError as error:
            print("[Error] Error in reset_board(), cause: ", error)

    """
    Function to show explored positions
    """
    def show_visited_pos(self):
        try:
            if len(self.visited_path) == 0:
                self.show_player_moves()
            else:
                next_position = self.visited_path.pop()
                self.create_image(*next_position, image = self.movement, tag = "visited")
                self.after(EXPLORED_POS_SPEED, self.show_visited_pos)
        except IOError as error:
            print("[Error] Error in show_visited_pos(), cause: ", error)
        return


    """
    Function to show path taken by player to reach food
    """
    def show_player_moves(self):
        try:
            self.reset_board()
            if len(self.player_path) == 0:
                return
            else:
                next_position = self.player_path.pop()
                self.move_player(next_position)
                self.after(CORRECT_PATH_SPEED, self.show_player_moves)
        except IOError as error:
            print("[Error] Error in show_player_moves(), cause: ", error)


    """
    Function to move player on the board and update the score
    """
    def move_player(self, next_position):
        # moving the player
        self.player_pos = next_position
        self.coords(self.find_withtag("player"), *self.player_pos)
        # updating the score
        self.num_moves += 1
        moves = self.find_withtag("moves")
        self.itemconfigure(moves, text=f"Moves: {self.num_moves}", tag="moves")


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
