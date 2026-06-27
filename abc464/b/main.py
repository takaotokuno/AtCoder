def main():
    H, W = map(int, input().split())
    grid = []

    top = H
    bottom = -1
    left = W
    right = -1

    for row in range(H):
        C = input().strip()
        grid.append(C)

        for col in range(W):
            if C[col] == "#":
                top = min(top, row)
                bottom = max(bottom, row)
                left = min(left, col)
                right = max(right, col)

    for row in range(top, bottom + 1):
        print(grid[row][left:right + 1])


if __name__ == "__main__":
    main()