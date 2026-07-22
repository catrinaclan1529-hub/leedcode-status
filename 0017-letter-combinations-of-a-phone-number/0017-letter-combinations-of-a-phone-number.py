class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination={
            '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=['']
        for i in range(len(digits)):
            current=combination[digits[i]]
            new_res=[]
            for combo in res:
                for letter in current:
                    new_res.append(combo+letter)
            res=new_res
        return res
                
                


            
        