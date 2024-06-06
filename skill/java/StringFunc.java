public class StringFunc {
    public static void main(String[] args) {
        String str = "ABCDE";
        StringBuffer sb = new StringBuffer(str);	//StringBuffer 객체에 ABCDE 입력
        String reverseStr = sb.reverse().toString();	//문자열 뒤집음

        String str2 = "aBcdEF";
        String upperStr = str2.toUpperCase();		//대문자로 변환
        String lowerStr = str2.toLowerCase();		//소문자로 변환

        String str3 = "aaabbbccc";
        String str4 = str3.replace("a", "b");		//str == aaabbbccc		str2 == bbbbbbccc

        String str5 = "“t0e0a1c2h0er";
        String str6 = str5.replaceAll("[^0-9]", "");        //str == teacher		str2 == 00120

        int a = Integer.parseInt("1");        // 1
        String b = Integer.toString(1);		  // "1"
    }
}
