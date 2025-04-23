package learningContents.component.polymorphism;

// 공통 부모 클래스
class Player {
    protected String name;
    protected String position;

    Player(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public void shoot() {
        System.out.println(position + " " + name + ": 기본 슛");
    }
}

class Sg extends Player {
    Sg(String argName) {
        super(argName, "슈팅 가드");
    }

    @ Override
    public void shoot() {
        System.out.println(position + " " + name + ": 3점슛!");
    }
}

class Pg extends Player {
    Pg(String argName) {
        super(argName, "포인트 가드");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 돌파 후 점퍼!");
    }
}

class Center extends Player {
    Center(String argName) {
        super(argName, "센터");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 골밑슛!");
    }
}

class Pf extends Player {
    Pf(String argName) {
        super(argName, "파워 포워드");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 미들슛!");
    }
}

class Sf extends Player {
    Sf(String argName) {
        super(argName, "스몰 포워드");
    }


}

public class Polymorphism1 {
}
