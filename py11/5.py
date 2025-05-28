class TreeNode:                             # Definimos la clase para un nodo del árbol
    def __init__(self, val):                # Método constructor que inicializa un nodo con un valor
        self.val = val                      # Guardamos el valor que tiene el nodo
        self.left = None                    # Inicializamos el puntero izquierdo como None (sin hijo izquierdo aún)
        self.right = None                   # Inicializamos el puntero derecho como None (sin hijo derecho aún)

def insert_bst(root, val):                  # Función para insertar un valor en el árbol BST
    if not root:                           # Si el árbol está vacío (root es None)
        return TreeNode(val)               # Creamos un nuevo nodo con el valor y lo devolvemos
    if val < root.val:                     # Si el valor a insertar es menor que el nodo actual
        root.left = insert_bst(root.left, val)    # Insertamos recursivamente en el subárbol izquierdo
    else:                                 # Si el valor a insertar es mayor o igual que el nodo actual
        root.right = insert_bst(root.right, val)  # Insertamos recursivamente en el subárbol derecho
    return root                           # Devolvemos el nodo raíz (actualizado)

def build_bst(values):                     # Función para construir un BST a partir de una lista de valores
    root = None                           # Inicializamos el árbol vacío (sin raíz)
    for val in values:                    # Recorremos cada valor en la lista de valores
        root = insert_bst(root, val)     # Insertamos cada valor en el árbol usando insert_bst
    return root                          # Devolvemos la raíz del árbol construido

def build_degenerate_bst(values):         # Construye un BST degenerado, que es como una lista enlazada
    if not values:                        # Si la lista de valores está vacía
        return None                      # Retornamos None porque no hay nodos para construir
    root = TreeNode(values[0])           # Creamos el primer nodo con el primer valor (raíz)
    current = root                       # Creamos un puntero auxiliar para recorrer y agregar nodos
    for val in values[1:]:               # Recorremos el resto de valores después del primero
        current.right = TreeNode(val)    # Cada nuevo nodo lo agregamos como hijo derecho (sin hijos izquierdos)
        current = current.right          # Movemos el puntero auxiliar al nuevo nodo creado
    return root                         # Retornamos la raíz del árbol degenerado creado

def bst_to_dll(root):                     # Función principal que convierte un BST en lista doblemente enlazada circular
    if not root:                         # Si el árbol está vacío
        return None                     # Retornamos None porque no hay nada que convertir

    first = last = None                  # Inicializamos dos punteros: 'first' para el primer nodo de la lista y 'last' para el último

    def inorder(node):                   # Función interna para hacer recorrido inorden (izquierda - nodo - derecha)
        nonlocal first, last             # Usamos 'nonlocal' para poder modificar variables 'first' y 'last' definidas fuera
        if not node:                    # Caso base: si el nodo es None, no hacemos nada
            return
        inorder(node.left)              # Recursivamente recorremos el subárbol izquierdo

        if last:                       # Si ya hemos visitado algún nodo antes (last no es None)
            last.right = node          # Conectamos el nodo anterior (last) con el nodo actual (node) hacia la derecha
            node.left = last           # Conectamos el nodo actual con el anterior hacia la izquierda
        else:                         # Si no hay nodo anterior, quiere decir que este es el primer nodo visitado
            first = node              # Guardamos este nodo como el primero de la lista

        last = node                   # Actualizamos 'last' al nodo actual, pues ahora es el último visitado

        inorder(node.right)            # Recursivamente recorremos el subárbol derecho

    inorder(root)                      # Llamamos a la función inorden para comenzar el recorrido desde la raíz

    first.left = last                  # Conectamos el primer nodo con el último para hacer la lista circular (izquierda del primero apunta al último)
    last.right = first                 # Conectamos el último nodo con el primero para cerrar el círculo (derecha del último apunta al primero)

    return first                      # Retornamos el puntero al primer nodo de la lista doblemente enlazada circular

def validate_circular_dll(head, expected_vals):  # Función para validar que la lista circular tiene los valores correctos en orden
    if not head and not expected_vals:            # Si la lista está vacía y la lista esperada también
        return True                               # Entonces la validación es correcta
    if not head or not expected_vals:             # Si uno está vacío y el otro no
        return False                              # No es válido porque no coinciden

    vals_forward = []                             # Lista para almacenar valores del recorrido hacia adelante
    node = head                                  # Comenzamos desde el nodo cabeza
    while True:                                  # Ciclo infinito hasta que se rompe manualmente
        vals_forward.append(node.val)            # Agregamos el valor actual a la lista
        node = node.right                        # Avanzamos al siguiente nodo en la lista
        if node == head:                         # Si volvimos al nodo inicial, terminamos el recorrido
            break

    vals_backward = []                            # Lista para almacenar valores del recorrido hacia atrás
    node = head.left                             # Comenzamos desde el nodo anterior al head (último nodo en la lista)
    while True:                                  # Ciclo infinito hasta romper manualmente
        vals_backward.append(node.val)           # Agregamos el valor actual a la lista
        node = node.left                         # Retrocedemos al nodo anterior
        if node == head.left:                    # Si volvimos al último nodo inicial, terminamos
            break
    vals_backward.reverse()                       # Invertimos la lista para que esté en orden ascendente

    return vals_forward == expected_vals and vals_backward == expected_vals  
    # Comparamos ambas listas con la lista esperada, si coinciden ambas, la validación es correcta

# Casos de prueba:

head1 = bst_to_dll(build_bst([2, 1, 3]))          # Construimos BST con valores 2, 1, 3 y convertimos a DLL
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # Validamos que la DLL contenga [1, 2, 3] circularmente

head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))   # BST más grande, convertido a DLL
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # Validamos orden correcto

head3 = bst_to_dll(build_bst([5]))              # BST con un solo nodo
print(validate_circular_dll(head3, [5]) == True)   # Validamos que el único nodo apunte a sí mismo circularmente

head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))  # BST degenerado (como lista) convertido a DLL
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # Validamos que contenga los valores correctos

head5 = bst_to_dll(None)                         # Árbol vacío convertido a DLL
print(head5 is None)                             # Debe devolver None porque no hay nodos
