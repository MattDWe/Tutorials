// Demonstrates comparing strings to put in alphabetical order

import java.util.Scanner;

public class OrderTwoCities{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Please enter two cities: ");
    String city1 = input.nextLine();
    String city2 = input.nextLine();
    if (city1.compareToIgnoreCase(city2) < 0){
      System.out.println(city1);
      System.out.println(city2);
    }
    else{
      System.out.println(city2);
      System.out.println(city1);
    }
  }
}
