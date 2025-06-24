package learningContents.component;

import java.util.ArrayList;
import java.util.function.Consumer;

class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class FunctionalInterface1 {
    public static void main(String[] args) {

        // List, Set, Map 등의 자료 구조를 제공하는 라이브러리 패키지
        // Collection Framework : package for Data Structures
        // java.util 패키지에 포함되어 있음
        ArrayList<Person> list = new ArrayList<>();

        list.add(new Person("Yon", 20));
        list.add(new Person("Jane", 31));
        list.add(new Person("Tack", 41));
        list.add(new Person("Qill", 51));

        // 출력
        Consumer<Person> prt = (obj) -> System.out.println(obj.name + ":" + obj.age);

        // Stream API는 데이터 컬렉션을 함수형 스타일로 처리할 수 있게 해주는 도구
        list.stream().forEach(prt);
    }
}
