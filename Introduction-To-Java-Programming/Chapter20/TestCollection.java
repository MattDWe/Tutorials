// Data Structure types
// Collections are for storing collections of elements
// Sets store a group of nonduplicate elements
// Lists store an ordered collection of elements
// Stacks store objects in a last in first out fashion
// Queues store objects that are first in first out fashion
// PriorityQueus store objects that are processed by priority

// Below is a example of using the collection interface

import java.util.*;

public class TestCollection {
  public static void main(String[] args) {
    ArrayList<String> collection1 = new ArrayList<>();
    collection1.add("New York");
    collection1.add("Atlanta");
    collection1.add("Dallas");
    collection1.add("Madison");

    System.out.print("A list of cities in collection1: ");
    System.out.println(collection1);

    System.out.println("\nIs Dallas in collection1? " + collection1.contains("Dallas"));

    System.out.println("Collection 1 size with dallas " + collection1.size());
    collection1.remove("Dallas");
    System.out.println("Collection 1 size without dallas " + collection1.size());

    Collection<String> collection2 = new ArrayList<>();
    collection2.add("Seattle");
    collection2.add("Portland");
    collection2.add("Los Angeles");
    collection2.add("Atlanta");

    System.out.println("\nA list of cities in collection2:");
    System.out.println(collection2);

    ArrayList<String> c1 = (ArrayList<String>)(collection1.clone());
    c1.addAll(collection2);
    System.out.println("Cities in collection1 or collection2: ");
    System.out.println(c1);

    c1 = (ArrayList<String>)(collection1.clone());
    c1.removeAll(collection2);
    System.out.print("\nCities in collection1, but not 2:");
    System.out.println(c1);
  }
}
