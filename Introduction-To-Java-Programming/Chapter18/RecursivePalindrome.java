import java.util.Scanner;

public class RecursivePalindrome{
  public static boolean isPalindrome(String s){
    if (s.length() <= 1){
      return true;
    }
    else if (s.charAt(0) != s.charAt(s.length() - 1)){
      return false;
    }
    else{
      return isPalindrome(s.substring(1, s.length() - 1));
    }
  }
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter a string: ");
    String s = input.nextLine();
    while (s.length() > 0){
      System.out.println("Is " + s + " a palindrome? " + isPalindrome(s));
      System.out.print("Enter a string or press enter to stop: ");
      s = input.nextLine();
    }
  }
}
