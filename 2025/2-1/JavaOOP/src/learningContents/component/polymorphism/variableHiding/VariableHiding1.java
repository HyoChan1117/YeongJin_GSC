package learningContents.component.polymorphism.variableHiding;

class Student {
    String name;
    int age;

    void info() {
        System.out.println(name + ", " + age + ", " + age);
    }
}

class GSC extends Student{
    String name = "GSC";
    int age = 20;
    void info() {
        System.out.println("이름: " + name + ", 나이: " + age + ", " + age);
    }
}

class Architect extends Student{
    String name = "Architect";
    int age = 30;
    void info() {
        System.out.println("name: " + name + ", age: " + age + ", " + age);
    }
}

public class VariableHiding1 {
    public static void main(String[] args) {
        Student s[] = new Student[2];

        s[0] = new GSC();
        s[1] = new Architect();

        for (int i = 0 ; i < s.length ; i++) {
            s[i].info();
        }
    }
}
