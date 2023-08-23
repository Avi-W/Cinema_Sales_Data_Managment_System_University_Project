import pandas
from Backend import MovieManipulation as Movies
from Backend import TicketSales as Sales
from Backend import Metadata

#read in Data files upon starting
MoviesCsv = "CurrentMovies.csv"
SalesCsv = "CinemaSales.csv"

currentMoviesData = pandas.read_csv(MoviesCsv)
currentMoviesData = currentMoviesData.set_index('Name') 
ticketSalesData = pandas.read_csv(SalesCsv)
ticketSalesData = ticketSalesData.set_index('SaleID')

exitProgram = False
while(not exitProgram):

    print("Options: Ticket Sales, Current Movies, Metadata, exit program")
    outerChoice = input("Choose option: ")

    if(outerChoice == "exit program"):
        exitProgram = True

    #Ticket Sale Menu Section
    elif(outerChoice == "Ticket Sales"):
        exitTicketSales = False
        while(not exitTicketSales):
            print("\nOptions: sell, refund, save, exit mode, exit program")
            ticketSalesChoice = input("Choose option: ")

            if(ticketSalesChoice == "exit mode"):
                exitTicketSales = True
                print('\n')
            
            elif(ticketSalesChoice == "sell"):
                print("Current Movies: \n",currentMoviesData)
                name = input("Input movie name: ")
                numTickets = input("Input number of tickets: ")
                ticketSalesData = Sales.sellTicket(currentMoviesData, ticketSalesData, name, numTickets)
                print("Ticket Sales Data: \n", ticketSalesData)

            elif(ticketSalesChoice == "refund"):
                print("Ticket Sales Data: \n", ticketSalesData)
                saleID = input("Input Sale ID: ")
                ticketSalesData = Sales.refundTicket(ticketSalesData, saleID)
                print("Ticket Sales Data: \n", ticketSalesData)
            
            elif(ticketSalesChoice == "exit program"):
                exitTicketSales = True
                exitProgram = True
            
            elif(ticketSalesChoice == "save"):
                ticketSalesData.to_csv("CinemaSales.csv")

            else:
                input("Please only enter valid options, enter to continue")

    #Current Movie Menu Selection 
    elif(outerChoice == "Current Movies"):
        exitMovieManip = False
        while(not exitMovieManip):
            print("\nCurrent Movies: \n",currentMoviesData)
            print("Options: input, delete, change ticket price, change movie name, \n save, exit mode, exit program")
            choice = input("Choose option: ")

            if(choice == "exit mode"):
                print('\n')
                exitMovieManip = True

            elif(choice == "save"):
                currentMoviesData.to_csv(MoviesCsv)

            elif(choice == "input"):
                name = input("input movie name: ")
                price = input("input movie ticket price: ")
                currentMoviesData = Movies.inputMovie(currentMoviesData, name, price)

            elif(choice == "delete"):
                name = input("input name of movie to delete: ")
                currentMoviesData = Movies.deleteMovie(currentMoviesData, name)

            elif(choice == "change ticket price"):
                name = input("input name of movie to change price: ")
                price = input("input new movie ticket price: ")
                currentMoviesData = Movies.changeTicketPrice(currentMoviesData, name, price)

            elif(choice == "change movie name"):
                oldName = input("input name of movie to change: ")
                newName = input("input new movie name: ")
                currentMoviesData = Movies.changeMovieName(currentMoviesData, oldName, newName)

            elif(choice == "exit program"):
                exitMovieManip = True
                exitProgram = True
        
            else:
                input("\nPlease only enter valid options, enter to continue")

    #Metadata Menu Section    
    elif(outerChoice == "Metadata"):

        exitMetadata = False
        while(not exitMetadata):
            print("\nOptions: sort sales by date, total sales profit, sort sales by movie\nsort movies by price, sort movies by name, \nsave, exit mode, exit program")
            choice = input("Choose option: ")

            if(choice == "exit mode"):
                exitMetadata = True
                print('\n')

            elif(choice == "exit program"):
                exitMetadata = True
                exitProgram = True
            
            elif(choice == "save"):
                currentMoviesData.to_csv(MoviesCsv)
                ticketSalesData.to_csv(SalesCsv)

            
            elif(choice == "total profit"):
                print("Current total movie sales profit =", Metadata.totalProfit(ticketSalesData))
                input("Press any key to continue.")
            

            elif(choice == "sort sales by date"):
                ticketSalesData = Metadata.sortByDatePurchesed(ticketSalesData)
                print("Sales sorted by date. \n", ticketSalesData)
                input("Press any key to continue.")

            elif(choice == "sort sales by movie"):
                ticketSalesData = Metadata.sortSalesByMovie(ticketSalesData)
                print("Sales sorted by movie name. \n", ticketSalesData)
                input("Press any key to continue.")

            elif(choice == "sort movies by price"):
                currentMoviesData = Metadata.sortMoviesByPrice(currentMoviesData)
                print("Movies sorted by price. \n", currentMoviesData)
                input("Press any key to continue.")

            elif(choice == "sort movies by name"):
                currentMoviesData = Metadata.sortMoviesByName(currentMoviesData)
                print("Movies sorted by name. \n", currentMoviesData)
                input("Press any key to continue.")
            
            else:
                input("Please only enter valid options, enter to continue")
                
    else:
        input("Please only enter valid options, enter to continue")
    
    #Saves all files when exiting
    if(exitProgram == True):
        currentMoviesData.to_csv(MoviesCsv)
        ticketSalesData.to_csv(SalesCsv)



        


