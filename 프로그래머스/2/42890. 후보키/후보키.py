from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for r in range(1, col + 1):
        for comb in combinations(range(col), r):
            tmp = [tuple([item[i] for i in comb]) for item in relation]
            if len(set(tmp)) == row:
                if any(set(c).issubset(set(comb)) for c in candidates):
                    continue
                candidates.append(comb)

    return len(candidates)