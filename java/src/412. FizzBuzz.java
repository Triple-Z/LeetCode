class Solution {
    // 8/8 cases passed (2 ms)
    // Your runtime beats 61.16 % of java submissions
    // Your memory usage beats 27.41 % of java submissions (40.2 MB)
        public List<String> fizzBuzz(int n) {
            List<String> ans = new LinkedList<>();
    
            Map<Integer, String> numMap = new LinkedHashMap<>() {{
                put(3, "Fizz");
                put(5, "Buzz");
            }};
    
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i <= n; i++) {
                sb.setLength(0);
                for (int k : numMap.keySet()) {
                    if (i % k == 0) sb.append(numMap.get(k));
                }
                if (sb.length() == 0) {
                    ans.add(String.valueOf(i));
                } else {
                    ans.add(sb.toString());
                }
            }
    
            return ans;
        }
    }