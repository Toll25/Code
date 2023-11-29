public class Main {
   public static void main(String[] args) {
      int[][] square = new int[4][4];
      
      // Befülle das Array entsprechend dem angegebenen Muster: 
square[0][3]= 4;
      square[1][2]= 3;
      square[2][1]= 2;
      square[3][0]=1;
      // Durchlaufe das 2dimensionale Array und gib die Werte entsprechend dem angegebenen Muster aus:
for (int[] squares:square){
   for (int i:squares){
      System.out.print(i+ " ");
   }
   System.out.println();
}
   }
}