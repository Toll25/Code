package org.example;

public class Generics {
    public Generics(){
        Pair<Integer, String> pair = new Pair<>();
        pair.doSomething1(15);
        pair.doSomething2("2");
    }

    public static void main(String[] args) {
        new Generics();
    }
}