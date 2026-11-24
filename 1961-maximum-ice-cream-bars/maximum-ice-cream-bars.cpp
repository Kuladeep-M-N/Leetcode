
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int count[100001] = {0};
        int maxi = 0;

        for(int i = 0; i < costs.size(); i++)
        {
            count[costs[i]]++;
            maxi = max(maxi, costs[i]);
        }

        int ans = 0;

        for(int i = 1; i <= maxi; i++)
        {
            while(count[i] > 0 && coins >= i)
            {  
                coins -= i;
                ans++;
                count[i]--;
            }

            if(coins < i)
                break;
        }

        return ans;
    }
};
