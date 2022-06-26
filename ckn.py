import os
import math
from showarrows import *
from lexer import *
from position import *
from error import *
from nodes import *
from keywords import *
from langtoken import *
from langparser import *
from langruntime import *
from langcontext import *
from langvalues import *
from symboltable import *
from langinterpreter import *

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(math.pi)

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def execute(self, args):
        execute_result = RuntimeResult()
        execute_context = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        execute_result.register(self.check_and_populate_args(
            method.arg_names, args, execute_context))
        if execute_result.should_return():
            return execute_result

        return_value = execute_result.register(method(execute_context))
        if execute_result.should_return():
            return execute_result
        return execute_result.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f'No execute_{self.name} method defined')

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function {self.name}>"

    def execute_print(self, execute_context):
        print(str(execute_context.symbol_table.get('value')))
        return RuntimeResult().success(Number.null)
    execute_print.arg_names = ['value']

    def execute_print_ret(self, execute_context):
        return RuntimeResult().success(String(str(execute_context.symbol_table.get('value'))))
    execute_print_ret.arg_names = ['value']

    def execute_input(self, execute_context):
        text = input()
        return RuntimeResult().success(String(text))
    execute_input.arg_names = []

    def execute_input_int(self, execute_context):
        while True:
            text = input()
            try:
                number = int(text)
                break
            except ValueError:
                print(f"'{text}' must be an integer. Try again!")
        return RuntimeResult().success(Number(number))
    execute_input_int.arg_names = []

    def execute_clear(self, execute_context):
        os.system('cls' if os.name == 'nt' else 'cls')
        return RuntimeResult().success(Number.null)
    execute_clear.arg_names = []

    def execute_is_number(self, execute_context):
        is_number = isinstance(execute_context.symbol_table.get("value"), Number)
        return RuntimeResult().success(Number.true if is_number else Number.false)
    execute_is_number.arg_names = ["value"]

    def execute_is_string(self, execute_context):
        is_number = isinstance(execute_context.symbol_table.get("value"), String)
        return RuntimeResult().success(Number.true if is_number else Number.false)
    execute_is_string.arg_names = ["value"]

    def execute_is_list(self, execute_context):
        is_number = isinstance(execute_context.symbol_table.get("value"), List)
        return RuntimeResult().success(Number.true if is_number else Number.false)
    execute_is_list.arg_names = ["value"]

    def execute_is_function(self, execute_context):
        is_number = isinstance(
            execute_context.symbol_table.get("value"), BaseFunction)
        return RuntimeResult().success(Number.true if is_number else Number.false)
    execute_is_function.arg_names = ["value"]

    def execute_append(self, execute_context):
        list_ = execute_context.symbol_table.get("list")
        value = execute_context.symbol_table.get("value")

        if not isinstance(list_, List):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                execute_context
            ))

        list_.elements.append(value)
        return RuntimeResult().success(Number.null)
    execute_append.arg_names = ["list", "value"]

    def execute_pop(self, execute_context):
        list_ = execute_context.symbol_table.get("list")
        index = execute_context.symbol_table.get("index")

        if not isinstance(list_, List):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                execute_context
            ))

        if not isinstance(index, Number):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be number",
                execute_context
            ))

        try:
            element = list_.elements.pop(index.value)
        except:
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                'Element at this index could not be removed from list because index is out of bounds',
                execute_context
            ))
        return RuntimeResult().success(element)
    execute_pop.arg_names = ["list", "index"]

    def execute_extend(self, execute_context):
        listA = execute_context.symbol_table.get("listA")
        listB = execute_context.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                execute_context
            ))

        if not isinstance(listB, List):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be list",
                execute_context
            ))

        listA.elements.extend(listB.elements)
        return RuntimeResult().success(Number.null)
    execute_extend.arg_names = ["listA", "listB"]

    def execute_len(self, execute_context):
        list_ = execute_context.symbol_table.get("list")

        if not isinstance(list_, List):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                execute_context
            ))

        return RuntimeResult().success(Number(len(list_.elements)))
    execute_len.arg_names = ["list"]

    def execute_run(self, execute_context):
        fn = execute_context.symbol_table.get("fn")

        if not isinstance(fn, String):
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be string",
                execute_context
            ))

        fn = fn.value

        try:
            with open(fn, "r") as f:
                script = f.read()
        except Exception as e:
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load script \"{fn}\"\n" + str(e),
                execute_context
            ))

        _, error = run(fn, script)

        if error:
            return RuntimeResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script \"{fn}\"\n" +
                error.as_string(),
                execute_context
            ))

        return RuntimeResult().success(Number.null)
    execute_run.arg_names = ["fn"]


BuiltInFunction.print = BuiltInFunction("print")
BuiltInFunction.print_ret = BuiltInFunction("print_ret")
BuiltInFunction.input = BuiltInFunction("input")
BuiltInFunction.input_int = BuiltInFunction("input_int")
BuiltInFunction.clear = BuiltInFunction("clear")
BuiltInFunction.is_number = BuiltInFunction("is_number")
BuiltInFunction.is_string = BuiltInFunction("is_string")
BuiltInFunction.is_list = BuiltInFunction("is_list")
BuiltInFunction.is_function = BuiltInFunction("is_function")
BuiltInFunction.append = BuiltInFunction("append")
BuiltInFunction.pop = BuiltInFunction("pop")
BuiltInFunction.extend = BuiltInFunction("extend")
BuiltInFunction.len = BuiltInFunction("len")
BuiltInFunction.run = BuiltInFunction("run")

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("math_pi", Number.math_PI)
global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("print_ret", BuiltInFunction.print_ret)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("input_int", BuiltInFunction.input_int)
global_symbol_table.set("clear", BuiltInFunction.clear)
global_symbol_table.set("cls", BuiltInFunction.clear)
global_symbol_table.set("is_num", BuiltInFunction.is_number)
global_symbol_table.set("is_str", BuiltInFunction.is_string)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_fun", BuiltInFunction.is_function)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("len", BuiltInFunction.len)
global_symbol_table.set("run", BuiltInFunction.run)


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate abstract syntax tree
    parser = Parser(tokens)
    abstract_syntax_tree = parser.parse()
    if abstract_syntax_tree.error:
        return None, abstract_syntax_tree.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(abstract_syntax_tree.node, context)

    return result.value, result.error
