create table if not exists Products(product_id int primary key,low_fats enum('Y', 'N'),recyclable enum('Y', 'N'));

insert into Products(product_id,low_fats,recyclable) Values(0,'Y','N');

insert into Products(product_id,low_fats,recyclable) Values(1,'Y','Y');

insert into Products(product_id,low_fats,recyclable) Values(2,'N','Y');

insert into Products(product_id,low_fats,recyclable) Values(3,'Y','Y');

insert into Products(product_id,low_fats,recyclable) Values(4,'N','N');

select product_id from Products where low_fats = 'Y' and recyclable = 'Y';