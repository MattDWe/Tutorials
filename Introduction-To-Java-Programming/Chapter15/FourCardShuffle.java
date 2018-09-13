import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import java.util.ArrayList;

public class FourCardShuffle extends Application{
  @Override
  public void start(Stage primaryStage){
    VBox vBox = new VBox();
    vBox.setAlignment(Pos.CENTER);
    vBox.setPadding(new Insets(10, 10, 10, 10));

    HBos hBox = new HBox(5);
    hBox.setAlignment(POS.CENTER);
    hBox.setPadding(new Insets(10, 10, 10, 10));
    getCards(hBox);

    Button btRefresh = new Button("Refresh");

    btRefresh.setOnAction(e -> getCards(hBox));

    vBox.getChildren().addAll(hBox, btRefresh);

    Scene scene = new Scene(vBox);
    primaryStage.setTitle("Four Card Shuffle");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  private void getCards(HBox box){
    box.getChildren().clear()
    ArrayList<Integer> cards = new ArrayList<>();
    for (int i = 1; i <= 52; i++){
      cards.add(i);
    }
    java.util.Collections.shuffle(cards);

    for (int i = 0; i < 4; i++){
      box.getChildren().add(new ImageView(new Image("./cards/" + cards.get(i) + ".png")));
    }
  }
}
