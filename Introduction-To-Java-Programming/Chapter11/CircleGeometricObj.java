public class CircleGeometricObj extends GeometricObject{
  private double radius;
  public CircleGeometricObj(){
  }
  public CircleGeometricObj(double radius){
    this.radius = radius;
  }
  public CircleGeometricObj(double radius, String color, boolean filled){
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
  public double getDiameter(){
    return 2 * radius;
  }
  public void printCircle(){
    System.out.println("The circle was created on " + getDateCreated() + " and the radius is " + radius);
  }
  public String toString(){ // Example of overriding
    return super.toString() + "\nradius is " + radius;
  }
}

// Cool thing to note is if the super() is not included it will
// run itself before the following code in the instructor
