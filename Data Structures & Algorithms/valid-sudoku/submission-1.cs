public class Solution {
    public bool IsValidSudoku(char[][] board) {
        // Checking rows is easy
        // Checking columns is easy
        // building boxes is tough, and should be done while we're checking other things.

        // Leveraging assumptions
        const int BOARD_SIZE = 9;
        const int BOX_SIZE = 3;
        
        // define our boxes
        // Note, integer division determines the position; such that 0, 0 is the top-left box and 2, 2 is the bottom-right
        var boxes = new Dictionary<(int, int), HashSet<int>>(); // Assumes C# 7+
        var columns = new HashSet<int>[BOARD_SIZE];
        var rows = new HashSet<int>[BOARD_SIZE];

        // initialize
        for (int i = 0; i < BOARD_SIZE; i++)
        {
            columns[i] = new HashSet<int>();
            rows[i] = new HashSet<int>();
            boxes[(i / 3, i % 3)] = new HashSet<int>();
        }
        

        for (var rowIndex = 0; rowIndex < BOARD_SIZE; rowIndex++)
        {
            for (var colIndex = 0; colIndex < BOARD_SIZE; colIndex++)
            {
                var ch = board[rowIndex][colIndex];
                if (ch == '.') continue;

                var value = (int)char.GetNumericValue(ch);
                int boxRow = rowIndex / BOX_SIZE;
                int boxCol = colIndex / BOX_SIZE;
                // Have we seen the value before? The board is invalid
                if (columns[colIndex].Contains(value) ||
                    rows[rowIndex].Contains(value) ||
                    boxes[(boxRow, boxCol)].Contains(value))
                    {
                        return false;
                    }

                // We haven't seen it before; let's add it!
                rows[rowIndex].Add(value);
                columns[colIndex].Add(value);
                boxes[(boxRow, boxCol)].Add(value);
            }
        }
        return true;
    }
}
