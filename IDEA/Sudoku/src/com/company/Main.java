package com.company;

import java.util.stream.IntStream;

public class Main {
    private static final int NO_VALUE = 0;
    private static final int MIN_VALUE = 1;
    private static final int MAX_VALUE = 9;
    private static final int BOARD_SIZE = 9;
    private static final int SECTION_SIZE = 3;
    private static final int BOARD_START_INDEX = 0;

    public static void main(String[] args) {
        int[][] board = {
                {3, 0, 2, 0, 0, 7, 9, 4, 0},
                {4, 0, 5, 9, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 4, 5, 0, 0},
                {8, 9, 0, 0, 0, 2, 0, 0, 0},
                {0, 2, 7, 0, 8, 1, 0, 6, 9},
                {1, 6, 3, 0, 5, 9, 0, 0, 7},
                {7, 0, 8, 0, 0, 0, 0, 0, 2},
                {2, 0, 9, 6, 7, 3, 0, 1, 0},
                {0, 5, 0, 2, 0, 0, 0, 0, 4}
        };

        solve(board);


        for (int[] ints : board) {
            for (int anInt : ints) {
                System.out.print(anInt + " | ");
            }
            System.out.println();
            System.out.println("-----------------------------------");
        }




        /*
        int[][] board = new int[9][9];
        for (int row = 0; row < board.length; row++) {
            System.out.println("Geben sie die erste Reihe ein: ");
            String temp = scan.nextLine();
            String[] temp2 = temp.split(",");
            for (int i = 0; i < temp2.length; i++) {
                board[row][i] = Integer.parseInt(temp2[i]);
            }
        }
        for (int[] ints : board) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
        */

    }


    private static boolean solve(int[][] board) {
        for (int row = BOARD_START_INDEX; row < board.length; row++) {
            for (int col = BOARD_START_INDEX; col < board[row].length; col++) {
                if (board[row][col] == NO_VALUE) {
                    for (int i = MIN_VALUE; i <= MAX_VALUE; i++) {
                        board[row][col] = i;
                        if (isValid(board, row, col) && solve(board))
                            return true;
                        board[row][col] = NO_VALUE;
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isValid(int[][] board, int row, int col) {
        return rowCheck(board, row) &&
                colCheck(board, col) &&
                sectionCheck(board, row, col);
    }

    private static boolean rowCheck(int[][] board, int row) {
        boolean[] con = new boolean[BOARD_SIZE];
        return IntStream.range(BOARD_START_INDEX, BOARD_SIZE).allMatch(col -> check(board, row, con, col));
    }

    private static boolean colCheck(int[][] board, int col) {
        boolean[] con = new boolean[BOARD_SIZE];
        return IntStream.range(BOARD_START_INDEX, BOARD_SIZE).allMatch(row -> check(board, row, con, col));
    }

    private static boolean sectionCheck(int[][] board, int row, int column) {
        boolean[] constraint = new boolean[BOARD_SIZE];
        int subsectionRowStart = (row / SECTION_SIZE) * SECTION_SIZE;
        int subsectionRowEnd = subsectionRowStart + SECTION_SIZE;

        int subsectionColumnStart = (column / SECTION_SIZE) * SECTION_SIZE;
        int subsectionColumnEnd = subsectionColumnStart + SECTION_SIZE;

        for (int r = subsectionRowStart; r < subsectionRowEnd; r++) {
            for (int c = subsectionColumnStart; c < subsectionColumnEnd; c++) {
                if (!check(board, r, constraint, c)) return false;
            }
        }
        return true;
    }

    private static boolean check(int[][] board, int row, boolean[] con, int col) {
        if (board[row][col] != NO_VALUE) {
            if (!con[board[row][col] - 1]) {
                con[board[row][col] - 1] = true;
            } else {
                return false;
            }
        }
        return true;
    }

}
