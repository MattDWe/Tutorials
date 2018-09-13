// Using loops to find GCD of given number

import java.util.Scanner;

public class GreatestCommonDivisor{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter first int: ");
    int n1 = input.nextInt();
    System.out.print("Enter second int: ");
    int n2 = input.nextInt();
    int gcd = 1;
    int k = 2;
    while (k <= n1 && k <= n2){
      if (n1%k == 0 && n2%k == 0){
        gcd = k;
      }
      k++;
    }
    System.out.println("Greatest Common Divisor: " + gcd);
  }
}
