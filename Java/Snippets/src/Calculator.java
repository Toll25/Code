public class Calculator {
    public static void main(String[] args) {
        var eingabe = new java.util.Scanner(System.in);
        char wh;
        do {
            var scan = new java.util.Scanner(System.in);
            int zahl1, zahl2, erg = 0;
            char rz;

            System.out.print("Bitte 1. Zahl eingeben");
            zahl1 = scan.nextInt();
            System.out.print("Bitte 2. Zahl eingeben");
            zahl2 = scan.nextInt();
            System.out.print("Bitte Rechenzeichen eingeben");
            rz = scan.next().charAt(0);

            switch (rz) {
                case '+', 'a' -> {
                    erg = zahl1 + zahl2;
                }
                case '-', 's' -> {
                    erg = zahl1 - zahl2;
                }
                case '*', 'm' -> {
                    erg = zahl1 * zahl2;
                }
                case '/', 'd' -> {
                    if (zahl2 == 0) {
                        System.out.print("Division durch 0 nicht definiert!");
                    } else {
                        erg = zahl1 / zahl2;
                    }
                }
                default -> System.out.println("Falsches Rechenzeichen");

            }

            if (zahl2 == 0) {
            } else {
                System.out.println("Ergebnis: " + zahl1 + rz + zahl2 + " = " + erg);
            }

            System.out.print("Wollen Sie wiederholen (J/N)");
            wh = eingabe.next().charAt(0);
        } while ((wh == 'J') || (wh == 'j'));
        if ((wh == 'N') || (wh == 'n')) {
            System.out.println("Programm Beendet");
        } else System.out.println("Bitte Ja oder Nein antworten");
        while((wh != 'J') || (wh != 'j')||(wh != 'N') || (wh != 'n'));
    }
}
