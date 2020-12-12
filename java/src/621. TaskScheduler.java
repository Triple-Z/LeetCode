class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (n == 0)
            return tasks.length;

        Map<Character, Integer> taskMap = new HashMap<>();
        int maxTaskNum = 0;
        for (char task : tasks) {
            taskMap.put(task, taskMap.getOrDefault(task, 0) + 1);
            maxTaskNum = Math.max(maxTaskNum, taskMap.get(task));
        }

        int cnt = 0;
        for (Map.Entry<Character, Integer> entry : taskMap.entrySet()) {
            if (entry.getValue() == maxTaskNum) {
                cnt++;
            }
        }

        return Math.max((maxTaskNum - 1) * (n + 1) + cnt, tasks.length);
    }
}