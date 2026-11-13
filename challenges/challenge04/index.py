def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    out = [f"{rods[0]} {rods[1]} {rods[2]}"]


    def move (k, src, dst, aux):
        if k == 0:
            return
        move(k -1, src, aux, dst)
        rods[dst].append(rods[src].pop())
        out.append(f"{rods[0]} {rods[1]} {rods[2]}")
        move(k -1, aux, dst, src)

    move(n, 0, 2,1)
    return "\n".join(out)
