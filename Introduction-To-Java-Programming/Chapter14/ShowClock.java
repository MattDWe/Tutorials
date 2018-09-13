import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.layout.HBox;
import javafx.geometry.Insets;

public class ShowClock extends Application{
  @Override
  public void start(Stage primaryStage){
    HBox pane = new HBox(20);
    pane.setPadding(new Insets(0, 10, 10, 0));

    ClockPane clock = new ClockPane();

    pane.getChildren().addAll(clock);

    Scene scene = new Scene(pane);
    primaryStage.setTitle("Clock");
    primaryStage.setScene(scene);
    primaryStage.show();
  }
}
