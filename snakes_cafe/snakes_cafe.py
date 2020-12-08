
# Variable Declarations
orders = {}

menu = {
  "Appetizers" : ['Wings', 'Cookies', 'Spring Rolls'],

  "Entrees" : ['Salmon', 'Steak', 'Meat Tornado', 'A literal Garden'],

  "Desserts" : ['Ice Cream', 'Cake', 'Pie'],

  "Drinks" : ['Coffee', 'Tea', 'Unicorn Tears'],
  
}

# formatting variables
app_block_seperator = ("*" * 34)
menu_block_seperator = ("-" * 9)

# Print initialization of app
print(app_block_seperator)
print("*" * 2 + "     Welcome to Snakes Cafe    " + "*" * 2)
print("*" * 2 + "   Please see our menu below   " + "*" * 2)
print("*" * 2)
print("*" * 2 + "To quit at any time, type 'quit' " + "*" * 2)
print(app_block_seperator + '\n')

# get a list of menu sections
menu_section = list(menu.keys()) 
 
# iterate through menu sections and their children and print to page
for course in menu_section:
  dishes = list(menu[course])
  
  print('\n' + menu_section[menu_section.index(course)] + '\n' + menu_block_seperator)

  for item in dishes: 
    print(item)

print('\n')

# prompt user for input
print(app_block_seperator)
print('*' * 2 + ' What would you like to order? ' + '*' * 2)
print(app_block_seperator)

def take_order():
  user_input = ' '

  while(user_input != 'quit'):
    user_input = input(' >')
    # confirm processing of user input and append the orders dictionary
    if (user_input in orders):
      orders[user_input] += 1
      order_confirmation(user_input)
    elif(user_input == 'quit'):
      # get keys of the Order dictionary
      ticket = list(orders.keys())
      
      # print Orders dictionary 
      for check in ticket:
        print(ticket[ticket.index(check)] + " " + str(orders[check]) + "\n")

      break
    
    else:
      orders[user_input] = 1

      order_confirmation(user_input)
      continue

def order_confirmation(user_input):
   print("*" * 2 + " " + str(orders[user_input]) + " " + user_input + " has been added to your meal " + "*" * 2)


take_order()    
      
 












