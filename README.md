# PythonBatchNovDec2024

## Class 1
Crete repo and git shortcuts
1. git checkout -b 'branch' = create branch
2. git branch = check branches
3. git clone 'https url'  = clone repo not for local devlopment
4. git status = stage changes
5. git diff = see changes made on single file for excat changes
6. git add 'name' = stage changes
7. git commit -m 'commit message' = commit chanhges
8. git push origin 'branchname' = push changes
9. PEP 8 is coding style in python enchancement proposal

## Class 2

1. ./ = execuituin or to add file type to execution
2. python code > python byte code> interpreter > compiler
3. python dynamic typed language
4. indentation error = expected things taht python will tell us 
5. interactive mode is usefull to visually see the things that 
 happen used for learning, script mode is as it is dispaly of results
 6. print statements for escape sequences
 \t = tab spaace
 \n = new line
 \b = overwrite previous character 

## Class 3
1. define numbers 
num1 = 1
num2 = 2
addition = num1 + num2 
print(Addtion) = 3
print("substraction", subtraction) = substraction = 1

## Class 4

1. Different types of using coment operater

print('Hello world1')
print("Hello #world2")
print("hello","world3", sep= "#")
print("hello world4") # 
print("hello world5" ) 

output : Hello world1
Hello #world2
hello#world3
hello world4
hello world5

2. print(keyword.kwlist) = helps with keywords in coding such as printf true etc there are 71 key words

3.  variable = view to all  public variable
_variable = accessed with in own class and subclass  protected variable
__variable = can be accsessed ub own class private variable


## Class 5 

 1. Code space has 30 days data retention time, even when the code is commited.
 2. Best practice : Start day with git pull request
 3. Moment "" come it becomes or reads as a string,  only one under score is permitted 
 eg:  #Larger numbers
    speed_of_light = 29999996
    print(type(speed_of_light),speed_of_light)

    speed_of_light = 299,999,96
    print(type(speed_of_light),speed_of_light)

    speed_of_light = 299_999_96
    print(type(speed_of_light),speed_of_light)

    speed_of_light = "299_999_96"
    print(type(speed_of_light),speed_of_light)

    output: int = 29999996
    tuple = (299,999,96)
    int = 29999996
    str = 299_999_96

 4. Run all will fail whenever there are expection 

 5. Design ration store - Arthmetic opertion 
    Steps to write code 
    >Write algorithm or plan of action or write it on paper
    > eg for ration store > steps >  (variables calcucation and then results) for eg: Cost , Name , quantity, compute seeling price, add total of times, subsidy, calcutaions and print results.
    > Comment indicated what happens in next step very important to hav comments 
    > For variable use underscore eg: cost_of_rice and for class cammel cases
    > logical mistake python wont help only syntax error python helps
    >Try using cmd lime more
    > Best practice use print statements write some statement and print it. eg: instead of output 1300 use The total price is 1300 USD
 6. Entire flow is understood in previous steps 
 7. Any program write the constants very imp 
 8. eg : Fruit store 
        Dozen = 12
        Discount = 25
        Tax = 30
 9. If variables not given get it from the user (the person running the code) python used input() = to get th value in runtime

 10. make sure to write .py file always for python file
 11. Input() will print what ever we enter eg : 4 and qunaity of rice is 4 
 12. String repetion opetaion: in other languuages when you multipy  string with integer it will throw error but in python we get repeate values 
 eg: cost_of_rice = 10 * per kg
 input() > Qty of rice : 4 
 SP of rice = 4444444444
 13. to avoid this we have to convert it. updating a vaiable eg: qty_of_rice = input ("Enter Qty if rice (in Kgs): ") = opertion
 qty_of_rice = int(qty_of_rice) = updating
 reason input() will take any input as string variable

 there is nothing wrong to do opertain and updation on same varialble

 14. Type conversion: 
 Data type conversions 
 int float complex boolean string None

 Interger 

 3 sets of conversion 
 decimal int() base 10 0-9
 binary bin() base 2 0-1
 hexadecimal hex() base 16  0-9 and A-F
 octal oct() base 8 0-7

 Float 
 float()

 String 
 str()

15. eg: 
#int to float 
print(12, float(12))
output: 12 12.0

16. eg:  str to float 

23 float 23 = 23 23.0
23.24 float 23.24 = 23.24
2 3 float2 3 = error cannot convert
Float very intelligent to convert try all types

