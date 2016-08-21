import time

answer = input("Do you send prayers to Harambe? [yes/no] ")

monkey = 1

harambe = """\
                 _
             ,.-" "-.,
            /   ===   \\
           /  =======  \\
        __|  (o)   (0)  |__      
       / _|    .---.    |_ \\         
      | /.----/ O O \----.\ |       
       \/     |     |     \/        
       |                   |            
       |                   |           
       |                   |          
       _\   -.,_____,.-   /_         
   ,.-"  "-.,_________,.-"  "-.,
  /          |       |          \\  
 |           l.     .l           | 
 |            |     |            |
 l.           |     |           .l             
  |           l.   .l           | \,     
  l.           |   |           .l   \,    
   |           |   |           |      \,  
   l.          |   |          .l        |
    |          |   |          |         |
    |          |---|          |         |
    |          |   |          |         |
    /"-.,__,.-"\   /"-.,__,.-"\\"-.,_,.-"\\
   |            \ /            |         |
   |             |             |         |
    \__|__|__|__/ \__|__|__|__/ \_|__|__/ ​
"""

def blessings(monkey):
    while monkey > 1:
        print(harambe)
	
if answer == "yes":
    monkey = monkey + 1
    print("Your prayers have been recieved. Harambe pours his infinite blessings upon you.")
    print("")
    time.sleep(4)
    blessings(monkey)
else:
    print("What blasphemy is this!?")
    time.sleep(3)
    print("!!!")
    time.sleep(1)

