class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = set()

        columns = set()
        
        grids = set()

        for i in range(9):

            for j in range(9):

                value = board[i][j]

                if value == ".":

                    continue

                row_entry = (i, value)

                column_entry = (j, value)

                grid_entry = (i // 3, j // 3, value)

                if (
                    row_entry in rows

                    or column_entry in columns

                    or grid_entry in grids
                ):

                    return False

                rows.add(row_entry)

                columns.add(column_entry)

                grids.add(grid_entry)

        return True