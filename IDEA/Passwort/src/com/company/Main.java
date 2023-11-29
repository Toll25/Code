package com.company;

public class Main {

    public static void main(String[] args) {
        boolean passt = true;
        var scan = new java.util.Scanner(System.in);
        System.out.println("Account anlegen");
        System.out.println("Username: noobslayer69");
        System.out.print("Passwort: ");
        do {
            String pass = scan.nextLine();

            int klein = 0, gross = 0, ziff = 0, sond = 0;

            for (int j = 0; j < pass.length(); j++) {
                if (pass.charAt(j) >= 'a' && pass.charAt(j) <= 'z')
                    klein++;
                if (pass.charAt(j) >= 'A' && pass.charAt(j) <= 'Z')
                    gross++;
                if (pass.charAt(j) >= '0' && pass.charAt(j) <= '9')
                    ziff++;
                if (pass.charAt(j) == '!')
                    sond++;
                if (pass.charAt(j) == '?')
                    sond++;
            }
            if (pass.length() < 8)
                System.out.println("Zu wenige Zeichen");
            if (gross < 1)
                System.out.println("Zu wenige Großbuchstaben");
            if (klein < 1)
                System.out.println("Zu wenige Kleinbuchstaben");
            if (sond < 1)
                System.out.println("Zu wenige Sonderzeichen");
            if (ziff < 1)
                System.out.println("Zu wenige Ziffern");
            if (pass.length() >= 8 && gross >= 1 && klein >= 1 && sond >= 1 && ziff >= 1)
                System.out.println("Passwort passt");
            else {
                passt = false;
                System.out.println();
                System.out.print("Ein passendes Passwort eingeben: ");
            }
        } while (!passt);
    }
}