import random

class Environment:
    def __init__(self, boundaries, stickman):
        self.boundaries = boundaries  # [width, height]
        self.stickman = stickman
        self.obstacles = []
        self.current_step = 0

    def reset(self):
        """Resets the environment and stickman."""
        self.stickman.reset()
        self.current_step = 0

    def step(self, action):
        """Takes an action and updates the environment."""
        self.stickman.perform_action(action)
        reward = self._calculate_reward()
        done = self._check_done()
        self.current_step += 1
        return self.get_state(), reward, done

    def _calculate_reward(self):
        """Reward for moving forward and jumping over obstacles."""
        for obs in self.obstacles:
            if self.stickman.position == obs:
                return -1  # Penalty for hitting an obstacle
        return 0.1  # Reward for progressing

    def _check_done(self):
        """Check if the stickman has reached the end."""
        return self.stickman.position[0] >= self.boundaries[0]

    def get_state(self):
        """Returns the current state of the environment and stickman."""
        return {
            "stickman_position": self.stickman.position,
            "obstacles": self.obstacles,
        }

    def render(self):
        """Simple print-based visualization for now."""
        grid = [[" " for _ in range(self.boundaries[0])] for _ in range(self.boundaries[1])]
        for obs in self.obstacles:
            grid[obs[1]][obs[0]] = "O"  # Obstacles
        grid[self.stickman.position[1]][self.stickman.position[0]] = "S"  # Stickman
        print("\n".join("".join(row) for row in grid))
