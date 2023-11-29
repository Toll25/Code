package at.htlhl.vererbung;

import java.util.ArrayList;
import java.util.List;

public class FleetV2 {

    private List<Aircraft> aircraftList;

    public FleetV2(){

        aircraftList= new ArrayList<>();
        System.out.println("Init Aircraft");
        //aircraft=new Aircraft();

        System.out.println("Init Airplane 1");
        aircraftList.add(new Airplane());

        System.out.println("Init Helicopter");
        aircraftList.add(new Helicopter());

        System.out.println("Init Airplane 2");
        aircraftList.add(new Airplane());
    }

    public void takeOffAll(){
        for (Aircraft i : aircraftList){
            i.takeOff();
        }
    }

    public void flyAll(){
        for (Aircraft i : aircraftList){
            i.fly();
        }
    }

    public void landAll(){
        for (Aircraft i : aircraftList){
            i.land();
        }
    }

    public static void main(String[] args){
        FleetV2 unitedAirlines =new FleetV2();
        unitedAirlines.takeOffAll();
        unitedAirlines.flyAll();
        unitedAirlines.landAll();
    }
}
