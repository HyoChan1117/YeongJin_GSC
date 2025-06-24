package learningContents.component;

class Person1 {
    String name;
    int age;
    Person1 (String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class FunctionalInterface2 {
    public static void main(String[] args) {

        // Wrapper classes : Integer, Float, Double, ...
        // Primitive DataType을 객체로 만드는 것
        // 기능
        // Auto-boxing : 기본형 값을 자동으로 해당 래퍼 클래스 객체로 변환하는 기능
        // Unboxing : 래퍼 클래스 객체를 자동으로 기본형 값으로 변환하는 기능
        Integer myValue = 10;  // Auto-boxing
//      Integer myValue = new Integer(10);  이런 모양으로 됨

        int myAge = 20;  // Unboxing

        Float myFloat = 5.0f;
        Double myDouble = 5.0;
        Byte myByte = Byte.valueOf((byte) 1);
        Short myShort = Short.valueOf((short) 1);

        System.out.println(myValue);

    }
}
