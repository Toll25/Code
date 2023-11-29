package Thread;

public class CounterRunnable implements Runnable {

    int runnableId;

    public CounterRunnable(int runnableId) {
        this.runnableId = runnableId;
    }

    @Override
    public void run() {
        int i = 0;
        while (!Thread.currentThread().isInterrupted()) {
            System.out.println("Thread " + runnableId + ": " + i);
            i++;
            try {
                Thread.sleep(generateRandomTime());
            } catch (InterruptedException e) {
                System.err.println("Thread was interrupted: " + e.getMessage());
                Thread.currentThread().interrupt();
            }
        }
    }

    private int generateRandomTime() {
        int min = 300;
        int max = 1500;

        return (int) Math.floor(Math.random() * (max - min + 1) + min);
    }
}
