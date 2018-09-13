// Insertion sort
// Algorithm sorts a list of values by repeatedly inserting a new element into a sorted sublist until whole list is sorted

public class InsertionSort {
  public static void insertionSort(int[] list){
    for (int i = 1; i < list.length; i++){
      int currentElement = list[i];
      int k;
      for (k = i - 1; k >= 0 && list[k] > currentElement; k--){
        list[k + 1] = list[k];
      }
      list[k + 1] = currentElement;

      for (int element: list){
        System.out.print(element + " ");
      }
      System.out.println("");
    }
  }
  public static void main(String[] args){
    int[] list = {12, 2, 6, 3, 9, 10, 1, 23};
    insertionSort(list);
  }
}
