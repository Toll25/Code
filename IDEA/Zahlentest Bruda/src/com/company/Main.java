//Paul Hösch 1AHITS 4.12.2020 ZahlenTest
package com.company;

public class Main {

    public static void main(String[] args) {
        var scan = new java.util.Scanner(System.in);
        char wh;
        int zahl;

        do {
            System.out.println("Bitte Zahl eingeben");
            zahl = scan.nextInt();
            if (zahl != 0) {
                if (zahl < 0) {
                    System.out.println("Zahl ist negativ");
                } else {
                    System.out.println("Zahl ist positiv");
                }
                if (zahl % 2 == 0) {
                    System.out.println("Zahl ist gerade");
                } else {
                    System.out.println("Zahl ist ungerade");
                }
            } else {
                System.out.println("Zahl ist 0");
            }

            do {
                System.out.print("Wollen Sie wiederholen? (J/N)");
                wh = scan.next().charAt(0);
            } while (!((wh == 'J') || (wh == 'j') || (wh == 'n') || (wh == 'N')));
        } while ((wh == 'J') || (wh == 'j'));
    }
}
