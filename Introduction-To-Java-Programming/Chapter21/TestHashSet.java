// A map is like a dictionary that provides quick lookup to retrieve a value using a key
// A set is an efficient data structure for storing and processing nonduplicate elements

// A HashSet can be used to store duplicate free elements

import java.util.*;

public class TestHashSet {
  public static void main(String[] args){
    Set<String> set = new HashSet<>();

    set.add("London");
    set.add("Paris");
    set.add("New York");
    set.add("San Francisco");
    set.add("Beijing");
    set.add("New York");

    System.out.println(set);

    for (String s: set){
      System.out.print(s.toUpperCase() + " ");
    }
  }
}
