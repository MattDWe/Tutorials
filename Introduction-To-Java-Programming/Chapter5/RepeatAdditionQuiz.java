// Basic program using while loops

import java.util.Scanner;

public class RepeatAdditionQuiz{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int number1 = (int)(Math.random() * 10);
    int number2 = (int)(Math.random() * 10);
    System.out.print("What is " + number1 + " + " + number2 + "? ");
    int ans = input.nextInt();
    while (number1 + number2 != ans){
      System.out.print("Wrong answer.");
      System.out.print(" What is " + number1 + " + " + number2 + "? ");
      ans = input.nextInt();
    }
    System.out.println("Good job!");
  }
}
