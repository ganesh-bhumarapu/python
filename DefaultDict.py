def find_word_indices():
    from collections import defaultdict
    n, m = map(int, input().split())
    group_a = [input().strip() for _ in range(n)]
    group_b = [input().strip() for _ in range(m)]

    positions = defaultdict(list)

    for i in range(n):
        word = group_a[i]
        positions[word].append(i + 1)
    result = []
    for word in group_b:
        if word in positions:
            result.append(' '.join(map(str, positions[word])))
        else:
            result.append('-1')
    for results in result:
        print(results)

find_word_indices()