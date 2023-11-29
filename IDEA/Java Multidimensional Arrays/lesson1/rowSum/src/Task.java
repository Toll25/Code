public class Task {

    public int[] rowSum(int[][] array) {
        // Vervollständige die Zeile zur Erzeugung des Arrays: 
        int[] results = new int[array.length];

        // Berechne die Summe jeder Zeile des obigen Arrays 
        // und speichere die Werte ins `results` Array.
        int point=0;
        for (int[] sums : array) {
            int sum = 0;
            for (int i : sums) {
                sum += i;
            }
            results[point] = sum;
            point++;
        }

        return results;
    }

}