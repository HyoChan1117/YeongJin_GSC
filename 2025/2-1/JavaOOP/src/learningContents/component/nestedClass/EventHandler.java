package learningContents.component.nestedClass;

import javax.swing.*;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;

class NonInnerClassExample extends JFrame {

    private String originalTitle = "Original Title";

    public NonInnerClassExample() {
        setTitle(originalTitle);
        setSize(300, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        addMouseListener(new ExternalMouseEventHandler(this));

        setVisible(true);
    }

    public void updateTitle(String title) { setTitle(title); }
    public String getOriginalTitle() { return originalTitle; }
}

class ExternalMouseEventHandler implements MouseListener {
    private NonInnerClassExample frame;

    public ExternalMouseEventHandler(NonInnerClassExample frame) { this.frame = frame; }

    public void mouseEntered(MouseEvent e) { frame.updateTitle("Mouse on"); }
    public void mouseExited(MouseEvent e) { frame.updateTitle(frame.getOriginalTitle()); }

    public void mouseClicked(MouseEvent e) {}
    public void mousePressed(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
}

public class EventHandler {
    public static void main(String[] args) { new NonInnerClassExample(); }
}
