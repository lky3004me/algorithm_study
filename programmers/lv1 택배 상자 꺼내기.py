def solution(n, w, num):
    rows = (n + w - 1) // w
    grid = [[0]*w for _ in range(rows)]

    cur = 1
    target_r = target_c = -1
    for r in range(rows):
        if r % 2 == 0:  # L->R
            for c in range(w):
                if cur > n: break
                grid[r][c] = cur
                if cur == num: target_r, target_c = r, c
                cur += 1
        else:            # R->L
            for c in range(w-1, -1, -1):
                if cur > n: break
                grid[r][c] = cur
                if cur == num: target_r, target_c = r, c
                cur += 1

    # 위(최상단)에서부터 num의 층까지, 해당 열에 상자가 있는 층만 센다
    cnt = 0
    for r in range(rows-1, -1, -1):   # top -> down
        if grid[r][target_c] != 0:
            cnt += 1
        if r == target_r:
            break
    return cnt
