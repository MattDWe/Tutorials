import java.util.Scanner;

public class ComputeFibonacci{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter an index for Fibonacci number: ");
    int index = input.nextInt();

    System.out.println("Fibonacci for " + index + " is " + fib(index));
  }
  public static long fib(long index){
    if (index <= 1){
      return index;
    }
    else{
      return fib(index - 1) + fib(index - 2);
    }
  }
}
