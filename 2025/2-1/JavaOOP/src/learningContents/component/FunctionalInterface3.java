package learningContents.component;

import java.util.ArrayList;

class Add {
    Object op(Object a, Object b) {

        if (a instanceof Integer && b instanceof Integer) {
            return (Integer) a + (Integer) b;
        }
        if (a instanceof String || b instanceof String) {
            return a.toString() + b.toString();
        }

        return null;
    }
}

public class FunctionalInterface3 {
    public static void main(String[] args) {

        ArrayList<Add> list = new ArrayList<>();

        list.add(new Add());

    }
}
