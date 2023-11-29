import java.io.IOException;

public class CharCounting {
    public static void main(String[] args) {

        String text = read();
        int lc = content(text, 'a', 'z');
        int uc = content(text, 'A', 'Z');
        int n = content(text, '1', '9');
        int s = special(text);

        System.out.println("LowerCase: " + lc + "\n" + "UpperCase: " + uc + "\n" + "Numbers: " + n + "\n" + "Special: " + s);
        try {
            writer(lc, uc, n, s);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //writing
    public static void writer(int lc, int uc, int n, int s) throws IOException {
        var fileName = java.nio.file.Paths.get("zeug.txt");
        var write = java.nio.file.Files.newBufferedWriter(fileName);
        write.write("Anzahl Kleinbuchstaben: " + lc + "\n");
        write.write("Anzahl Großbuchstaben: " + uc + "\n");
        write.write("Anzahl Ziffern: " + n + "\n");
        write.write("Restliche Symbole: " + s + "\n");
        write.close();
    }

    //counting
    public static int content(String text, char first, char second) {
        int c = 0;
        for (int i = 0; i < text.length(); i++)
            if (text.charAt(i) >= first && text.charAt(i) <= second)
                c++;
        return c;
    }

    //special character counting
    public static int special(String text) {
        return text.length() - content(text, 'a', 'z') - content(text, 'A', 'Z') - content(text, '1', '9');
    }

    //reading
    public static String read() {
        var scan = new java.util.Scanner(System.in);
        System.out.println("Please enter text");
        return scan.nextLine();
    }
}
