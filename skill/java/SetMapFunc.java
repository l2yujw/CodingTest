import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class SetMapFunc {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();			//객체 생성
        set.add(1);									//값 추가
        set.contains(1);							//1이 포함되어있는지 확인
        set.isEmpty();								//비어있는지 확인
        set.remove(1);								//값 삭제
        set.size();									//사이즈

        Map<Integer, String> map = new HashMap<>();		//객체 생성
        map.put(1, "A");								//값 추가 key = 1, value = A
        map.get(1);										//key에 해당하는 value. 없으면 null 반환
        map.containsKey(1);								//map에 해당 키가 있는지 확인 (boolean 반환)
        map.remove(1);									//key에 해당하는 아이템 삭제(1,"A") 후 value 반환
        map.size();										//map에 들어가 있는 쌍 갯수
        map.keySet();									//map의 key들을 모아 Set으로 반환.

        Map<String, String> map2 = new HashMap<>();
        map2.put("a", "A");
        map2.put("b", "B");
        map2.put("c", "C");
//
        for(String key : map2.keySet()){
            System.out.println(key);			//a b c 출력
        }
    }
}
