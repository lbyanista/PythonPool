kata = (2019, 9, 25, 3, 30)

from datetime import datetime

def main():
    dt = datetime(*kata)
    # print(f"{kata[1]}/{kata[2]}/{kata[0]} {kata[3]}:{kata[4]}")
    print(dt.strftime("%m/%d/%Y %H:%M"))
    
main()