✅ = Test and works <br>
🔄 = under test <br>
❌ = Not test <br>


# ‎class List ✅
It allows you to interact with lists.
### enum(list)
This function displays all the values in the list that you will give.
### addAlphabet‎(list)
It just adds the alphabet to your list =)

---
# class Document ✅
This class makes it easy to interact with .txt files <br>
**Please do not mark the extension (in this case ".txt"). It will be added automatically.**

### create(string)
Create a txt file with the name you give

### write(file,string)
write a string into a txt file

### open(file)
print the Content of a file

An example of a code:  
`from SimpleLib import Document`<br>
`Document.create("mytextfile")`	<br>
`Document.write("mytextfile","Hello World")`<br>
`Document.read("mytextfile")`<br>
The first line import the Document class. <br>
The second create a text file name "mytextfile" <br>
The third write into the file "mytextfile" the string "Hello World" <br>
And the last print into the output the content of the file "mytextfile" <br>

---
# class Json ❌


