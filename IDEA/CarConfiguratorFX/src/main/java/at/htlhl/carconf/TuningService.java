package at.htlhl.carconf;

import javafx.concurrent.Service;
import javafx.concurrent.Task;
import javafx.concurrent.WorkerStateEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Priority;
import javafx.stage.Stage;
import javafx.stage.Window;
import org.controlsfx.control.tableview2.filter.filtereditor.SouthFilter;

public class TuningService extends Service<Integer> {

    //Fields ###########################################################################################################

    private Alert tuneAlert;
    private final Label progressLabel;
    private final ProgressBar progressBar;
    private Window actualParentWindow;
    private Car model;

    // Instance Creation ###############################################################################################

    public TuningService(){
        super();

        progressLabel=new Label();
        progressBar=new ProgressBar();

        progressLabel.textProperty().bind(messageProperty());
        progressBar.progressProperty().bind(progressProperty());

        setOnCancelled(new EventHandler<WorkerStateEvent>() {
            @Override
            public void handle(WorkerStateEvent event) {
                Alert alert =new Alert(Alert.AlertType.WARNING);
                alert.initOwner(actualParentWindow);
                alert.setTitle(App.APP_NAME);
                alert.setHeaderText("Tuning cancelled");
                alert.show();
            }
        });
        setOnSucceeded(new EventHandler<WorkerStateEvent>() {
            @Override
            public void handle(WorkerStateEvent event) {
                tuneAlert.hide();
                Alert alert =new Alert(Alert.AlertType.INFORMATION);
                alert.initOwner(actualParentWindow);
                alert.setTitle(App.APP_NAME);
                alert.setHeaderText("Tuning successful");
                alert.show();
            }
        });
    }

    //API ##############################################################################################################


    public void tune(Window parentWindow, Car model){
        this.model=model;
        this.actualParentWindow=parentWindow;

        tuneAlert=buildProgressAlert();
        tuneAlert.initOwner(parentWindow);
        tuneAlert.show();

        reset();
        start();

    }
    @Override
    protected Task<Integer> createTask() {
        return new TuneTask();
    }

    private Alert buildProgressAlert(){
        Alert alert=new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(App.APP_NAME);

        GridPane gridPane=new GridPane();
        gridPane.setHgap(10);
        gridPane.setVgap(10);
        gridPane.add(progressLabel,0,0);
        gridPane.add(progressBar, 0,1);

        GridPane.setHgrow(progressLabel, Priority.ALWAYS);
        GridPane.setVgrow(progressBar, Priority.ALWAYS);
        progressBar.setMaxWidth(Double.MAX_VALUE);

        alert.getDialogPane().setContent(gridPane);
        alert.getDialogPane().setPrefWidth(400);

        alert.getButtonTypes().setAll(ButtonType.CANCEL);

        return alert;
    }

    private class TuneTask extends Task<Integer>{
        public TuneTask(){
            super();
        }

        @Override
        protected Integer call() throws Exception{
            int actualTunePart;
            int totalTuneParts=10;

            for(actualTunePart=1; actualTunePart<=totalTuneParts;actualTunePart++){

                updateProgress(actualTunePart, totalTuneParts);
                updateMessage("Part " + actualTunePart + " of " + totalTuneParts + " is tuned");

                if(tuneAlert.getResult() == ButtonType.CANCEL){
                    cancel();
                }

                try{
                    Thread.sleep(1000);
                    model.setPower(model.getPower()+1);
                    System.out.println("Power is now " + model.getPower());
                }catch( InterruptedException ex){
                    if(isCancelled()){
                        updateMessage("Tuning cancelled");
                        break;
                    }
                }

            }

            return actualTunePart;
        }
    }
}
