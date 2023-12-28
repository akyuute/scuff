from enum import Enum

class Tokens(Enum):
    ENDMARKER
    NAME
    COMMENT
    SPACE

    STRING
    NUMBER
    TRUE
    FALSE
    NONE

    LPAR = '('
    RPAR = ')'
    LSQB = '['
    RSQB = ']'
    COLON = ':'
    COMMA = ','
    SEMI = ';'
    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'
    DOUBLESLASH = '//'
    VBAR = '|'
    AMPER = '&'
    LESS = '<'
    GREATER = '>'
    EQUAL = '='
    DOT = '.'
    PERCENT = '%'
    LBRACE = '{'
    RBRACE = '}'
    EQEQUAL = '=='
    NOTEQUAL = '!='
    LESSEQUAL = '<='
    GREATEREQUAL = '>='
    TILDE = '~'
    CIRCUMFLEX = '^'
    LEFTSHIFT = '<<'
    RIGHTSHIFT = '>>'
    DOUBLESTAR = '**'
    EXCLAMATION = '!'
    QUESTION = '?'


class TokenGroups:
    '''
    '''
    T_Literal = {
        Tokens.STRING,
        Tokens.NUMBER,
        Tokens.TRUE,
        Tokens.FALSE,
        Tokens.NONE,
    }
    T_AssignEvalNone = {Tokens.NEWLINE, Tokens.EOF}
    T_Ignore = {Tokens.SPACE, Tokens.COMMENT}
    T_Invisible = {*T_Ignore, Tokens.NEWLINE}
    T_Syntax = {
        Tokens.L_BRACKET,
        Tokens.L_CURLY_BRACE,
        Tokens.L_PAREN,
        Tokens.R_BRACKET,
        Tokens.R_CURLY_BRACE,
        Tokens.R_PAREN,
    }


