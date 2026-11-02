def adjacency_list_to_matrix(lista):
        n = len(lista)

        matrix = [[0] * n for _ in range(n)]

        for node, neighbors in lista.items():
            for neighbor in neighbors:
                matrix[node][neighbor] = 1

        for row in matrix:
            print(row)

        return matrix
