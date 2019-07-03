def gasup(gas, dist):
    zipped = [(g, d) for g, d in zip(gas, dist)]
    n = len(zipped)

    result = [] # index

    for i, (g, d) in enumerate(zipped):
        distance = g * 20 - d

        for j in range(1, n):
            if distance < 0: break
                
            _g, _d = zipped[(i + j) % n]
            distance = distance + (_g * 20) - _d
        else:
            result.append(i)

        continue

    return result

# 20 miles per gallon
gas = [50, 20, 5, 30, 25, 10, 10]
dist = [900, 600, 200, 400, 600, 200, 100]

print(gasup(gas, dist))
