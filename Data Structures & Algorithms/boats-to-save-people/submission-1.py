class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len( people )
        boats = 0
        i = 0
        j = n-1
        1,1,2,3,3,5,5
        count = 0
        while i <= j:
            if i==j: 
                count +=1
                break
            while i < j and people[j] + people[i] > limit: 
                count+=1
                j-=1
            count += 1
            i+=1
            j-=1
        return count