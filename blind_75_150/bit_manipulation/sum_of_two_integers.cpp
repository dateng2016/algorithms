
class Solution
{
  public:
    int getSum(int a, int b)
    {
        // Solution 1: wrong
        int base = a;
        int carry = b;
        while (carry != 0)
        {
            int old_base = base;
            base = base ^ carry;
            carry = (old_base & carry) << 1;
        }
        return base;
    }
};

