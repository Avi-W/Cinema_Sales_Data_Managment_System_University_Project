import pandas
import datetime

#Movie Manipulation class
class MovieManipulation:

    #Inputs movie with the name: name and price of the ticket: TicketPrice to CurrentMovies.csv
    def inputMovie(currentMoviesData, name, TicketPrice):
        if(name in currentMoviesData.index):
            input("Error: Movie already exists, delete that movie or choose a different name. \n Any key to continue.")
        else:
            currentMoviesData.loc[name] = [TicketPrice]
        return currentMoviesData

    def deleteMovie(currentMoviesData, name):
        if(name in currentMoviesData.index):
            currentMoviesData = currentMoviesData.drop(name)
        else:
            input("Error: Movie not found. \nAny key to continue.")
        return currentMoviesData

    def changeTicketPrice(currentMoviesData, name, newPrice):
        if(name in currentMoviesData.index):
            currentMoviesData.loc[name] = [newPrice]
        else:
            input("Error: Movie not found. \nAny key to continue.")
        return currentMoviesData

    def changeMovieName(currentMoviesData, oldName, newName):
        if(oldName in currentMoviesData.index):

            if(newName in currentMoviesData.index):
                input("Error: New name already exists. \nAny key to continue.")
            else:
                currentMoviesData.loc[newName] = [currentMoviesData.loc[oldName].TicketPrice]
                currentMoviesData = MovieManipulation.deleteMovie(currentMoviesData, oldName)
        
        else:
            input("Error: Movie name to be changed not found. \nAny key to continue.")
        
        return currentMoviesData


#end Movie Manipulation Class

#Ticket Sales Class
class TicketSales:

    #Sell a ticket, recording it in the system
    def sellTicket(currentMoviesData, ticketSalesData, name, numTickets):

        if(name in currentMoviesData.index):
            if(1 in ticketSalesData.index): #wasn't working with .empty() so just checked if index 1 exists, so if saleID 1 gets deleted it will replace with a new sale with same ID
                saleID = 1
            else:
                saleID = ticketSalesData.index[-1] + 1

            #stored in ticketSalesData in case price changes but then can still see how much tickets were sold for
            currentTicketPrice = int(currentMoviesData.loc[name].TicketPrice)

            ticketSalesData.loc[saleID] = [name, datetime.datetime.now().strftime("%d/%m/%Y"), numTickets, currentTicketPrice, currentTicketPrice * int(numTickets)]
        else:
            input("Error: Movie not found. \nAny key to continue.")

        return ticketSalesData

    #refund using saleID which would have been printed on ticket given to customer
    def refundTicket(ticketSalesData, saleID):
        if(int(saleID) in ticketSalesData.index):
            ticketSalesData = ticketSalesData.drop(int(saleID))
        else:
            input("Error: Sale ID not found. \nAny key to continue.")
        return ticketSalesData
#End Ticket Sales Class

#Metadata Class
class Metadata:

    def totalProfit(ticketSalesData):
        return ticketSalesData.TotalProfit.sum()

    def sortByDatePurchesed(ticketSalesData):
        ticketSalesData.Date.apply(lambda string: datetime.datetime.strptime(string, "%d/%m/%Y"))
        return ticketSalesData.sort_values(['Date'], ascending=False)

    def sortSalesByMovie(ticketSalesData):
        return ticketSalesData.sort_values(by=['Movie'])

    def sortMoviesByPrice(currentMoviesData):
        return currentMoviesData.sort_values(by=['TicketPrice'])

    def sortMoviesByName(currentMoviesData):
        return currentMoviesData.sort_index()

    





        

        
