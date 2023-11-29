package at.htlhl.vererbung;

public abstract class Aircraft {
    protected float speed;
    protected float altitude;

    public Aircraft() {
        speed=0.0f;
        altitude=0.0f;
    }

    public abstract void takeOff();

    public abstract void fly();

    public abstract void land();
}