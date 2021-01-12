import math

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
        self.wall_pos = [(400,220),(380,220),(360,220),(340,220),(320,220),(420,220),(440,220),
                        (400,200),(380,200),(360,200),(340,200),(320,200),(420,200),(440,200),
                        (340,180),(320,180),(340,160),(320,160),(340,140),(320,140),(340,120),(320,120),
                        (420,240),(440,240),(420,260),(440,260),(420,280),(440,280),(420,300),(440,300),
                        (140,100),(140,120),(140,80),(140,200),(140,220),(140,180),(140,300),(140,320),(140,280),
                        (600,100),(600,120),(600,80),(600,200),(600,220),(600,180),(600,300),(600,320),(600,280)]
        self.food_pos = (660,360)


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
