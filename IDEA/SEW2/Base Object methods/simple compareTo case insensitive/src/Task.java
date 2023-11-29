import java.util.Objects;

public class Task {
    private String name;
    private int dob;

    public Task(String name, int dob) {
        this.name = name;
        this.dob = dob;
    }

    public int compareTo(Task other) {
        if (dob == other.dob) {
            if (Objects.equals(this.name.toLowerCase(), other.name.toLowerCase())) {
                return 0;
            } else {
                return this.name.toLowerCase().compareTo(other.name.toLowerCase());
            }
        } else {
            return (dob - other.dob);
        }
    }
}