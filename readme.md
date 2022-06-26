# **The CKN Language**
CKN is a programming language with simple syntaxes aimed for those that are new\
to the programming world and doesn't have any experiences before in terms of programming. 

## **Features**
-	Simple syntaxes
-	Basic math operations
-	Assigning variables
-	Conditional statements
-	Error handling 
-	Multiline code 
-	Functions
-	For loop and while loop
-	Strings

## **Requirements**
If you decided to try out this program, you should have at least Python 3.8 installed, since\
the development process was made using that specific version of Python. You can try\
out other versions, but make sure that you install at least Python 3. 

## **How to use**
For those that are interested in trying out this programming language, simply clone\
this repository and make a new virtual environment first in the cloned folder that has been\
created. To make a new virtual environment in Python, open the terminal and point it to the current folder path, then type 
```sh
python -m venv <environment_name>
```
You can specify any environment name according to your liking, but `env` is the most\
commonly used (at least from what I know). After you've created the venv, type
```sh
<environment_name>\scripts\Activate
```
then press Enter. It will activate the newly created venv. After that, you can start using the\
programming language by typing
```sh
python shell.py
```

## **Syntaxes**
### **Variable declaration**
The value of the variable can be either numbers or strings. Strings must be declared with\
double quotation marks ("..."). Single quotation mark will not work. The syntax is `let <var_name> = <value>`
```
let a = 1
```
### **Conditional statements**
There's `if`, `elif`, and `else` for declaring conditional statements. Conditional statements\
must be ended with the "end" keyword. The syntax is `if <expression> then <statement>` for a single line code, and `if <expression> then <statement> end` for multi line code.
```
if a != 1 then print("i love bred")

if a == 1 then
    print("namba wan")
elif a > 1 then
    print("uwogh im more than 1")
else
    print("sadge")
end
```
### **Loops**
There are two loops in the CKN language, which is the `while` loop and the `for` loop. Both\
do the same thing, which is looping through something. Both have similar syntax, which is `for/while <expression> then <statement>` for single line code, and `for/while <expression> then <statement> end` for multiline code.
```
for i = 0 until 10 then print("menyefunk jefun")

for i = 0 until 10 then
    print("yadda")
end
```

### **Functions**
The syntax for function declaration is `function <func_name>(<args>) -> <statement>` for single line code and `function <func_name>(<args>) <newline> <statement> end` for multi line code. The single line code version always returns the\
declared statement.
```
function dhuar() -> "bumi datar"

function waras()
    let orang_waras = "percaya bumi bulat"
    return orang_waras
end
```

### **BASIC math operations**
Almost forgot to mention this but of course CKN can do basic math operations.
```
1 + 1 = 2
1 * 1 = 1
8 * 2 (2 + 2) = 20
420 / 69 = 6.08695652173913
1 / 0 = your computer explodes
```

That's it I guess. Have fun trying out CKN. 
<br>
<br>
> Made with stress and desperation by Karel Bondan