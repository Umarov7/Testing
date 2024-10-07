import os,mysql.connector as mc
os.system('clear')
# 1-task
class Database:
    db = None
    def __init__(self,dbN = 'tech'):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702')
        self.cur = self.con.cursor()
        self.cur.execute(f'Create database if not exists {dbN}')
        self.con.commit()
        Database.db = dbN
    def cr_table(self,tb = 'Product'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'Create table if not exists {tb}(maker varchar(20),model int primary key,type varchar(20))'
            self.cur.execute(sql)
            
            ls_brand = ['B','A','A','E','A','D','A','C','A','A','D','E','B','A','E','E']
            ls_model = [1121,1232,1233,1260,1276,1288,1298,1321,1401,1408,1433,1434,1750,1752,2112,2113]
            ls_type = ['PC','PC','PC','PC','Printer','Printer','Laptop','Laptop','Printer','Printer','Printer','Printer','Laptop','Laptop','PC','PC']
            try:
                for x,y,z in zip(ls_brand,ls_model,ls_type):
                    self.cur.execute(f'Insert into {tb}(maker,model,type) Values(%s,%s,%s)',(x,y,z))
            except:
                print(f'Information has already been added to {tb}')
            self.con.commit()
        else:
            print('Database not found')
    def cr_lp(self,tb = 'Laptop'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'Create table if not exists {tb}(id int primary key auto_increment,model int,speed int,ram int,hd int,screen int,price float)'
            self.cur.execute(sql)
            
            ls_model2 = [1298,1321,1750,1298,1752,1298]
            ls_speed = [350,500,750,600,750,450]
            ls_ram = [32,64,128,64,128,64]
            ls_hd = [4,8,12,10,10,10]
            ls_screen = [11,12,14,15,14,12]
            ls_price = [700.00,970.00,1200.00,1050.00,1150.00,950.00]
            self.cur.execute(f'SELECT COUNT(*) FROM {tb}')
            row_count = self.cur.fetchone()[0]
            if row_count == 0:
                for a,b,c,d,e,f in zip(ls_model2,ls_speed,ls_ram,ls_hd,ls_screen,ls_price):
                    self.cur.execute(f'Insert into {tb}(model,speed,ram,hd,screen,price) Values(%s,%s,%s,%s,%s,%s)',(a,b,c,d,e,f))
            else:
                print(f'Information has already been added to {tb}')
            self.con.commit()
        else:
            print('Database not found')
    def cr_pc(self,tb = 'PC'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'Create table if not exists {tb}(id int primary key auto_increment,model int,speed int,ram int,hd int,cd varchar(10),price float)'
            self.cur.execute(sql)

            ls_model2 = [1232,1121,1233,1121,1121,1233,1232,1232,1232,1260,1233,1233]
            ls_speed = [500,750,500,600,600,750,500,450,450,500,900,800]
            ls_ram = [64,128,64,128,128,128,32,64,32,32,128,128]
            ls_hd = [5,14,5,14,8,20,10,8,10,10,40,20]
            ls_cd = ['12x','40x','12x','40x','40x','50x','12x','24x','24x','12x','40x','50x']
            ls_price = [600.00,850.00,600.00,850.00,850.00,950.00,400.00,350.00,350.00,350.00,980.00,970.00]
            self.cur.execute(f'Select Count(*) from {tb}')
            row_count = self.cur.fetchone()[0]
            if row_count == 0:
                for a,b,c,d,e,f in zip(ls_model2,ls_speed,ls_ram,ls_hd,ls_cd,ls_price):
                    self.cur.execute(f'Insert into {tb}(model,speed,ram,hd,cd,price) Values(%s,%s,%s,%s,%s,%s)',(a,b,c,d,e,f))
            else:
                print(f'Information has already been added to {tb}')
            self.con.commit()
        else:
            print('Database not found')
    def cr_printer(self,tb = 'Printer'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'Create table if not exists {tb}(id int primary key auto_increment,model int,color varchar(5),type varchar(20),price float)'
            self.cur.execute(sql)

            ls_model = [1276,1433,1434,1401,1408,1288]
            ls_color = ['n','y','y','n','n','n']
            ls_type = ['Laser','Jet','Jet','Matrix','Matrix','Laser']
            ls_price = [400.00,270.00,290.00,150.00,270.00,400.00]
            self.cur.execute(f'Select Count(*) from {tb}')
            row_count = self.cur.fetchone()[0]
            if row_count == 0:
                for a,b,c,d in zip(ls_model,ls_color,ls_type,ls_price):
                    self.cur.execute(f'Insert into {tb}(model,color,type,price) Values(%s,%s,%s,%s)',(a,b,c,d))
            else:
                print(f'Information has already been added to {tb}')
            self.con.commit()
        else:
            print('Database not found')
    def task_1(self,tb1 = 'Product',tb2 = 'PC'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'Select * from {tb2} Join {tb1} ON {tb2}.model = {tb1}.model')
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
    def task_2(self,tb1 = 'Product',tb2 = 'Laptop'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'Select * from {tb2} Join {tb1} ON {tb2}.model = {tb1}.model')
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
    def task_3(self,tb1 = 'Product',tb2 = 'Printer'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'Select * from {tb2} Join {tb1} ON {tb2}.model = {tb1}.model')
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
    def task_4(self,tb = 'Printer'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'Select model,type,price from {tb} where {tb}.color = "y" ')
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
    def task_5(self,tb = 'PC'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'select SUM(price) / COUNT(price) from {tb} where model = 1232 or model = 1233;')
            print(f'Average price of {tb}s by maker A: {self.cur.fetchone()[0]}')
        else:
            print('Database not found')
    def task_6(self,tb1 = 'Product',tb2 = 'PC'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            self.cur.execute(f'Select {tb1}.maker,{tb1}.model,{tb2}.speed from {tb1} Inner Join {tb2} ON {tb1}.model = {tb2}.model where {tb2}.speed > 450')
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
    def task_7(self,tb1 = 'Product',tb2 = 'PC'):
        if Database.db is not None:
            self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'SELECT {tb1}.maker, MAX({tb2}.price) AS most_expensive_PC FROM {tb1} INNER JOIN {tb2} ON {tb1}.model = {tb2}.model WHERE {tb1}.type = "{tb2}" GROUP BY {tb1}.maker;'
            self.cur.execute(sql)
            info = self.cur.fetchall()
            for i in info:
                print(i)
        else:
            print('Database not found')
db = Database()
# db.cr_table()
# db.cr_lp()
# db.cr_pc()
# db.cr_printer()
# db.task_1()
# db.task_2()
# db.task_3()
# db.task_4()
# db.task_5()
# db.task_6()
# db.task_7()

# 2-task
class Food:
    db = None
    def __init__(self,dbName = 'National_food'):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702')
        self.kur = self.con.cursor()
        self.kur.execute(f'Create database if not exists {dbName}')
        self.con.commit()
        Food.db = dbName
    def base(self):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Food.db}')
        self.kur = self.con.cursor()
    def cr_table(self,tb = 'Meals'):
        self.base()
        sql = f'Create table if not exists {tb}(id int primary key auto_increment,name varchar(30),ingredients varchar(30))'
        self.kur.execute(sql)

        ls = ['Pilaf','Shashlik','Lagman','Manti','Samsa','Shurpa','Narin','Dimlama','Chuchvara','Mashhorda']
        ing = ['Meat, Carrots, Rice','Meat, Bread','Noodles, Vegetables, Meat','Minced meat, Onions','Meat, Onions, Spices',
        'Meat, Vegetables, Herbs','Meat, Noodles','Meat, Potatoes, Vegetables','Minced meat, Dough','Beans, Rice, Meat']
        self.kur.execute(f'Select Count(*) from {tb}')
        row_count = self.kur.fetchone()[0]
        if row_count == 0:
            for x,y in zip(ls,ing):
                self.kur.execute(f'Insert into {tb}(name,ingredients) Values(%s,%s)',(x,y))
        else:
            print(f'Information has already been added to {tb}')
        self.con.commit()
    def find_meal(self,tb = 'Meals'):
        self.base()
        self.kur.execute(f'Select * from {tb} where name like "%a" ')
        info = self.kur.fetchall()
        for i in info:
            print(i)
    def find_ingredient(self,tb = 'Meals',ingr = 'Rice'):
        self.base()
        self.kur.execute(f'Select * from {tb} where ingredients LIKE "%{ingr}%" ')
        info = self.kur.fetchall()
        for i in info:
            print(i)
f = Food()
# f.cr_table()
# f.find_meal()
# print('*' * 44)
# f.find_ingredient()

class Market:
    db = None
    def __init__(self,dbName = 'Market'):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702')
        self.kur = self.con.cursor()
        self.kur.execute(f'Create database if not exists {dbName}')
        self.con.commit()
        Market.db = dbName
    def base(self):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Market.db}')
        self.kur = self.con.cursor()
    def cr_table(self,tb = 'Fruit'):
        self.base()
        