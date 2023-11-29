package at.htlhl;

public class Main {
    public static void main(String[] args) {
        int rownumber = 5;

        for (int row = 0; row < rownumber; row++) {
            for (int j = row + 1; j < rownumber; j++) {
                System.out.print("#");
            }
            for (int k = rownumber; k >= row; k--) {
                System.out.print("+");
            }
            System.out.println();
        }
    }
}