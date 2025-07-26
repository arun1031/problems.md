#minloss
num_of_years = int(input("Enter num of years"))
price = list(map(int, input("Enter the price").split()))

min_loss = 99999999999999

buy_year = -1
sell_year = 0

for i in range(num_of_years):
    for j in range(i+1 , num_of_years):
        if price[i] > price[j]:
            loss = price[i] - price[j]
            if loss < min_loss:
                min_loss = loss 
                buy_year = i + 1
                sell_year += j
                

print("Buy year", buy_year , "at a price of " , price[buy_year-1])
print("Sell year", sell_year , "at a price of " , price[sell_year-1])

                
            
        
    
