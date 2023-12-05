from tkinter import *
from expiriesModule import expiry
from InterestRateModule import interest
from StocksModule import stock_price_ccy
from tkinter.messagebox import *


def show_answer():

    stock_info = stock_price_ccy(ticker.get().upper())
    #ticker looks within stocks module for list  - puts to upper to avoid issues in imput
    stock_price = stock_info[0]
    #first element in list is stock price
    ccy = stock_info[1]
    #second element is CCY
    days = expiry(time.get().capitalize())
    #expiry module used to find the days of future until expiry
    interpolated_interest_rate = interest(days,ccy)
    #interpolator works out the interest rate with days and set to ccy curve
    duration = (days / 365)
    rate_basis = interpolated_interest_rate - float(borrow.get())
    #interest rate basis including any borrow cost/repo
    div_basis = float(div.get())*float(div2.get())
    #dividend basis net for any taxes
    Ans = round((float((stock_price * rate_basis * duration) - div_basis)),2)
    #Answer both in basis and below in futures price (Stock less basis)
    FP = round((float(stock_price + Ans)),2)

    blank.insert(0, Ans)
    blank2.insert(0,FP)

global start
start = 0

global refi_rate
refi_rate = 0.85

def borrow_change_increase():
    global start
    start += 0.001
    increase = round((float(start)),4)
    borrow.delete(0,END)
    blank.delete(0,END)
    blank2.delete(0,END)
    borrow.insert(0,float(increase))
    show_answer()


def borrow_change_decrease():
    global start
    start -= 0.001
    decrease = round((float(start)), 4)
    borrow.delete(0, END)
    blank.delete(0, END)
    blank2.delete(0, END)
    borrow.insert(0, float(decrease))
    show_answer()

def refinance_rate_increase():
    global refi_rate
    refi_rate += 0.01
    increase_refi = round((float(refi_rate)), 2)
    div2.delete(0, END)
    blank.delete(0, END)
    blank2.delete(0, END)
    div2.insert(0,float(increase_refi))
    show_answer()

def refinance_rate_decrease():
    global refi_rate
    refi_rate -= 0.01
    decrease_refi = round((float(refi_rate)), 2)
    div2.delete(0, END)
    blank.delete(0, END)
    blank2.delete(0, END)
    div2.insert(0, float(decrease_refi))
    show_answer()

def clear():
    ticker.delete(0,END)
    time.delete(0,END)
    borrow.delete(0,END)
    div.delete(0,END)
    div2.delete(0,END)
    blank.delete(0,END)
    blank2.delete(0,END)
    global start
    start = 0


#main GUI contruction.
main = Tk()
title = main.title('Futures PricerV1')
Label(main, text="Stock Ticker:").grid(row=0)
Label(main, text="Expiry:").grid(row=1)
Label(main, text="Borrow cost:").grid(row=2)
Label(main,text='Gross Dividend:').grid(row=3, pady=2)
Label(main,text='Refinancing Rate:').grid(row=4)
Label(main, text="The basis is:").grid(row=5, pady=5)
Label(main, text='Futures price is:').grid(row=6)

ticker = Entry(main)
time = Entry(main)
borrow = Entry(main)
div = Entry(main)
div2 = Entry(main)
blank = Entry(main)
blank2 = Entry(main)


ticker.configure(bg='lightgreen')
time.configure(bg='lightgreen')
borrow.configure(bg='lightgreen')
div.configure(bg='lightgreen')
div2.configure(bg='lightgreen')

ticker.grid(row=0, column=1)
time.grid(row=1, column=1)
borrow.grid(row=2, column=1)
div.grid(row=3, column=1)
div2.grid(row=4,column=1)
blank.grid(row=5, column=1)
blank2.grid(row=6, column=1)

Button(main, text='Quit', command=main.destroy).grid(row=8, column=0, sticky=W, pady=10)
Button(main, text='Show', command=show_answer).grid(row=8, column=1, sticky=W, pady=10)
Button(main, text='<', height=1, width=1, command=borrow_change_increase).grid(row=2,column=2,sticky=W, padx=4)
Button(main, text='>', height=1, width=1, command=borrow_change_decrease).grid(row=2,column=3,sticky=W)
Button(main, text='<', height=1, width=1, command=refinance_rate_increase).grid(row=4,column=2,sticky=W, padx=4)
Button(main, text='>', height=1, width=1, command=refinance_rate_decrease).grid(row=4,column=3,sticky=W)

Button(main, text='Clear all', command=clear).grid(row=0, column=3,sticky=W, pady=10)
mainloop()
