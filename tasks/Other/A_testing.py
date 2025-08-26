from itertools import combinations

if __name__ == '__main__':
    k, nn = [int(i) for i in input().split()]
    n = []
    for i in range(nn):
        n.append(i)
    m = list(combinations(n, k))
    for j in range(len(m)):
        print(*m[j])
