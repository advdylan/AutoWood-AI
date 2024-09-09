from ortools.sat.python import cp_model

def pack_pieces_on_boards(pieces, board_length, board_width, saw_thickness, max_boards):
    # Create the CP-SAT model.
    model = cp_model.CpModel()

    # Variables to represent the starting position of each piece on the board (1D packing along length).
    starts = []
    ends = []
    boards = []  # Variable for the board number of each piece
    intervals = []
    lengths = [p[0] for p in pieces]  # Only the length of each piece
    widths = [p[1] for p in pieces]   # Only the width of each piece

    for i in range(len(pieces)):
        start_var = model.NewIntVar(0, board_length, f'start_{i}')
        end_var = model.NewIntVar(0, board_length, f'end_{i}')
        starts.append(start_var)
        ends.append(end_var)

        # Board assignment variable (which board the piece is placed on)
        board_var = model.NewIntVar(0, max_boards - 1, f'board_{i}')
        boards.append(board_var)

        # Create interval variables for the length of each piece
        interval = model.NewOptionalIntervalVar(start_var, lengths[i], end_var, board_var == board_var.IndexOf(), f'interval_{i}')
        intervals.append(interval)

    # Ensure no overlap on the same board.
    for board in range(max_boards):
        board_intervals = [intervals[i] for i in range(len(pieces)) if boards[i] == board]
        model.AddNoOverlap(board_intervals)

    # Ensure that the total length used on each board does not exceed the board length.
    for board in range(max_boards):
        board_intervals = [intervals[i] for i in range(len(pieces)) if boards[i] == board]
        total_board_length_used = model.NewIntVar(0, board_length, f'total_length_board_{board}')
        model.AddMaxEquality(total_board_length_used, [ends[i] for i in range(len(pieces)) if boards[i] == board])
        model.Add(total_board_length_used <= board_length)

    # Optional: Minimize the number of boards used.
    model.Minimize(sum([1 if boards[i] else 0 for i in range(len(pieces))]))

    # Solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('Solution found!')
        for i in range(len(pieces)):
            print(f'Piece {i} is on board {solver.Value(boards[i])}, starts at {solver.Value(starts[i])}, ends at {solver.Value(ends[i])}')
        return [(solver.Value(boards[i]), solver.Value(starts[i]), solver.Value(ends[i])) for i in range(len(pieces))]
    else:
        print('No solution found.')
        return None


# Example usage
board_length = 3000  # Length of the board
board_width = 600    # Fixed width of the board
saw_thickness = 3.2  # Saw thickness
max_boards = 3       # Maximum number of boards available
pieces = [(500, 200), (1200, 400), (800, 150), (600, 200), (400, 300)]  # (length, width) of each piece

# Call the packing function
solution = pack_pieces_on_boards(pieces, board_length, board_width, saw_thickness, max_boards)
