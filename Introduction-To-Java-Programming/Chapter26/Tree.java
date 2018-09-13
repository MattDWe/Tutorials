// Tree data structures are hierarchical and consist of a root and left and right subtrees

public interface Tree<E> extends Iterable<E>{
  public boolean search(E e); // Return true if given element is in tree
  public boolean insert(E e); // Returns true if element is inserted successfully
  public boolean delete(E e); // Return true if element is deleted successfully
  public void inorder(); // Inorder traversal from the root.
  public void postorder(); // Postorder traversal from the root
  public void preorder(); //Preorder traversal from root
  public int getSize(); // Return number of nodes
  public boolean isEmpty(); // Return true if tree is empty
}
