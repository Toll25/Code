import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<AusgabeSt> ausgabeStArrayList=new ArrayList<>();
        Ausgabe.fill(ausgabeStArrayList);
        Ausgabe.print(ausgabeStArrayList);
    }
}