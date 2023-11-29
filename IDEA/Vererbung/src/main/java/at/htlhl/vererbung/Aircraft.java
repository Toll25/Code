package at.htlhl.vererbung;

public class Aircraft {
    protected float speed;
    protected float altitude;

    public Aircraft() {
        speed=0.0f;
        altitude=0.0f;
    }

    public void takeOff() {
        System.out.println("An aircraft is taking off");
    }

    public void fly() {
        System.out.println("An aircraft is flying");
    }

    public void land() {
        System.out.println("An aircraft is landing");
    }
}