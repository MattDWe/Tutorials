import java.util.*;

public class CountWords{
  public static void main(String[] args){
    String text = "Good morning. Have a good class. Have a good visit. Have Fun!";

    Map<String, Integer> map = new TreeMap<>();

    String[] words = text.split(" ");

    for (int i = 0; i < words.length; i++){
      String key = words[i].toUpperCase();

      if (key.length() > 0) {
        if (!map.containsKey(key)){
          map.put(key, 1);
        }
        else{
          int value = map.get(key);
          value++;
          map.put(key, value);
        }
      }
    }
    Set<Map.Entry<String, Integer>> entrySet = map.entrySet();

    for (Map.Entry<String, Integer> entry: entrySet){
      System.out.println(entry.getValue() + "\t" + entry.getKey());
    }
  }
}
