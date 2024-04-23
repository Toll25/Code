package org.example;

public class Main {
    public static void main(String[] args) {
        Pizza pizza = new Pizza.PizzaBuilder(5).setHam(false).build();
        System.out.println(pizza);
    }
}

