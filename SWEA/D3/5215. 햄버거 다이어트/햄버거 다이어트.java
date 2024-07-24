import java.util.Scanner;


// 민기가 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록
// 정해진 칼로리 이하의 조합 중에서 민기가 가장 선호하는 햄버거를 조합해주는 프로그램
class Solution
{
    static int ans;
    static int n, l;
    static int[] scoreArr;
    static int[] kcalArr;

    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            n = sc.nextInt();
            l = sc.nextInt();
            scoreArr = new int[n];
            kcalArr = new int[n];
            ans = 0;

            for (int i = 0; i < n; i++) {
                scoreArr[i] = sc.nextInt();
                kcalArr[i] = sc.nextInt();
            }

            combineHam(0, 0, 0);
            System.out.println("#" + test_case + " " + ans);
        }
    }

    private static void combineHam(int cur, int kcal, int score) {
        if (kcal > l) {
            return;
        }

        if (cur == n) {
            ans = Math.max(ans, score);
            return;
        }

        combineHam(cur + 1, kcal + kcalArr[cur], score + scoreArr[cur]);
        combineHam(cur + 1, kcal, score);
    }
}