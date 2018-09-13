// Using loops guess number until matches randomly selected number

import java.util.Scanner;

public class GuessNumber{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int number = (int)(Math.random() * 101);
    System.out.print("Guess a number between 0-100. ");
    int guess = input.nextInt();
    while (guess != number){
      System.out.println("Incorrect.");
      if (guess < number){
        System.out.print("Your guess was too low. Try again. ");
      }
      else{
        System.out.print("Your guess was too high. Try again. ");
      }
      guess = input.nextInt();
    }
    System.out.println("Correct.");
  }
}
