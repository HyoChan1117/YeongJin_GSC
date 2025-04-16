package learningContents.component.classObjectInstance;

class Car2 {
    String brand;

    void prtInfo() {
        System.out.println("Brand: " + brand);
    }
}

public class study4 {
    public static void main(String[] args) {

        Car2 car1 = new Car2();
        Car2 car2 = new Car2();

        car1.brand = "BMW";
        car2.brand = "KIA";

        car1.prtInfo();
        car2.prtInfo();
    }
}
