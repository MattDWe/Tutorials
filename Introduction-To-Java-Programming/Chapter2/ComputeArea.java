// Reading input to calculate area of circle

import java.util.Scanner;

public class ComputeArea{
  public static void main(String[] args){
    Scanner input =  new Scanner(System.in);
    final double PI = 3.14159; // Final makes it a constant and unchangable
    System.out.print("Please enter a radius: ");
    double radius = input.nextDouble();
    double area = radius * radius * PI;
    System.out.println("The area is " + area);
  }
}
