class ShoppingList:
    def __init__(self, shopping_List):
        self.shopping_List = shopping_List

    def get_item_count(self):
        return len(self.shopping_List)
    
    def get_total_price(self):
        total_price = 0

        for price in self.shopping_List.values():
            total_price += price
        return total_price
    
my_list = {
   "纸巾":8,
   "帽子":30,
   "拖鞋":15
}

shop = ShoppingList(my_list)


print("商品数量：", shop.get_item_count())  
print("总价：", shop.get_total_price()) 