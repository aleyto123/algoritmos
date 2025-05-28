class TreeNode:
    def __init__(self, val=0, left=None, right=None):               # Nodo del árbol con valor y referencias a hijos
        self.val = val                                              # Valor del nodo
        self.left = left                                            # Hijo izquierdo
        self.right = right                                          # Hijo derecho

def build_tree(vals):
    """Construye un árbol binario completo desde una lista (nivel por nivel)"""
    if not vals:
        return None                                                # Retorna None si la lista está vacía
    nodes = [None if v is None else TreeNode(v) for v in vals]     # Crear nodos o None para cada valor
    kids = nodes[::-1]                                             # Copia invertida para asignar hijos
    root = kids.pop()                                              # Nodo raíz (primer elemento)
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()                        # Asignar hijo izquierdo si existe
            if kids: node.right = kids.pop()                       # Asignar hijo derecho si existe
    return root                                                   # Retornar el nodo raíz del árbol

def build_invalid_tree1():
    # Árbol inválido: hijo izquierdo > padre (violación BST)
    #   5
    #  / \
    # 6   7   <-- 6 > 5 es inválido
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    return root

def build_invalid_tree2():
    # Árbol inválido: hijo derecho < padre (violación BST)
    #   5
    #  / \
    # 3   4   <-- 4 < 5 pero está en hijo derecho, inválido
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root

def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    if root is None:                                              # Si nodo es None, árbol vacío válido
        return True
    if not (low < root.val < high):                               # Si valor del nodo no está en rango válido
        return False                                              # No cumple propiedad BST
    left_valid = is_valid_bst(root.left, low, root.val)           # Validar subárbol izquierdo con nuevo límite superior
    right_valid = is_valid_bst(root.right, root.val, high)        # Validar subárbol derecho con nuevo límite inferior
    return left_valid and right_valid                             # Retorna True sólo si ambos subárboles son válidos

# Pruebas completas con impresión del resultado
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)  # True, árbol válido
print(is_valid_bst(build_invalid_tree1()) == False)             # False, hijo izquierdo inválido
print(is_valid_bst(build_invalid_tree2()) == False)             # False, hijo derecho inválido
print(is_valid_bst(build_tree([42])) == True)                   # True, solo un nodo
print(is_valid_bst(None) == True)                               # True, árbol vacío
