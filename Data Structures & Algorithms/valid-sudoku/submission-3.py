class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We're going to rely on 3 sets to solve this, one for rows, columns, and boxes
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        boxes = collections.defaultdict(list)

        # There's nothing needed to pre-init here, so we can simply dive into the loop
        # remember, the board has a fixed size; do not make the problem dynamic.
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                # Guard first, items to skip: '.'
                if (value == "."):
                    continue

                # either the row has a dupe, the column does, or the box
                if (value in rows[row] or
                    value in cols[col] or
                    value in boxes[(row // 3, col // 3)]):
                    return False

                # no collision found yet
                rows[row].append(value)
                cols[col].append(value)
                boxes[(row // 3, col // 3)].append(value)

        return True

        