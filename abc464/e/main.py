import sys
input = sys.stdin.readline

def main():
    h, w, q = map(int, input().split())

    a = [[0] * w for _ in range(h)]
    xs = ["A"]
    for i in range(1, q + 1):
        r, c, x = input().split()
        xs.append(x)
        a[int(r)-1][int(c)-1] = i

    for r in range(h - 1, -1, -1):
        for c in range(w - 1, -1, -1):
            if r != 0: 
                a[r-1][c] = max(a[r][c], a[r-1][c])

            if c != 0: 
                a[r][c-1] = max(a[r][c], a[r][c-1])

    for r in range(h):
        print("".join(xs[a[r][c]] for c in range(w)))

if __name__ == "__main__":
    main()


