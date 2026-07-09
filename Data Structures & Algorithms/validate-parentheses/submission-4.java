class Solution {
    public boolean isValid(String s) {
        Stack<Character> paraStack = new Stack<>();
        char[] sCharArray = s.toCharArray();
        for (char c : sCharArray) {
            if (c == '(' || c == '{' || c == '[') {
                paraStack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (paraStack.isEmpty()) return false;
                char tempPara = paraStack.pop();
                if (c == ')' && tempPara != '(') return false;
                if (c == '}' && tempPara != '{') return false;
                if (c == ']' && tempPara != '[') return false;
            }
        }
        return paraStack.isEmpty();
    }
}
