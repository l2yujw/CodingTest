import java.util.*;

public class ArraySort {

    public static void main(String[] args) {
        int[] arr = {5, 0, 2, 3, 4, 1};

        Arrays.sort(arr);		//오름차순 정렬
        Arrays.sort(arr, 1, 4);		//인덱스 1부터 3까지 오름차순 정렬

        Integer[] arr2 = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(arr2, Collections.reverseOrder());        //내림차순 정렬

        int[] arr3 = {0, 1, 2, 3, 4, 5};
        arr3 = Arrays.copyOfRange(arr, 0, 3);        //인덱스 0~2까지 슬라이싱

        int[][] arr4 = new int[][]{{5,40},{3,50},{1,30},{4,20},{2,10}};
        Arrays.sort(arr4, Comparator.comparingInt((int[] o) -> o[0]));	//첫 번째 숫자 기준 오름차순 정렬
        Arrays.sort(arr4, Comparator.comparingInt((int[] o) -> o[1]));	//두 번째 숫자 기준 오름차순 정렬
        Arrays.sort(arr4, Comparator.comparingInt((int[] o) -> o[0]).reversed());	//첫 번째 숫자 기준 내림차순 정렬
        Arrays.sort(arr4, Comparator.comparingInt((int[] o) -> o[1]).reversed());	//두 번째 숫자 기준 내림차순 정렬

        ArrayList<Integer> arr5 = new ArrayList<>();
        Collections.sort(arr5);
        arr5.sort(Comparator.reverseOrder());
    }
}
