# import threading
# lock = threading.RLock()
# def fun():
#     with lock:
#         print("Acquired Lock Inside Function.")
#     with lock:
#         print("Acquired Lock Inside Nested Function.")
# t1 = threading.Thread(target=fun)
# t2 = threading.Thread(target=fun)
# t3 = threading.Thread(target=fun)
# t1.start()
# t2.start()
# if __name__ == '__main__':
#     main()
#     for i in range (0,20):
#         print("Main Function ",i)
    
# t3.start()





# # t1.join()
# # t2.join()
# # t3.join()



###########################################################################################################################################



from queue import Queue
j=3
q=Queue(maxsize=j)
for i in range (1,4):
    x =  input("Enter the Character Element:-")
    q.put(x)
    
if(i>=j):
    print("\n The Queue is Full!!!")
else:
    print("\n DIE!!!!")    
    
for i in range (1,4):
    x = q.get(i)
    print("Element at Index",i,"is",x,".")