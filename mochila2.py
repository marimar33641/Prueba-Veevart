def knapsackTabOpt3(M, N):
    tab = [0 for _ in range(M + 1)]
    items_taken = [[] for _ in range(M + 1)]
    not_items_taken = [list(range(N)) for _ in range(M + 1)]  # Inicializamos con todos los índices

    for n in range(1, N + 1):
        for m in range(M, 0, -1):
            if m - wb[n - 1][0] >= 0:
                new_val = tab[m - wb[n - 1][0]] + wb[n - 1][1]
                if new_val > tab[m]:
                    tab[m] = new_val
                    items_taken[m] = items_taken[m - wb[n - 1][0]] + [n - 1]
                    not_items_taken[m] = [item for item in not_items_taken[m - wb[n - 1][0]] if item != n - 1]
    max_value = tab[M]
    items_selected = [wb[item] for item in items_taken[M]]
    items_not_selected = [wb[item] for item in not_items_taken[M] if item not in items_taken[M]]
    total_value_not_selected = sum([item[1] for item in items_not_selected])
    return max_value, items_selected, items_not_selected, total_value_not_selected

wb = [(2, 3), (3, 4), (4, 5), (5, 6)]
N = len(wb)
M = 8

max_value, items_selected, items_not_selected, total_value_non_selected = knapsackTabOpt3(M, N)
print("Valor maximo: ",max_value)
print("Objetos seleccionados (peso, valor):", items_selected)
print("Objetos no seleccionados (peso, valor):", items_not_selected)
print("Valor total de objetos no seleccionados:", total_value_non_selected)