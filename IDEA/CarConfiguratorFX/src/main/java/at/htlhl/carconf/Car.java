package at.htlhl.carconf;

import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class Car {

    //Constants ***************************************************************

    public static final int MAX_POWER = 200;
    public static final int MAX_RANGE = 1000;

    //Fields ***********************************************

    //Bei Properties kein GET verwenden!!!
    //private String manufacturer;
    private StringProperty manufacturerProperty = new SimpleStringProperty(this, "manufacturer");

    //type, power, range

    private StringProperty typeProperty = new SimpleStringProperty(this, "type");

    private IntegerProperty powerProperty = new SimpleIntegerProperty(this, "power");

    private IntegerProperty rangeProperty = new SimpleIntegerProperty(this, "range");

    // Instance creation ***********************************

    public Car(){

    }

    //Accessors ********************************************

    //Manufacturer
    public String getManufacturer() {
        return manufacturerProperty.get();
    }

    public void setManufacturer(String manufacturer) {
        manufacturerProperty.set(manufacturer);
    }

    public StringProperty manufacturerProperty(){
        return manufacturerProperty;
    }

    //Type
    public String getType(){
        return typeProperty.get();
    }

    public void setType(String type){
        typeProperty.set(type);
    }

    public StringProperty typeProperty(){
        return typeProperty;
    }

    //Power
    public int getPower() {
        return powerProperty.get();
    }

    public void setPower(int power) {
        if (power > MAX_POWER) {
            powerProperty.set(MAX_POWER);
        } else {
            powerProperty.set(power);
        }
    }

    public IntegerProperty powerProperty(){
        return powerProperty;
    }

    //Range
    public int getRange(){
        return rangeProperty.get();
    }

    public void setRange(int range){
        rangeProperty.set(range);
    }

    public IntegerProperty rangeProperty(){
        return rangeProperty;
    }
}