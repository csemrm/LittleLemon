# LittleLemon
Final Project of [APIs Course by Meta](https://www.coursera.org/learn/apis?specialization=meta-back-end-developer)

* Developed RESTful APIs of a restaurant app using Django REST framework
* Used Djoser library for user management and authentication
* Worked with permissions in Django
* Implemented throttling to secure the APIS

In this project, the APIs need to make it possible for end-users to perform certain tasks and the reviewer will be looking for the following functionalities.

1.  The admin can assign users to the manager group

2.  You can access the manager group with an admin token

3.  The admin can add menu items

4.  The admin can add categories

5.  Managers can log in

6.  Managers can update the item of the day

7.  Managers can assign users to the delivery crew

8.  Managers can assign orders to the delivery crew

9.  The delivery crew can access orders assigned to them

10. The delivery crew can update an order as delivered

11. Customers can register

12. Customers can log in using their username and password and get access tokens

13. Customers can browse all categories

14. Customers can browse all the menu items at once

15. Customers can browse menu items by category

16. Customers can paginate menu items

17. Customers can sort menu items by price

18. Customers can add menu items to the cart

19. Customers can access previously added items in the cart

20. Customers can place orders

21. Customers can browse their own orders


RUBRIC
Test if the admin can assign users to the manager group:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/groups/manager/users
 with a valid admin token and a valid username in the HTTP REQUEST body.

Was the user added to the manager group with an admin token?


1 pt
Yes

0 pts
No
 Test if you can access the manager group with an admin token:

Make a GET call to
http://127.0.0.1:8000/api/groups/manager/users
 with an admin token.

Is there a list of users from the manager group in the API output?


1 pt
Yes

0 pts
No
Test if the admin can add menu items:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/menu-items
 with the admin token and necessary data. Or, log into the Django admin panel as super admin and then browse this endpoint in your browser and add some menu items.

Can the admin add menu items?


1 pt
Yes

0 pts
No
Test if the admin can add categories:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/categories
 with the admin token and necessary data. Or log into the Django admin panel as super admin and then browse this endpoint in your browser and add some menu items.

Can the admin add categories?


1 pt
Yes

0 pts
No
Test if the manager can log in:

Make a POST call to this endpoint
http://127.0.0.1:8000/auth/token/login/
 with the username and password of a manager.

Is the access token in the API output?




1 pt
Yes

0 pts
No
Test if the manager can update the item of the day:

Make a PATCH call to the endpoint of any single menu item endpoint like this
http://127.0.0.1:8000/api/menu-items/1
 with a manager token. Add a featured field in the REQUEST body with its value set to true or false.

Did the value of the featured field update for this particular menu item?


1 pt
Yes

0 pts
No
Test if the manager can assign users to the delivery crew:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/groups/manager/users
 with a valid manager token and a valid username in the HTTP REQUEST body.

Can the manager assign users to the delivery crew group?


1 pt
Yes

0 pts
No
Test if the manager can assign orders to the delivery crew:

Make a PATCH call to an endpoint of any single order item like this
http://127.0.0.1:8000/api/orders/1
  with a manager token. Add a delivery_crew field in the REQUEST body with its value set to any delivery crew user id.

Can the managers assign orders to a delivery crew?


1 pt
Yes

0 pts
No
Test if the delivery crew can view orders assigned to them:

Make a GET call to this endpoint
http://127.0.0.1:8000/api/orders
 with a delivery crew token.

Can the delivery crew browse orders that were assigned to them?


1 pt
Yes

0 pts
No
Test if the delivery crew can update an order as delivered:

Make a PATCH call to this endpoint to any single order item endpoint like this
http://127.0.0.1:8000/api/orders/1
  with a delivery crew token. Add a status field in the REQUEST body with its value set to true or false.

Can the delivery crew update the order status?


1 pt
Yes

0 pts
No
Test if customers can register:

Make a POST call to this endpoint
http://127.0.0.1:8000/auth/users/
 with a username, password and email in the HTTP REQUEST body.

Can customers register using this endpoint?




1 pt
Yes

0 pts
No
Test if customers can log in using their username and password and get access tokens:

 Make a POST call to this endpoint
http://127.0.0.1:8000/auth/token/login/
 with a valid username and password in the HTTP Request body.

 Is the access token visible in the API output?


1 pt
Yes

0 pts
No
Test if customers can browse all categories:

Make a GET API call to this endpoint
http://127.0.0.1/api/categories
 with a customer token

Are the categories visible to customers?


1 pt
Yes

0 pts
No
Test if customers can browse all menu items:

Make a GET API call to this endpoint
http://127.0.0.1/api/menu-items
 with a customer token

Are the menu items visible to customers?


1 pt
Yes

0 pts
No
Test if customers can browse menu items by category:

Make a GET API call to these endpoints,
http://127.0.0.1:8000/api/menu-items?search=Icecream
 or any available category name instead of Icecream with a customer token.

Do the menu items in the category display for customers?


1 pt
Yes

0 pts
No
Test if customers can paginate menu items:

Make a GET API call to the endpoints
http://127.0.0.1:8000/api/menu-items?page=1
 or
http://127.0.0.1:8000/api/menu-items?page=2
 with a customer token.

Do the menu items display proper pagination for customers?


1 pt
Yes

0 pts
No
Test if customers can sort menu items by price:

Make a GET API call to the endpoint
http://127.0.0.1:8000/api/menu-items?ordering=price
or
http://127.0.0.1:8000/api/menu-items?ordering=-price
with a customer token.

Are the menu items properly sorted by price in ascending or descending order for customers?


1 pt
Yes

0 pts
No
Test if customers can add menu items to the cart:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/cart/menu-items
 with a customer token. Add these fields with valid data in the REQUEST body for menuitem, unit_price, quantity.

Can customers add menu items to the cart?


1 pt
Yes

0 pts
No
Test if customers can see previously added items in the cart:

Make a GET call to this endpoint
http://127.0.0.1:8000/api/cart/menu-items
 with a customer token.

Are previous items added to the cart visible for customers?




1 pt
Yes

0 pts
No
Test if customers can place orders:

Make a POST call to this endpoint
http://127.0.0.1:8000/api/cart/orders
 with a customer token. Add only the date field with valid data in the REQUEST body. Here is a sample date – 2022-11-16.

Can customers successfully place an order?


1 pt
Yes

0 pts
No
Customers can view their own orders:

Make a GET call to this endpoint
http://127.0.0.1:8000/api/cart/orders
 with a customer token.

Can customers browse their own orders?


1 pt
Yes

0 pts
No