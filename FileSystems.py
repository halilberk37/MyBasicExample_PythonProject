import os
file = open("NotePads/deneme.txt", "w")
file.write("Dosyadaki ne varsa silip uzerine yazdim.")
file.close()

file=open("NotePads/deneme.txt", "r")
print(file.read())
#"a" dosyadaki yazıları silmeden ekleme yapıyor
f = open("NotePads/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("NotePads/demofile2.txt", "r")
print(f.read())

#"w" dosyadakileri silip üzerine yazdırıyor.
f = open("NotePads/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("NotePads/demofile3.txt", "r")
print(f.read())

file = open("demofile.txt","x")
file.close()

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("File deleted.")
else:
  print("The file does not exist")

