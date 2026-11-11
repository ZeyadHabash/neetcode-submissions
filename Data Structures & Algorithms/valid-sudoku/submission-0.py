class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # naive solution would be to search every row, column and 3x3 sub box 
        # let me implement that and maybe an idea will pop up in my head midway through
        # we can make 3 arrays of 9 sets each
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subboxes = [[set() for i in range(3)] for j in range(3)] # sb[0] = board[0-2][0-2], sb[1] = board[0-2][3-5], sb[2] = board[0-2][6-8], sb[3] = board[3-5][0-2]
        # sb[i] = board[i//3 * 3 - i//3 * 3 + 2] [i%3 * 3 - i%3 * 3 + 2]
        # so if I have board[1][2] how do i find out which subbox it's in
        # i//3 * 3 <= 1 <= i // 3 * 3 + 2 AND i%3 * 3 <= 2 <= i%3 * 3 + 2
        
        # now that sb is a 2d array
        # sb[0][0] = board[0-2][0-2], sb[0][1] = board[0-2][3-5], sb[0][2] = board[0-2][6-8], sb[1][0] = board[3-5][0-2]
        # sb[i][j] contains board[i//3 * 3][j//3 * 3]
        # board[i][j] in sb[i//3][j//3]

        # then loop over the whole 2d array while saving the numbers that show in each row, col and subbox
        for i in range(9):
            for j in range(9):
                curr_cell = board[i][j]
                if curr_cell == '.':
                    continue

                # row check 
                if curr_cell in rows[i]:
                    return False
                else:
                    rows[i].add(curr_cell)
                # col check
                if curr_cell in cols[j]:
                    return False
                else:
                    cols[j].add(curr_cell)
                # subbox check
                if curr_cell in subboxes[i//3][j//3]:
                    return False
                else:
                    subboxes[i//3][j//3].add(curr_cell)
                
        return True