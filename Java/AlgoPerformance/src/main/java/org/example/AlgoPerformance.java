package org.example;

public class AlgoPerformance {

    public static final int N = 8;

    public AlgoPerformance(){
        constantRuntime(N);
        logarithmicRuntime(N);
        linearRuntime(N);
    }

    /**
     * The code takes a constant amount of time to run.
     * It's not dependent on the site of n
     * <p>
     * O(1)
     * @param n
     */
    private void constantRuntime(int n){
        System.out.println("Constant Runtime O(1)");
        System.out.println("    The input is: " + n);
        System.out.println();
    }

    /**
     * The running time grows in proportion to the logarithm of n
     * <p>
     * O(log(n))
     * @param n
     */
    private void logarithmicRuntime(int n){
        System.out.println("Logarithmic Runtime O(log(n))");
        System.out.println("    The input is: " + n);
        for (int i=1; i < n ; i=i*2){
            System.out.println("    Busy looking at: " + i);
        }
        System.out.println();
    }

    /**
     * The running time grows linearly compared to n
     * <p>
     * O(n)
     * @param n
     */
    private void linearRuntime(int n){
        System.out.println("Linear Runtime O(log(n))");
        System.out.println("    The input is: " + n);
        for (int i=1; i < n ; i++){
            System.out.println("    Busy looking at: " + i);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        new AlgoPerformance();
    }
}