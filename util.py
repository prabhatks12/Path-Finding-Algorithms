import math

MOVE_INCREMENT = 20
GAME_SPEED = 10

class Util():
    def __init__(self):
        self.player_pos = [(40,60)]
        self.wall_pos = [(400,220),(380,220),(360,220),(340,220),(320,220),(420,220),(440,220),
                        (400,200),(380,200),(360,200),(340,200),(320,200),(420,200),(440,200),
                        (340,180),(320,180),(340,160),(320,160),(340,140),(320,140),(340,120),(320,120),
                        (420,240),(440,240),(420,260),(440,260),(420,280),(440,280),(420,300),(440,300),
                        (140,100),(140,120),(140,80),(140,200),(140,220),(140,180),(140,300),(140,320),(140,280),
                        (600,100),(600,120),(600,80),(600,200),(600,220),(600,180),(600,300),(600,320),(600,280)]
        self.food_pos = [(660,400)]

    def manhattan_dist(self, our_pos):
        (x_pos_food, y_pos_food) = self.food_pos[0]
        (x_pos_current, y_pos_current) = our_pos[0]

        return abs(x_pos_food - x_pos_current) + abs(y_pos_food - y_pos_current)

    def euclidean_dist(self, our_pos):
        (x_pos_food, y_pos_food) = self.food_pos[0]
        (x_pos_current, y_pos_current) = our_pos[0]

        return math.sqrt((x_pos_food - x_pos_current)**2 + (y_pos_food - y_pos_current)**2)

    def near_by_pos(self, current_loc):
        (x_pos, y_pos) = current_loc[0]
        dir_list = []

        if not self.check_collisions([(x_pos, y_pos - MOVE_INCREMENT)]):
            dir_list.append("Up")
        if not self.check_collisions([(x_pos, y_pos + MOVE_INCREMENT)]):
            dir_list.append("Down")
        if not self.check_collisions([(x_pos - MOVE_INCREMENT, y_pos)]):
            dir_list.append("Left")
        if not self.check_collisions([(x_pos + MOVE_INCREMENT , y_pos)]):
            dir_list.append("Right")

        return dir_list

    def check_collisions(self, new_position):
        (x_pos, y_pos) = new_position[0]

        return (
            x_pos in (20, 780)
            or y_pos in (40, 440)
            or (x_pos, y_pos) in self.wall_pos
        )

    def legal_move(self, prev_pos, new_pos):
        (x_pos_food, y_pos_food) = prev_pos
        (x_pos_current, y_pos_current) = new_pos

        if abs(x_pos_food - x_pos_current) + abs(y_pos_food - y_pos_current) == MOVE_INCREMENT:
            return True
        else:
            return False


    def direction_to_loc(self, new_direction, player_pos):
        (x_pos, y_pos) = player_pos[0]

        if new_direction == "Up":
            return [(x_pos, y_pos - MOVE_INCREMENT)]
        elif new_direction == "Down":
            return [(x_pos, y_pos + MOVE_INCREMENT)]
        elif new_direction == "Left":
            return [(x_pos - MOVE_INCREMENT, y_pos)]
        elif new_direction == "Right":
            return [(x_pos + MOVE_INCREMENT, y_pos)]

    def check_food_reached(self, current_pos):
        if self.food_pos == current_pos:
            return True
        else:
            return False

    def get_walls_pos(self):
        return self.wall_pos

    def get_player_pos(self):
        return self.player_pos

    def get_food_pos(self):
        return self.food_pos
