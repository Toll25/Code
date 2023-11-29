public class Main {
   public static void main(String[] args) {
      int[][] array = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
      
      // Berechne die Summe jeder "Zeile" des Arrays vervollständige den Code so,
      // dass die angeführte Ausgabe erzeugt wird:

      for (int[] sums : array) {
         System.out.print("Sum [");
         int sum = 0;
         for (int i : sums) {
            System.out.print(" "+i);
            sum += i;

         }
         System.out.println(" ] = " + sum);
      }
   }
}