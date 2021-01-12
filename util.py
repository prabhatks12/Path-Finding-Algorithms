import math
import random
# for each direction, we move 20 pixel
MOVE_INCREMENT = 20
GAME_SPEED = 10

"""
Util Class:
    Defininig all the functions which are going to be use repeatedly by other classes
"""

class Util():
    def __init__(self):
        self.player_pos = (40,60)
        """
        self.wall_pos = [(400,220),(380,220),(360,220),(340,220),(320,220),(420,220),(440,220),(400,200),(380,200),(360,200),(340,200),(320,200),(420,200),(440,200),
                        (340,180),(320,180),(340,160),(320,160),(340,140),(320,140),(340,120),(320,120),(420,240),(440,240),(420,260),(440,260),(420,280),(440,280),(420,300),(440,300),
                        (140,100),(140,120),(140,80),(140,200),(140,220),(140,180),(140,300),(140,320),(140,280),(600,100),(600,120),(600,80),(600,200),(600,220),(600,180),(600,300),(600,320),(600,280)]
        """
        self.wall_pos = [(60, 80), (60, 140), (60, 280), (80, 120), (80, 140), (80, 160), (80, 180), (80, 240), (80, 300), (80, 380), (100, 140), (100, 280), (100, 320), (120, 80), (120, 160), (120, 180), (120, 200), (120, 220), (120, 240), (120, 300), (140, 80), (140, 120), (140, 160), (140, 180), (140, 260), (140, 320), (140, 340), (140, 360), (140, 380), (160, 100), (160, 180), (160, 260), (160, 280), (160, 360), (180, 140), (180, 160), (180, 200), (180, 320), (200, 80), (200, 140), (200, 160), (200, 200), (200, 360), (220, 120), (220, 140), (220, 180), (220, 260), (240, 80), (240, 100), (240, 140), (240, 240), (240, 260), (240, 320), (240, 360), (240, 380), (260, 100), (260, 280), (260, 300), (260, 340), (260, 360), (280, 140), (280, 180), (280, 260), (280, 300), (280, 320), (280, 340), (280, 360), (280, 380), (300, 80), (300, 100), (300, 140), (300, 180), (300, 240), (300, 340), (300, 380), (320, 200), (320, 260), (320, 380), (340, 140), (340, 280), (340, 320), (340, 340), (360, 80), (360, 100), (360, 140), (360, 160), (360, 260), (360, 320), (360, 360), (360, 380), (380, 100), (380, 240), (380, 340), (400, 100), (400, 200), (400, 220), (400, 240), (400, 260), (400, 300), (400, 340), (400, 360), (420, 180), (420, 220), (420, 240), (420, 260), (440, 300), (440, 380), (460, 80), (460, 100), (460, 160), (460, 240), (460, 300), (480, 160), (480, 220), (480, 300), (480, 320), (500, 100), (500, 220), (500, 260), (520, 80), (520, 140), (540, 140), (540, 220), (540, 340), (540, 360), (560, 100), (560, 180), (560, 280), (560, 320), (580, 200), (580, 220), (580, 360), (600, 80), (600, 100), (600, 180), (600, 300), (600, 340), (620, 80), (620, 140), (620, 180), (620, 200), (620, 260), (620, 300), (620, 340), (620, 380), (640, 120), (640, 200), (640, 260), (640, 320), (660, 80), (660, 100), (660, 140), (660, 180), (660, 200), (660, 220), (660, 280), (660, 300), (660, 380), (680, 100), (680, 120), (680, 240), (680, 260), (680, 280), (680, 340), (700, 100), (700, 140), (700, 160), (700, 180), (700, 200), (700, 260), (700, 280), (700, 320), (700, 340), (720, 180), (720, 200)]
        # self.food_pos = self.random_food_pos()
        self.food_pos = (460, 340)
        # Can use random walls generator function too change walls
        # self.wall_pos = self.get_random_walls()


    """
    Function to calculate manhatten distance between current_pos and target_pos
    returns:
        int : distance between two positions
    """
    def manhattan_dist(self, current_pos, target_pos):
        (x_target_pos, y_target_pos) = target_pos
        (x_current_pos, y_current_pos) = current_pos
        return abs(x_target_pos - x_current_pos) + abs(y_target_pos - y_current_pos)


    """
    Function to calculate euclidean distance between current_pos and target_pos
    returns:
        double : distance between two positions
    """
    def euclidean_dist(self, current_pos, target_pos):
        (x_target_pos, y_target_pos) = target_pos
        (x_current_pos, y_current_pos) = current_pos
        return math.sqrt((x_target_pos - x_current_pos)**2 + (y_target_pos - y_current_pos)**2)


    """
    Function to find near by directions without colliding with walls; Up. Down, Rigt, Left
    returns:
        list : list of near by positions
    """
    def near_by_pos(self, current_loc):
        (x_pos, y_pos) = current_loc
        dir_list = []

        if not self.check_collisions((x_pos, y_pos - MOVE_INCREMENT)):
            dir_list.append("Up")
        if not self.check_collisions((x_pos, y_pos + MOVE_INCREMENT)):
            dir_list.append("Down")
        if not self.check_collisions((x_pos - MOVE_INCREMENT, y_pos)):
            dir_list.append("Left")
        if not self.check_collisions((x_pos + MOVE_INCREMENT , y_pos)):
            dir_list.append("Right")

        return dir_list


    """
    Function to check collisions
    returns:
        true : if there is a collisions
        false : if not
    """
    def check_collisions(self, new_position):
        (x_pos, y_pos) = new_position

        return (
            x_pos in (20, 780)
            or y_pos in (40, 440)
            or (x_pos, y_pos) in self.wall_pos
        )


    """
    Function to change directions into  coordinates or locations on the board
    returns:
        list : list of coordinates near by
    """
    def direction_to_loc(self, new_direction, player_pos):
        (x_pos, y_pos) = player_pos

        if new_direction == "Up":
            return (x_pos, y_pos - MOVE_INCREMENT)
        elif new_direction == "Down":
            return (x_pos, y_pos + MOVE_INCREMENT)
        elif new_direction == "Left":
            return (x_pos - MOVE_INCREMENT, y_pos)
        elif new_direction == "Right":
            return (x_pos + MOVE_INCREMENT, y_pos)


    """
    Function to generate random food position
    returns:
        (int,int) : random position on board
    """
    def random_food_pos(self):
        empty_space = self.get_empty_space()
        random_pos = random.randint(0,len(empty_space)-1)
        return empty_space[random_pos]


    """
    Function to get empty space from baord
    returns:
        list : list of empty space on board
    """
    def get_empty_space(self):
        empty_space = []
        # board limits = (60, 740), (80, 400)
        for i in range(60, 740, MOVE_INCREMENT):
            for j in range(80, 400, MOVE_INCREMENT):
                if (i,j) not in self.wall_pos and not (i,j) == self.player_pos:
                    empty_space.append((i,j))
        return empty_space


    """
    Function to get generate random walls on board
    returns:
        list : list of walls on board
    """
    def get_random_walls(self):
        wall_list = []
        for i in range(60, 740, MOVE_INCREMENT):
            for j in range(80, 400, MOVE_INCREMENT):
                random_pos = random.randint(0,2)
                if random_pos == 1:
                    wall_list.append((i,j))
        return wall_list


    """
    Function to check if the player reached to the food position
    return:
        true: if reached to food
        false: if not
    """
    def check_food_reached(self, current_pos):
        if self.food_pos == current_pos:
            return True
        else:
            return False


    """
    Function to get walls positions
    return:
        list : list contining walls position on board
    """
    def get_walls_pos(self):
        return self.wall_pos


    """
    Function to get player's position
    return:
        touple : containing player's position
    """
    def get_player_pos(self):
        return self.player_pos


    """
    Function to get food's position
    return:
        touple : containing food's position
    """
    def get_food_pos(self):
        return self.food_pos
