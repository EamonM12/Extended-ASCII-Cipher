# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:49:44 2021

@author: Eamon
"""



#option = ""#input("encryption or decyption:")
#text = ""#input("PHRASE:")
#key = ""#input("Key:")


def  ext_vigenere(text, key, option):
 ciphermessage = []
 plaintext = []   

    
 if not (option == "encrypt") and not (option == "decrypt"): 
     print("Inavlid option!")              
                 
    
 
    
 if (option == "encrypt"):
   #check key length to see if neded to be extended
       if (len(text) == len(key)):
           key = list(key) 
    
       else:
           key_index = 0
           key = list(key)
           for key_index in (range(len(text)-len(key))):
        
               key.append(key[key_index])
               key_index = key_index+1
          
   
        
        
       x = 0
       key_index = 0 
            # encryption
       for i in range(len(text)):
                cipher_index = ((ord(text[x])+ord(key[key_index]))-32)
                x = (x+1)
                key_index = key_index+1
                ciphertext = chr(cipher_index)
                ciphermessage.append(ciphertext)
       text = "".join(ciphermessage)
     #  print(anwser)                 
     #  print(text)               
       return(text)
                
                
                
                
                
                
 if(option == "decrypt"):
         #key mappinhg
          if len(text) == len(key):
            key = list(key)
          else:
                key_index = 0
                key = list(key)
                for key_index in (range(len(text)-len(key))):
     
                    key.append(key[key_index])
                    key_index = key_index+1
         

           
    # cipher index            
          x= 0 
          key_index = 0
          
    #decryption
          for i in range(len(text)):
                tex_index = (ord(text[x])-ord(key[key_index])+127)
                x = x+1
                key_index = key_index+1
                Text = chr(tex_index)
                plaintext.append(Text)
          text = "".join(plaintext)
         
         # print(text)                 
                

          return(text)

              
ext_vigenere("VIGENERE","CIPHER","encrypt")
ext_vigenere("<UcY6dK`","testing","decrypt")
ext_vigenere("<UcY6dK`","testing","endecrypt")  
    
