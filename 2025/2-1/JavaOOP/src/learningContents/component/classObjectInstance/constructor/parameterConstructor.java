package learningContents.component.classObjectInstance.constructor;

class Bar1 {

    // 멤버 변수 - 데이터
    String name;
    int age;

    // 생성자
    Bar1(String argName, int argAge) {
        name = argName;
        age = argAge;
        System.out.println(name + "님, " + age + "세");
    }
}

public class parameterConstructor {
    public static void main(String[] args) {

        // Bar1 클래스 객체 생성
        Bar1 bar1 = new Bar1("hyochan", 26);

    }
}
