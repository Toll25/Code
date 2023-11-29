package com.company;

public class Main {

    public static void main(String[] args) {
        int[] arr = {5, 9, 1, 7, 6};
        int l, i, ii, temp;
        boolean swap = false;

        l = arr.length;
        do {
                    if (arr[ii] > arr[ii + 1]) {
                        temp = arr[ii];
                        arr[ii] = arr[ii + 1];
                        arr[ii + 1] = temp;
                        swap = true;
                    }
        }while (swap&&ii>0);
        for (int j : arr) {
            System.out.println(j);
        }
    }
}