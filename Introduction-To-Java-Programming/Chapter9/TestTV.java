// Testing TV.java controller

public class TestTV{
  public static void main(String[] args){
    TV tv = new TV();
    tv.turnOn();
    tv.setChannel(30);
    tv.volumeUp();
    System.out.println("Is TV on? " + tv.on);
    System.out.println("What Channel? " + tv.channel);
    System.out.println("Volume? " + tv.volume);
  }
}
