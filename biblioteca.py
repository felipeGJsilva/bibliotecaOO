class Autor:
    def __init__(self,nome,nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    
    def get_nome(self):
        return self._nome

    def get_nacionalidade(self):
        return self._nacionalidade

class Livro:
    def __int__(self,titulo,autor,ISBN):
        self._titulo = titulo
        self._autor = autor 
        self._ISBN = ISBN
        self._disponivel = True

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._isbn

    def is_disponivel(self):
        return self._disponivel

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        else:
            return False

    def devolver(self):
        self._disponivel = True

