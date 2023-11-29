package at.htlhl;
import java.util.Scanner;

public class SchleifenDemo {
    private static void drawSimplePyramid(int input){
        for(int i=1; i<=input; i++){
            for(int j=1; j<=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    private static void drawMirroredPyramid(int input){
        for(int i=1; i<=input; i++){
            for(int j=input; j>i; j--){
                System.out.print(" ");
            }
            for(int k=1; k<=i; k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    private static void drawSymmetricPyramid(int input){
        for(int i=1; i<=input; i++){
            for(int j=input; j>i; j--){
                System.out.print(" ");
            }
            for(int k=1; k<i; k++){
                System.out.print("*");
            }

            System.out.print("*");

            for(int k=1; k<i; k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        System.out.println("Please enter a number:");
        Scanner scan = new Scanner(System.in);
        int input=scan.nextInt();


        drawSimplePyramid(input);
        drawMirroredPyramid(input);
        drawSymmetricPyramid(input);




        System.out.println("ich weiß nicht was ich hier schreiben sollen my name is walter hartwell white, i live at 308 negra arroy lane alberquerque new mexico, this is my confesion");
    }
}