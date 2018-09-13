// Testing usage of static variables
// Static variables are universal variables between all objects of same class

public class CircleStaticMembers{
  double radius;
  static int numberOfObjects = 0;
  CircleStaticMembers(){
    radius = 1;
    numberOfObjects++;
  }
  CircleStaticMembers(double newRadius){
    radius = newRadius;
    numberOfObjects++;
  }
  static int getNumberOfObjects(){
    return numberOfObjects;
  }
  double getArea(){
    return radius*radius*Math.PI;
  }
}
