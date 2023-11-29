public class Main {

   // Aufgabenstellung:
   // Ergänze die System.out.println() mit den entsprechenden int-Werten
   public static void main(String[] args) {
      IntWrapper a = new IntWrapper(30);
      IntWrapper b = new IntWrapper(45);
      // Werte a.a und b.a bevor die Methode aufgerufen wurde
      System.out.println("a.a=" + /* TODO 1 add int value for a.a */ + ", b.a=" + /* TODO 2 add int value for b.a */);
      swapFunction(a, b);
      // Werte a.a und b.a, nachdem die Methode aufgerufen wurde
      System.out.println("a.a=" + /* TODO 3 add int value for a.a */ + ", b.a=" + /* TODO 4 add int value for b.a */);
   }
   public static void swapFunction(IntWrapper a, IntWrapper b) {
      IntWrapper c = new IntWrapper(a.a);
      a.a = b.a;
      b.a = c.a;
   }
}