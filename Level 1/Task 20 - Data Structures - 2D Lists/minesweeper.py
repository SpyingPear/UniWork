def count_adjacent_mines(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    mine_count = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0),   (1, 1)]
    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == "#":
                mine_count += 1

    return mine_count

def minesweeper(grid):
    result = []

    for row_index, row in enumerate(grid):
        result_row = []
        for col_index, cell in enumerate(row):
            if cell == "#":
                result_row.append("#")
            else:
                mine_count = count_adjacent_mines(grid, row_index, col_index)
                result_row.append(mine_count)
        result.append(result_row)

    return result

if __name__ == "__main__":
    input_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    output_grid = minesweeper(input_grid)

    for row in output_grid:
        print(row)