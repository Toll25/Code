package at.htlhl.vererbung;

public class Helicopter extends Aircraft implements Rentable{
    private float rotorBladeSize;

    public Helicopter(){
        rotorBladeSize=8.3f;
    }

    @Override
    public void takeOff(){
        System.out.println("A helicopter is taking off");
    }

    @Override
    public void fly() {
        System.out.println("A helicopter is flying");
    }

    @Override
    public void land(){
        System.out.println("A helicopter is landing");
    }

    @Override
    public boolean isRentable() {
        System.out.println("A helicopter is not rentable");
        return false;
    }
}
