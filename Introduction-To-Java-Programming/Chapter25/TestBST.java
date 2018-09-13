public class TestBST{
  public static void main(String[] args){
    BST<String> tree = new BST<>();
    tree.insert("George");
    tree.insert("Michael");
    tree.insert("Tom");
    tree.insert("Adam");
    tree.insert("Jones");
    tree.insert("Peter");
    tree.insert("Daniel");

    System.out.print("Inorder (sorted): ");
    tree.inorder();
    System.out.print("\nPostorder: ");
    tree.postorder();
    System.out.print("\nPreorder: ");
    tree.preorder();
    System.out.print("\nThe number of nodes is " + tree.getSize());

    System.out.print("\nIs peter in the tree? " + tree.search("Peter"));

    System.out.print("\nA path from the root peter is: ");
    java.util.ArrayList<BST.TreeNode<String>> path = tree.path("Peter");
    for (String s: tree){
      System.out.print(s + " ");
    }
    Integer[] numbers = {2, 4, 4, 1, 8, 5, 6, 7};
    BST<Integer> intTree = new BST<>(numbers);
    System.out.print("\nInorder (sorted): ");
    intTree.inorder();

    tree.delete("George");
    System.out.print("\nInorder (sorted) after deleting george: ");
    tree.inorder();
  }
}
