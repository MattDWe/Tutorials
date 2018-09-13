// Reading data using scanner

import java.util.Scanner;
import java.io.*;

public class ReadData{
  public static void main(String[] args) throws Exception{
    java.io.File file = new java.io.File(".\\scores.txt");
    Scanner input = new Scanner(file);
    String firstName = input.next();
    String mi = input.next();
    String lastName = input.next();
    String age = input.next();
    System.out.println(firstName + " " + mi + " " + lastName + " Age: " + age);
  }
}
