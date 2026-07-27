# Flood Fill
# In computer graphics, an uncompressed raster image is presented as a matrix of numbers. Each entry of the matrix represents the color of a pixel. A flood fill algorithm takes a coordinate r, c and a replacement color, and replaces all pixels connected to r, c that have the same color (i.e., the pixels connected to the given coordinate with same color and all the other pixels connected to the those pixels of the same color) with the replacement color. (e.g. MS-Paint's paint bucket tool).

# Input & Output
# Input
# r — row
# c — column
# replacement — replacement color
# image — an 2D array of integers representing the image
# Output
# the replaced image
# Example
# Input
# r = 2
# c = 2
# replacement = 9
# arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
# Output
# [[0,1,3,4,1],[3,9,9,3,3],[6,7,9,9,3],[12,2,9,9,1],[12,3,1,3,2]]
# Explanation
# From

# 0 1 3 4 1
# 3 8 8 3 3
# 6 7 8 8 3
# 12 2 8 9 1
# 12 3 1 3 2
# to

# 0 1 3 4 1
# 3 9 9 3 3
# 6 7 9 9 3
# 12 2 9 9 1
# 12 3 1 3 2



from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    num_rows,num_cols = len(image), len(image[0])
    def get_neighbors(coord,color):
        row,col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighb_row = row + delta_row[i]
            neighb_col = col + delta_col[i]
            if 0 <= neighb_row < num_rows and 0 <= neighb_col < num_cols:
                if image[neighb_row][neighb_col] == color:
                    yield neighb_row,neighb_col
    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r,c = root
        color = image[r][c]
        image[r][c] = replacement
        visited[r][c] = True

        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node,color):
                r,c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited[r][c] = True
    bfs((r, c))
    return image


# --- Daily tests ---
if __name__ == "__main__":
    image = [[0, 1, 3, 4, 1], [3, 8, 8, 3, 3], [6, 7, 8, 8, 3], [12, 2, 8, 9, 1], [12, 3, 1, 3, 2]]
    expected = [[0, 1, 3, 4, 1], [3, 9, 9, 3, 3], [6, 7, 9, 9, 3], [12, 2, 9, 9, 1], [12, 3, 1, 3, 2]]
    TESTS = [
        (2, 2, 9, image, expected),
        (0, 0, 5, [[0, 0], [0, 0]], [[5, 5], [5, 5]]),
        (1, 1, 2, [[1, 1], [1, 1]], [[2, 2], [2, 2]]),
    ]
    passed = 0
    for r, c, replacement, img, exp in TESTS:
        got = flood_fill(r, c, replacement, [row[:] for row in img])
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] ({r},{c}) fill={replacement} -> ok")
    print(f"\n{passed}/{len(TESTS)} passed")

