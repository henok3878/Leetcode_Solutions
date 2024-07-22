class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peoples  = list(zip(heights,names))
        peoples.sort(reverse = True) 
        return [people[1] for people in peoples]