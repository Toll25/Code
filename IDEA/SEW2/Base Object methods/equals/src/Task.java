import java.util.Objects;
public class Task {
    private String name;
    private int dob;

    public Task(String name, int dob) {
        this.name = name;
        this.dob = dob;
    }

    @Override
    public boolean equals(Object other) {
        // 1. wenn die beiden Instanzen gleich sind
        if (this == other) return true;

        // 2. wenn die Klassen nicht zusammenpassen
        if (other == null || getClass() != other.getClass()) return false;

        // 3. ... und wenn die Attribute (Inhalte) gleich sind
        Task yes = (Task) other;
        return dob == yes.dob && Objects.equals(name, yes.name);
    }

}