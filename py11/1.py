# Clase para representar un nodo en el Árbol Binario de Búsqueda (BST)
class TreeNode:
    def __init__(self, val):
        # El valor que contiene el nodo
        self.val = val
        # Puntero al hijo izquierdo (valores menores)
        self.left = None
        # Puntero al hijo derecho (valores mayores)
        self.right = None

# Función para construir un BST a partir de una lista de valores
def build_bst(values):
    # Si la lista está vacía, el árbol será None
    if not values:
        return None

    # Función auxiliar para insertar un valor en el árbol de forma recursiva
    def insert(root, val):
        # Si no hay nodo actual, creamos uno nuevo con el valor dado
        if root is None:
            return TreeNode(val)
        # Si el valor es menor al nodo actual, insertamos a la izquierda
        if val < root.val:
            root.left = insert(root.left, val)
        # Si el valor es mayor o igual, insertamos a la derecha
        else:
            root.right = insert(root.right, val)
        # Retornamos el nodo raíz actualizado
        return root

    # Creamos la raíz del BST con el primer valor
    root = TreeNode(values[0])
    # Insertamos el resto de valores en el BST
    for val in values[1:]:
        insert(root, val)
    # Retornamos la raíz del árbol construido
    return root

# Función que busca los valores dentro de un rango específico en un BST
def range_query(root, min_val, max_val):
    """Encuentra todos los valores en el BST que estén dentro del rango [min_val, max_val]"""
    # Lista donde almacenaremos los valores que cumplen con el rango
    result = []

    # Función interna recursiva para recorrer el árbol en inorden
    def inorder(node):
        # Caso base: si el nodo es None, no hay nada que procesar
        if not node:
            return

        # Si el valor del nodo actual es mayor al mínimo del rango,
        # entonces podría haber valores válidos en el subárbol izquierdo
        if node.val > min_val:
            inorder(node.left)

        # Si el valor del nodo actual está dentro del rango, lo agregamos a la lista
        if min_val <= node.val <= max_val:
            result.append(node.val)

        # Si el valor del nodo actual es menor al máximo del rango,
        # entonces podría haber valores válidos en el subárbol derecho
        if node.val < max_val:
            inorder(node.right)

    # Iniciamos el recorrido desde la raíz del BST
    inorder(root)

    # Retornamos la lista de valores encontrados en orden ascendente
    return result

# ================================
# ✅ Casos de prueba
# ================================

# Test 1: Rango normal dentro del árbol
# BST creado a partir de [7, 3, 11, 1, 5, 9, 13]
# BST en orden: [1, 3, 5, 7, 9, 11, 13]
# Rango: [5, 10] → Resultado esperado: [5, 7, 9]
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])

# Test 2: Rango que cubre todos los valores del árbol
# BST: [2, 4, 6, 8] → Resultado esperado: [2, 4, 6, 8]
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])

# Test 3: Rango fuera de los valores del árbol
# BST: [10, 20, 30] → Rango [1, 5] → Resultado esperado: []
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])

# Test 4: Un solo nodo y el rango lo incluye
# BST: [15] → Rango [10, 20] → Resultado esperado: [15]
print(range_query(build_bst([15]), 10, 20) == [15])

# Test 5: Rango que coincide con valores de los bordes
# BST: [5, 10, 15, 20, 25] → Rango [10, 20] → Resultado esperado: [10, 15, 20]
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])
