
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> freq(1001, 0);
        vector<int> result;

        for (int num : nums1) {
            freq[num] = 1;
        }

        for (int num : nums2) {
            if (freq[num] == 1) {
                result.push_back(num);
                freq[num] = 0;
            }
        }

        return result;
    }
};
