import pandas as pd #gọi thư viện 

path = 'bai2.csv'# gán file dữ liệu
df = pd.read_csv(path)#đọc dữ liệu từ file csv

#chuyển dữ liệu sang float
df[['Gold', 'Silver', 'Bronze']] = df[['Gold', 'Silver', 'Bronze']].astype(float)
#tổng huy chương vàng
df['Total'] = df['Gold'] + (df['Silver'] / 2) + (df['Bronze'] / 3)


#sắp xếp các nước theo tổng số hcv
gold_top = df.groupby('NOC')['Total'].sum().reset_index()
gold_top = gold_top.sort_values(by = 'Total', ascending = False)

#trường hợp nếu có 2 nước đồng hạng
gold_top['Rank'] = gold_top['Total'].rank(method = 'min', ascending = False)


#thên hậu tố st nd rd
gold_top['Rank'] = ['1st', '2nd', '3rd'] + [''] * (len(gold_top) - 3)

#in ra top 3 có tổng hcv cao nhất
top_3 = gold_top.head(3)
print("3 nước có hcv cao nhất")
print(top_3)



#Xuất file csv mới
gold_top.to_csv('bai2moi.csv', index = False)
print('File csv mới đã hoàn thành') 