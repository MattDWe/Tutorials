// Using a do loop until an integer is given

import java.util.*;

public class InputException{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    boolean continueInput = true;
    int number;
    do {
      try {
        System.out.print("Enter an int: ");
        number = input.nextInt();
        System.out.print("Integer entered: " + number);
        continueInput = false;
      }
      catch (InputMismatchException ex){
        System.out.println("Incorrect input type. An integer is needed.");
        input.nextLine(); // Discards input
      }
    } while (continueInput);
  }
}
