package Prep.Lab;

import java.util.Scanner;

public class Lab4_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 사용자 입력
        System.out.print("초기 자본금 입력: ");
        double initialCapital = scanner.nextDouble();

        System.out.print("주식의 구매 가격 입력: ");
        double purchasePrice = scanner.nextDouble();

        System.out.print("구매할 주식 수 입력: ");
        int stockQuantity = scanner.nextInt();

        System.out.print("판매 시 주식 가격 입력: ");
        double sellingPrice = scanner.nextDouble();

        // 주식 구매 비용 계산
        double totalPurchaseCost = purchasePrice * stockQuantity;

        // 남은 자본금 계산
        double remainingCapital = initialCapital - totalPurchaseCost;

        // 판매 예상 이익(또는 손실) 계산
        double totalSellingRevenue = sellingPrice * stockQuantity;
        double expectedProfitOrLoss = totalSellingRevenue - totalPurchaseCost;

        // 결과 출력
        System.out.printf("주식 구매 후 남은 자본금: %.2f원\n", remainingCapital);
        System.out.printf("예상되는 이익(또는 손실): %.2f원\n", expectedProfitOrLoss);

        if (expectedProfitOrLoss > 0) {
            System.out.println("예상되는 이익입니다.");
        } else if (expectedProfitOrLoss < 0) {
            System.out.println("예상되는 손실입니다.");
        } else {
            System.out.println("이익도 손실도 없습니다.");
        }

        scanner.close();
    }
}