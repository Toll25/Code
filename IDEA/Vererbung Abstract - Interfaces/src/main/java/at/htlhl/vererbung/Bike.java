package at.htlhl.vererbung;

public class Bike implements Rentable {
    public Bike(){

    }

    @Override
    public boolean isRentable() {
        System.out.println("A bike is rentable");
        return true;
    }
}
