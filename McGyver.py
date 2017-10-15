class McGyver:
    """McGyver have to collect 3 items to get out of the maze, if he don't he
    die."""

    def __init__(self):
        """At the start of the game McGyver is at the position 1, 1. He have a backpack to be able to count the items he collect."""
        self._x = 1
        self._y = 1
        self._backpack = []

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def backpack(self):
        return self._backpack


    def teleport(self, maze):
        """McGyver has the ability to go anywhere in the map"""

        teleport = False

        while not teleport:
            try:
                line = int(input("Line: "))
                column = int(input("Column: "))
                if maze.check_coordinates(line, column):
                    # delete the position of McGyver
                    maze.coord[(self._x, self._y)] = " "
                    # McGyver teleport himself in the new position
                    maze.coord[line, column] = 'M'
                    self._x, self._y = line, column
                    teleport = True
                else:
                    print("McGyver can't teleport here, try again !")
            except KeyError:
                print("You try to teleport out of the boundaries!")
            except ValueError:
                print("You must use integer!")

    def move(self, maze, action):
        """McGyver can move forward, backward, and sideward."""
        new_x = self._x
        new_y = self._y

        if action == "up":
            new_x -= 1
        elif action == "down":
            new_x += 1
        elif action == "right":
            new_y += 1
        elif action == "left":
            new_y -= 1

        if maze.coord[(new_x, new_y)] == "#":
            # revert changes
            new_x = self._x
            new_y = self._y
        else:
            items = ['T', 'E', 'N']
            # If McGyver move on an item, he pick it up
            for item in items:
                if item in maze.coord[(new_x, new_y)]:
                    self.pick_up_items(maze, item)

            # delete the position of McGyver
            maze.coord[(self._x, self._y)] = " "
            # McGyver move to the direction
            maze.coord[new_x, new_y] = 'M'
            self._x, self._y = new_x, new_y

        print(self._backpack)
        print(len(self._backpack))
    def pick_up_items(self, maze, item):
        self._backpack.append(item)
