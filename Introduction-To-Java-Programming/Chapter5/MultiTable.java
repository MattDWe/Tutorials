// Example using nested for loops and printing formatting

public class MultiTable{
  public static void main(String[] args){
    System.out.println("Multiplication Table");
    System.out.print("    ");
    System.out.println();
    for (int j = 1; j <= 10; j++){
      System.out.print(j + " | ");
      for (int i = 1; i <= 10; i++){
        System.out.printf("%4d", i * j);
      }
      System.out.println();
    }
  }
}
