package at.htlhl.vererbung;

import java.util.ArrayList;

public class Rental {

    private ArrayList<Rentable> rentableList;

    public Rental(){
        rentableList=new ArrayList<>();
        rentableList.add(new Airplane());
        rentableList.add(new Helicopter());
        rentableList.add(new Bike());

        checkRentability();
    }

    private void checkRentability(){
        for(Rentable rentable:rentableList){
            rentable.isRentable();
        }
    }

    public static void main(String[] args){
        new Rental();
    }
}
