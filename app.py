import random
import datetime
import time


def random_value():
    ran_val=random.randint(1,10)
    return ran_val


def main():
    i=0
    f=open("./log.txt","w")
    
    while i<100:

        ranVal= random_value()
        write_time= datetime.datetime.now().strftime("%y-%m-%d %h:%m:%s")

        f.write(f"[{write_time}] : random value is {ranVal} ")
        f.close()
        f=open("./app_log.txt","a")
        i+=1
        time.sleep(10)
        


if __name__=="__main__":
    main()
    