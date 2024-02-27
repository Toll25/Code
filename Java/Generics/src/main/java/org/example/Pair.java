package org.example;

public class Pair<E extends Number,Z> {

    public void doSomething1(E e) {
        System.out.println("Show first value: " + e);
        System.out.println("Show first class: " + e.getClass());
    }


    public void doSomething2(Z z) {
        System.out.println("Show second value: " + z);
        System.out.println("Show second class: " + z.getClass());
    }

}
