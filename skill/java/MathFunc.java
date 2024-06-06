public class MathFunc {
    public static void main(String[] args) {
//        반올림 - Math.round() : 소수점 첫째자리에서 반올림
        double val = 1.12345;
        Math.round(val);			// 1 반환
//        소수점 몇 째 자리까지 반올림 (스킬)
        /* 둘째자리까지 반올림 예제 */
        double val2 = 1.12345;
        val2 *= 100;					// val == 123.45
        Math.round(val2);			// val == 123
        val2 /= 100.0;				// val == 1.23
//        절대값 - Math.abs()
        double val3 = -1.12345;
        Math.abs(val3);				// 1.12345 반환
//        두 값 중 큰 값 - Math.max()
        Math.max(1.1, 2.2);            // 2.2 반환
//        두 값 중 작은 값 - Math.min()
        Math.min(1.1, 2.2);            // 1.1 반환
    }
}
