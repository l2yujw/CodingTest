import java.util.Arrays;
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            String n = sc.next();
            String[] split = n.split("");

            String num = "1";

            int count = 0;

            for (String s : split) {
                if (s.equals(num)) {
                    count += 1;
                    if (num.equals("1")) {
                        num = "0";
                    } else {
                        num = "1";
                    }
                }
            }

            System.out.println("#" + test_case + " " + count);
        }
    }
}