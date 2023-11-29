import org.junit.Assert;
import org.junit.Test;

public class Tests {
    @Test
    public void testLastWord() {
        Task task = new Task();
        String line = "Beachte,Analog,Beamte,Diagramm,Beate,Heraus,Besen";
        Assert.assertEquals("Besen", task.findLastWord(line, "Be"));
        Assert.assertEquals("", task.findLastWord(line, "Ge"));
        Assert.assertEquals("", task.findLastWord(line, "be"));
    }
}