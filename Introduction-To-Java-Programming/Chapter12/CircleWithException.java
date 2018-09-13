// Using circle class with an exception

import java.util.*;

public class CircleWithException{
  private double radius;
  private static int numberOfObjects = 0;

  public CircleWithException(){
    this(1.0);
  }
  public CircleWithException(double newRadius){
    setRadius(newRadius);
    numberOfObjects++;
  }
  public double getRadius(){
    return radius;
  }
  public void setRadius(double newRadius)
    throws IllegalArgumentException {
    if (newRadius >= 0){
      radius = newRadius;
    }
    else{
      throw new IllegalArgumentException("Radius cannot be negative.");
    }
    this.radius = radius;
  }
  public static int getNumberOfObjects(){
    return numberOfObjects;
  }
}

// You can create your own exceptions by creating a class for it extending exception
