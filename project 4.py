import pandas as pd
df=pd.read_csv("products.csv")
class Product:
    def __init__(self,product_id,category,price):
        self.prod_id = product_id
        self.category = category
        self.price = float(price)

    def apply_discount(self, percent_off):
        discount_amount = self.price * (percent_off / 100)
        self.price -= discount_amount
        return self.price


electronics_df = df[df["Category"] == "Electronics"].copy()

discounted_price = []

for i, r in electronics_df.iterrows():
    item = Product(r["price"], r["prod_id"], r["category"])

    new_price=item.apply_discount(20)

    discounted_price.append(new_price)

electronics_df["Price"] = discounted_price
electronics_df["Promo_Active"] = "Yes"
electronics_df.to_excel("holiday_promos.xlsx")
print(electronics_df)

