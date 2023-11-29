package PlanesOOP;

public class Main {

    public static void main(String[] args) throws java.io.IOException {

        PassengerPlane boeing = new PassengerPlane("Boeing 767-400ER", 255, 10454, 0.80f);

        PassengerPlane airbus = new PassengerPlane("Airbus A340-600", 300, 14630, 0.83f);

            boeingtour(boeing);

            airbustour(airbus);
    }

    public static void boeingtour(PassengerPlane boeing) throws java.io.IOException{
        var fileName = java.nio.file.Paths.get("route_boeing.txt");
        var write = java.nio.file.Files.newBufferedWriter(fileName);
        try {
            //Wien
            boeing.enterPlane(177);
            write.write("Wien takeoff " + boeing + "\n");
            //Zürich
            write.write("Zürich landing " + boeing + "\n");
            boeing.leavePlane(58);
            boeing.enterPlane(89);
            write.write("Zürich takeoff " + boeing + "\n");
            //New York
            write.write("New York landing " + boeing + "\n");
            boeing.leavePlane(208);
            boeing.enterPlane(213);
            write.write("New York takeoff " + boeing + "\n");
            //Zürich
            write.write("Zürich landing " + boeing + "\n");
            boeing.leavePlane(17);
            boeing.enterPlane(59);
            write.write("Zürich take off " + boeing + "\n");
            //Wien
            write.write("Wien landing " + boeing + "\n");
            boeing.leavePlane(255);
        }catch (IllegalArgumentException e){
            e.printStackTrace();
        }
        write.close();
    }

    public static void airbustour(PassengerPlane airbus) throws java.io.IOException{
        var fileName = java.nio.file.Paths.get("route_airbus.txt");
        var write = java.nio.file.Files.newBufferedWriter(fileName);
        try {
            //Wien
            airbus.enterPlane(255);
            write.write("Wien takeoff " + airbus + "\n");
            //Zürich
            write.write("Mailand landing " + airbus + "\n");
            airbus.leavePlane(35);
            airbus.enterPlane(79);
            write.write("Mailand takeoff " + airbus + "\n");
            //New York
            write.write("Rom landing " + airbus + "\n");
            airbus.leavePlane(299);
            airbus.enterPlane(118);
            write.write("Rom takeoff " + airbus + "\n");
            //Zürich
            write.write("Mailand landing " + airbus + "\n");
            airbus.leavePlane(2);
            airbus.enterPlane(184);
            write.write("Mailand take off " + airbus + "\n");
            //Wien
            write.write("Wien landing " + airbus + "\n");
            airbus.leavePlane(300);
        }catch (IllegalArgumentException e){
            e.printStackTrace();
        }
        write.close();
    }
}