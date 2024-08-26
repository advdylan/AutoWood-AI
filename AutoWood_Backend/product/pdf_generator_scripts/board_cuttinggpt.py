from ortools.sat.python import cp_model
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

X = 2000
Y = 800

elements  = [
    (1200, 430),
    (760, 430),
    (760, 430),
    (1160, 430),
    (1190, 250),
    (1190, 250),
    (1190, 250)
]



def solve_with_board_size(X, Y, elements):
    model = cp_model.CpModel()

    x = []
    y = []
    x_intervals = []
    y_intervals = []

    for i, (width, height) in enumerate(elements):
        x_var = model.NewIntVar(0, X - width, f'x_{i}')
        y_var = model.NewIntVar(0, Y - height, f'y_{i}')
        x.append(x_var)
        y.append(y_var)

        x_interval = model.NewIntervalVar(x_var, width, x_var + width, f'x_interval_{i}')
        y_interval = model.NewIntervalVar(y_var, height, y_var + height, f'y_interval_{i}')
        
        x_intervals.append(x_interval)
        y_intervals.append(y_interval)

    model.AddNoOverlap2D(x_intervals, y_intervals)

    

    return status, x, y, solver



# Try first board
status, x, y, solver = solve_with_board_size(X, Y, elements)

if status == cp_model.OPTIMAL:
    for i in range(len(elements)):
        print(f'Element {i} pozycja: ({solver.Value(x[i])}, {solver.Value(y[i])})')
else:
    print('No solution on the first board, trying a second board...')
    
    # Split the elements into two groups
    mid_point = len(elements) // 2
    elements_first_board = elements[:mid_point]
    elements_second_board = elements[mid_point:]

    # Solve for the first board
    status_1, x_1, y_1, solver_1 = solve_with_board_size(X, Y, elements_first_board)

    # Solve for the second board
    status_2, x_2, y_2, solver_2 = solve_with_board_size(X, Y, elements_second_board)

    if status_1 == cp_model.OPTIMAL and status_2 == cp_model.OPTIMAL:
        print('Solution found using two boards:')
        
        print('First board:')
        for i in range(len(elements_first_board)):
            print(f'Element {i} pozycja: ({solver_1.Value(x_1[i])}, {solver_1.Value(y_1[i])})')

        print('Second board:')
        for i in range(len(elements_second_board)):
            print(f'Element {i+mid_point} pozycja: ({solver_2.Value(x_2[i])}, {solver_2.Value(y_2[i])})')
    else:
        print('No solution found even using two boards.')


c = canvas.Canvas("cutting_plan.pdf", pagesize=A4)
c.drawString(100, 800, "Plan cięcia")

# Skala do konwersji z wymiarów rzeczywistych na A4
scale_x = A4[0] / X
scale_y = A4[1] / Y

for i in range(len(elements)):
    x_pos = solver.Value(x[i]) * scale_x
    y_pos = A4[1] - (solver.Value(y[i]) + elements[i][1]) * scale_y  # odwrócenie osi y
    width = elements[i][0] * scale_x
    height = elements[i][1] * scale_y
    c.rect(x_pos, y_pos, width, height)

c.showPage()
c.save()