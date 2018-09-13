// To Write to a text file do
// PrintWriter output = new PrintWriter("Temp.txt");
// output.print("java 101");
// output.close();
// Or to gain input from the text file
// Scanner input = new Scanner(new File("temp.txt"));
// System.out.println(input.nextLine());


// Using File input/output it is for reading/writing bytes into or from files
import java.io.*;

public class TestFileStream{
  public static void main(String[] args) throws IOException{
    try (
    FileOutputStream output = new FileOutputStream("temp.dat");
    ) {
      for (int i = 1; i <= 10; i++){
        output.write(i);
      }
    }
    try (
    FileInputStream input = new FileInputStream("temp.dat");
    ) {
      int value;
      while ((value = input.read()) != -1){
        System.out.print(value + " ");
      }
    }
  }
}

// Using try and the streams cleate an auto closable file so closing isn't needed
