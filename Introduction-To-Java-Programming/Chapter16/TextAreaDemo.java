import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.ImageView;

public class TextAreaDemo extends Application{
  @Override
  public void start(Stage primaryStage){
    DescriptionPane descriptionPane = new DescriptionPane();

    descriptionPane.setTitle("US");
    String description = "The US Flag";
    descriptionPane.setImageView(new ImageView("./us.gif"));
    descriptionPane.setDescription(description);

    Scene scene = new Scene(descriptionPane, 450, 200);
    primaryStage.setTitle("TextAreaDemo");
    primaryStage.setScene(scene);
    primaryStage.show();
  }
}
