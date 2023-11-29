package at.htlhl.vererbung;

public class Fleet {

    //private Aircraft aircraft;
    private Aircraft airplane1;
    private Aircraft helicopter;
    private Aircraft airplane2;

    public Fleet(){

        System.out.println("Init Aircraft");
        //aircraft=new Aircraft();

        System.out.println("Init Airplane 1");
        airplane1 = new Airplane();

        System.out.println("Init Helicopter");
        helicopter=new Helicopter();

        System.out.println("Init Airplane 2");
        airplane2 = new Airplane();
    }

    public void takeOffAll(){
        airplane1.takeOff();
        helicopter.takeOff();
        airplane2.takeOff();
    }

    public void flyAll(){
        airplane1.fly();
        helicopter.fly();
        airplane2.fly();
    }

    public void landAll(){
        airplane1.land();
        helicopter.land();
        airplane2.land();
    }

    public static void main(String[] args){
        Fleet unitedAirlines =new Fleet();
        unitedAirlines.takeOffAll();
        unitedAirlines.flyAll();
        unitedAirlines.landAll();
    }
}
