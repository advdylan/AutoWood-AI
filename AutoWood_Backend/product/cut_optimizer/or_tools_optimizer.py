from ortools.sat.python import cp_model

def pack_pieces_on_board(pieces, board_length, board_width, saw_thickness):
    # Create the CP-SAT model.
    model = cp_model.CpModel()

    # Variables to represent the starting position of each piece on the board (1D packing along length).
    starts = []
    ends = []
    intervals = []
    lengths = [p[0] for p in pieces]  # Only the length of each piece
    widths = [p[1] for p in pieces]   # Only the width of each piece

    for i in range(len(pieces)):
        start_var = model.NewIntVar(0, board_length, f'start_{i}')
        end_var = model.NewIntVar(0, board_length, f'end_{i}')
        starts.append(start_var)
        ends.append(end_var)

        # Create interval variables for the length of each piece
        interval = model.NewIntervalVar(start_var, lengths[i], end_var, f'interval_{i}')
        intervals.append(interval)

    # Ensure no overlap in the horizontal axis (1D strip packing).
    model.AddNoOverlap(intervals)

    # Optional: minimize the total length of the board used (to fit as many as possible).
    obj_var = model.NewIntVar(0, board_length, 'objective')
    model.AddMaxEquality(obj_var, ends)
    model.Minimize(obj_var)

    # Solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total board length used: {solver.Value(obj_var)}')
        for i in range(len(pieces)):
            print(f'Piece {i} starts at {solver.Value(starts[i])}, ends at {solver.Value(ends[i])}')
        return [(solver.Value(starts[i]), solver.Value(ends[i])) for i in range(len(pieces))]
    else:
        print('No solution found.')
        return None


# Example usage
board_length = 3000  # Length of the board
board_width = 600    # Fixed width of the board
saw_thickness = 3.2  # Saw thickness
#pieces = [(500, 200), (1200, 400), (800, 150)]  # (length, width) of each piece

# Call the packing function
#solution = pack_pieces_on_board(pieces, board_length, board_width, saw_thickness)
