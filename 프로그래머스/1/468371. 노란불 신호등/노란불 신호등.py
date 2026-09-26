def solution(signals):
    s = [sum(x) for x in signals]
    import math
    length = math.lcm(*s)

    results = []

    for a, b, c in signals:
        d = a + b + c
        result = [a + i*d + j for i in range(length // d) for j in range(1, b+1)]
        results.append(result)
        
    common = set.intersection(*map(set, results))
    if common:
        answer = min(common)
    else:
        answer = -1
    return answer