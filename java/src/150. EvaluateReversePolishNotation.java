class Solution {
    public int evalRPN(String[] tokens) {
        LinkedList<Integer> numStack = new LinkedList<>();

        int a, b;
        for (String token : tokens) {
            switch(token) {
            case "+":
                b = numStack.removeLast();
                a = numStack.removeLast();
                numStack.addLast(a + b);
                break;
            case "-":
                b = numStack.removeLast();
                a = numStack.removeLast();
                numStack.addLast(a - b);
                break;
            case "*":
                b = numStack.removeLast();
                a = numStack.removeLast();
                numStack.addLast(a * b);
                break;
            case "/":
                b = numStack.removeLast();
                a = numStack.removeLast();
                numStack.addLast(a / b);
                break;
            default:
                numStack.addLast(Integer.valueOf(token));
            }
        }
        
        return numStack.removeLast();
    }
}