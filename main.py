import os
import pygame
from core.stickman import Stickman
from scenarios.jump_and_run import JumpAndRunEnvironment
from agents.q_learning_agent import QLearningAgent
from core.renderer import Renderer

# Configuration
BOUNDARIES = [10, 5]  # Width x Height
OBSTACLES = [(3, 0), (6, 0), (8, 0)]  # Obstacles at ground level
stickman = Stickman(initial_position=(0, 0))

# Initialize Environmentpython main.py

environment = JumpAndRunEnvironment(boundaries=BOUNDARIES, stickman=stickman, obstacle_positions=OBSTACLES)

# Initialize Agent
actions = ["move_right", "jump", "fall"]
agent = QLearningAgent(actions)

# Initialize Renderer (animation)
renderer = Renderer(width=BOUNDARIES[0], height=BOUNDARIES[1], stickman=stickman, obstacles=OBSTACLES)

# Training Loop
episodes = 10  # Set episodes to a small number for quick testing
frame_count = 0

for episode in range(episodes):
    environment.reset()
    state = environment.get_state()
    done = False
    total_reward = 0

    while not done:
        # Choose an action based on the current state
        action = agent.choose_action(state)

        # Perform the action in the environment
        next_state, reward, done = environment.step(action)

        # Update the agent's Q-values based on the transition
        agent.update_q_value(state, action, reward, next_state)

        # Move to the next state
        state = next_state
        total_reward += reward

        # Render and save each frame (for animation)
        renderer.render()  # Display the current frame
        renderer.save_frame(frame_count)  # Save the frame
        frame_count += 1

    # Optionally print the reward every 100 episodes
    if episode % 1 == 0:
        print(f"Episode {episode}, Total Reward: {total_reward}")

# Close the renderer window after training
renderer.close()

print("Training complete!")
