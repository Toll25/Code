package com.company;

public class Tree {
    private int size;
    private char character;
    private Decoration decoration;

    public Tree(int size) {
        this.size = size;
    }

    public Tree(int size, char character) {
        this.size = size;
        this.character = character;
    }

    public Tree(int size, char character, Decoration decoration) {
        this.size = size;
        this.character = character;
        this.decoration = decoration;
    }

    private int getCharCount() {
        int sum = 0;
        for (int i = 1; i <= this.size; i++) {
            sum += i;
        }
        return sum;
    }

    private boolean isNumTree() {
        return this.character == '\u0000';
    }

    public boolean isChristmasTree() {
        return decoration.getFrequency() > 0;
    }

    public void draw() {
        System.out.println();
        for (int i = 1; i <= this.size; i++) {
            for (int k = 1; k <= (this.size - 1) - i + 1; k++) {
                System.out.print(" ");
            }
            int num = 1;
            for (int j = 1; j <= i; j++) {
                if (decoration.getFrequency() > 0 && (j % decoration.getFrequency()) == 0) {
                    System.out.print(decoration.getCharacter() + " ");
                } else {
                    if (isNumTree()) {
                        System.out.print(num + " ");
                    } else {
                        System.out.print(this.character + " ");
                    }
                }
                num++;
            }
            System.out.println();
        }
    }

    @Override
    public String toString() {
        String result = "";
        if (isNumTree()) {
            result += "This number-tree has " + getCharCount() + " characters.";
        } else {
            result += "This " + this.character + "-tree has " + getCharCount() + " characters.";
        }
        if (isChristmasTree()) {
            result += " And it's a Christmas Tree!!";
        }
        return result;
    }

}