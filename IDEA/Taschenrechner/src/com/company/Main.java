//Paul Hösch 20.11.2020 einfacher Taschenrechner
package com.company;

public class Main {

    public static void main(String[] args) {
        var scan = new java.util.Scanner(System.in);
        int zahl1, zahl2, erg = 0;
        char rz;

        System.out.print("Bitte 1.Zahl eingeben");
        zahl1 = scan.nextInt();
        System.out.print("Bitte 2.Zahl eingeben");
        zahl2 = scan.nextInt();
        System.out.print("Bitte Rechenzeichen eingeben");
        rz = scan.next().charAt(0);

        if ((rz == '+') || (rz == 'a')) {
            erg = zahl1 + zahl2;
        } else if ((rz == '-') || (rz == 's')) {
            erg = zahl1 - zahl2;
        } else if ((rz == '*') || (rz == 'm')) {
            erg = zahl1 * zahl2;
        } else if ((rz == '/') || (rz == 'd')) {
            erg = zahl1 / zahl2;
        } else {
            System.out.println("Falsches Rechenzeichen!");
        }

        System.out.println("Ergebnis:" + zahl1 + rz + zahl2 + " = " + erg);
    }
}