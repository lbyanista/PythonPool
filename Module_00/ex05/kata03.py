kata = "The right format"

def main():
    # lenght = len(kata)
    # if len(kata) < 42: 
    #     print(f"{kata}")
    # else:
    #     print("is 42")
    print("-" * (41 - len(kata)) + kata)
    
main()