// Algorithm design is to develop mathematical process for solving a problem.
// Big O notation is a method for measuring algorithm time complexity based on input size.

// Below is a performance test by testing the change in run time based on input

public class PerformanceTest{
  public static void main(String[] args){
    getTime(1000000);
    getTime(10000000);
    getTime(100000000);
    getTime(1000000000);
  }

  public static void getTime(long n){
    long startTime = System.currentTimeMillis();
    long k = 0;
    for (int i = 1; i <= n; i++){
      k += 5;
    }
    long endTime = System.currentTimeMillis();
    System.out.println("Exe time for n = " + n + " is " + (endTime - startTime) + " ms");
  }
}
