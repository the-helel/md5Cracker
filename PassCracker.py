import hashlib


flag = 0;
counter = 0;

pass_hash = input("Enter md5 Hash : ");
wordlist = input("Enter filename : ");

try:
  pass_file = open (wordlist , "r");
except:
  print("No File Found");
  quit();

for word in pass_file:
  enc_wrd = word.encode('utf-8');
  digest = hashlib.md5(enc_wrd.strip()).hexdigest();

  counter +=1



  if digest == pass_hash:
    print("Password Found");
    print("Password is " + word);
    print(counter)
    flag = 1;
    break;

if flag == 0:
  print("Password is not in the list");
