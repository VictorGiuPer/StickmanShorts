class Stickman:
    def __init__(self, initial_position=(0, 0)):
        self.initial_position = initial_position
        self.position = list(initial_position)  # [x, y]

    def reset(self):
        """Resets the stickman to its initial position."""
        self.position = list(self.initial_position)

    def perform_action(self, action):
        """
        Updates the position based on the action.
        Actions: {"move_right": (1, 0), "jump": (0, 1), "fall": (0, -1)}
        """
        if action == "move_right":
            self.position[0] += 1
        elif action == "jump":
            self.position[1] += 1
        elif action == "fall":
            self.position[1] = max(0, self.position[1] - 1)  # Prevent going below ground level
