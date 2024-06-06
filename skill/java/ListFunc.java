import java.util.*;

public class ListFunc {
    public static void main(String[] args) {

        Integer[] arr = {4, 3, 0, 2, 1};

// 오름차순 정렬
        Arrays.sort(arr); // [0, 1, 2, 3, 4]
        Arrays.sort(arr, Comparator.comparingInt(s -> s));
// 내림차순 정렬
        Arrays.sort(arr, Comparator.reverseOrder());

        System.out.println(Arrays.toString(arr));

        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("nvidia");
        list.add("tesla");
        list.add("samsung");

        Collections.sort(list);
        System.out.println(list);  // ["apple", "nvidia", "samsung", "tesla"]
        Collections.sort(list, Collections.reverseOrder());
        System.out.println(list); // ["tesla", "samsung", "nvidia", "apple"]
    }
}
