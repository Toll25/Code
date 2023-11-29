package com.company;

import java.io.BufferedReader;
import java.io.FileReader;

public class Main {

    public static void main(String[] args) throws java.io.IOException {
        var scan=new java.util.Scanner(System.in);

        String arr= scan.nextLine();

      /*
        System.out.println("Bitte anzahl der Zahlen eingeben");
        int n=scan.nextInt();
        int[] arr=new int[n];
        System.out.println("Bitte Zahlen eingeben");
        for(int i=0;i<n;i++)
            arr[i]=scan.nextInt();
    */

        var fileName = java.nio.file.Paths.get("zeug.txt");
        var writeZahlen = java.nio.file.Files.newBufferedWriter(fileName);

        writeZahlen.write(arr + "\n");

        for (final int zahl : arr) {
            writeZahlen.write(zahl + "\n");
        }

        writeZahlen.close();

        File fil = new File("zeug.txt");
        FileReader inputFil = new FileReader(fil);
        BufferedReader in = new BufferedReader(inputFil);

        BufferedReader br = new BufferedReader(new FileReader("zeug.txt"));
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
    }
}
