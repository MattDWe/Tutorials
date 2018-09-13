// Example using a two dimensional array

import java.util.Scanner;

public class PassTwoDimensionalArray{
  public static void main(String[] args){
    int[][] matrix = getArray();
    System.out.println("Sum of all elements is " + sum(matrix));
    showMatrix(matrix);
  }
  public static int[][] getArray(){
    Scanner input = new Scanner(System.in);
    int[][] matrix = new int[3][4];
    System.out.println("Enter " + matrix.length + " rows and " + matrix[0].length + " coloums: ");
    for (int x = 0; x < matrix.length; x++){
      for (int y = 0; y < matrix[0].length; y++){
        matrix[x][y] = input.nextInt();
      }
    }
    return matrix;
  }
  public static int sum(int[][] matrix){
    int total = 0;
    for (int x = 0; x < matrix.length; x++){
      for (int y = 0; y < matrix[0].length; y++){
        total += matrix[x][y];
      }
    }
    return total;
  }
  public static void showMatrix(int[][] matrix){
    for (int x = 0; x < matrix.length; x++){
      for (int y = 0; y < matrix[0].length; y++){
        System.out.print(matrix[x][y] + "  ");
      }
      System.out.println();
    }
  }
}
