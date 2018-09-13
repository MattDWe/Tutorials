// While loop example using output redirection example

import java.util.Scanner;

public class SentinelValue{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter an int (To stop enter 0): ");
    int num = input.nextInt();
    int sum = 0;
    while (num != 0){
      sum += num;
      System.out.print("Enter an int (To stop enter 0): ");
      num = input.nextInt();
    }
    System.out.println("Total is: " + sum);
  }
}
