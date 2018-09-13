// Hashing are like dictionaries from python
// Hashing uses a hashing function to map a key to an index
// A typical hash function first convers a search key to an integer value called
// a hash code, then compresses the hash code into an index to the hash table.
// Two ways to avoid collisions
// Open addressing is the process of finding an open location in the hash table.
// Separate chaining places all entries with the same hash index in the same location.
// Rehashing is the process when a hash table is full then recreate the hash table with larger space.

public interface MyMap<K, V> {
  public void clear(); // Remove all entries
  public boolean containsKey(K key); // Return true if key is in map
  public boolean containsValue(V value); // Return true if value is in map
  public java.util.Set<Entry<K, V>> entrySet(); // Return a set of entries in the map
  public V get(K key); // Return value that matches specified key
  public boolean isEmpty(); // Return true if empty
  public java.util.Set<K> keySet(); // Return set holding all the keys
  public V put(K key, V value); // Add entry into map
  public void remove(K key); // Remove entry from map
  public int size(); // Return number of mappings in this map
  public java.util.Set<V> values(); // return set consisting of values
  public static class Entry<K, V> {
    K key;
    V value;
    public Entry(K key, V value){
      this.key = key;
      this.value = value;
    }
    public K getKey(){
      return key;
    }
    public V getValue(){
      return value;
    }
    @Override
    public String toString(){
      return "[" + key + ", " + value + "]";
    }
  }
}
