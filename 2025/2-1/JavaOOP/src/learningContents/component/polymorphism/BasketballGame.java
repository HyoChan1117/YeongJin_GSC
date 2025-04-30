package learningContents.component.polymorphism;

class PlayerFactory {
    Player createPlayer(String type) {
        switch (type) {
            case "SG": return new Sg();
            case "learningContents.component.polymorphism.Center": return new Center();
            default: return new Player();
        }
    }
}

class Coach {
    // 매개변수 타입: learningContents.component.polymorphism.Player -> 자식 클래스 모두 전달 가능
    void train(Player player) {
        System.out.print("훈련 중 -> ");
        player.shoot(); // 동적 바인딩 : 실제 객체의 shoot() 실행
    }
}

class Player {
    protected String name;
    protected String position;

    Player() {
        this.name = "default";
        this.position = "default";
    }

    Player(String argName, String argPosition) {
        this.name = argName;
        this.position = argPosition;
    }

    void shoot() {
        System.out.println(position + " " + name + ": 기본 슛");
    }
}

class Sg extends Player {
    Sg() {
        name = "준호";
        position = "Shooting Guard";
    }

    Sg(String argName) {
        super(argName, "슈팅가드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 3점슛!");
    }
}

class Pg extends Player {
    Pg(String argName) {
        super(argName, "포인트 가드");
    }
    
    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 돌파 후 점퍼!");
    }
}

class Center extends Player {
    Center() {
        name = "성민";
        position = "learningContents.component.polymorphism.Center";
    }
    
    Center(String argName) {
        super(argName, "센터");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 골밑슛!");
    }
}

class Pf extends Player {
    Pf(String argName) {
        super(argName, "파워 포워드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 미들슛!");
    }
}

class Sf extends Player {
    Sf(String argName) {
        super(argName, "스몰 포워드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 슬래시 앤 드라이브!");
    }
}

public class BasketballGame {
    public static void main(String[] args) {

        Player[] team = {
            new Pg("민수"),
            new Sg("준호"),
            new Sf("지훈"),
            new Pf("영철"),
            new Center("성민")
        };

        System.out.println("[ 팀 슛 연습 시작! ]\n");

        for (Player p : team) {
            p.shoot();
        }

        System.out.println();

        System.out.println("[ 훈련 중인 인원 ]");
        Coach coach = new Coach();
        coach.train(new Sg("성식"));
        coach.train(new Center());

        System.out.println();

        PlayerFactory factory = new PlayerFactory();
        Player p1 = factory.createPlayer("SG");
        p1.shoot();
    }
}
