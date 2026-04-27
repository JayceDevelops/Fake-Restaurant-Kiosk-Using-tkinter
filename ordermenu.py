import tkinter as tk
from tkinter import messagebox
from datetime import datetime

### ITEMS MADE USING AI (GEMINI) ###
#   1. Resturant Logo (CompanyLogo.ico) 
#   2. Picture Of Burgers, Fries, Drinks, and Desserts. It only made a picture of the food itself, I made the holder that the foods price and description is in. 
#   3. Fake descriptions and prices for the food. 
#   4. Partial App layout such as where buttons should be places for a minimalist design
#################################

# EVERYTHING ELSE WAS DESIGNED AND IMPLEMENTED BY ME. 

class OrderMenu:
   
   def __init__(self):
      self._mode = 'dark'
      self._photoPath = 'assets/darkmode/'
      self._colors: dict = {
         'Background': '#1A1A1A',
         'Primary':  '#D4AF37',
         'Secondary': '#C41E3A',
         'Border': '#525252',
         'Frame': '#B4B4B8'
      }

      self._itemsPrice: dict = {
         
         # Burgers
         "The Trojan": 18.99,
         "The Spartan": 14.99,
         "The Viking": 16.99,
         "The Samurai": 15.99,
         "The Ninja": 14.99,
         "The Amazon": 15.99,

         # Sides
         "Amazon Elote Bites": 8.49,
         "Ninja Black Bean Sliders": 8.99,
         "Samurai Edamame Pods": 5.99,
         "Spartan Fries": 4.99,
         "Trojan Truffle Tots": 7.99,
         "Viking Sriracha Slaw": 6.99,
         
         # Drinks
         "The Battle Axe": 5.49,
         "The Horn": 6.99,
         "The Plume": 4.99,
         "The Shield": 4.49,
         "The Sword": 5.49,
         "The Spear": 5.99,

         # Desserts
         "Viking Cinnamon Rolls": 9.99,
         "The Valhalla Lava Cake": 11.99,
         "Spartan Cheesecake Bites": 8.99,
         "The Trophy Brownie": 10.99,
         "The Victory Cake": 10.99,
         "The Banner Sunday": 12.99
      }

      self._orderCount = 0
      self._orderTotal: float = 0.0
      self._orderItemCount = 0
      self._order = ""
     

      # Window
      self._window = tk.Tk()
      self.configureWindow()

      # Heading
      self.configureHeading()

      # Selection
      self.configureFoodOptions()

      # Order
      self.configureOrder()

      # Order Control Buttons
      self.configureOrderControl()

      # Menu Items
      self.menuItems()

      # Heading 
      tk.mainloop()
   
   def configureWindow(self) -> None:

      # Window Size & Grid
      self._window.geometry('1250x700')

      # Rows
      self._window.rowconfigure(0)
      self._window.rowconfigure(1)
      self._window.rowconfigure(2)

      # Columns
      #self._window.columnconfigure(0)
      #self._window.columnconfigure(1)
      #self._window.columnconfigure(2)

      # Window Color & Resizeability
      self._window.configure(background=self._colors['Background'])
      self._window.resizable(False, False)

      # Window Task Bar
      self._window.title("")
      self._window.iconbitmap('assets/companyLogo.ico')


   def configureHeading(self):

      # Heading Image 
      self._companyLogoImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'CompanyLogo.png')
      self._companyLogo: tk.Label = tk.Label(
         self._window, 
         image=self._companyLogoImage, 
         width=100, 
         height=100, 
         background=self._colors['Background']
      )
      self._companyLogo.grid(row=0, sticky='w')

      # Lighting Mode Button
      self._lightingButtonImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'Mode.png')
      self._lightingButton: tk.Button = tk.Button(
         self._window, 
         image = self._lightingButtonImage, 
         width = 256, 
         height = 100, 
         background = self._colors['Background'], 
         relief = 'flat',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.lightingModeChange()
      )
      self._lightingButton.grid(row=0, sticky='w', padx=(975, 0))

   
   def configureFoodOptions(self):

      # Frame For Food Option Buttons
      self._foodTypesFrame: tk.Frame = tk.Frame(
         self._window,
         background = self._colors['Background'],
         highlightbackground = self._colors['Frame'],
         highlightthickness = 1,
         bd = 0,
         width = 2,
         height = 467
      )
      self._foodTypesFrame.grid(row=1, sticky='w', padx=(195, 0))

      # Food Option Buttons

      # Burgers
      self._burgerButtonImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'Burgers.png')
      self._burgerButton: tk.Button = tk.Button(
         self._window, 
         width = 164,
         height = 86,
         image = self._burgerButtonImage,
         background = self._colors['Background'],
         relief = 'flat',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.generateBurgers()
      )
      self._burgerButton.grid(row=1, sticky='nw', padx=(15, 0), pady=(5, 0))

      # Sides
      self._sidesButtonImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'Sides.png')
      self._sidesButton: tk.Button = tk.Button(
         self._window, 
         width = 164,
         height = 86,
         image = self._sidesButtonImage,
         background = self._colors['Background'],
         relief = 'flat',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.generateSides()
      )
      self._sidesButton.grid(row=1, sticky='nw', padx=(15, 0), pady=(130, 0))

      # Drinks
      self._drinksButtonImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'Drinks.png')
      self._drinksButton: tk.Button = tk.Button(
         self._window, 
         width = 164,
         height = 86,
         image = self._drinksButtonImage,
         background = self._colors['Background'],
         relief = 'flat',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.generateDrinks()
      )
      self._drinksButton.grid(row=1, sticky='nw', padx=(15, 0), pady=(260, 0))

      # Desserts
      self._dessertsButtonImage: tk.PhotoImage = tk.PhotoImage(file=self._photoPath + 'Desserts.png')
      self._dessertsButton: tk.Button = tk.Button(
         self._window, 
         width = 164,
         height = 86,
         image = self._dessertsButtonImage,
         background = self._colors['Background'],
         relief = 'flat',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.generateDesserts()
      )
      self._dessertsButton.grid(row=1, sticky='nw', padx=(15, 0), pady=(390, 0))

   def configureOrder(self):

      self._orderFrame: tk.Frame = tk.Frame (
         self._window, 
         background = self._colors['Background'], 
         highlightbackground = self._colors['Frame'], 
         highlightthickness = 1, 
         bd = 0, 
         width = 270, 
         height = 467
      )
      self._orderFrame.grid(row=1, column=0, sticky='w', padx=(975, 0))

      self._orderHeading: tk.Label = tk.Label(
         self._window,
         text = "Order",
         font = ('Arial', 15, 'bold'),
         background = self._colors['Background'],
         fg = '#FFF8E1'
      )
      self._orderHeading.grid(row=1, sticky='w', padx=(1075, 0), pady=(0, 430))

   def configureOrderControl(self):
      
      # Cancel Order
      self._cancelOrderImage: tk.PhotoImage = tk.PhotoImage(file='assets/CancelOrder.png')
      self._cancelOrder: tk.Button = tk.Button(
         self._window,
         background = self._colors['Secondary'],
         image = self._cancelOrderImage,
         width = 180,
         height = 80,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.cancelOrder()
      )
      self._cancelOrder.grid(row=2, sticky='w', padx=(15, 0), pady=(10, 0))
      
      # Place Order
      self._placeOrderImage: tk.PhotoImage = tk.PhotoImage(file='assets/PlaceOrder.png')
      self._placeOrder: tk.Button = tk.Button(
         self._window,
         background = self._colors['Secondary'],
         image = self._placeOrderImage,
         width = 270,
         height = 80,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.placeOrder()
      )
      self._placeOrder.grid(row=2, sticky='w', padx=(975, 0), pady=(10, 0))

   def menuItems(self): 
      
      self._firstItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Spartan.png')
      self._firstItem: tk.Button = tk.Button(
         self._window, 
         image=self._firstItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Spartan")
      )
      self._firstItem.grid(row = 1, sticky='w', padx=(230, 0), pady=(0, 240))

      self._secondItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Viking.png')
      self._secondItem: tk.Button = tk.Button(
         self._window, 
         image=self._secondItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Viking")
      )
      self._secondItem.grid(row = 1, sticky='w', padx=(480, 0), pady=(0, 240))

      self._thirdItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Trojan.png')
      self._thirdItem: tk.Button = tk.Button(
         self._window, 
         image=self._thirdItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Trojan")
      )
      self._thirdItem.grid(row = 1, sticky='w', padx=(730, 0), pady=(0, 240))

      self._fourthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Amazon.png')
      self._fourthItem: tk.Button = tk.Button(
         self._window, 
         image=self._fourthItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Amazon")
      )
      self._fourthItem.grid(row = 1, sticky='w', padx=(230, 0), pady=(240, 0))

      self._fifthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Samurai.png')
      self._fifthItem: tk.Button = tk.Button(
         self._window, 
         image=self._fifthItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Samurai")
      )
      self._fifthItem.grid(row = 1, sticky='w', padx=(480, 0), pady=(240, 0))

      self._sixthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/The Ninja.png')
      self._sixthItem: tk.Button = tk.Button(
         self._window, 
         image=self._sixthItemImage,
         height = 225,
         width = 210,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.configureBurger("The Ninja")
      )
      self._sixthItem.grid(row = 1, sticky='w', padx=(730, 0), pady=(240, 0))

   # Button Functions

   def addItemToOrder(self, itemName, wants = '', itemCount = 1):
      if self._orderItemCount + 1 <= 23:
         self._orderItemCount += 1
         if self._mode == 'light':
            Background = '#FFF8E1'
            Forground = self._colors['Background']
         else:
            Background = self._colors['Background']
            Forground = '#FFF8E1'

         if itemName == 'The Amazon' or itemName == 'The Ninja' or itemName == 'The Samurai' or itemName == 'The Spartan' or itemName == 'The Trojan' or itemName == 'The Viking':
            newOrder = f'{itemName} x {itemCount}     ${self._itemsPrice[itemName] * itemCount}'
            
            if 'o' in wants: newOrder += f'\n Onions|'
            if 'l' in wants: newOrder += f'Lettuce|'
            if 't' in wants: newOrder += f'Tomato|'
            if 's' in wants: newOrder += f'Sauce'
         else:
            newOrder: str = f'{itemName} x 1     ${self._itemsPrice[itemName]}'

         self._order += '\n' + newOrder
         self._orderTotal += self._itemsPrice[itemName] * itemCount

         self._item: tk.Label = tk.Label(
            self._window,
            text = self._order,
            width = 32,
            height = 24,
            font = ('Ariel', 10, 'bold'),
            justify='left',
            anchor='nw',
            foreground= Forground,
            background = Background
         )
         self._item.grid(row=1, padx=(979, 0), pady=(0, 0) ,sticky='w')

         self._price: tk.Label = tk.Label(
            self._window,
            text = f'Total: ${self._orderTotal:.2f}',
            width = 15,
            height = 1,
            font = ('Ariel', 10, 'bold'),
            justify='left',
            anchor='w',
            foreground= Forground,
            background = Background
         )
         self._price.grid(row=1, padx=(979, 0), pady=(425, 0) ,sticky='w')
      else:
         messagebox.showerror("Order Item Count Error", "You may not have more then 23 unique items on your order. Please place your order and start another. Sorry for the inconvience.")



   def lightingModeChange(self):

      if self._mode == 'dark':

         self._mode = 'light'
         self._photoPath = 'assets/lightmode/'

         Background = '#FFF8E1'
         Primary = '#C41E3A'
         Secondary = '#D4AF37'
         Border = '#1A1A1A'

         self._window.configure(background=Background)

         # Heading Change
         self._companyLogoImage.configure(file=self._photoPath + 'CompanyLogo.png')
         self._companyLogo.configure(background=Background)

         self._lightingButtonImage.configure(file=self._photoPath + 'Mode.png')
         self._lightingButton.configure(background=Background, activebackground=Background)

         # Frame Border Change
         self._foodTypesFrame.configure(background=Background, highlightbackground=Border)
         self._orderFrame.configure(background=Background, highlightbackground=Border)

         # Option Image Change
         self._burgerButtonImage.configure(file=self._photoPath + 'Burgers.png')
         self._burgerButton.configure(background=Background, activebackground=Background)

         self._sidesButtonImage.configure(file=self._photoPath + 'Sides.png')
         self._sidesButton.configure(background=Background, activebackground=Background)

         self._drinksButtonImage.configure(file=self._photoPath + 'Drinks.png')
         self._drinksButton.configure(background=Background, activebackground=Background)

         self._dessertsButtonImage.configure(file=self._photoPath + 'Desserts.png')
         self._dessertsButton.configure(background=Background, activebackground=Background)

         # Order Heading Change
         self._orderHeading.configure(background=Background, fg=self._colors['Background'])

         # Changing Background When Button Is Clicked

         # Menu Items
         self._firstItem.configure(activebackground=Background)
         self._secondItem.configure(activebackground=Background)
         self._thirdItem.configure(activebackground=Background)
         self._fourthItem.configure(activebackground=Background)
         self._fifthItem.configure(activebackground=Background)
         self._sixthItem.configure(activebackground=Background)

         # Order Control
         self._cancelOrder.configure(activebackground=Background)
         self._placeOrder.configure(activebackground=Background)
         
         # Item Label
         self._item.configure(foreground=self._colors['Background'], background = Background)

         # Total Label
         self._price.configure(background=Background, foreground=self._colors['Background'])
         
      else:
         self._mode = 'dark'
         
         self._photoPath = 'assets/darkmode/'

         self._window.configure(background=self._colors['Background'])

         # Heading
         self._companyLogoImage.configure(file=self._photoPath + 'CompanyLogo.png')
         self._companyLogo.configure(background=self._colors['Background'])

         self._lightingButtonImage.configure(file=self._photoPath + 'Mode.png')
         self._lightingButton.configure(background=self._colors['Background'], activebackground=self._colors['Background'])

         # Frame Border Change
         self._foodTypesFrame.configure(background=self._colors['Background'], highlightbackground=self._colors['Frame'])
         self._orderFrame.configure(background=self._colors['Background'], highlightbackground=self._colors['Frame'])

         # Option Image Change
         self._burgerButtonImage.configure(file=self._photoPath + 'Burgers.png')
         self._burgerButton.configure(background=self._colors['Background'], activebackground=self._colors['Background'])

         self._sidesButtonImage.configure(file=self._photoPath + 'Sides.png')
         self._sidesButton.configure(background=self._colors['Background'], activebackground=self._colors['Background'])

         self._drinksButtonImage.configure(file=self._photoPath + 'Drinks.png')
         self._drinksButton.configure(background=self._colors['Background'], activebackground=self._colors['Background'])

         self._dessertsButtonImage.configure(file=self._photoPath + 'Desserts.png')
         self._dessertsButton.configure(background=self._colors['Background'], activebackground=self._colors['Background'])

         # Order Heading Change
         self._orderHeading.configure(background=self._colors['Background'], fg='#FFF8E1')

         # Changing Background When Button Is Clicked

         # Menu Items
         self._firstItem.configure(activebackground=self._colors['Background'])
         self._secondItem.configure(activebackground=self._colors['Background'])
         self._thirdItem.configure(activebackground=self._colors['Background'])
         self._fourthItem.configure(activebackground=self._colors['Background'])
         self._fifthItem.configure(activebackground=self._colors['Background'])
         self._sixthItem.configure(activebackground=self._colors['Background'])

         # Order Control
         self._cancelOrder.configure(activebackground=self._colors['Background'])
         self._placeOrder.configure(activebackground=self._colors['Background'])

         # Item Label
         self._item.configure(foreground='#FFF8E1', background = self._colors['Background'])

         # Total Label
         self._price.configure(background=self._colors['Background'], foreground='#FFF8E1')
   
   def generateBurgers(self):
      self._currentTab = 'burgers'
      self._firstItemImage.configure(file='assets/burgers/The Spartan.png')
      self._secondItemImage.configure(file='assets/burgers/The Trojan.png')
      self._thirdItemImage.configure(file='assets/burgers/The Viking.png')
      self._fourthItemImage.configure(file='assets/burgers/The Amazon.png')
      self._fifthItemImage.configure(file='assets/burgers/The Samurai.png')
      self._sixthItemImage.configure(file='assets/burgers/The Ninja.png')

      self._firstItem.configure(command= lambda: self.configureBurger("The Spartan"))
      self._secondItem.configure(command=lambda: self.configureBurger("The Trojan"))
      self._thirdItem.configure(command=lambda: self.configureBurger("The Viking"))
      self._fourthItem.configure(command=lambda: self.configureBurger("The Amazon"))
      self._fifthItem.configure(command=lambda: self.configureBurger("The Samurai"))
      self._sixthItem.configure(command=lambda: self.configureBurger("The Ninja"))



   def generateSides(self):
      self._currentTab = 'sides'
      self._firstItemImage.configure(file='assets/sides/SpartanFries.png')
      self._secondItemImage.configure(file='assets/sides/TrojanTots.png')
      self._thirdItemImage.configure(file='assets/sides/VikingSlaw.png')
      self._fourthItemImage.configure(file='assets/sides/AmazonBites.png')
      self._fifthItemImage.configure(file='assets/sides/SamuraiPods.png')
      self._sixthItemImage.configure(file='assets/sides/NinjaSliders.png')

      self._firstItem.configure(command= lambda: self.addItemToOrder("Spartan Fries"))
      self._secondItem.configure(command=lambda: self.addItemToOrder("Trojan Truffle Tots"))
      self._thirdItem.configure(command=lambda: self.addItemToOrder("Viking Sriracha Slaw"))
      self._fourthItem.configure(command=lambda: self.addItemToOrder("Amazon Elote Bites"))
      self._fifthItem.configure(command=lambda: self.addItemToOrder("Samurai Edamame Pods"))
      self._sixthItem.configure(command=lambda: self.addItemToOrder("Ninja Black Bean Sliders"))


   def generateDrinks(self):
      self._currentTab = 'drinks'
      self._firstItemImage.configure(file='assets/drinks/TheSpear.png')
      self._secondItemImage.configure(file='assets/drinks/TheSword.png')
      self._thirdItemImage.configure(file='assets/drinks/TheHorn.png')
      self._fourthItemImage.configure(file='assets/drinks/TheAxe.png')
      self._fifthItemImage.configure(file='assets/drinks/TheShield.png')
      self._sixthItemImage.configure(file='assets/drinks/ThePlume.png')

      self._firstItem.configure(command=lambda: self.addItemToOrder("The Spear"))
      self._secondItem.configure(command=lambda: self.addItemToOrder("The Sword"))
      self._thirdItem.configure(command=lambda: self.addItemToOrder("The Horn"))
      self._fourthItem.configure(command=lambda: self.addItemToOrder("The Battle Axe"))
      self._fifthItem.configure(command=lambda: self.addItemToOrder("The Shield"))
      self._sixthItem.configure(command=lambda: self.addItemToOrder("The Plume"))
   
   def generateDesserts(self):
      self._currentTab = 'desserts'
      self._firstItemImage.configure(file='assets/desserts/SpartanCheesecake.png')
      self._secondItemImage.configure(file='assets/desserts/TheBrownie.png')
      self._thirdItemImage.configure(file='assets/desserts/TheCake.png')
      self._fourthItemImage.configure(file='assets/desserts/LavaCake.png')
      self._fifthItemImage.configure(file='assets/desserts/CinnamonRolls.png')
      self._sixthItemImage.configure(file='assets/desserts/TheSunday.png')

      self._firstItem.configure(command=lambda: self.addItemToOrder("Spartan Cheesecake Bites"))
      self._secondItem.configure(command=lambda: self.addItemToOrder("The Trophy Brownie"))
      self._thirdItem.configure(command=lambda: self.addItemToOrder("The Victory Cake"))
      self._fourthItem.configure(command=lambda: self.addItemToOrder("The Valhalla Lava Cake"))
      self._fifthItem.configure(command=lambda: self.addItemToOrder("Viking Cinnamon Rolls"))
      self._sixthItem.configure(command=lambda: self.addItemToOrder("The Banner Sunday"))

   def configureBurger(self, burgertype: str):
      
      self._onions: bool = True
      self._tomatos: bool = True
      self._lettuce: bool = True
      self._sauce: bool = True

      self._itemCount = 1
      
      self._burgerConfigWindow = tk.Tk()

      # Window Config
      self._burgerConfigWindow.geometry("250x550")
      self._burgerConfigWindow.title("")
      self._burgerConfigWindow.iconbitmap('assets/companyLogo.ico')
      self._burgerConfigWindow.resizable(False, False)

      if self._mode == 'dark':
         photoPath: str = 'assets/darkmode/'
         Background = self._colors['Background']
         self._burgerConfigWindow.configure(background=Background)
      else: 
         photoPath: str = 'assets/lightmode/'
         Background = '#FFF8E1'
         self._burgerConfigWindow.configure(background=Background)

      
      # Burger Image 
      self._burgerImage: tk.PhotoImage = tk.PhotoImage(file=f'assets/burgers/{burgertype}.png', master=self._burgerConfigWindow)
      self._burgerItem: tk.Label = tk.Label(
         self._burgerConfigWindow, 
         image=self._burgerImage,
         height = 225,
         width = 210,
         border = 0
      )
      self._burgerItem.grid(row = 0, sticky='w', padx=(20, 0), pady=(10, 0))

      self._onionsImage: tk.PhotoImage = tk.PhotoImage(file=f'{photoPath}CheckedOnions.png', master=self._burgerConfigWindow)
      self._onions: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 205,
         height = 40,
         image = self._onionsImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
          command= lambda: changeItemChecked("onions", photoPath)
      )
      self._onions.grid(row=1, sticky='w', padx=(20, 0), pady=(20, 0))

      self._tomatosImage: tk.PhotoImage = tk.PhotoImage(file=f'{photoPath}CheckedTomatos.png', master=self._burgerConfigWindow)
      self._tomatos: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 205,
         height = 40,
         image = self._tomatosImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
         command= lambda: changeItemChecked("tomatos", photoPath)
      )
      self._tomatos.grid(row=2, sticky='w', padx=(20, 0), pady=(10, 0))

      self._lettuceImage: tk.PhotoImage = tk.PhotoImage(file=f'{photoPath}CheckedLettuce.png', master=self._burgerConfigWindow)
      self._lettuce: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 205,
         height = 40,
         image = self._lettuceImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
          command= lambda: changeItemChecked("lettuce", photoPath)
      )
      self._lettuce.grid(row=3, sticky='w', padx=(20, 0), pady=(10, 0))

      self._sauceImage: tk.PhotoImage = tk.PhotoImage(file=f'{photoPath}CheckedSauce.png', master=self._burgerConfigWindow)
      self._sauce: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 205,
         height = 40,
         image = self._sauceImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
          command= lambda: changeItemChecked("sauce", photoPath)
      )
      self._sauce.grid(row=4, sticky='w', padx=(20, 0), pady=(10, 0))

      self._add: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 2,
         height = 1,
         text = "+",
         background = self._colors['Background'],
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
         font = ('Ariel', 12, 'bold'),
         foreground = '#FFF8E1',
         command= lambda: add()
      )
      self._add.grid(row=5, sticky='w', padx=(73, 0), pady=(10, 0))

      self._count: tk.Label = tk.Label(
         self._burgerConfigWindow, 
         width = 2,
         height = 1,
         text = "1",
         background = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0,
         font = ('Ariel', 12, 'bold'),
         foreground = '#FFF8E1',
      )
      self._count.grid(row=5, sticky='w', padx=(110, 0), pady=(10, 0))

      self._subtract: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 2,
         height = 1,
         text = "-",
         background = self._colors['Background'],
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
         font = ('Ariel', 15, 'bold'),
         foreground = '#FFF8E1',
         command= lambda: subtract()
      )
      self._subtract.grid(row=5, sticky='w', padx=(144, 0), pady=(10, 0))

      if self._mode == "light":
         self._add.configure(background=Background, fg=self._colors['Background'])
         self._count.configure(background=Background, fg=self._colors['Background'])
         self._subtract.configure(background=Background, fg=self._colors['Background'])

      self._cancelImage: tk.PhotoImage = tk.PhotoImage(file='assets/CancelItem.png', master=self._burgerConfigWindow)
      self._cancelItem: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 92,
         height = 40,
         background='#FFF8E1',
         image = self._cancelImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.cancelItem()
      )
      self._cancelItem.grid(row=6, sticky='w', padx=(20, 0), pady=(10, 0))

      self._addToOrderImage: tk.PhotoImage = tk.PhotoImage(file='assets/AddItem.png', master=self._burgerConfigWindow)
      self._addToOrder: tk.Button = tk.Button(
         self._burgerConfigWindow, 
         width = 92,
         height = 40,
         background='#FFF8E1',
         image = self._addToOrderImage,
         activebackground = Background,
         highlightthickness = 0,
         borderwidth = 0,
         command = lambda: self.addBurgerToOrder(burgertype, self._itemCount)
      )
      self._addToOrder.grid(row=6, sticky='w', padx=(133, 0), pady=(10, 0))

      def changeItemChecked(item: str, path: str):
         match item:
            case "onions":
               if self._onions:
                  self._onions = False
                  self._onionsImage.configure(file=f'{path}Onions.png')
               else:
                  self._onions = True
                  self._onionsImage.configure(file=f'{path}CheckedOnions.png')
            
            case "tomatos":
               if self._tomatos:
                  self._tomatos = False
                  self._tomatosImage.configure(file=f'{path}Tomatos.png')
               else:
                  self._tomatos = True
                  self._tomatosImage.configure(file=f'{path}CheckedTomatos.png')
            
            case "lettuce":
               if self._lettuce:
                  self._lettuce = False
                  self._lettuceImage.configure(file=f'{path}Lettuce.png')
               else:
                  self._lettuce = True
                  self._lettuceImage.configure(file=f'{path}CheckedLettuce.png')

            case "sauce":
               if self._sauce:
                  self._sauce = False
                  self._sauceImage.configure(file=f'{path}Sauce.png')
               else:
                  self._sauce = True
                  self._sauceImage.configure(file=f'{path}CheckedSauce.png')
      
      def add():
         if self._itemCount + 1 <= 10:
            self._itemCount += 1
            self._count.configure(text=f'{self._itemCount}')
         else:
            messagebox.showerror("Item Count Error", "You may only order a maximum of 10 per item. Sorry for the inconvience.")
      
      def subtract():
         if self._itemCount - 1 > 0:
            self._itemCount -= 1
            self._count.configure(text=f'{self._itemCount}')
         else:
            messagebox.showerror("Item Count Error", "You must order at minimum 1 per item to add item to order.")


      self._burgerConfigWindow.mainloop()

   def addBurgerToOrder(self, burgerName, burgerCount):
      order = ''

      if self._onions:
         order += 'o'
      
      if self._tomatos:
         order += 't'

      if self._lettuce:
         order += 'l'
      
      if self._sauce:
         order += 's'

      self._burgerConfigWindow.destroy()
      self.addItemToOrder(burgerName, order, burgerCount)
      

   def cancelItem(self):
      response = messagebox.askyesno("Cancel", "Are you sure you want to cancel?")

      if response:
         self._burgerConfigWindow.destroy()
   
   def cancelOrder(self):
      response = messagebox.askyesno("Cancel Order", "Are you sure you want to cancel this order and start over?")

      if response:
         self._order = ""
         self._item.configure(text=self._order)

         self._orderTotal = 0
         self._price.configure(text=f'Total: ${self._orderTotal:.2f}')

   def placeOrder(self):
      self._orderCount += 1

      now = datetime.now()
      self._dayandtime = now.strftime('%d/%m/%Y %H:%M:%S')

      self._order: str = f'### Order {self._orderCount} @ {str(self._dayandtime)} ###{self._order}\n\n'
 
      with open('orders.txt', 'a') as file:
         file.write(self._order)
      
      self._order = ""
      self._item.configure(text=self._order)

      self._orderTotal = 0
      self._price.configure(text=f'Total: ${self._orderTotal:.2f}')

      self._orderItemCount = 0


def main():
   menu: OrderMenu = OrderMenu()

if __name__ == '__main__':
   main()