class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        print(" ---" * cols)  
        
        for i in range(rows):
            print("| " + " | ".join(self.grid[i]) + " |")  
            print(" ---" * cols)  

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        # 检查每一行是否有赢家
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        # 检查每一列是否有赢家
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != " ":
                return self.grid[0][col]

        # 检查主对角线是否有赢家
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != " ":
            return self.grid[0][0]

        # 检查副对角线是否有赢家
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != " ":
            return self.grid[0][2]

        # 检查是否平局
        for row in self.grid:
            if " " in row:
                return None  # 游戏未结束

        return "Draw"  # 平局

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)