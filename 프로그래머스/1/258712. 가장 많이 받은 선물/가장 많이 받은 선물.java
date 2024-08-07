import java.util.*;

/*
    친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측
    if 두 사람이 선물을 주고 받은 기록O => 조금 준사람이 선물
    if 기록이 없거나 같음 => 선물 지수가 작은사람이 선물 / !근데 선물지수도 같아 => 쉬쉬

    선물지수 => 총 자신이 친구들에게 준 선물 수 - 받은 선물 수

    선물을 가장 많이 받을 친구가 받은 선물의 수

    friends => 친구 이름을 담은 1차원 배열
    gifts => 주고 받은 선물 기록을 담은 1차원 문자열 배열 / "(선물 준 친구) (받은 친구)" 형태
*/
class Solution {
    public int solution(String[] friends, String[] gifts) {

        // 친구들의 이름을 키 값으로 고유 value를 등록해 추후 배열 위치 선정에 편리함을 가져옵니다.
        Map<String, Integer> id = new HashMap<>();
        int num = 0;
        for (String friend : friends) {
            id.put(friend, num++);
        }

        // "(선물 준 친구) (받은 친구)" 형태를 따와 해당 위치에 gifts 기록에 따라 +1을 해줍니다
        int[][] jugoBodgo = new int[friends.length][friends.length];
        for (String gift : gifts) {
            String[] split = gift.split(" ");
            jugoBodgo[id.get(split[0])][id.get(split[1])]++;
        }

        // 총 자신이 친구들에게 준 선물 수 - 받은 선물 수
        // jugobodgo를 잘 생각해보면 받은 친구를 나로 잡고 준 친구를 돌리면 받은 선물 수를 구할 수도 있습니다.
        // 수직 행렬 느낌으로 고정값과 변동값을 설정한 후 첫줄 값을 찾아줍니다
        // 그런 후 본인의 jisoo를 등록합니다.
        int[] jisoo = new int[friends.length];
        for (int j = 0; j < jugoBodgo.length; j++) {
            int left = 0;
            int right = 0;
            for (int k = 0; k < jugoBodgo.length; k++) {
                left += jugoBodgo[j][k];
                right += jugoBodgo[k][j];
            }
            jisoo[j] = left - right;
        }

        // if 두 사람이 선물을 주고 받은 기록O => 조금 준사람이 선물
        // if 기록이 없거나 같음 => 선물 지수가 작은사람이 선물 / !근데 선물지수도 같아 => 쉬쉬
        // jugobodgo 기록을 통해 선물을 받아옵니다
        // jisoo를 구할 때 처럼 배열을 대칭 시켜서 a가 b에게 받은 선물과 b가 a에게 받은 선물을 비교 할 수 있습니다
        // 위의 조건에 따라 조건문을 작성합니다
        int[] result = new int[friends.length];
        for (int j = 1; j < jugoBodgo.length; j++) {
            for (int k = 0; k < j; k++) {
                if (jugoBodgo[j][k] > jugoBodgo[k][j]) {
                    result[j]++;
                } else if (jugoBodgo[j][k] < jugoBodgo[k][j]) {
                    result[k]++;
                } else {
                    if (jisoo[j] > jisoo[k]) {
                        result[j]++;
                    } else if (jisoo[j] < jisoo[k]) {
                        result[k]++;
                    }
                }
            }
        }

        int answer = 0;
        for (int i : result) {
            answer = Math.max(answer, i);
        }

        return answer;
    }
}