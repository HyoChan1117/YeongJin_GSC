package learningContents.component.nestedClass.innerClass.localInnerClass;

public class LocalInnerClass {
    public static void main(String[] args) {

        int x = 3;

        if (x == 3) {
            class Test{}

            Test test1 = new Test();
        }

//        Test test2 = new Test();
    }
}
