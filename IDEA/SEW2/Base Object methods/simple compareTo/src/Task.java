import java.util.Objects;

public class Task {
  private String name;
  private int dob;

    public Task(String name, int dob) {
        this.name = name;
        this.dob = dob;
    }


    public int compareTo (Task other) {
        if (Objects.equals(this.name, other.name)){
            if (dob == other.dob) {
                return 0;
            }else{
                return (dob-other.dob);
            }
        }else{
            return this.name.compareTo(other.name);
        }

    }
}