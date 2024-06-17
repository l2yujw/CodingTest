import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        int i = 0;
        for (String s : players) {
            map.put(s, i++);
        }

        for (String calling : callings) {
            int rank = map.get(calling);

            String front = players[rank - 1];

            map.replace(front, rank);
            players[rank] = front;

            map.replace(calling, rank - 1);
            players[rank - 1] = calling;
        }

        return players;
    }
}