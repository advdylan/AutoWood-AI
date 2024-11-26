from ortools.sat.python import cp_model

def pack_pieces_on_boards(pieces, board_length, board_width, saw_thickness, max_boards):
    # Create the CP-SAT model.
    model = cp_model.CpModel()

    # Variables to represent the starting position of each piece on the board (1D packing along length).
    starts = []
    ends = []
    boards = []  # Variable for the board number of each piece
    intervals_per_board = [[] for _ in range(max_boards)]
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

        # Create interval variables for the length of each piece, depending on the board
        for board in range(max_boards):
            # Create a literal that indicates whether a piece is on this board.
            is_on_board = model.NewBoolVar(f'is_on_board_{i}_{board}')
            model.Add(board_var == board).OnlyEnforceIf(is_on_board)
            model.Add(board_var != board).OnlyEnforceIf(is_on_board.Not())

            # Create interval variable for this board, conditioned on whether the piece is on this board.
            interval = model.NewOptionalIntervalVar(start_var, lengths[i], end_var, is_on_board, f'interval_{i}_board_{board}')
            intervals_per_board[board].append(interval)

    # Ensure no overlap on the same board.
    for board in range(max_boards):
        model.AddNoOverlap(intervals_per_board[board])

    # Ensure that the total length used on each board does not exceed the board length.
    for board in range(max_boards):
        total_board_length_used = model.NewIntVar(0, board_length, f'total_length_board_{board}')

        # Use BoolVar to filter which pieces belong to the current board
        board_pieces_ends = []
        for i in range(len(pieces)):
            is_on_board = model.NewBoolVar(f'is_piece_{i}_on_board_{board}')
            model.Add(boards[i] == board).OnlyEnforceIf(is_on_board)
            model.Add(boards[i] != board).OnlyEnforceIf(is_on_board.Not())
            board_pieces_ends.append(ends[i] if is_on_board else 0)

        # Find the maximum end position for pieces on this board
        model.AddMaxEquality(total_board_length_used, board_pieces_ends)
        model.Add(total_board_length_used <= board_length)

    # Optional: Minimize the number of boards used.
    num_boards_used = model.NewIntVar(0, max_boards - 1, 'num_boards_used')
    model.AddMaxEquality(num_boards_used, boards)
    model.Minimize(num_boards_used)

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
