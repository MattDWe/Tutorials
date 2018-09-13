// Testing arraylist

import java.util.ArrayList;

public class TestArrayList{
  public static void main(String[] args){
    ArrayList<String> cityList = new ArrayList<>();
    cityList.add("London");
    cityList.add("Denver");
    cityList.add("Miami");
    System.out.println("List size? " + cityList.size());
    System.out.println("Is Miami in the list? " + cityList.contains("Miami"));
    System.out.println("Is the list empty? " + cityList.isEmpty());
    System.out.println(cityList.toString());
  }
}
