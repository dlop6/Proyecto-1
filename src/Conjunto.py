class Conjunto:
    """
    Clase que implementa un conjunto utilizando listas para almacenar los elementos.
    """

    def __init__(self, size, name) -> None:
        """
        Inicializa el conjunto con una lista vacía.
        
        Parámetros:
        - size (int): Este parámetro ya no afecta directamente la implementación, pero se conserva para futuros usos o referencias.
        - name (str): El nombre del conjunto.
        """
        self.name = name
        self.size = size  # Tamaño (referencial) del conjunto
        self.elementos = []  # Lista para almacenar los elementos del conjunto


    def add(self, value):
        """
        Agrega un valor al conjunto si no está presente. Utiliza una lista para
        almacenar los elementos, y solo agrega el valor si no está ya presente.

        Parámetros:
        - value: El valor a agregar al conjunto.
        """
        if value not in self.elementos:
            self.elementos.append(value)

    def remove(self, value):
        """
        Elimina un valor del conjunto si está presente. Utiliza una lista y
        verifica si el valor está contenido antes de eliminarlo.

        Parámetros:
        - value: El valor a eliminar del conjunto.
        """
        if value in self.elementos:
            self.elementos.remove(value)    

    def contains(self, value):
        """
        Verifica si un valor está en el conjunto. Busca el valor en la lista de elementos.

        Parámetros:
        - value: El valor a verificar.

        Retorna:
        - bool: True si el valor está en el conjunto, False en caso contrario.
        """
        return value in self.elementos

    def __str__(self):
        """
        Retorna una representación en cadena del conjunto.

        Retorna:
        - str: Representación del conjunto como una lista de elementos.
        """
        return str(self.elementos).replace("[", "{").replace("]", "}")
    
    def __iter__(self):
        """
        Inicializa el iterador para recorrer los elementos del conjunto.

        Retorna:
        - Conjunto: El objeto iterable (self).
        """
        self.current_index = 0  # Índice actual dentro de la lista de elementos
        return self

    def __next__(self):
        """
        Retorna el siguiente elemento del conjunto durante la iteración.

        Retorna:
        - El siguiente elemento en el conjunto.

        Lanza:
        - StopIteration: Si no hay más elementos para iterar.
        """
        if self.current_index >= len(self.elementos):
            raise StopIteration

        value = self.elementos[self.current_index]
        self.current_index += 1
        return value

    def union(self, other: 'Conjunto') -> 'Conjunto':
        """
        Realiza la unión de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto con el que se hará la unión.

        Retorna:
        - Conjunto: Un nuevo conjunto que es la unión de ambos conjuntos.
        """
        union_size = self.size + len(other.elementos)
        new_set = Conjunto(union_size - 1, "Union")

        for value in self.elementos:
            new_set.add(value)
            
        for value in other.elementos:
            if not self.contains(value):
                new_set.add(value)
        
        return new_set
            
        
    def complemento(self, other: 'Conjunto') -> 'Conjunto':
        """
        Realiza el complemento de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto para calcular el complemento.

        Retorna:
        - Conjunto: Un nuevo conjunto que es el complemento (diferencia) de ambos conjuntos.
        """
        reference_list = []
        
        for value in other.elementos:
            if not self.contains(value):
                reference_list.append(value)
        
        new_set = Conjunto(len(reference_list), "Complemento")
        for value in reference_list:
            new_set.add(value)
            
        return new_set
    
    def interseccion(self, other):
        """
        Realiza la intersección de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto para calcular la intersección.

        Retorna:
        - Conjunto: Un nuevo conjunto que contiene la intersección entre este conjunto y el ingresado.
        """
        reference_list = []
        for value in self:
            if other.contains(value):
                reference_list.append(value)

        new_set = Conjunto(len(reference_list), "Interseccion")
        for value in reference_list:
            new_set.add(value)
        return new_set
    
    def diferencia(self, other):
        """
        Realiza la diferencia de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto para calcular la diferencia.

        Retorna:
        - Conjunto: Un nuevo conjunto con el resultado de la diferencia entre este conjunto y el ingresado.
        """
        reference_list = []
        for value in self:
            if not other.contains(value):
                reference_list.append(value)

        new_set = Conjunto(len(reference_list), "Diferencia")
        for value in reference_list:
            new_set.add(value)
        return new_set

    def diferencia_simetrica(self, other):
            """
            Realiza la diferencia simetrica de este conjunto con otro conjunto.

            Parámetros:
            - other (Conjunto): Otro conjunto para calcular la diferencia simetrica.

            Retorna:
            - Conjunto: Un nuevo conjunto con el resultado de la diferencia simetrica entre este conjunto y el ingresado.
            """

            reference_list = []
            for value in self:
                if not other.contains(value):
                    reference_list.append(value)

            for value in other:
                if not self.contains(value):
                    reference_list.append(value)

            new_set = Conjunto(len(reference_list), "Diferencia")
            for value in reference_list:
                new_set.add(value)
            return new_set