17. Integer
binary reprsesentaion in only for interger not floating values

0b is stating that his is a binary vlaue 

assignments 
Savings bank 
bank loan SI and CI
convert from  hexa to oct vice versa
Feet to Conversion 

18. abs value give positive or negative 

19. complex value > will have real and imaginary vlaue 


20. Library import math will import all math oprations (beacuse python doesnot have sqrt opertaion )

21. Complex number > made to be complex :) 
  complex number =  real number +/- imaginary number
  pythin j is used to represent imajinary number 



  0j is also complex 
  number folloed by j is complex 
  4*j j4 j*5 not possible

  22. complex built in fucntio we can crete own complex numbers
  23. == checks value equvilance 
   eg: 3 + 4j ==4j + 3
   is true real value compare with real value j value compared with j vlaue






## Class 6

1. Recap check the git status every day and check if yo are behind any commits.
2. Also every do git pull which gives latest changes 
3. String operations > create a new branch 
4. git branch = list of branches
5. git checkout -b class05 = create new brach
6. to create a jupyter notebook use .ipynb
7. String operation can be represented using 
   single quotes , double quotes, triple single quotes and triple double quotes
8. eg: language = 'Pythob Programming'
print(language, type(language))
output: Python Programming <class ;'str'>
9. String can be defined 4 ways in python.
note: PEP8 = is guidelines > use triple double quotes for doc string
10. eg: where_abouts = 'what's up?'
      print(where_abouts, type(where_abouts))
      output: error: Ssyntax error unterminated string literal 
      means whenwe use single quotes for string we have also use apostrophy which is read as string quotes hence not recommende to use single quotes

11.  so to over come that issue we can use placing \ before any operator with results in treating it as ordinary character 
12. If you are using multiple single quotes it is not practical to use \ for every single quote
in this case we can use double quotes ""
13. what if scenario we have single and double quotes in a string. in that case we can use single triple quotes else we can also use double triple quotes
14. Multi line strings: python is interpretor based languauge line by line execution is happening. here is line contunation operation \
15. for triple quote the python reads is complete multiple line we donot need to use the line continutaion operation 
16. better practice to use ; eg: """ My name is "HAZY""""
 instead we can use "HAZY";"""
17. String indexing : len()
= to get the no of charc in string 
forward indexing and reverse indexing
18. Mat lab and fotron indexing starts at 1 all other languages start indexing from 0
19. Reverse indexing doesnot start from 0 becuas 0 doesnot have negative sign 
20. forward indexing : 0 1 2 3 4 5 
reverse indexing:  -6 -5 -4 -3 -2 -1
21. indexerror = index out of range
22. how reverse indexing works = if you give  string of 5 charctes 
when you ask for -3 index it will minus from total lenght and give the character 
23. used to get last charcters in string is use case example
24. we can only as for integers floating point does not work 
25. String slicing operation:
we need to give start index and end index
eg : we want 0 to 3 in a string of 10 charcters 
26. **** in python it doesnot include last value in the a boubdary condition.
27. Slciing operation is used to get group of charcter from a big string for eg: want to paint red to first 5 houses in a row
28. in slicing if yo go beyond the limit of the string it doesnot throw error. 

## Class 7

1. Recap String slicing will take 3 arguments. eg: language[1:5 :1] means it is step of 1 with adding 1 to every digit and give the charcter
2. it works with - 1 or negative step also work slcing will never throw an error
3. string slicing [start_index: final_index, step]
   default start_index = 0
   default final_index = string lenght
   default step = +1
4. If step is -ve abd start_index and final_index were not given, then start_index = lenghth of string -1 final _index = -1 bqasically it will make it reverse index
5. Assignment : Do perform inplace word reversal for a given string 
6. Assignment: reverse each word in given sentence in same order
7. not recomemnded to use combination if pos and neg indices
eg: print("name[-6] : , name[-6:])
print("name[len(name)-6:] :", name[len(name)-6:])
8. most asked interview question : Demostration of palindrome check
algorith: 
TAke string in runtime and store varibale
create a reverse string from given string usinf string reversal
compare both with a condition and decide

eg: test_string = input("Enter string")
print("test_string = ", test_string)
 
reverse_string = test_string[::-1]
print("reverse_string: ", reverse_string)
print(test_string == reverse_string)
 9. Assignment test given sentence is pallindrom or not hint ignore the whote spaces
 10. recheck string 
 

 ##Class 8
 