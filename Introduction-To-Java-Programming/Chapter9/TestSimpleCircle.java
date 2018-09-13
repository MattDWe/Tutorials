// Simple example demonstrating classes

public class TestSimpleCircle{
  public static void main(String[] args){
    SimpleCircle circle1 = new SimpleCircle();
    System.out.println("Area of R: " + circle1.getRadius() + " is " + circle1.getArea());
    SimpleCircle circle2 = new SimpleCircle(25);
    System.out.println("Area of R: " + circle2.getRadius() + " is " + circle2.getArea());
    circle2.setRadius(100);
    System.out.println("Area of R: " + circle2.getRadius() + " is " + circle2.getArea());
  }
}

class SimpleCircle{
  private double radius; // Adding private makes so circle.radius will not give radius
  SimpleCircle(){
    radius = 1;
  }
  SimpleCircle(double newRadius){
    radius = newRadius;
  }
  double getArea(){
    return radius*radius*Math.PI;
  }
  void setRadius(double newRadius){
    radius = newRadius;
  }
  double getRadius(){
    return radius;
  }
}
