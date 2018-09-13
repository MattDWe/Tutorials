// Takes seconds as an integer and returns minutes and seconds

import java.util.Scanner;

public class DisplayTime{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Please enter total seconds: ");
    int seconds = input.nextInt();
    int minutes = seconds / 60;
    int remainingSeconds = seconds % 60;
    System.out.println("Minutes: " + minutes + " Seconds: " + remainingSeconds);
  }
}
