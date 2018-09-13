import java.util.*;

public class TestTreeSet{
  public static void main(String[] args){
    Set<String> set = new HashSet<>();

    set.add("London");
    set.add("Paris");
    set.add("New York");
    set.add("San Francisco");
    set.add("Beijing");
    set.add("New York");

    TreeSet<String> treeSet = new TreeSet<>(set);
    System.out.println("Sorted tree set: " + treeSet);

    System.out.println("first() " + treeSet.first()); // First
    System.out.println("last() " + treeSet.last()); // Last
    System.out.println("headSet(\"New York\") " + treeSet.headSet("New York")); // Returns elements before new york
    System.out.println("tailSet(\"New York\") " + treeSet.tailSet("New York")); // returns elements after new york

    System.out.println("lower(\"P\"): " + treeSet.lower("P")); // largest element less than P
    System.out.println("higher(\"P\"): " + treeSet.higher("P")); // Smallest element less than P
    System.out.println("floor(\"P\"): " + treeSet.floor("P")); // Returns largest element less than or equal to P
    System.out.println("ceiling(\"P\"): " + treeSet.ceiling("P")); // returns smallest element greater than or equal to P
    System.out.println("pollFirst(): " + treeSet.pollFirst()); // removes first element in tree set and returns the removed element
    System.out.println("pollLast(): " + treeSet.pollLast()); // removes the last element in tree set and returns removed element
    System.out.println("New tree set: " + treeSet);
  }
}
