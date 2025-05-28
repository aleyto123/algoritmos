# Nodo del árbol BST
class TreeNode:                                    # Defino la clase para un nodo del árbol
    def __init__(self, val):                       # Constructor que inicializa el nodo con un valor
        self.val = val                             # Guardo el valor del nodo
        self.left = None                           # Inicializo el puntero al hijo izquierdo en None
        self.right = None                          # Inicializo el puntero al hijo derecho en None

def insert_bst(root, val):                         # Función para insertar un valor en el BST
    if root is None:                               # Si el árbol está vacío (nodo raíz es None)
        return TreeNode(val)                       # Creo y retorno un nuevo nodo con el valor dado
    if val < root.val:                             # Si el valor es menor que el valor del nodo actual
        root.left = insert_bst(root.left, val)   # Inserto recursivamente en el subárbol izquierdo
    else:                                         # Si el valor es mayor o igual que el nodo actual
        root.right = insert_bst(root.right, val) # Inserto recursivamente en el subárbol derecho
    return root                                   # Retorno la raíz actualizada (sin cambios o con hijos nuevos)

def build_bst(values):                             # Construye un BST a partir de una lista de valores
    root = None                                   # Inicializo la raíz como None
    for v in values:                              # Recorro cada valor en la lista de valores
        root = insert_bst(root, v)                # Inserto el valor en el BST
    return root                                  # Retorno la raíz del BST construido

def find_lca(root, val1, val2):                   # Función para encontrar el ancestro común más bajo (LCA)
    while root:                                   # Mientras el nodo raíz no sea None
        if val1 < root.val and val2 < root.val:  # Si ambos valores son menores que el nodo actual
            root = root.left                      # Me muevo al subárbol izquierdo para buscar el LCA
        elif val1 > root.val and val2 > root.val:# Si ambos valores son mayores que el nodo actual
            root = root.right                     # Me muevo al subárbol derecho para buscar el LCA
        else:                                     # Si los valores se dividen, uno menor y otro mayor (o igual)
            return root.val                        # Retorno el valor del nodo actual que es el LCA
    return None                                   # Si no encuentro LCA (caso borde), retorno None

# Casos de prueba
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # LCA de 2 y 8 es 6
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 4) == 2)  # LCA de 2 y 4 es 2
print(find_lca(build_bst([5, 3, 7]), 3, 7) == 5)                    # LCA de 3 y 7 es 5
print(find_lca(build_bst([5]), 5, 5) == 5)                          # LCA de 5 y 5 es 5
print(find_lca(None, 1, 2) == None)                                 # Árbol vacío, LCA no existe
