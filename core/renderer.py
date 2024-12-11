import pygame

class Renderer:
    def __init__(self, width, height, stickman, obstacles):
        self.width = width
        self.height = height
        self.stickman = stickman
        self.obstacles = obstacles

        # Initialize pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((width * 50, height * 50))  # Grid is 50x50 pixels
        self.clock = pygame.time.Clock()

    def render(self):
        """Render the environment and stickman."""
        # Set background color (light blue)
        self.screen.fill((173, 216, 230))

        # Draw obstacles
        for obs in self.obstacles:
            pygame.draw.rect(self.screen, (255, 0, 0), (obs[0] * 50, obs[1] * 50, 50, 50))  # Red obstacles

        # Draw stickman (S)
        pygame.draw.circle(self.screen, (0, 0, 255), (self.stickman.position[0] * 50 + 25, self.stickman.position[1] * 50 + 25), 20)  # Blue stickman

        # Update display
        pygame.display.update()

    def close(self):
        """Close the pygame window."""
        pygame.quit()

    def save_frame(self, frame_count):
        """Save the current frame as an image."""
        pygame.image.save(self.screen, f"frame_{frame_count}.png")
