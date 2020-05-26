import numpy as np


def hamilton(votes, seats):
    stolki = []
    reszty = []
    for glosy_partii in votes:
        quota = seats * glosy_partii / sum(votes)
        integer = int(quota)
        stolki.append(integer)

        reszta = quota-integer
        reszty.append(reszta)

    pozostale = seats - sum(stolki)
    for i in range(pozostale):
        idx = reszty.index(max(reszty))
        stolki[idx] += 1
        reszty[idx] = 0

    assert sum(stolki) == seats, "coś się spierdoliło"
    print("hamilton\t", stolki)


def jefferson(votes, seats, step=0.001):
    d = sum(votes)/seats

    def policz_stolki(votes, d):
        return list(map(lambda x: int(x/d), votes))

    stolki = policz_stolki(votes, d)

    while sum(stolki) < seats:
        d *= (1-step)
        stolki = policz_stolki(votes, d)

    assert sum(stolki) == seats, "zmniejsz step bo przeskoczyłem"
    print("jefferson\t", stolki)


# metoda d'Hondta
def dont(votes, seats):
    podzielone = []
    for i in range(1, seats+1):
        podzielone.append(list(map(lambda x: x/i, votes)))

    podzielone = np.array(podzielone)

    stolki = np.zeros(len(votes))
    for i in range(seats):
        row, col = np.unravel_index(np.argmax(podzielone), podzielone.shape)
        podzielone[row, col] = -1
        stolki[col] += 1

    assert sum(stolki) == seats, "coś się spierdoliło"
    print("d'Hondt\t\t", stolki)

def all(votes, seats):
    hamilton(votes, seats)
    jefferson(votes, seats)
    dont(votes, seats)


if __name__ == '__main__':
    hamilton([2560, 3315, 995, 5012], seats=20)
    hamilton([24, 113, 113], seats=25)
    hamilton([24, 113, 113], seats=26)

    print()
    jefferson([2560, 3315, 995, 5012], seats=20)
    jefferson([24, 113, 113], seats=26)

    print()
    dont([240, 360, 150], seats=8)
    dont([720, 300, 480], seats=8)

    print()
    all([2560, 3315, 995, 5012], seats=20)
