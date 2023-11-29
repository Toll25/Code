package com.company;

public class Main {

    public static void main(String[] args) {
        var scan = new java.util.Scanner(System.in);
        int eingabe;

        System.out.println("Bitte eine Zahl im Dezimalen Zahlensystem eingeben");
        eingabe = scan.nextInt();
        String binZahl = Integer.toHexString(eingabe);
        System.out.println(binZahl);
    }
}