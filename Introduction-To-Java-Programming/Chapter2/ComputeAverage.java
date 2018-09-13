// Demonstrates taking multiple inputs from single line

import java.util.Scanner;

public class ComputeAverage{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Please enter 3 numbers: ");
    double num1 = input.nextDouble();
    double num2 = input.nextDouble();
    double num3 = input.nextDouble();
    double avg = (num1 + num2 + num3)/3;
    System.out.println("Average: " + avg);
  }
}
