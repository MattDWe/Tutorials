// Generic allows for a wildcare type that is specified later
// The E represents the type that is specified when the actual class is used

public class GenericMethodDemo{
  public static void main(String[] args){
    Integer[] integers = {1, 2, 3, 4, 5};
    String[] strings = {"London", "Paris", "New York"};

    GenericMethodDemo.<Integer>print(integers);
    GenericMethodDemo.<String>print(strings);
  }

  public static <E> void print(E[] list){
    for (int i = 0; i < list.length; i++){
      System.out.print(list[i] + " ");
    }
    System.out.println();
  }
}
