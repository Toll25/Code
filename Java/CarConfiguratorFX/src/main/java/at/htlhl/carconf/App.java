package at.htlhl.carconf;

import com.fasterxml.jackson.databind.ObjectMapper;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.util.Locale;
import java.util.ResourceBundle;

public class App extends Application {
    // Constances **********************************************************
    public static final String APP_NAME = "CarConfiguratorFX";

    public static final String CONFIG_DIR_PATH = System.getProperty("user.home") + "/." + APP_NAME;
    public static final String MODEL_FILE_PATH = CONFIG_DIR_PATH + "/car.json";

    public static final ObjectMapper JSON_MAPPER = new ObjectMapper();

    //Logic *****************************************************************
    @Override
    public void start(Stage stage) throws IOException {
        initConfigDir(); //Create configuration directory if it doesn't exist.

        ResourceBundle resourceBundle = java.util.ResourceBundle.getBundle("at.htlhl.carconf.CarView");

        FXMLLoader fxmlLoader = new FXMLLoader(App.class.getResource("CarView.fxml"), resourceBundle);
        Scene scene = new Scene(fxmlLoader.load(), 640, 480);
        CarController carController = fxmlLoader.getController();

        Car car = new Car();
        car.setManufacturer("Ferrari");

        carController.init(car);

        stage.setTitle(APP_NAME);
        stage.setScene(scene);
        stage.show();
    }

    private void initConfigDir(){
        File configDir = new File(CONFIG_DIR_PATH);
        if(!configDir.exists()){
            configDir.mkdirs();
        }
    }

    public static void main(String[] args) {
        //Force a specifiv locale (e.g. ENGLISH, GERMAN, ARABIC, ...
        Locale.setDefault(new Locale("de"));
        launch();
    }
}