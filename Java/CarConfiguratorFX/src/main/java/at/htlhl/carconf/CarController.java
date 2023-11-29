package at.htlhl.carconf;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.stage.Window;
import org.controlsfx.validation.ValidationResult;
import org.controlsfx.validation.ValidationSupport;
import org.controlsfx.validation.Validator;

import java.io.File;
import java.io.IOException;
import java.util.ResourceBundle;

public class CarController {

    // Fields ********************************

    @FXML
    private Button loadButton;

    @FXML
    private Button saveButton;

    @FXML
    private Button tuneButton;

    @FXML
    private TextField manufacturerTextField;

    @FXML
    private TextField typeTextField;

    @FXML
    private Slider powerSlider;

    @FXML
    private Slider rangeSlider;

    private Car model;

    private ResourceBundle resourceBundle;

    private TuningService tuningService;

    // Instance creation*****************

    public CarController() {
        resourceBundle=ResourceBundle.getBundle("at.htlhl.carconf.Misc");
        tuningService=new TuningService();
    }
    public void init(Car model){
        this.model=model;

        powerSlider.setMax(Car.MAX_POWER);
        rangeSlider.setMax((Car.MAX_RANGE));

        initBinding();
        initValidation();
    }

    private void initBinding(){
        manufacturerTextField.textProperty().bindBidirectional(model.manufacturerProperty());
        typeTextField.textProperty().bindBidirectional(model.typeProperty());
        powerSlider.valueProperty().bindBidirectional(model.powerProperty());
        rangeSlider.valueProperty().bindBidirectional(model.rangeProperty());

        //Über Textänderungen im TextField benachrichtigen lassen:
        /*manufacturerTextField.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {

                System.out.println("old: " + oldValue + ", new: " + newValue);
            }
        });*/
    }

    private void updateModel(Car newModel){
        model.setManufacturer(newModel.getManufacturer());
        model.setType(newModel.getType());
        model.setPower(newModel.getPower());
        model.setRange(newModel.getRange());
    }

    /**
     * Initializes validation support using ControlsFX
     */
    private void initValidation(){
        ValidationSupport validationSupport =new ValidationSupport();
        validationSupport.registerValidator(manufacturerTextField,
                Validator.createEmptyValidator("Manufacturer is required"));

        validationSupport.registerValidator(rangeSlider, new Validator<Double>() {
            @Override
            public ValidationResult apply(Control control, Double newValue) {
                return ValidationResult.fromErrorIf(control,
                        "Range should be >=400",
                        newValue<400);
            }
        });

        saveButton.disableProperty().bind(validationSupport.invalidProperty());
    }

    // API ******************************
    @FXML
    protected void onLoadAction(ActionEvent event) {
        System.out.println("Load clicked......" + event.getSource());

        File configFile = new File(App.MODEL_FILE_PATH);

        if (configFile.exists()) {
            try {
                configFile=new File("C:/dir_does_not_exist/file_does_not_exist.json");
                Car car = App.JSON_MAPPER.readValue(configFile, Car.class);
                updateModel(car);
            } catch (IOException ex) {
                System.out.println("Problem reading file: " + ex.getMessage());

                Alert alert =new Alert(Alert.AlertType.ERROR);
                alert.initOwner(findParentWindow(event));
                alert.setTitle(App.APP_NAME);
                alert.setHeaderText(resourceBundle.getString("loadErrorAlert.headerText"));
                alert.setContentText(resourceBundle.getString("loadErrorAlert.contentText") + " " + ex.getLocalizedMessage());
                alert.showAndWait();
            }
        }
    }
    @FXML
    protected void onSaveAction(ActionEvent event){
        System.out.println("Save clicked......" + event.getSource());

        File configFile = new File(App.MODEL_FILE_PATH);

        try {
            configFile=new File("C:/dir_does_not_exist/file_does_not_exist.json");

            App.JSON_MAPPER.writerWithDefaultPrettyPrinter().writeValue(configFile, model);
        }catch(IOException ex){
            System.err.println("Error saving file: " + ex.getMessage());
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.initOwner(findParentWindow(event));
            alert.setTitle(App.APP_NAME);
            alert.setHeaderText(resourceBundle.getString("saveAlert.headerText"));
            alert.setContentText(resourceBundle.getString("saveAlert.contentText"));
            alert.showAndWait();
        }




        /*model.setManufacturer((manufacturerTextField.getText().trim()));
        model.setType((typeTextField.getText().trim()));
        model.setPower((int) powerSlider.getValue());
        model.setRange((int) rangeSlider.getValue());*/
    }

    @FXML
    protected void onTuneAction(ActionEvent event){
        System.out.println("Tune clicked......" + event.getSource());

        tuningService.tune(findParentWindow(event),model);

        /*Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.initOwner(findParentWindow(event));
        alert.setTitle(App.APP_NAME);
        alert.setHeaderText(resourceBundle.getString("tuneAlert.headerText"));
        alert.setContentText(resourceBundle.getString("tuneAlert.contentText"));
        alert.showAndWait();
*/
        System.out.println("Actual manufacturer: " + model.getManufacturer());

        System.out.println("Actual type: " + model.getType());

        System.out.println("Actual power: " + model.getPower());

        System.out.println("Actual range: " + model.getRange());
    }

    private Window findParentWindow(ActionEvent event) {
        return ((Node) event.getTarget()).getScene().getWindow();
    }
}