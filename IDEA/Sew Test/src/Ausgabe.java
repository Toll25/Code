
import java.util.ArrayList;

public class Ausgabe {
    protected float betrag;

    public float getBetrag() {
        return betrag;
    }

    public static void fill(ArrayList<AusgabeSt> ausgabeStArrayList){
        for(float i =200f; i<=900f;i=i+100f)
            ausgabeStArrayList.add(new AusgabeSt(i));
    }

    public static void print(ArrayList<AusgabeSt> ausgabeStArrayList){
        for(AusgabeSt i:ausgabeStArrayList)
            System.out.println("Betrag: " + i.getBetrag() + " | Steuerbetrag: " + i.getSteuer());
    }
}
