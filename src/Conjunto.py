
class Conjunto:
    
    def __init__(self, size) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash(self, value):
        return hash(value) % self.size
    
    def add(self, value):
        hash_value = self.hash(value)
        bucket = self.buckets[hash_value]
        
        if value not in bucket:
            bucket.append(value)
    
    def remove(self, value):
        hash_value = self.hash(value)
        bucket = self.buckets[hash_value]
        
        if value in bucket:
            bucket.remove(value)
            
    def contains(self, value):
        hash_value = self.hash(value)
        bucket = self.buckets[hash_value]
        
        return value in bucket

    def __str__(self) -> str:
        return str(self.buckets)
    
    def __iter__(self):
        self.current_bucket = 0
        self.current_index = 0
        return self
    
    def __next__(self):
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
        new_set = Conjunto(self.size)
        
        for value in self:
            new_set.add(value)
        
        for value in other:
            if (not new_set.contains(value)):
                new_set.add(value)
        
        return new_set
    
    def complemento(self, other):
        new_set = Conjunto(self.size)
        
        for value in self:
            if (not other.contains(value)):
                new_set.add(value)
        
        return new_set
    
    



        
       