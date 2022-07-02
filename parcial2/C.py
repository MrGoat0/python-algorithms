n = int(input())
pars = []
for i in range(n):
    lst = input().split()
    pars.append(lst)
res = []
for par in pars:
    if par[2] == par[0]:
        res.append([2, par[0]])
        res.append([0, par[1]])
    elif par[2] == par[1]:
        res.append([2, par[1]])
        res.append([0, par[0]])
    else:
        res.append([1, par[0],])
        res.append([1, par[1]])
def process_input(lst):
    result = []
    for i in lst:
        k = i
        result.append(k)
    i = 0
    lon = len(result)
    while i < lon:
        k = i+1
        while k < lon:
            tupla_i = result[i]
            tupla_k = result[k]
            if tupla_i[1] == tupla_k[1]:
                tupla_i[0] += tupla_k[0]
                del result[k]
                lon -= 1
                k -= 1
            k += 1
        i += 1
    result.sort()
    result.reverse()
    return result
a = process_input(res)
for i in a:
    i[0] = str(i[0])
    print(i[1] + " " + i[0])