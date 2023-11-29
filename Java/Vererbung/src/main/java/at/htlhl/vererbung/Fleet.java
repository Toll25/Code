package at.htlhl.vererbung;

public class Fleet {

    private Aircraft aircraft;
    private Airplane airplane;
    private Helicopter helicopter;

    public Fleet(){

        System.out.println("Init Aircraft");
        aircraft =new Aircraft();

        System.out.println("Init Airplane");
        airplane = new Airplane();

        System.out.println("Init Helicopter");
        helicopter=new Helicopter();
    }

    public void takeOffAll(){
        aircraft.takeOff();
        airplane.takeOff();
        helicopter.takeOff();
    }

    public void flyAll(){
        aircraft.fly();
        airplane.fly();
        helicopter.fly();
    }

    public void landAll(){
        aircraft.land();
        airplane.land();
        helicopter.land();
    }

    public static void main(String[] args){
        Fleet unitedAirlines =new Fleet();
        unitedAirlines.takeOffAll();
        unitedAirlines.flyAll();
        unitedAirlines.landAll();
    }
}
