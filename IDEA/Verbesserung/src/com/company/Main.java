package com.company;

public class Main {

    public static void main(String[] args) {
//Aufgabe 1
       int i;
        for (i = 1000; i >= 100; i--) {
            if (i % 2 == 1) {
                System.out.println(i+" ist eine Ungerade Zahl");
            }
        }
//Aufgabe 2
        int zahl;
        var Scanner = new java.util.Scanner(System.in);
        System.out.println("Bitte eine Zahl eingeben");
        zahl = Scanner.nextInt();
        if (zahl == 0) {
            System.out.println("Zahl ist Null");
        } else if (zahl % 3 == 0) {
            System.out.println(zahl+" ist durch 3 teilbar");
        } else {
            System.out.println(zahl+" ist nicht durch 3 teilbar");
        }
    }
}
