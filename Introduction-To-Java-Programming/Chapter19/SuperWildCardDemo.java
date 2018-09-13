public class SuperWildCardDemo{
  public static void main(String[] args){
    GenericStack<Object> stack = new GenericStack<>();
    stack.push("Java");
    stack.push(2);
    stack.push('A');
    System.out.println(stack.toString());
  }
}
