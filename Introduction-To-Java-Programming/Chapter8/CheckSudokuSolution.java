// Verify a sudoku solution using matrix

import java.util.Scanner;

public class CheckSudokuSolution{
  public static void main(String[] args){
    int[][] grid = readASolution();
    System.out.println(isValid(grid) ? "Valid solution" : "Invalid Solution");
  }
  public static int[][] readASolution(){
    Scanner input = new Scanner(System.in);
    System.out.println("Enter a Sudoku puzzle solution:");
    int[][] grid = new int[9][9];
    for (int x = 0; x < 9; x++){
      for (int y = 0; y < 9; y++){
        grid[x][y] = input.nextInt();
      }
    }
    return grid;
  }
  public static boolean isValid(int[][] grid){
    for (int x = 0; x < 9; x++){
      for (int y = 0; y < 9; y++){
        if (grid[x][y] < 1 || grid[x][y] > 9 || !isValid(x,y,grid)){
          return false;
        }
      }
    }
    return true;
  }
  public static boolean isValid(int x, int y, int[][] grid){
    for (int column = 0; column < 9; column++){
      if (column != y && grid[x][column] == grid[x][y]){
        return false;
      }
    }
    for (int row = 0; row < 9; row++){
      if (row != x && grid[row][y] == grid[x][y]){
        return false;
      }
    }
    for (int row = (x/3)*3; row < (x/3)*3 + 3;row++){
      for (int col = (y / 3) * 3; col < (y / 3) * 3 + 3; col++){
        if (row != x && col != y && grid[row][col] == grid[x][y]){
          return false;
        }
      }
    }
    return true;
  }
}
