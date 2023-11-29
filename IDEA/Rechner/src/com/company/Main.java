package com.company;

public class Main {

    public static void main(String[] args) {
        var scan=new java.util.Scanner (System.in);
        int zahl1, zahl2, erg;
        System.out.print("Bitte 1.Zahl eingeben");
        zahl1=scan.nextInt();
        System.out.print("Bitte 2.Zahl eingeben");
        zahl2=scan.nextInt();
        erg=zahl1+zahl2;
        System.out.println ("Ergebnis:"+zahl1+"+"+zahl2+"="+erg);
    }
}