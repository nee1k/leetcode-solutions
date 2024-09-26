class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hash_map = dict()

        for s in students:
            hash_map[s] = hash_map.get(s, 0) + 1

        for sandwich in sandwiches:
            if sandwich in hash_map.keys() and hash_map[sandwich] > 0:
                hash_map[sandwich] -= 1
            else:
                break
        
        count = 0
        for key in hash_map.keys():
            count += hash_map[key]
        return count
            
        