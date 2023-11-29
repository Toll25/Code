public class ChessRice {
    public static void main(String[] args) {
        long reis = 1, reissum = 0, temp;
        int feld, start = 0, end = 63, i = 0;
        long[] reise = new long[64];

        System.out.println("Reiskörner auf einem Schachbrett");
        for (feld = 64; feld >= 1; feld--) {
            reise[i] = reis;
            reis *= 2;
            reissum += reis;
            i++;
        }
        while (start < end) {
            temp = reise[start];
            reise[start] = reise[end];
            reise[end] = temp;
            start++;
            end--;
        }
        for (long j : reise) {
            System.out.println(Long.toUnsignedString(j));
        }
        System.out.println(" ");
        System.out.println("Reiskörner insgesamt: " + Long.toUnsignedString(reissum));
    }
}
