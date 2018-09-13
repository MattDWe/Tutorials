public class Circle extends GeometricObject{
  private double radius;
  public Circle(){
  }
  public Circle(double radius){
    this.radius = radius;
  }
  public Circle(double radius, String color, boolean filled){
    super(color, filled); // Calls the super families constructor
    this.radius = radius;
  }
  public double getRadius(){
    return radius;
  }
  public void setRadius(double radius){
    this.radius = radius;
  }
  public double getArea(){
    return radius * radius * Math.PI;
  }
  public String toString(){
    return super.toString() + "\nradius is " + radius;
  }
}
