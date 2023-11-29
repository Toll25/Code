import java.util.Objects;

public class Task {

    private String name;
    private int dob;

    public Task(String name, int dob) {
        this.name = name;
        this.dob = dob;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, dob);
    }
}