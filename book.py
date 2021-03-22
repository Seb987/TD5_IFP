class Order:
    def __init__(self, n, price, type, idd):
        self.n = n
        self.price = price
        self.type = type
        self.idd = idd

    def toString(self):
        print("        "+str(self.type)+" "+ str(self.n)+"@"+ str(self.price)+  " id="+ str(self.idd))


class Book:
    def __init__(self,name):
        self.name=name
        self.idd = 1
        self.orders= []
        self.orders_buy = []
        self.orders_sell = []

    def insert_buy(self, n, price):
        order = Order(n, price, "BUY", self.idd)
        print("--- Insert ", str(order.type), str(n) + "@" + str(price), "id=", str(self.idd), "on", str(self.name))

        self.update_order(order)


    def insert_sell(self, n, price):
        order = Order(n, price, "SELL", self.idd)
        print("--- Insert ", str(order.type), str(n) + "@" + str(price), "id=", str(self.idd), "on", str(self.name))

        self.update_order(order)

    def update_order(self,order):
        boolean = True
        index = 0
        stock= order.n
        price = order.price
        #if(order.type == "BUY"):
            #for i in range(len(self.orders_sell)):
               # if (price <= self.orders_buy[i].price and stock <= self.orders_buy[i].n):
                    #print("Execute " + str(stock) + " at " + str(self.orders_buy[i].price) + " on " + self.name)
                    #boolean = False
                    #break

        if (order.type == "SELL"):
            for i in range(len(self.orders_buy)):
                if(price >= self.orders_buy[i].price and stock <= self.orders_buy[i].n):
                    print("Execute "+str(stock)+" at "+str(self.orders_buy[i].price)+ " on " +self.name)
                    boolean = False
                    break

        if(boolean):
            if(order.type == "BUY"):
                self.orders_buy.append(order)
                self.orders_buy.sort(key=lambda x: x.price, reverse=True)
            if (order.type == "SELL"):
                self.orders_sell.append(order)
                self.orders_sell.sort(key=lambda x: x.price, reverse=True)
            self.orders.append(order)
            self.orders.sort(key=lambda x: x.price, reverse=True)

        print("Book on ", str(self.name))
        self.print_order()
        print("------------------------")
        self.idd = self.idd + 1

    def print_order(self):
        for i in range(len(self.orders)):
            self.orders[i].toString()


