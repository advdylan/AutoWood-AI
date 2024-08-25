from ortools.sat.python import cp_model
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

X = 2000 #board width
Y = 1000 #board height

elements  = [
    (1200, 430),
    (760, 430),
    (760, 430),
    (1160, 430),
    (1190, 250),
    (1190, 250),
    (1190, 250)
]

model = cp_model.CpModel()

# Tworzenie zmiennych decyzyjnych
x = []  # Pozycja x dla każdego elementu
y = []  # Pozycja y dla każdego elementu
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

# Dodawanie ograniczeń na nieprzekraczanie granic planszy
for i, (width, height) in enumerate(elements):
    model.Add(x[i] + width <= X)
    model.Add(y[i] + height <= Y)

# Dodawanie ograniczeń, żeby elementy nie zachodziły na siebie
model.AddNoOverlap2D(x_intervals, y_intervals)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    for i in range(len(elements)):
        print(f'Element {i} pozycja: ({solver.Value(x[i])}, {solver.Value(y[i])})')
else:
    print('Nie znaleziono optymalnego rozwiązania.')


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