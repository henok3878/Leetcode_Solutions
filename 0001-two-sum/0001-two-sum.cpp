class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp; 
        for(int i = 0; i < nums.size(); i++){
            int comp = target - nums[i]; 
            if(mp.count(comp)){
                return vector<int>{mp[comp], i}; 
            }
            mp[nums[i]] = i; 
        }
        return {};
    }
};