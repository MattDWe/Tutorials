// Display current time using System.currentTimeMillis()

public class CurrentTime{
  public static void main(String[] args){
    long milliseconds = System.currentTimeMillis();
    long totalSeconds = milliseconds / 1000;
    long currentSecond = totalSeconds % 60;
    long totalMinutes = totalSeconds / 60;
    long currentMinute = totalMinutes % 60;
    long totalHours = totalMinutes / 60;
    long currentHour = totalHours % 24;
    System.out.println("Current time in GMT is H: " + currentHour + " M: " + currentMinute + " S: " + currentSecond);
  }
}
