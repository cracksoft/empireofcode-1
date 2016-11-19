def c(r):
 for i in range(1,len(r)):
  if r[i]==r[i-1]:return True
 return False
golf=lambda x:not any([c(r)for g in x+list(zip(*x))for r in g]+[c(r)for g in zip(*x)for r in zip(*g)])

if __name__ == "__main__":
 assert golf([[["X", "Z"],
                  ["Z", "X"]],
                 [["Z", "X"],
                  ["X", "Z"]]]) == True, "1st example"
 assert golf([[["X", "Z"],
                  ["Z", "X"]],
                 [["X", "Z"],
                  ["Z", "X"]]]) == False, "2nd example"
 print("All done? Earn rewards by using the 'Check' button!")
