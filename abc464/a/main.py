def main():
    S=input().strip()
    count_e = count_w = 0
    for s in S:
        if s =="E":
            count_e +=1
        else:
            count_w +=1
    print("East" if count_e > count_w else "West")


if __name__ == "__main__":
    main()
