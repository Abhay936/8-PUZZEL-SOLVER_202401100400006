# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J1VoFybgL2d11mlFqiirF56T7w6GdRD3
"""

import heapq

# Define the goal state of the puzzle
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Possible moves (up, down, left, right) as (row_offset, col_offset)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic function: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal_state.index(state[i])
            current_pos = i
            # Calculate the Manhattan distance for each tile
            distance += abs(goal_pos // 3 - current_pos // 3) + abs(goal_pos % 3 - current_pos % 3)
    return distance

# A* algorithm to solve the 8-puzzle
def solve_puzzle(start_state):
    # Priority Queue (min-heap) to store the states
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, []))

    # Set to keep track of visited states
    visited = set()
    visited.add(start_state)

    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)

        # If we reached the goal state
        if current_state == goal_state:
            return path

        # Find the position of 0 (empty space)
        zero_pos = current_state.index(0)

        # Generate possible moves
        for move in MOVES:
            new_zero_pos = zero_pos + move[0] * 3 + move[1]
            if 0 <= new_zero_pos < 9:
                new_state = list(current_state)
                new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]

                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_g = g + 1
                    heapq.heappush(open_list, (new_g + manhattan_distance(new_state), new_g, new_state_tuple, path + [new_state]))

    return None

# Function to print the puzzle state
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Function to get user input for the start state
def get_user_input():
    print("Enter the initial state of the puzzle (9 numbers from 0 to 8, where 0 represents the empty space):")
    input_state = input("Enter the state as a single line, space-separated (e.g., '1 2 3 4 5 6 7 8 0'): ")
    state_list = list(map(int, input_state.split()))

    if len(state_list) != 9 or any(x not in range(9) for x in state_list):
        print("Invalid input! Please ensure you enter exactly 9 numbers between 0 and 8.")
        return get_user_input()  # Prompt again if the input is invalid
    return tuple(state_list)

# Main function to run the solver
if __name__ == "__main__":
    # Get user input for the start state
    start_state = get_user_input()

    print("\nStart state:")
    print_puzzle(start_state)

    # Solve the puzzle
    solution = solve_puzzle(start_state)

    if solution:
        print("\nSolution path:")
        for step in solution:
            print_puzzle(step)
    else:
        print("\nNo solution found.")