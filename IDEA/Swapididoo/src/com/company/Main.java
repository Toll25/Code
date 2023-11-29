package com.company;

public class Main {
    // Aufgabenstellung:
    // Ergänze die System.out.println() mit den entsprechenden int-Werten
    public static void main(String[] args){
        System.out.println(Task.cutFirstCurrency("€100.12,€200.23,€300.99"));
        System.out.println(Task.cutLastCurrency("€100.12,€200.23,€300.99"));
    }
}