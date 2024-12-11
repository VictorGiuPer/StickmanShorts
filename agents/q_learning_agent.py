import random
import numpy as np

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.2):
        self.actions = actions  # List of possible actions
        self.learning_rate = learning_rate  # Alpha
        self.discount_factor = discount_factor  # Gamma
        self.epsilon = epsilon  # Exploration rate
        self.q_table = {}  # Q-table for storing Q-values
        
    def get_state_key(self, state):
        """Generates a key from the state for the Q-table."""
        return tuple(state['stickman_position'])  # Just using position as the state key

    def choose_action(self, state):
        """Choose an action based on epsilon-greedy strategy."""
        state_key = self.get_state_key(state)
        
        # If state not in Q-table, initialize it
        if state_key not in self.q_table:
            self.q_table[state_key] = {action: 0.0 for action in self.actions}
        
        if random.uniform(0, 1) < self.epsilon:
            # Exploration: random action
            return random.choice(self.actions)
        else:
            # Exploitation: best action based on Q-values
            return max(self.q_table[state_key], key=self.q_table[state_key].get)

    def update_q_value(self, state, action, reward, next_state):
        """Update Q-value based on the reward and next state."""
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)
        
        # Initialize next state in Q-table if not present
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {action: 0.0 for action in self.actions}
        
        # Q-learning update rule
        old_q_value = self.q_table[state_key][action]
        max_future_q = max(self.q_table[next_state_key].values())
        
        # Update Q-value
        new_q_value = old_q_value + self.learning_rate * (reward + self.discount_factor * max_future_q - old_q_value)
        self.q_table[state_key][action] = new_q_value
