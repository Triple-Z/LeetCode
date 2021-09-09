class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_maps = [{} for _ in range(9)]
        col_maps = [{} for _ in range(9)]
        block_maps = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if not self.add_number(row_maps, i, num):
                        return False
                    if not self.add_number(col_maps, j, num):
                        return False
                    if not self.add_number(block_maps, 3 * (i // 3) + j // 3, num):
                        return False
        
        return True
                
    def add_number(self, maps: List[Dict[str, int]], i: int, num: str) -> bool:
        cur_count = maps[i].get(num, 0)
        if cur_count > 0:
            return False
        maps[i][num] = cur_count + 1
        return True