package Thread;

public class Nebenlaeufigkeit {

    public Nebenlaeufigkeit() {
        Thread t1 = new Thread(new CounterRunnable(1));
        t1.start();
        Thread t2 = new Thread(new CounterRunnable(2));
        t2.start();
    }

    public static void main(String[] args) {
        new Nebenlaeufigkeit();
    }
}