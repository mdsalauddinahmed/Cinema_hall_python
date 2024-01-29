class Star_cinema:
    hall_list =[]
    def entry_hall(self,hall_objects):
        self.hall_list.append(hall_objects)

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
       self.hall_no=hall_no
       self.rows=rows
       self.cols=cols
       self.seats={}
       self.show_list=[]
       

    
    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.show_list.append(show_info)

        
        show_seats = [[{"occupied": False} for _ in range(self.cols)] for _ in range(self.rows)]
        # show_seats = []
        # for _ in range(self.rows):
        #  row = []
        #  for _ in range(self.cols):
        #    seat = {"occupied": False}
        #    row.append(seat)
        #    show_seats.append(row)


        self.seats[show_id] = show_seats

    def book_tickets(self):
        show_id = input("Enter the show ID: ")
        if show_id not in self.seats:
            print("Invalid show ID.")
            return

        self.view_available_seats(show_id)

        num_tickets = int(input("Enter the number of tickets to book: "))
        seats_to_book = []
        for _ in range(num_tickets):
            row = int(input("Enter the row number for the seat: "))
            col = int(input("Enter the column number for the seat: "))
            seats_to_book.append((row, col))

        self.book_seats(show_id, seats_to_book)
        self.view_available_seats(show_id)
        print("Tickets booked successfully!")
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Invalid show ID.")
            return

        show_seats = self.seats[show_id]

        for row, col in seat_list:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                seat = show_seats[row - 1][col - 1]
                if not seat["occupied"]:
                    seat["occupied"] = True
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
    
    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("Invalid show ID.")
            return

        show_seats = self.seats[show_id]

        print(f"Booked Seats Matrix for Show {show_id}:")
        for row in range(self.rows):
            for col in range(self.cols):
                if show_seats[row][col]["occupied"]:
                    print("B", end=" ")   
                else:
                    print("O", end=" ")   
            print()

 
    def view_show_list(self):
        print("Show List:")
        for show_info in self.show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")










#replica 
        
while(True):
    print('----------Hall tickets management----------')
    print("1. view All Show ")
    print("2. view available seats ")
    print("3.Book tickets ")
    print("4.Exit")
    hall1 = Hall(rows=5, cols=8, hall_no=1)

# Entry of a show
    hall1.entry_show(show_id="S1", movie_name="Avengers", show_time="6:00 PM")
    hall1.entry_show(show_id="S2", movie_name="Twelve Fail", show_time="3:00 PM")

    ch=int(input("Enter an Option : "))

    if ch == 1:
        print('view all show')
        hall1.view_show_list()
    elif ch == 2:
        print('view available seats')
        ch=input("Enter Show id S1/S2 :")
        if ch=='S1':
           hall1.view_available_seats(show_id="S1")
        else:
           hall1.view_available_seats(show_id="S2")
    elif ch == 3:
      
        hall1.book_tickets()
      
    elif ch ==4:
        print("exit the program")
        break
    else:
        print("invalid number")