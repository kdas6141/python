import pickle
import shelve

fruits_to_buy = { 'banana':2, 'pear':3, 'kiwi': 6}
dairy_to_buy = { 'swiss cheese pkg':3, '6-gallon milk':1, 'quart of yogurt': 2}
misc = ['soap', 'beer']
shopping_time = '6:40PM'

shopping_list = [ fruits_to_buy, dairy_to_buy]
f = open('groceries.pkl', 'wb')
pickle.dump(shopping_list, f)
f.close()
f = open('groceries.pkl', 'rb')
my_list = pickle.load(f)
f.close
for l in my_list:
	print(l)

shopping = shelve.open('shopping.my_db')
shopping['fruits'] = fruits_to_buy
shopping['dairy_stuff'] = dairy_to_buy
shopping['misc_items'] = misc
shopping['time'] = shopping_time
shopping.close()

shopping = shelve.open('shopping.my_db')
fruits = shopping['fruits']

for fruit, quanatity in fruits.item():
	print(f"{fruit}: {quantity}")

shopping.close()
