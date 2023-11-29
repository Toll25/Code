import java.util.Scanner;

public class DiamondPattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter number of lines:");

        int input = scanner.nextInt();
        System.out.println("Diamond:");

        for (int line = 1; line <= input; line++) {
            for (int space = input; space > line; space--) {
                System.out.print(" ");
            }
            for (int star = 1; star <= (line * 2) - 1; star++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int line = input - 1; line >= 1; line--) {
            // Print space in increasing order
            for (int space = input - 1; space >= line; space--) {
                System.out.print(" ");
            }
            // Print star in decreasing order
            for (int star = 1; star <= (line * 2) - 1; star++) {
                System.out.print("*");
            }

            System.out.println();
        }
        scanner.close();
    }
}
