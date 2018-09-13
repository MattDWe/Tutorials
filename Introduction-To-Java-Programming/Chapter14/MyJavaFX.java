// Basic structure of JavaFX

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class MyJavaFX extends Application{
  @Override
  public void start(Stage primaryStage){
    Button btOK = new Button("OK");
    Scene scene = new Scene(btOK, 200, 250); // node, width, height
    primaryStage.setTitle("MyJavaFX");
    primaryStage.setScene(scene);
    primaryStage.show();
  }
  public static void main(String[] args){ // This is not needed if running from command line as it will automatically run the launch command
    Application.launch(args);
  }
}
