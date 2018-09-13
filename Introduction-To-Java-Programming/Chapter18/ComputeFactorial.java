// Basic example of recursion

import java.util.Scanner;

public class ComputeFactorial{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter a nonnegative int: ");
    int n = input.nextInt();
    System.out.println("Factorial of " + n + " is " + factorial(n));
  }
  public static long factorial(int n){
    if (n <= 1) {
      return n;
    }
    else {
      return n * factorial(n - 1);
    }
  }
}
