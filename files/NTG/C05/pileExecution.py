import tkinter as tk


def fonctionA():                        	
    print("Début fonctionA")   	

    for i in range(5): print(f"fonctionA {i}")  	


    print ("Fin fonctionA") 	
    	
def fonctionB():    	
    print("Début fonctionB")   	

    i=0 	
    while i<5:  	
        if i==3:    	
            fonctionA() 	
            print("Retour à la fonctionB")  	
        print(f"fonctionB {i}") 	
        i = i + 1   	

    print ("Fin fonctionB") 	



fonctionB()


root.mainloop()