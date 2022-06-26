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
Before jumping into the syntaxes, I should mention that CKN can be operated in two ways:\
by directly using the shell or by using a text editor.\
Since this is a school project and I'm broke you can use any text editor out there. If you\
want to use Notepad feel free, but what the heck is wrong with you. If you decided to\
use a text editor to make a CKN program, make sure the extension of the file is `.ckn`, \
because I'm a narcissist. To execute the source code written inside the `.ckn` file, put the\
file in the same directory as where `shell.py`, heck, the entire project resides. Type
```sh
<filename>.ckn
```
into the CKN console (execute `shell.py` first) and CKN will know that you are trying to\
execute a program written inside a file. Without further a do, here are the syntaxes for CKN:

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

function waras(yang_bener)
    if yang_bener == true:
        let orang_waras = "percaya bumi bulat"
    else
        let orang_waras = "ga waras"
    end
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