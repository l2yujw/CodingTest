import java.util.ArrayList;

class CreateVar {

    public static void main(String[] args) {
        String[] arr1 = new String[5];
        int[] arr2 = {1, 2, 3};

        int N = 3;
        int[] arr3 = new int[N];

//      깊은 복사
        ArrayList<Integer> w = new ArrayList<>();
        ArrayList<Integer> copy_w = new ArrayList<>();
        copy_w.addAll(w);
    }
}
