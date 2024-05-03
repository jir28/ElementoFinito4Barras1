import numpy as np
from numpy.linalg import solve
# Matrices de rigidez elementales

k1 = np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]]) * (29.5e6 / 40)
print(k1)

k2 = np.array([[0, 0, 0, 0], [0, 1, 0, -1], [0, 0, 0, 0], [0, -1, 0, 1]]) * (29.5e6 / 30)
print(k2)

k3 = np.array([[0.64, 0.48, -0.64, -0.48], [0.48, 0.36, -0.48, -0.36], [-0.64, -0.48, 0.64, 0.48],
               [-0.48, -0.36, 0.48, 0.36]]) * (29.5e6 / 50)
print(k3)

k4 = np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]]) * (29.5e6 / 40)
print(k4)

# Matriz de rigidez global de 8x8
K_global = np.zeros((8, 8))


# Función para colocar las matrices elementales en la matriz global según los GdL que afectan
def place_in_global(K_elem, indices, K_global):
    for i, index_i in enumerate(indices):
        for j, index_j in enumerate(indices):
            K_global[index_i - 1, index_j - 1] += K_elem[i, j]
    return K_global


# Colocando cada matriz elemental en la matriz global
indices_elementos = {
    'k1': [1, 2, 3, 4],
    'k2': [5, 6, 3, 4],
    'k3': [1, 2, 5, 6],
    'k4': [7, 8, 5, 6]
}

for key, indices in indices_elementos.items():
    K_global = place_in_global(eval(key), indices, K_global)

#print(K_global)

indices_to_delete = [0, 1, 3, 6, 7]  # Ajustar para índices base cero, se eimnan los Gdl que no tienen movimiento, 1,2,4 7 y 8

# Eliminando las filas y columnas
K_reduced = np.delete(K_global, indices_to_delete, axis=0)  # Eliminar filas
K_reduced = np.delete(K_reduced, indices_to_delete, axis=1)  # Eliminar columnas

print(K_reduced)
# Definir el vector de fuerzas externas
F_reduced = np.array([20000, 0, -25000])

# Resolviendo para obtener los desplazamientos
desplazamientos = solve(K_reduced, F_reduced)
print("Desplazamientos nodales:", desplazamientos)