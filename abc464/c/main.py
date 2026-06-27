import sys
input = sys.stdin.readline


def solve(N, M, records):
    cnt = [0] * (N + 1)
    changes = [[] for _ in range(M + 1)]
    kind = 0

    for A, D, B in records:
        if cnt[A] == 0:
            kind += 1
        cnt[A] += 1

        changes[D].append((A, B))

    ans = []

    for day in range(1, M + 1):
        for A, B in changes[day]:
            cnt[A] -= 1
            if cnt[A] == 0:
                kind -= 1

            if cnt[B] == 0:
                kind += 1
            cnt[B] += 1

        ans.append(kind)

    return ans


def main():
    N, M = map(int, input().split())
    records = [tuple(map(int, input().split())) for _ in range(N)]

    ans = solve(N, M, records)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()