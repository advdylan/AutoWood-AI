
def set_ticks(X,scale):
    ticks = []

    x = 0
    tick = X / scale
 

    while x <= X:
        if len(ticks) == 0:
            ticks.append(0)

        elif len(ticks) >= 1:
            ticks.append(x)

        x+=scale

    return ticks


#print(f"Tick_b : {tick_b}")