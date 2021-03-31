# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

def BuySellStock(stocks):
    n=len(stocks)
    maxProfit=0

    for i in range(0,n):
        for j in range(i+1,n):
            profit=stocks[j]-stocks[i]
            if profit>maxProfit:
                maxProfit=profit

    return maxProfit


stocks=[7,1,5,3,6,4]
print(BuySellStock(stocks))

#optimized
# shortest value is subtracted with every other value to identify the largest difference

def optimized(stocks):
    n=len(stocks)
    minPrice=9999999999
    maxProfit=0

    for i in range(n):
        if stocks[i]<minPrice:
            minPrice=stocks[i]
        elif stocks[i]-minPrice > maxProfit:
            maxProfit=stocks[i]-minPrice

    return maxProfit

print("optimized")
stocks=[7,1,5,3,6,4]
print(optimized(stocks))