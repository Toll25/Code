public class PrimeNumbers {
    public static void main(String[] args) {
        var sc = new java.util.Scanner(System.in);
        int start, end, count;

        System.out.print("Startnummer: ");
        start = sc.nextInt();

        System.out.print("Endnummer: ");
        end = sc.nextInt();

        System.out.println("Primzahlen zwischen " + start + " und " + end + " sind : ");
        for (int i = start; i <= end; i++) {
            count = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0)
                    count = count + 1;
            }
            if (count == 2)
                System.out.print(i + ", ");
        }
    }
}
