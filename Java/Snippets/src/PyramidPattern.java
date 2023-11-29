import java.util.Scanner;

public class PyramidPattern {
    private static void drawSimplePyramid(int input) {
        for (int i = 1; i <= input; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    private static void drawMirroredPyramid(int input) {
        for (int i = 1; i <= input; i++) {
            for (int j = input; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    private static void drawSymmetricPyramid(int input) {
        for (int i = 1; i <= input; i++) {
            for (int j = input; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k < i; k++) {
                System.out.print("*");
            }

            System.out.print("*");

            for (int k = 1; k < i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        System.out.println("Please enter a number:");
        Scanner scan = new Scanner(System.in);
        int input = scan.nextInt();

        drawSimplePyramid(input);
        drawMirroredPyramid(input);
        drawSymmetricPyramid(input);

    }
}
