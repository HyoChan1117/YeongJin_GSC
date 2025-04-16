package lab.Operator;

class PermissionManager {
    // 권한 비트 위치 상수 정의
    static final int READ = 0;   // 읽기 권한 비트 위치
    static final int WRITE = 1;  // 쓰기 권한 비트 위치
    static final int EDIT= 2;    // 수정 권한 비트 위치
    static final int DELETE = 3; // 삭제 권한 비트 위치

    private byte permissions = 0;  // 초기 권한 설정은 모두 비활성화 (0)

    // 권한 설정 메서드
    void setPermissions(int permission, boolean enable) {
        // 마스크 변수 설정
        int mask = 1 << permission;

        // enable이 true인 경우:
        if (enable) {
            // - permission 위치에 있는 비트를 1로 설정 (| 연산과 << 연산 사용)
            permissions |= mask;
        }
        // enable이 false인 경우:
        else {
            // - permission 위치에 있는 비트를 0으로 설정(& 연산과 ~ 연산 사용)
            permissions &= ~mask;
        }
    }

    // 권한 확인 메서드
    boolean checkPermissions(int permission) {
        // permission : 확인하려는 권한 (0번째, 1번째, 2번째, 3번째 비트 자리 중 하나)
        if (permission == 1) {
            return (permissions & (1 << permission)) != 0;
        }
        // - permission 위치 비트가 1이면 true, 그렇지 않으면 false를 반환
        // - & 연산과 << 연산을 사용해 비트 값 확인
        return (permissions & (1 << permission)) != 0;
    }

    // 모든 권한 초기화 메서드
    void removeAllPermissions() {
        // permissions 값을 0으로 설정하여 모든 비트를 0으로 만듦
        permissions = 0;
    }
}

public class OperatorLab2 {
    public static void main(String[] args) {
        PermissionManager pm = new PermissionManager();

        // 읽기, 쓰기, 삭제
        pm.setPermissions(PermissionManager.READ, true);    // 읽기 권한 활성화
        pm.setPermissions(PermissionManager.WRITE, true);   // 쓰기 권한 활성화
        pm.setPermissions(PermissionManager.DELETE, true);  // 삭제 권한 활성화

        // 권한 확인
        System.out.println(pm.checkPermissions(PermissionManager.READ));   // 출력: true
        System.out.println(pm.checkPermissions(PermissionManager.WRITE));  // 출력: true
        System.out.println(pm.checkPermissions(PermissionManager.EDIT));   // 출력: false
        System.out.println(pm.checkPermissions(PermissionManager.DELETE)); // 출력: true

        // 모든 권한 제거
        pm.removeAllPermissions();
        System.out.println(pm.checkPermissions(PermissionManager.READ));   // 출력: false
        System.out.println(pm.checkPermissions(PermissionManager.DELETE)); // 출력: false
    }
}