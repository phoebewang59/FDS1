def mean(nums):
    added = 0
    for i in nums:
        added = added + i
    return (added/len(nums))

def variance(nums):
    added = 0
    ss = 0
    for i in nums: #this for loop calculates the mean
        added = added + i
    average = (added/len(nums))
    for i in nums: #calculates the variance
        sq = (i - average)**2 #(x - mean)^2
        ss = ss + sq #sum of all squares
    return ss/(len(nums) - 1)

def stdv(nums): #standard deviation
    added = 0
    ss = 0
    for i in nums: #this for loop calculates the mean
        added = added + i
    average = (added/len(nums))
    for i in nums: #calculates the variance
        sq = (i - average)**2 #(x - mean)^2
        ss = ss + sq #sum of all squares
    return ((ss/(len(nums) - 1))**0.5) #square root of the variance

def stde(nums): #standard error
    added = 0
    ss = 0
    for i in nums: #this for loop calculates the mean
        added = added + i
    average = (added/len(nums))
    for i in nums: #calculates the variance
        sq = (i - average)**2 #(x - mean)^2
        ss = ss + sq #sum of all squares
    standard_deviation = ((ss/(len(nums) - 1))**0.5) #square root of the variance is standard deviation
    return standard_deviation/(len(nums)**0.5) # se = standard deviation/sqrt(n)

def z_score(nums,user_num): #user_num = the observation/data point that user enters to compute the z-score
    added = 0
    ss = 0
    for i in nums: #this for loop calculates the mean
        added = added + i
    average = (added/len(nums))
    for i in nums: #calculates the variance
        sq = (i - average)**2 #(x - mean)^2
        ss = ss + sq #sum of all squares
    standard_deviation = ((ss/(len(nums) - 1))**0.5) #square root of the variance is standard deviation
    return ((user_num - average)/standard_deviation) #z-score
    
    


    


