devInput = """ 
Matematyka Fizyka Literatura
0.375
0.375
0.25
0.3
0.45
0.9
0.45
0.9
0.5
4
A 18 16 14
B 18 14 16
C 14 16 14
D 14 14 16
"""
inputLineNr = 0
dev = True


def get_input(n):
    global inputLineNr, dev
    if dev:
        inputLineNr += 1
        print(n, end="")
        x = devInput.split('\n')[inputLineNr]
        print(x)
        return x
    else:
        return input(n)


def zeros_and_ones(n):
    results = [[False], [True]]
    for i in range(n - 1):
        results = [[False] + x for x in results] + [[True] + x for x in results]
    return results


def all_subsets(lista):
    true_false = zeros_and_ones(len(lista))
    subsets = []
    for i in true_false:
        current = []
        for j in range(len(i)):
            if i[j]:
                current.append(lista[j])
        subsets.append(current)
    return subsets


if __name__ == '__main__':
    attributes = [x.strip() for x in get_input("podaj nazw atrybututów po spacji\n").split(' ')]
    weights = []
    for i in attributes:
        weights.append(float(get_input('podaj wagę {}:\n'.format(i))))
    subsets = all_subsets(attributes)[1:]
    values = []
    for i in subsets[:-1]:
        values.append(float(get_input('podaj u({}):\n'.format(i))))
    values.append(1.)
    subsets = [set(x) for x in subsets]
    
    bois_count = int(get_input("ile będzie osobników?\n"))
    bois = []
    for _ in range(bois_count):
        x = get_input("podaj kolejnego\n").split(' ')
        bois.append([x[0]] + [float(y) for y in x[1:]])
    for i in bois:
        print(i)
    for boi in bois:
        stats = boi[1:]
        suma_warzona = 0.
        for i in range(len(weights)):
            suma_warzona += weights[i] * stats[i]

        zbior = {}
        for i in range(len(attributes)):
            zbior[attributes[i]] = stats[i]
        usuniete = {}
        suma = 0.
        print()
        print(boi)
        print()
        while zbior:
            current_set = set([])
            worst_nieusuniety = 100000000.
            for key, value in zbior.items():
                if value:
                    current_set.add(key)
                    if value < worst_nieusuniety:
                        worst_nieusuniety = value
            best_usuniety = 0.
            for _, value in usuniete.items():
                if value > best_usuniety:
                    best_usuniety = value
            value_for_current_set = 0.
            for i in range(len(subsets)):
                if subsets[i] == current_set:
                    value_for_current_set = values[i]
            do_dodania = (worst_nieusuniety - best_usuniety) * value_for_current_set
            print(list(zbior.keys()))
            print('({} - {}) * {} = {}'.format(worst_nieusuniety, best_usuniety, value_for_current_set, do_dodania))
            print()
            suma += do_dodania
            to_be_removed = {}
            for key, value in zbior.items():
                if value == worst_nieusuniety:
                    to_be_removed[key] = value
            for key, value in to_be_removed.items():
                zbior.pop(key, None)
                usuniete[key] = value
        print(boi, suma_warzona, suma)
        print()
