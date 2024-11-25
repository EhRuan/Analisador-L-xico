import re

class AnalisadorLexico:
    def __init__(self):
        # definiçao generica de tokens
        self.token_specification = [
            ('NUMBER', r'\b\d+(\.\d+)?\b'),
            ('IDENTIFIER', r'[A-Za-z_]\w*'),
            ('KEYWORD', r'\b(if|else|while|for|def|return|class|int|float|print|var|function|let)\b'),
            ('OPERATOR', r'[+\-*/=<>!&|]+'),
            ('STRING', r'".*?"|\'.*?\''),
            ('PUNCTUATION', r'[;,:.{}()\[\]]'),
            ('WHITESPACE', r'\s+'),
            ('COMMENT', r'//.*?$|/\*.*?\*/|#.*?$'),
            ('MISMATCH', r'.'),
        ]
        # compila as regras
        self.regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification), re.DOTALL)

    def analise(self, text):
        tokens = []
        for match in self.regex.finditer(text):
            kind = match.lastgroup
            value = match.group()
            if kind in {'WHITESPACE', 'COMMENT'}:
                continue  # ignora espaços em branco e os comentarios
            elif kind == 'MISMATCH':
                raise ValueError(f"Token inválido: {value}")
            tokens.append((kind, value))
        return tokens

# testando o analisador
if __name__ == "__main__":
    print("Insira o código: ")
    code = input(">>> ")

    lexer = AnalisadorLexico()
    try:
        tokens = lexer.analise(code)
        
        # mostra os tokens
        print("\nTokens identificados:")
        for token in tokens:
            print(token)
        
        # mostra a quantidade de tokens
        print(f"\nQuantidade total de tokens: {len(tokens)}")
    except ValueError as e:
        print(f"Erro durante análise: {e}")
