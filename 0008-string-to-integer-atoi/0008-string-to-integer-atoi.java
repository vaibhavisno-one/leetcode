class Solution {
    public int myAtoi(String s) {
        int r = 0;
        int i = 0;
        int sign = 1;

        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }


        if (i < s.length()) {
            if (s.charAt(i) == '-') {
                sign = -1;
                i++;
            } else if (s.charAt(i) == '+') {
                i++;
            }
        }

        while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            int digit = s.charAt(i) - '0';

            if (r > (Integer.MAX_VALUE - digit) / 10) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            r = r * 10 + digit;
            i++;
        }

        return r * sign;
    }
}
