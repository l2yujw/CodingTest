import java.util.*;
class Solution {
    public int solution(int[] nums) {
		int answer = -1;
		answer = dfs(0, 0, 0, nums);
		return answer;
	}

	public int dfs(int count, int start, int num, int[] nums) {
		if (count == 3) {
			if (num % 2 != 0) {
				for (int i = 3; i <= Math.sqrt(num); i += 2) {
					if (num % i == 0) {
						return 0;
					}
				}
				return 1;
			}
			return 0;
		}

		int answer = 0;

		for (int i = start; i < nums.length; i++) {
			answer += dfs(count + 1, i + 1, num + nums[i], nums);
		}
		return answer;
	}
}