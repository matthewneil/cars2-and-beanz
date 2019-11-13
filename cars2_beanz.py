from bs4 import BeautifulSoup
import requests

print("Cars 2 4k Bluray Prices")

#Getting Price of Cars 2 4K bluray from MightyApe
source = requests.get('https://www.mightyape.co.nz/product/cars-2-4k-uhd-uhd-blu-ray/31420594').text
soup = BeautifulSoup(source, 'lxml')

carsMA = soup.find('span', class_='price').text.strip()
carsMA = carsMA.replace('$', '');
print("MightyApe.co.nz:\t$", carsMA)

#Getting Price of Cars 2 4K bluray from JB HiFi
source = requests.get('https://www.jbhifi.co.nz/family/cars-2/372219/').text
soup = BeautifulSoup(source, 'lxml')

carsJB = " ".join(soup.find('span', class_='amount regular').text.strip().split())
carsJB = carsJB.replace(' ', '');
carsJB = carsJB.replace('$', '');
print("jbhifi.co.nz:\t\t$", carsJB)

#Getting Heinz Beans Price from Countdown
source = requests.get('https://shop.countdown.co.nz/shop/productdetails?stockcode=362231&name=heinz-baked-beans&searchString=beanz').text
soup = BeautifulSoup(source, 'lxml')

print("\nHeinz Beanz Prices")

beanzCD = soup.find('span', class_='price din-medium').text.strip()
beanzCD = beanzCD.replace('$', '');
beanzCD = beanzCD.replace('ea', '').strip();
print("countdown.co.nz:\t$", beanzCD)

#Getting Heinz Beans Price from New World
source = requests.get('https://www.ishopnewworld.co.nz/product/5012022_ea_000nw?name=beanz-english-recipe-baked-beans').text
soup = BeautifulSoup(source, 'lxml')

beanzNW = " ".join(soup.find('div', class_='fs-price-lockup fs-price-lockup--large u-margin-bottom u-margin-top').text.strip().split())
beanzNW = beanzNW.replace('ea', '').strip();
beanzNW = beanzNW.replace(' ', '.');
print("newworld.co.nz:\t\t$", beanzNW)

#Calculate the best conbination in price
carsMA = float(carsMA)
carsJB = float(carsJB)
beanzCD = float(beanzCD)
beanzNW = float(beanzNW)

print("\nBest Combination is:")

total = 0

if carsMA < carsJB:
    print("MightyApe @ $", carsMA)
    total += carsMA
else:
    print("JB HiFi @ $", carsJB)
    total += carsJB

if beanzCD < beanzNW:
    print("Countdown @ $", beanzCD)
    total += beanzCD
else:
    print("New World @ $", beanzNW)
    total += beanzNW
    
print("\nTotal Price:", total) 
