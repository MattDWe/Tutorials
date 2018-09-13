// Example of exception handling

import java.util.Scanner;

public class QuotientWithException{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter two ints: ");
    int num1 = input.nextInt();
    int num2 = input.nextInt();
    int result;
    try{
      result = num1/num2;
      System.out.println(num1 + " / " + num2 + " is " + result);
    }
    catch(ArithmeticException ex){ // catch (type ex){} Example: Exception in thread "main" java.lang.ArithmeticException: / by zero at Quotient.main(Quotient.java:11)
      System.out.println("Exception: integer cannot be divided by zero.");
    }
  }
}
