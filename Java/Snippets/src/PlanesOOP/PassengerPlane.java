package PlanesOOP;

public class PassengerPlane {
    private String model;
    private int maxNumberOfPassengers;
    private int currentNumberOfPassengers ;
    private int range;
    private float travelSpeed;


    public PassengerPlane(String model, int maxNumberOfPassengers, int range, float travelSpeed) {
        this.model = model;
        this.maxNumberOfPassengers = maxNumberOfPassengers;
        this.range = range;
        this.travelSpeed = travelSpeed;
    }

    public float getTravelSpeed() {
        return travelSpeed;
    }

    public int getPassengers() {
        return currentNumberOfPassengers;
    }

    public void enterPlane(int passengers)throws IllegalArgumentException{
        if ((this.currentNumberOfPassengers + passengers) <= maxNumberOfPassengers) {
            this.currentNumberOfPassengers += passengers;
        } else {
            throw new IllegalArgumentException("Zu viele Passagiere!");
        }
    }

    public void leavePlane(int passengers) throws IllegalArgumentException {
        if ((this.currentNumberOfPassengers  - passengers) >= 0){
            this.currentNumberOfPassengers  -= passengers;
        }else {
            throw new IllegalArgumentException("Weniger als 0 Passagiere übrig");
        }
    }

    @Override
    public String toString() {
        return "Model: "+model+" , max. Passengers: "+maxNumberOfPassengers+", passengers: "+currentNumberOfPassengers+", travel speed: "+travelSpeed+" and range: "+range;
    }
}