class TreeNode:  # Definición de nodo para el BST
    def __init__(self, val=0, left=None, right=None):  # Constructor del nodo
        self.val = val          # Valor del nodo
        self.left = left        # Hijo izquierdo del nodo
        self.right = right      # Hijo derecho del nodo

def insert_into_bst(root, val):  # Función para insertar un valor en el BST
    if root is None:             # Si el árbol está vacío
        return TreeNode(val)     # Crear un nuevo nodo y retornarlo
    if val < root.val:           # Si el valor es menor que el nodo actual
        root.left = insert_into_bst(root.left, val)  # Insertar en el subárbol izquierdo
    else:                        # Si el valor es mayor o igual
        root.right = insert_into_bst(root.right, val)  # Insertar en el subárbol derecho
    return root                  # Retornar el nodo raíz actualizado

def build_bst(vals):             # Construye un BST a partir de una lista de valores
    root = None                  # Inicializar árbol vacío
    for v in vals:               # Recorrer cada valor en la lista
        root = insert_into_bst(root, v)  # Insertar valor en BST
    return root                  # Retornar la raíz del árbol construido

def kth_smallest(root, k):       # Función para encontrar el k-ésimo elemento más pequeño
    count = 0                   # Contador de nodos visitados
    result = None               # Variable para almacenar el resultado cuando se encuentre

    def inorder(node):          # Función recursiva para recorrido inorder (izquierda-raíz-derecha)
        nonlocal count, result  # Para modificar variables externas dentro de la función
        if node is None or result is not None:  # Caso base: nodo nulo o resultado ya encontrado
            return
        inorder(node.left)      # Recorrer el subárbol izquierdo primero
        count += 1              # Incrementar el contador al visitar el nodo actual
        if count == k:          # Si se alcanzó el k-ésimo nodo
            result = node.val   # Guardar el valor del nodo actual como resultado
            return              # Terminar la recursión
        inorder(node.right)     # Recorrer el subárbol derecho

    inorder(root)               # Iniciar recorrido inorder desde la raíz
    return result               # Retornar el valor encontrado

# Casos de prueba
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)   # Esperado: 2 (2do menor)
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # Esperado: 2 (mínimo)
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # Esperado: 8 (máximo)
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # Esperado: 4 (medio)
print(kth_smallest(build_bst([10]), 1) == 10)  # Esperado: 10 (único nodo)
