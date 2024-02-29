import os
os.system('cls' if os.name == 'nt' else 'clear')

import widgets

# init
quote = widgets.info()
line = widgets.info()
dat = widgets.datemanager()




# Output
dat.today()
line.line()
print(quote.rand_quote())
#line.line()

#widgets.quotes()
