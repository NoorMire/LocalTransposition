import math 

def encryptMessage(msg,key): 
    cipher = "" 
  
    # track key indices 
    index = 0
  
    msg_len = float(len(msg)) 
    msg_list = list(msg) 
    key_list = sorted(list(key)) 
  
    #matrix is of dimension row x col
    
    col = len(key) 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' for empty cells
    padding = int((row * col) - msg_len) 
    msg_list.extend('_' * padding) 
  
    #print(msg_list)

    #create the matrix 
    matrix = [msg_list[i: i + col]  
              for i in range(0, len(msg_list), col)] 
  
    # print("Matrix Construction...\n")
    # print(matrix)

    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_list[index]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        #print(cipher)
        index += 1
  
    return cipher 
  
# Decryption 
def decryptMessage(cipher,key, flag = 0): 
    msg = "" 
  
    # track key indices 
    index = 0
  
    # track msg indices 
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_list = list(cipher) 
  
    # calculate column of the matrix 
    col = len(key) 
    row = int(math.ceil(msg_len / col)) 
  
    # convert key into list and sort  
    # alphabetically so we can access  
    # each character by its alphabetical position. 
    key_list = sorted(list(key)) 
  
    # create an empty matrix to  
    # store deciphered message 
    deciphered = [] 

    for _ in range(row): 
        deciphered += [[None] * col] 
  
    # Arrange the matrix column wise according  
    # to permutation order by adding into new matrix 
    for _ in range(col): 
        curr_idx = key.index(key_list[index]) 
  
        for j in range(row): 
            deciphered[j][curr_idx] = msg_list[msg_indx] 
            msg_indx += 1
        index += 1
    #print(deciphered)
    # convert decrypted msg matrix into a string 
    try: 
        msg = ''.join(sum(deciphered, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
    if flag == 1:
        return msg
    
    else:
      null_count = msg.count('_') 
  
      if null_count > 0: 
          return msg[: -null_count] 
  
      return msg 

  
# Driver Code 

if __name__ == '__main__':
    ans=True
    while ans:
        print("=================================================")
        print("\t\t\tTRANSPOSITION CIPHERS")
        print("=================================================")
        print ("""
        1.Local Transposition
        2.Exit/Quit
        """)
        ans=input("Please choose one of the above encryption methods: \n >> ")

        if ans!="2":

            choice=input("Choose 1. Encryption 2. Decryption \n >> ")
            msg=input("Please enter the message you wish to encrypt/decrypt below:\n >> ")
            if ans=="1": 
                print("\nYou have picked Local Transposition Cipher!")
                n=input("Please enter the key: \n >> ")
                if choice=="1":
                    cipher = encryptMessage(msg,n)
                else: 
                    cipher = decryptMessage(msg,n) 
            

            if choice == "1":
                print("Encrypted Message: {}". 
                   format(cipher)) 
            else:
                print("Decrypted Message: {}". 
                   format(cipher)) 
                
        elif ans=="4":
            print("\nGoodbye!")
            exit() 
        else:
            print("\nNot Valid Choice Try again")
            exit()