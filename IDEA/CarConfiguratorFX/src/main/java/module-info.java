module at.htlhl.carconf {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;

    requires com.fasterxml.jackson.databind;
    requires javafx.base;

    opens at.htlhl.carconf to javafx.fxml;
    exports at.htlhl.carconf;
}