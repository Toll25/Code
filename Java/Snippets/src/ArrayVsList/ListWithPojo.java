package ArrayVsList;

import java.util.ArrayList;

public class ListWithPojo {

    private ArrayList<Subject> subjectList;
    public ListWithPojo(){
        subjectList = new ArrayList<>();
        fillList();

        //Berechnung und Ausgabe der Wochenstundenanzahl:
        System.out.println("Anzahl der Wochenstunden: " + calcTotalWeeklyHours());
        System.out.println("Stundenanzahl von FIMI: "+ calcHoursofTeacher ("FIMI"));
    }

    private void fillList(){
        subjectList.add(new Subject("SYT", "FIMI", 5));
        subjectList.add(new Subject("NWT1", "FIMI", 4));
        subjectList.add(new Subject("BESP", "RIH", 2));
        subjectList.add(new Subject("GGP", "PAUL", 2));
        subjectList.add(new Subject("SEW", "GEI", 3));
        subjectList.add(new Subject("D", "PAUL", 2));
        subjectList.add(new Subject("NW", "SWA", 2));
        subjectList.add(new Subject("ITP2", "ZOG", 5));
        subjectList.add(new Subject("AM", "LAN", 3));
        subjectList.add(new Subject("INSY", "STO", 3));
        subjectList.add(new Subject("E", "HAID", 2));
        subjectList.add(new Subject("MEDT", "FICI,CH", 2));
        subjectList.add(new Subject("RK", "FAST", 2));
    }

    private int calcTotalWeeklyHours(){
        int totalWeeklyHours = 0;
        for(Subject s : subjectList){
            totalWeeklyHours += s.getWeeklyHours();
        }
        return totalWeeklyHours;
    }

    private int calcHoursofTeacher(String teacher){
        int hoursOfTeacher = 0;
        for(Subject s : subjectList){
            if(teacher.equals(s.getTeacher())){
                hoursOfTeacher += s.getWeeklyHours();
            }
        }
        return hoursOfTeacher;
    }

    public static void main(String[] args) {
        new ListWithPojo();
    }
}