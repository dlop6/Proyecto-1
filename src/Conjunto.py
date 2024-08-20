class Conjunto:
    """
    Clase que implementa un conjunto utilizando una tabla hash con listas enlazadas para manejar colisiones.
    """

    def __init__(self, size, name) -> None:
        """
        Inicializa el conjunto con una tabla hash de un tamaño dado.
        
        Parámetros:
        - size (int): Tamaño de la tabla hash (número de buckets).
        """
        self.name = name
        self.size = size  # Tamaño de la tabla hash
        self.buckets = [[] for _ in range(size)]  # Lista de listas para los buckets

    def hash(self, value):
        """
        Implementación de una función hash simple para convertir un valor en un índice de la tabla hash.
        Esta forma evita colisiones para sets de tamaños pequeños.
        """
        if isinstance(value, str):
            return sum(ord(char) for char in value) % self.size
        else:
            return hash(value) % self.size

    def add(self, value):
        """
        Agrega un valor al conjunto si no está presente.

        Parámetros:
        - value: El valor a agregar al conjunto.
        """
        hash_value = self.hash(value)  # Calcula el valor hash
        bucket = self.buckets[hash_value]  # Obtiene el bucket correspondiente
        if value not in bucket:  # Solo agrega si no está presente
            bucket.append(value)


    def remove(self, value):
        """
        Elimina un valor del conjunto si está presente.

        Parámetros:
        - value: El valor a eliminar del conjunto.
        """
        hash_value = self.hash(value)  # Calcula el valor hash
        bucket = self.buckets[hash_value]  # Obtiene el bucket correspondiente

        if value in bucket:  # Solo elimina si está presente
            bucket.remove(value)

    def contains(self, value):
        """
        Verifica si un valor está en el conjunto.

        Parámetros:
        - value: El valor a verificar.

        Retorna:
        - bool: True si el valor está en el conjunto, False en caso contrario.
        """
        hash_value = self.hash(value)  # Calcula el valor hash
        bucket = self.buckets[hash_value]  # Obtiene el bucket correspondiente

        return value in bucket

    def __str__(self):
        """
        Retorna una representación en cadena del conjunto.
        
        Retorna:
        - str: Representación del conjunto como una lista de buckets.
        """
        values = []
        for bucket in self.buckets:
            for val in bucket:
                values.append(val)
        return str(values)

    def __iter__(self):
        """
        Inicializa el iterador para recorrer los elementos del conjunto.

        Retorna:
        - Conjunto: El objeto iterable (self).
        """
        self.current_bucket = 0  # Índice del bucket actual
        self.current_index = 0  # Índice dentro del bucket actual
        return self

    def __next__(self):
        """
        Retorna el siguiente elemento del conjunto durante la iteración.

        Retorna:
        - El siguiente elemento en el conjunto.

        Lanza:
        - StopIteration: Si no hay más elementos para iterar.
        """
        while self.current_bucket < self.size:
            bucket = self.buckets[self.current_bucket]

            if self.current_index < len(bucket):
                value = bucket[self.current_index]
                self.current_index += 1
                return value

            self.current_bucket += 1
            self.current_index = 0

        raise StopIteration

    def union(self, other):
        """
        Realiza la unión de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto con el que se hará la unión.

        Retorna:
        - Conjunto: Un nuevo conjunto que es la unión de ambos conjuntos.
        """
        union_size = self.size + self.complemento(other).size
        new_set = Conjunto(union_size -1, "Union")

        # Agrega todos los elementos de este conjunto al nuevo conjunto
        for value in self:
            new_set.add(value)

        # Agrega los elementos del otro conjunto que no están en el nuevo conjunto
        for value in other:
            if not new_set.contains(value):
                new_set.add(value)

        return new_set

    def complemento(self, other):
        """
        Realiza el complemento de este conjunto con otro conjunto.

        Parámetros:
        - other (Conjunto): Otro conjunto para calcular el complemento.

        Retorna:
        - Conjunto: Un nuevo conjunto que es el complemento (diferencia) de ambos conjuntos.
        """
        reference_list = []
        for value in other:
            if not self.contains(value):
                reference_list.append(value)

        new_set = Conjunto(len(reference_list), "Complemento")

        # Agrega los elementos de este conjunto que no están en el otro conjunto
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


# # main

# # Crea dos conjuntos
set1 = Conjunto(4, "A")
# set2 = Conjunto(3, "B")

# # Agrega elementos a los conjuntos

set1.add('1')
set1.add('0')
set1.add('x')
set1.add('y')

# set2.add(3)
# set2.add(4)
# set2.add(5)

# # Muestra los conjuntos
# print(set1)
# print(set2)

# # Realiza la unión de los conjuntos
# union_set = set1.union(set2)
# print(union_set)


# # Realiza el complemento de los conjuntos
# complemento_set = set1.complemento(set2)

# print(complemento_set)

# # Itera sobre los elementos del conjunto
# for value in set1:
#     print(value)
    