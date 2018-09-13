// Testing static variables

public class TestCircleStatic{
  public static void main(String[] args){
    System.out.println("Before creating objects");
    System.out.println("The number of Circle objects is " + CircleStaticMembers.numberOfObjects);
    CircleStaticMembers c1 = new CircleStaticMembers();
    System.out.println("After creating objects");
    System.out.println("The number of Circle objects is " + CircleStaticMembers.numberOfObjects);
    CircleStaticMembers c2 = new CircleStaticMembers();
    CircleStaticMembers c3 = new CircleStaticMembers();
    System.out.println("After creating more objects");
    System.out.println("The number of Circle objects is " + CircleStaticMembers.numberOfObjects);
  }
}
