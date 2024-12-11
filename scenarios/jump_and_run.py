from core.environment import Environment

class JumpAndRunEnvironment(Environment):
    def __init__(self, boundaries, stickman, obstacle_positions):
        super().__init__(boundaries, stickman)
        self.obstacles = obstacle_positions  # List of obstacle positions

    def reset(self):
        """Resets the stickman and obstacles."""
        super().reset()
        # Obstacles remain static in this version
