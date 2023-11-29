public class Main {
   // Aufgabenstellung:
   // Ergänze die System.out.println() mit den entsprechenden int-Werten
   public static void main(String[] args){
      int a = 30;
      int b = 45;
      // Werte a und b bevor die Methode aufgerufen wurde
      System.out.println("a=" + /* TODO 1 add int value for a */ + ", b=" + /* TODO 2 add int value for b */);
      swapFunction(a, b);
      // Werte a und b, nachdem die Methode aufgerufen wurde
      System.out.println("a=" + /* TODO 3 add int value for a */ + ", b=" + /* TODO 4 add int value for b */);
   }
   public static void swapFunction(int a, int b) {
      int c = a;
      a = b;
      b = c;
   }
}