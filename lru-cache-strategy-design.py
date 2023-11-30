from abc import ABC, abstractmethod
import time

# Strategy interface
class EvictionStrategy(ABC):
    @abstractmethod    
    def evict(self, cache):
        pass

# Concrete strategy    
class LRUEvictionStrategy(EvictionStrategy):
    def evict(self, cache):
        lru_entry = None
        oldest_access_time = float("inf")
        
        for key, entry in cache.items():
            if entry.access_time < oldest_access_time:
                lru_entry_key = key  
                oldest_access_time = entry.access_time
                
        print(f"Evicting {lru_entry_key} from cache")     
        cache.pop(lru_entry_key)   

# Cache entries
class CacheEntry:
    def __init__(self, value):
        self.value = value
        self.access_time = time.time()

# Cache interface        
class Cache:
    def __init__(self, eviction_policy):
        self._eviction_policy = eviction_policy 
        self._entries = {}
        
    def get(self, key):
        entry = self._entries[key]
        entry.access_time = time.time()
        return entry.value
    
    def set(self, key, value):
        entry = CacheEntry(value)
        self._entries[key] = entry 
        
        self._eviction_policy.evict(self._entries)
                              
# Usage            
cache = Cache(LRUEvictionStrategy()) 
cache.set("a", 1)
cache.set("b", 2)

cache.get("a")

cache.set("c", 3)
