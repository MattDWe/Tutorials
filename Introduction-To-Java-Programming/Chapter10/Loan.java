// Loan class used in TestLoanClass.java

public class Loan{
  private double AnnualInterestRate;
  private int numberOfYears;
  private double loanAmount;
  private java.util.Date loanDate;
  public Loan(){
    this(2.5,1,1000);
  }
  public Loan(double AnnualInterestRate, int numberOfYears, double loanAmount){
    this.AnnualInterestRate = AnnualInterestRate;
    this.numberOfYears = numberOfYears;
    this.loanAmount = loanAmount;
    loanDate = new java.util.Date();
  }
  public double getAnnualInterestRate(){
    return AnnualInterestRate;
  }
  public void setAnnualInterestRate(double AnnualInterestRate){
    this.AnnualInterestRate = AnnualInterestRate;
  }
  public int getNumberOfYears(){
    return numberOfYears;
  }
  public void setLoanAmount(double loanAmount){
    this.loanAmount = loanAmount;
  }
  public double getMonthlyPayment(){
    double monthlyInterestRate = AnnualInterestRate/1200;
    double monthlyPayment = loanAmount*monthlyInterestRate/(1-(1/Math.pow(1+monthlyInterestRate, numberOfYears*12)));
    return monthlyPayment;
  }
  public double getTotalPayment(){
    double totalPayment = getMonthlyPayment() * numberOfYears*12;
    return totalPayment;
  }
  public java.util.Date getLoanDate(){
    return loanDate;
  }
}
