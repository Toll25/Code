package at.htlhl.vererbung;

public class Airplane extends Aircraft implements Rentable {
    private float wingSpan;

    public Airplane(){

    }

    public float getWingSpan() {
        return wingSpan;
    }

    public void setWingSpan(float wingSpan) {
        this.wingSpan = wingSpan;
    }

    @Override
    public void takeOff(){
        System.out.println("An airplane is taking off");
    }

    @Override
    public void fly() {
        System.out.println("An airplane is flying");
    }

    @Override
    public void land() {
        System.out.println("An airplane is landing");
    }

    @Override
    public boolean isRentable() {
        System.out.println("An airplane is rentable");
        return true;
    }
}
