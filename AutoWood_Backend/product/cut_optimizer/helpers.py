
def set_ticks(X,scale):
    ticks = []

    x = 0
    tick = X / scale
    print(tick)
    ticks.append(0)

    while x <= X:
        ticks.append(tick)
        x+=tick
        tick+=tick

  
    return ticks


#print(f"Tick_b : {tick_b}")