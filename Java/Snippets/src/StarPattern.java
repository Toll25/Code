public class StarPattern {
    public static void main(String[] args) {
        var scan = new java.util.Scanner(System.in);
        int stern, eingabe;

        do {
            do {
                System.out.println("Bitte eine Zahl zwischen 3 und 9 eingeben");
                eingabe = scan.nextInt();
            } while (!((eingabe == 0) || ((eingabe >= 3) && (eingabe <= 9))));
            if (eingabe != 0) {
//obere Hälfte
                for (stern = 1; stern <= eingabe; stern++) {

                    for (int sb = 1; sb <= eingabe - stern; sb++) {
                        System.out.print("  ");
                    }

                    for (int sl = 1; sl <= stern - 1; sl++) {
                        System.out.print("*");
                        System.out.print(" ");
                    }

                    for (int sr = 1; sr < stern; sr++) {
                        System.out.print("*");
                        System.out.print(" ");
                    }
                    System.out.println("*");
                }
//untere Hälfte
                for (stern = eingabe - 1; stern > 0; stern--) {

                    for (int sb = 1; sb <= eingabe - stern; sb++) {
                        System.out.print("  ");
                    }

                    for (int sl = 1; sl <= stern - 1; sl++) {
                        System.out.print("*");
                        System.out.print(" ");
                    }

                    for (int druck = 1; druck < stern; druck++) {
                        System.out.print("*");
                        System.out.print(" ");
                    }
                    System.out.println("*");
                }
                System.out.println(" ");

            } else {
                System.exit(0);
            }
        } while ((eingabe >= 3) && (eingabe <= 9));

    }
}
