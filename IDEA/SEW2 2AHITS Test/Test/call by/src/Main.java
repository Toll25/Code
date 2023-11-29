public class Main {
    public static void main(String[] args) {
        Example example = new Example();
        System.out.println("1st: " + example.a + "/" + example.b);
        example.call(example);
        System.out.println("2nd: " + example.a + "/" + example.b);
    }
}
class Example {
    public int a = 10;
    public int b = 30;

    public void call(Example ex) {
        ex.a = ex.a + 10;
    }
}