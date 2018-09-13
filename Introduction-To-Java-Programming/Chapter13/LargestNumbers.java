import java.util.ArrayList;
import java.math.*;

public class LargestNumbers{
  public static Number getLargestNumber(ArrayList<Number> list){
    if (list == null || list.size() == 0){
      return null;
    }
    Number number = list.get(0);
    for (int i =1; i < list.size(); i++){
      if (number.doubleValue() < list.get(i).doubleValue()){
        number = list.get(i);
      }
    }
    return number;
  }
  public static void main(String[] args){
    ArrayList<Number> list = new ArrayList<>();
    list.add(45);
    list.add(3445.53);
    list.add(new BigInteger("343243223132131321313"));
    list.add(new BigDecimal("213133.13203203032321313"));
    System.out.println("The largest number is " + getLargestNumber(list));
  }
}
