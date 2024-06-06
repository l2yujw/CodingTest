import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class StackQueueFunc {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<>();
        st.push(1);
        st.push(2);
        st.push(3);
        st.pop(); // 가장 마지막에 들어온 값 추출 3
        st.peek(); // 가장 윗값 출력: 2
        st.clear(); // 스택 전체 비우기
        st.size(); // 스택의 크기 출력
        st.empty(); // 스택 비었는지 확인(비었으면 true)
        st.contains(1); // 스택에 1이라는 값이 있는지 확인

        Queue<Integer> q = new LinkedList<>();
        Queue<String> q2 = new LinkedList<>();

        q.offer(1);
        q.offer(2);
        q.offer(3);
        q.add(4); // add, offer 모두 큐에 값을 집어넣을 수 있음
        q.poll(); // q에 제일 처음 들어간 값 반환 후 삭제 -> 1
        q.remove(); // queue의 제일 아랫값 제거
        q.peek(); // 제일 아랫값 return, 삭제하진 않음
        q.clear(); // 큐 전체 비우기
        q.size(); // 큐 사이즈 리턴
    }
}
