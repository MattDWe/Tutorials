// Quick Sort
// Algorithm selects an element, called pivot, in the array.
// It divides the array into two parts, so that all the elements
// in the first part are less than or equal to the pivot and all
// elements in the second part are greater than the pivot. The
// quick sort algorithm is then recursively applied to the first part
// and then the second part.

public class QuickSort{
  public static void quickSort(int[] list){
    quickSort(list, 0, list.length - 1);
  }
  public static void quickSort(int[] list, int first, int last){
    if (last > first){
      int pivotIndex = partition(list, first, last);
      quickSort(list, first, pivotIndex - 1);
      quickSort(list, pivotIndex + 1, last);
    }
  }
  public static int partition(int[] list, int first, int last){
    int pivot = list[first];
    int low = first + 1;
    int high = last;

    while (high > low){
      while (low <= high && list[low] <= pivot){
        low++;
      }
      while (low <= high && list[high] > pivot){
        high--;
      }
      if (high > low){
        int temp = list[high];
        list[high] = list[low];
        list[low] = temp;
      }
    }
    while (high > first && list[high] >= pivot){
      high--;
    }
    if (pivot > list[high]){
      list[first] = list[high];
      list[high] = pivot;
      return high;
    } else {
      return first;
    }
  }
  public static void main(String[] args){
    int[] list = {2, 3, 2, 5, 6, 1, -2, 3, 14, 12};
    quickSort(list);
    for (int element: list){
      System.out.print(element + " ");
    }
    System.out.println("");
  }
}
