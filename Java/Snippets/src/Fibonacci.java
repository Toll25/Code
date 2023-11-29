public class Fibonacci {
    public static void main(String[] args) {
        for(long i=1;i<=100;i++){
            System.out.println(fib(i));
        }
    }

    public static long fib(long n){
        if(n==1){
            return 1;
        }else if(n==2) {
            return 1;
        }else{
            return  fib(n-1) + fib(n-2);
        }
    }
}
