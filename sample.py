import sys

def main(cnt: int):
    for _ in range(int(cnt)):
        print("Hello world")
        
if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        cnt = sys.argv[1]
    else:
        cnt = 10
    
    main(cnt)    
