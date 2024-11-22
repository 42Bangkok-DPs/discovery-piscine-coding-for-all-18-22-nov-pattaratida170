 if len(rows) != 4 or any(len(row) != 4 for row in rows):
        print("Chessboard must be 4x4")
        return

    kings = [(i, j) for i in range(4) for j in range(4) if rows[i][j] == 'K']
    if not kings:
        print("No King found")
        return

    moves = {
        'P': [(1, -1), (1, 1)],  # Pawn
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # Queen
    }

    def isinbounds(x, y):
        """ตรวจสอบว่าอยู่ในขอบเขตของกระดานหรือไม่"""
        return 0 <= x < 4 and 0 <= y < 4

    for kingx, kingy in kings:
        for i in range(4):
            for j in range(4):
                piece = rows[i][j]
                if piece in moves: 
                    for dx, dy in moves[piece]:
                        x, y = i, j
                        while is_in_bounds(x + dx, y + dy):
                            x += dx
                            y += dy
                            if (x, y) == (king_x, king_y): 
                                print("Success")
                                return
                            if rows[x][y] != '.': 
                                break
    print("Fail")

if __name == "__main":
    board = """\
K...
....
.Q..
....
"""
    checkmate(board)
