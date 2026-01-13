# make the language faster 
# python is already a slow language you want 


#[] stored in list /make entire list in memory
#() like a stream

daily_sales=[5,10,12,15,17,20]

total_cups1=[sales for sales in daily_sales if sales>10]
print(total_cups1)#()with these it gives geneartor object




total_cups2=sum(sales for sales in daily_sales if sales>10)
print(total_cups2)
