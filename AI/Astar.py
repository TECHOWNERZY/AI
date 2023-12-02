def a_star(initial_state, goal_state):
  """Solve the 8-puzzle problem using A* algorithm.

  Args:
    initial_state: The initial state of the puzzle.
    goal_state: The goal state of the puzzle.

  Returns:
    The solution to the puzzle, as a list of moves.
  """

  open_list = [initial_state]
  closed_list = []

  while open_list:
    current_state = open_list.pop(0)
    if current_state == goal_state:
      return get_solution(current_state)

    closed_list.append(current_state)
    for new_state in get_successors(current_state):
      if new_state not in closed_list:
        f_score = get_f_score(new_state, goal_state)
        open_list.append((f_score, new_state))

  return []

def get_successors(state):
  """Get all successors of the given state.

  Args:
    state: The state to get the successors of.

  Returns:
    A list of successors.
  """

  successors = []
  for i in range(3):
    for j in range(3):
      if state[i][j] == 0:
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          new_i = i + direction[0]
          new_j = j + direction[1]
          if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = list(state)
            new_state[i][j] = state[new_i][new_j]
            new_state[new_i][new_j] = 0
            successors.append(new_state)

  return successors

def get_f_score(state, goal_state):
  """Get the f-score of the given state.

  Args:
    state: The state to get the f-score of.
    goal_state: The goal state.

  Returns:
    The f-score of the state.
  """

  g_score = get_g_score(state)
  h_score = get_h_score(state, goal_state)

  return g_score + h_score

def get_g_score(state):
  """Get the g-score of the given state.

  Args:
    state: The state to get the g-score of.

  Returns:
    The g-score of the state.
  """

  return len(get_path(state))

def get_h_score(state, goal_state):
  """Get the h-score of the given state.

  Args:
    state: The state to get the h-score of.
    goal_state: The goal state.

  Returns:
    The h-score of the state.
  """

  misplaced_tiles = 0
  for i in range(3):
    for j in range(3):
      if state[i][j] != goal_state[i][j]:
        misplaced_tiles += 1

  return misplaced_tiles

def get_path(state):
  """Get the path from the initial state to the given state.

  Args:
    state: The state to get the path to.

  Returns:
    A list of states, from the initial state to the given state.
  """

  path = []
  while state != []:
    path.append(state)
    state = state[1:]

  path.reverse()

  return path

def print_solution(solution):
  """Print the solution to the puzzle.

  Args:
    solution: The solution to the puzzle, as a list of moves.
  """

  for move in solution:
    print(move)

  print("The puzzle is solved!")