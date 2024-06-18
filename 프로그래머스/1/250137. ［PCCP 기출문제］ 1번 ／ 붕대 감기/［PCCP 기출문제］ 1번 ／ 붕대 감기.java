class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int maxTime = attacks[attacks.length - 1][0];
        int charge = 0;
        int attackNum = 0;
        int curHealth = health;
        for (int i = 0; i <= maxTime; i++) {
            if (attacks[attackNum][0] == i) {
                curHealth -= attacks[attackNum][1];
                charge = 0;
                attackNum++;
            } else {
                curHealth += bandage[1];
                charge++;
                if (charge == bandage[0]) {
                    curHealth += bandage[2];
                    charge = 0;
                }
            }
            if (curHealth >= health) {
                curHealth = health;
            } else if (curHealth <= 0) {
                return -1;
            }
        }

        return curHealth;
    }
}