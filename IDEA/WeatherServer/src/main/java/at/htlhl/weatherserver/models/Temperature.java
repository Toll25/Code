package at.htlhl.weatherserver.models;

import java.time.LocalDateTime;

public class Temperature {
    private float temp;
    private LocalDateTime measureTime;

    public Temperature(float temp, LocalDateTime measureTime) {
        this.temp = temp;
        this.measureTime = measureTime;
    }
    public Temperature() {
    }

    public float getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
    }

    public LocalDateTime getMeasureTime() {
        return measureTime;
    }

    public void setMeasureTime(LocalDateTime measureTime) {
        this.measureTime = measureTime;
    }

    @Override
    public String toString() {
        return "temperature{" +
                "temp=" + temp +
                ", measureTime=" + measureTime +
                '}';
    }
}
