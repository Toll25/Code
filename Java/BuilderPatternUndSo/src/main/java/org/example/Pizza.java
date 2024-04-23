package org.example;

public class Pizza {
    private int price;
    private boolean salami;
    private boolean ham;

    public Pizza(PizzaBuilder pizzaBuilder){
        this.price=pizzaBuilder.price;
        this.salami=pizzaBuilder.salami;
        this.ham=pizzaBuilder.ham;
    }

    @Override
    public String toString(){
        return "Pizza{price: " + price + ", salami: " + salami + ", ham: " + ham + "}";
    }

    static class PizzaBuilder{
        private int price;
        private boolean salami;
        private boolean ham;

        public PizzaBuilder(int price){
            this.price=price;
        }

        public PizzaBuilder setSalami(boolean salami){
            this.salami=salami;
            return this;
        }

        public PizzaBuilder setHam(boolean ham){
            this.ham=ham;
            return this;
        }

        public Pizza build(){
            return new Pizza(this);
        }

    }
}
