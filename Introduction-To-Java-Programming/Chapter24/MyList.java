// Interface for future list types

public interface MyList<E> extends java.lang.Iterable<E>{
  public void add(E e); // Add new element at end of list
  public void add(int index, E e); // Add new element at index
  public void clear(); // Clear list
  public boolean contains(E e); // Return true if contains element
  public E get(int index); // Returns the element at the index
  public int indexOf(E e); // Return index of first matching element in list or -1 if no match
  public boolean isEmpty(); // Return true if empty
  public int lastIndexOf(E e); // Return last matching element in this list or -1 if no match
  public boolean remove(E e); // Remove first occurance of element from list
  public E remove(int index); // Remove element at given index
  public Object set(int index, E e); // Replace element at index with given element
  public int size(); // Return number of items in list
}
