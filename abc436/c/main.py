import sys
input = sys.stdin.readline

OFFSETS = ((0,0),(0,1),(1,0),(1,1))

def convert_to_index(r,c):
    return (r-1)*n + (c-1)

n,m = map(int,input().split())
used_cells = set()
ans = 0

for _ in range(m):
    r,c = map(int,input().split())

    block = set()
    conflict = False
    for dr,dc in OFFSETS:
        block.add(convert_to_index(r+dr,c+dc))

    if block & used_cells:
        continue

    used_cells |= block
    ans += 1

print(ans)