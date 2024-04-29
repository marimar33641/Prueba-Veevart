def knapsackTab(M, N):
    tab = [0 for _ in range(M + 1)]
    items_taken = [[] for _ in range(M + 1)]  

    for n in range(1, N + 1):
        for m in range(M, 0, -1):
            if m - wb[n - 1][0] >= 0:
                new_val = tab[m - wb[n - 1][0]] + wb[n - 1][1]
                if new_val > tab[m]:
                    tab[m] = new_val
                    items_taken[m] = items_taken[m - wb[n - 1][0]] + [n - 1]
    return tab[M], [wb[item] for item in items_taken[M]]

wb = [(2, 3), (3, 4), (4, 5), (5, 6)]  
N = len(wb)
M = 8

max_value, items_selected = knapsackTab(M,N)
print("Valor maximo: ",max_value)
print("Lista: ", items_selected)