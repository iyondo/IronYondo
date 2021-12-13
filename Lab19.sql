SELECT * FROM olist.order_items;

#Question 1
SELECT order_id, max(price) FROM olist.order_items; #6735
SELECT order_id, min(price) FROM olist.order_items; #0.85

#Question 2

SELECT max(shipping_limit_date) FROM olist.order_items; #2020-04-10 00:35:08
SELECT min(shipping_limit_date) FROM olist.order_items; #2016-09-19 02:15:34
SELECT shipping_limit_date FROM olist.order_items  
WHERE shipping_limit_date BETWEEN '2016-09-19' AND '2020-04-10'order by shipping_limit_date ;
              

SELECT * FROM olist.customers; 

# Question 3: SP, RJ, MG, RS

SELECT customer_state, count(customer_id) FROM olist.customers
GROUP BY customer_state 
ORDER BY count(customer_id) desc
LIMIT 4;

# Question 4: Sao Paulo, Campinasm Guarulhos, Sao bernado do campo

SELECT customer_state, customer_city, count(customer_id) FROM olist.customers
WHERE customer_state = 'SP' 
GROUP BY customer_city
ORDER BY count(customer_id) desc
limit 4;


SELECT * FROM olist.closed_deals;

# Question 5: 841

SELECT distinct count(business_segment) FROM olist.closed_deals #SELECT DISTINCT permet d`éviter les doublons
WHERE business_segment != 'NULL';

# Question 6: No duplicate values
# construction_tools_house_garden, phone_mobile, home_decor

SELECT business_segment, sum(declared_monthly_revenue) FROM olist.closed_deals
GROUP BY business_segment
ORDER BY sum(declared_monthly_revenue) desc
LIMIT 3;


SELECT * FROM olist.order_reviews;

#Question 7: 407089

SELECT distinct sum(review_score) FROM olist.order_reviews;

# Question 8 :

SELECT distinct review_score, concat(review_comment_title, review_comment_message)  FROM olist.order_reviews



