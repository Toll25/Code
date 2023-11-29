public class Main {
   public static void main(String[] args) {
      boolean[][] bools = {
              {true, true, true, true},
              {true, true, true, false},
              {true, false, false, true},
              {true, false, true, true},
              {false, false, true, true} };
      
      // Werte anpassen:

      // Array durchlaufen. Gib für true ein X und für false 0 aus.
       for (boolean[] bool : bools) {
           for (boolean b : bool) {
               if (b) {
                   System.out.print("X  ");
               } else {
                   System.out.print("0  ");
               }
           }
           System.out.println();
       }
}

}