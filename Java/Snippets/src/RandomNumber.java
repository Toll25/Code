import java.util.Random;

public class RandomNumber {
    public static void main(String[] args) {
        int up=9999;
        int down=-9999;
        System.out.println("Deine JÖ Punkte:");
        Random rand= new Random();
        int i= rand.nextInt
                (up-down)+down;
        System.out.println(i);
    }
}
