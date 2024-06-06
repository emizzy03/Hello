# Below lists detail all eight possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def isSafe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


# Flood fill using BFS
def floodfill(mat, x, y, replacement):
    # creating an empty queue and enqueue starting pixel
    queue = []
    queue.append((x, y))
    # get target color
    target = mat[x][y]
    while queue:
        # get the current pixel
        x, y = queue.pop(0)
        # replace the color of current pixel with that of replacement
        mat[x][y] = replacement
        # process all eight adjacent pixels of the current pixel and
        # if a adjacent pixel has same color as that of target, enqueue it
        for k in range(len(row)):
            if isSafe(mat, x + row[k], y + col[k], target):
                queue.append((x + row[k], y + col[k]))


if __name__ == '__main__':
    # matrix showing portion of the screen having different colors
    mat = [
        ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

    # start node
    x, y = (3, 9)   # having a target color `X`

    # replacement color
    replacement = 'C'

    # replace the target color with a replacement color using BFS

    floodfill(mat, x, y, replacement)

    # print the colors after replacement
    for r in mat:
        print(r)
