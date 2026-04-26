import tkinter as tk

# ITEMS MADE USING AI (GEMINI):
# Company Logo 
# Pictures Of Burgers, description, and price
#
class OrderMenu:
   
   def __init__(self):
      self._mode = 'dark'
      self._currentTab = 'burgers'
      self._photoPath = 'assets/darkmode/'
      self._colors: dict = {
         'Background': '#1A1A1A',
         'Primary':  '#D4AF37',
         'Secondary': '#C41E3A',
         'Border': '#525252',
         'Frame': '#B4B4B8'
      }

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
         text = "Place Order",
         width = 180,
         height = 80,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._cancelOrder.grid(row=2, sticky='w', padx=(15, 0), pady=(10, 0))
      
      # Place Order
      self._placeOrderImage: tk.PhotoImage = tk.PhotoImage(file='assets/PlaceOrder.png')
      self._placeOrder: tk.Button = tk.Button(
         self._window,
         background = self._colors['Secondary'],
         image = self._placeOrderImage,
         text = "Place Order",
         width = 270,
         height = 80,
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._placeOrder.grid(row=2, sticky='w', padx=(975, 0), pady=(10, 0))

   def menuItems(self): 
      
      self._firstItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheSpartan.png')
      self._firstItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._firstItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._firstItem.grid(row = 1, sticky='w', padx=(230, 0), pady=(0, 240))

      self._secondItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheViking.png')
      self._secondItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._secondItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._secondItem.grid(row = 1, sticky='w', padx=(480, 0), pady=(0, 240))

      self._thirdItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheTrojan.png')
      self._thirdItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._thirdItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._thirdItem.grid(row = 1, sticky='w', padx=(730, 0), pady=(0, 240))

      self._fourthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheAmazon.png')
      self._fourthItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._fourthItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._fourthItem.grid(row = 1, sticky='w', padx=(230, 0), pady=(240, 0))

      self._fifthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheSamurai.png')
      self._fifthItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._fifthItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._fifthItem.grid(row = 1, sticky='w', padx=(480, 0), pady=(240, 0))

      self._sixthItemImage: tk.PhotoImage = tk.PhotoImage(file='assets/burgers/TheNinja.png')
      self._sixthItem: tk.Button = tk.Button(
         self._window, 
         text = "burger",
         image=self._sixthItemImage,
         height = 225,
         width = 210,
         background='green',
         activebackground = self._colors['Background'],
         highlightthickness = 0,
         borderwidth = 0
      )
      self._sixthItem.grid(row = 1, sticky='w', padx=(730, 0), pady=(240, 0))

   # Button Functions
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
   
   def generateBurgers(self):
      self._currentTab = 'burgers'
      self._firstItemImage.configure(file='assets/burgers/TheSpartan.png')
      self._secondItemImage.configure(file='assets/burgers/TheTrojan.png')
      self._thirdItemImage.configure(file='assets/burgers/TheViking.png')
      self._fourthItemImage.configure(file='assets/burgers/TheAmazon.png')
      self._fifthItemImage.configure(file='assets/burgers/TheSamurai.png')
      self._sixthItemImage.configure(file='assets/burgers/TheNinja.png')

   def generateSides(self):
      self._currentTab = 'sides'
      self._firstItemImage.configure(file='assets/sides/SpartanFries.png')
      self._secondItemImage.configure(file='assets/sides/TrojanTots.png')
      self._thirdItemImage.configure(file='assets/sides/VikingSlaw.png')
      self._fourthItemImage.configure(file='assets/sides/AmazonBites.png')
      self._fifthItemImage.configure(file='assets/sides/SamuraiPods.png')
      self._sixthItemImage.configure(file='assets/sides/NinjaSliders.png')

   def generateDrinks(self):
      self._currentTab = 'drinks'
      self._firstItemImage.configure(file='assets/drinks/TheSpear.png')
      self._secondItemImage.configure(file='assets/drinks/TheSword.png')
      self._thirdItemImage.configure(file='assets/drinks/TheHorn.png')
      self._fourthItemImage.configure(file='assets/drinks/TheAxe.png')
      self._fifthItemImage.configure(file='assets/drinks/TheShield.png')
      self._sixthItemImage.configure(file='assets/drinks/ThePlume.png')
   
   def generateDesserts(self):
      self._currentTab = 'desserts'
      self._firstItemImage.configure(file='assets/desserts/SpartanCheesecake.png')
      self._secondItemImage.configure(file='assets/desserts/TheBrownie.png')
      self._thirdItemImage.configure(file='assets/desserts/TheCake.png')
      self._fourthItemImage.configure(file='assets/desserts/LavaCake.png')
      self._fifthItemImage.configure(file='assets/desserts/CinnamonRolls.png')
      self._sixthItemImage.configure(file='assets/desserts/TheSunday.png')
   


def main():
   menu: OrderMenu = OrderMenu()

if __name__ == '__main__':
   main()