package learningContents.component.interfaceExplain.defaultMethod;

interface Scan {
    // public abstract void doScan();
    void doScan();

    // public static final int scanNum = 2;
    int scanNum = 2;

    default void prePaper() {
        System.out.println("Prepaper");
    }
}
class Equipment implements Scan {
    public void doScan() {
        System.out.println("Equipment scan");
    }

    @Override
    public void prePaper() {
        System.out.println("Equipment- Prepaper");
    }
}

class Device implements Scan {
    int scanNum = 10;
    @Override
    public void doScan() {
        System.out.println(Scan.scanNum);
    }
}
public class DefaultMethod {
    public static void main(String[] args) {
        Device device = new Device();
        device.doScan();
        device.prePaper();

        Equipment e = new Equipment();
        e.doScan();
        e.prePaper();
    }

}
