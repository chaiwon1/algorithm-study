def counting (li) :
    count = [0] * (max(li) +1)
      
    for i in range(len(li)) :
        count[li[i]] += 1
        
    output = []
    for i in range(len(count)) :
        for j in range(count[i]) :
            output.append(i)
    return output
            
li = [10, 10, 2, 1, 7, 4, 3, 0, 0]    
print(counting(li)) # [0, 0, 1, 2, 3, 4, 7, 10, 10]

# 짧은 범위내에서 효율적
# 시간 복잡도 O(n+k)