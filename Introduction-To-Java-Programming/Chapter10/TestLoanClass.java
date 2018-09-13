// Example of object orientated programming using encapsulation

import java.util.Scanner;

public class TestLoanClass{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter annual interest rate: ");
    double AnnualInterestRate = input.nextDouble();
    System.out.print("Enter number of years as int: ");
    int numberOfYears = input.nextInt();
    System.out.print("Enter loan amount: ");
    double loanAmount = input.nextDouble();
    Loan loan = new Loan(AnnualInterestRate, numberOfYears, loanAmount);
    System.out.printf("The loan was created on %s\n" + "Monthly payment is %.2f\nThe total payment is %.2f\n", loan.getLoanDate().toString(), loan.getMonthlyPayment(), loan.getTotalPayment());
  }
}
