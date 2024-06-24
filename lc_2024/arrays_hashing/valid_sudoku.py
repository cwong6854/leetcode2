class Solution(object):
    def isValidSudoku(self, board):
        # Intuition
        # for rows and columns -> double for loop
        # for group -> hash map with sets (to check that there's no duplicate num in group?
        # group 1 (0,0 .... 2,2), group 2 (0,3 ... 2,5)
        #  3x3x3 -> 27
        # dont understand how to get the exact group to put number into
        # AFTER LOOKING AT SOLUTION (i // 3) * 3 + (j // 3)

        # Time Complexity: 
        # O (N ^ 2)
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                if cell == ".":
                    continue
                group = (i // 3) * 3 + (j // 3)
                if cell in row[i] or cell in col[j] or cell in box[group]:
                    return False
                else:
                    row[i].add(cell)
                    col[j].add(cell)
                    box[group].add(cell)
        return True
if __name__ == "__main__":
    solution = Solution().isValidSudoku
    assert(solution([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))==True
    # Add your test cases here
    print("All test cases pass!")

        