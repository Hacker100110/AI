import math

P, O, E = 'X', 'O', '_'

def print_board(b): print('\n'.join(' '.join(r) for r in b), '\n')

def moves_left(b): return any(E in r for r in b)

def evaluate(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != E: return 1 if b[i][0] == P else -1
        if b[0][i] == b[1][i] == b[2][i] != E: return 1 if b[0][i] == P else -1
    if b[0][0] == b[1][1] == b[2][2] != E: return 1 if b[0][0] == P else -1
    if b[0][2] == b[1][1] == b[2][0] != E: return 1 if b[0][2] == P else -1
    return 0

def minimax(b, d, max_turn):
    score = evaluate(b)
    if score or not moves_left(b): return score
    best = -math.inf if max_turn else math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == E:
                b[i][j] = P if max_turn else O
                val = minimax(b, d+1, not max_turn)
                b[i][j] = E
                best = max(best, val) if max_turn else min(best, val)
    return best

def best_move(b):
    move, best_val = (-1, -1), -math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == E:
                b[i][j] = P
                val = minimax(b, 0, False)
                b[i][j] = E
                print(f"Position ({i},{j}) has utility: {val}")
                if val > best_val: move, best_val = (i, j), val
    return move

def main():
    b = [[E]*3 for _ in range(3)]
    print("Initial Board:"); print_board(b)
    while moves_left(b) and not evaluate(b):
        x, y = best_move(b); b[x][y] = P
        print("AI plays:"); print_board(b)
        if evaluate(b) or not moves_left(b): break
        try:
            r, c = map(int, input("Enter your move (row col): ").split())
            if not (0 <= r < 3 and 0 <= c < 3) or b[r][c] != E: raise ValueError
            b[r][c] = O
        except: print("Invalid move. Try again."); continue
        print("After your move:"); print_board(b)
        if evaluate(b) or not moves_left(b): break
    print("AI wins!" if evaluate(b) == 1 else "You win!" if evaluate(b) == -1 else "It's a draw!")

if __name__ == "__main__":
    main()
