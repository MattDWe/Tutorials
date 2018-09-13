// Example of abstract classes
// Simply an abstract class contains abstract methods that are implemented more accurately in a subclass.

import java.util.*;

public abstract class GeometricObject{
  private String color = "white";
  private boolean filled;
  private java.util.Date dateCreated;
  protected GeometricObject(){
    dateCreated = new java.util.Date();
  }
  protected GeometricObject(String color, boolean filled){
    dateCreated = new java.util.Date();
    this.color = color;
    this.filled = filled;
  }
  public String getColor(){
    return color;
  }
  public void setColor(String color){
    this.color = color;
  }
  public boolean isFilled(){
    return filled;
  }
  public void setFilled(boolean filled){
    this.filled = filled;
  }
  public java.util.Date getDateCreated(){
    return dateCreated;
  }
  @Override // For reference will push an error if the below methods are not overrided
  public String toString(){
    return "created on " + dateCreated + " color: " + color + " and filled: " + filled;
  }
  public abstract double getArea();
}
