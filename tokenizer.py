import sys

RESERVED_KEYWORDS = {
    "program" : 1, 
    "begin" : 2,
    "end" : 3,
    "int" : 4,
    "if" : 5,
    "then" : 6,
    "else" : 7,
    "while" : 8,
    "loop" : 9,
    "read" : 10,
    "write" : 11,
}

SYMBOLS = {
    ";" : 12,
    "," : 13,
    "=" : 14,
    "!" : 15,
    "[" : 16,
    "]" : 17,
    "&&" : 18,
    "||" : 19,
    "(" : 20,
    ")" : 21,
    "+" : 22,
    "-" : 23, 
    "*" : 24,
    "!=" : 25,
    "==" : 26,
    "<" : 27,
    ">" : 28,
    "<=" : 29,
    ">=" : 30
}

TOK_INT = 31
TOK_ID = 32
TOK_EOF = 33
TOK_ERR = 34

class Tokenizer:
    def __init__(self, filename):
        self.reader = open(filename, 'r', encoding='utf-8')
        self.tokens: list[tuple[int, str]] = []
        self.current_token_index = 0
        self.eof = False
        self.tokenizeLine()

    def getToken(self) -> int:
        return self.tokens[self.current_token_index][0]
    
    def skipToken(self):
        t = self.getToken()
        if t in (TOK_EOF, TOK_ERR):
            return
        self.current_token_index += 1
        if self.current_token_index >= len(self.tokens):
            self.tokenizeLine()
            
    def intVal(self) -> int:
        if self.getToken() != TOK_INT:
            raise Exception("Current token is not an integer")
        return int(self.tokens[self.current_token_index][1])  
    
    def idName(self) -> str:
        if self.getToken() != TOK_ID:
            raise Exception("Current token is not an identifier")
        return self.tokens[self.current_token_index][1]
    
        