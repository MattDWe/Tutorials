// Test GeometricObject with abstract methods

public class TestGeometricObj{
  public static void main(String[] args){
    Circle c = new Circle(5);
    System.out.println(c.toString());
  }
}

/*  Notes about abstract classes
Abstract methods cannot be contained in an nonabstract class
Objects cannot be created from an abstract class*/
