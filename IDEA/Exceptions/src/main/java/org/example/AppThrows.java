package org.example;

public class AppThrows {

    public static void main(String[] args) {
        AppThrows appThrows=new AppThrows();
    }

    public AppThrows() {
        try{
            int squared =squareAdvanced(300,2,25);
            System.out.println("Squared: " + squared);
        }catch (IllegalArgumentException ex) {
            System.err.println("Can´t square: " + ex.getMessage());
        }
    }

    protected int squareAdvanced(int value, int lowerBound, int upperBound)
            throws IllegalArgumentException {
        if (value < lowerBound || value > upperBound) {
            throw new IllegalArgumentException("Out of bounds");
        }
        return value * value;
    }
}
