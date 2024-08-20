class Autor:
    def __init__(self,nomeA,nacionalidade):
        self._nomeA = nomeA
        self._nacionalidade = nacionalidade

    
    def get_nome(self):
        return self._nome

    def get_nacionalidade(self):
        return self._nacionalidade

class Livro:
    __livros = []  

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


    def adicionar(livro):
        Livro.__livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao sistema.")

    def buscar(criterio, valor):
        for livro in livro._livros:
            if criterio == 'titulo' and valor.lower() in livro.titulo.lower():
                return livro
            elif criterio == 'autor' and valor.lower() in livro.autor.nome.lower():
                return livro
        return None
    
    def devolver(self, usuario):
        if self in usuario.livros_emprestados:
            self.__disponivel = True
            usuario.livros_emprestados.remove(self)
            print(f"livro '{self.titulo}' devolvido por {usuario.nome}.")
        else:
            print("não foi emprestado por este usuário.")

class Usuario:

    def __init__(self, nomeU, id , livros_emprestados):
        self._nomeU = nomeU
        self._id = id
        self._livros_emprestados = livros_emprestados

    def get_nome(self):
        return self._nomeU
    
    def get_id(self):
        return self._id
    
    def get_livros_emprestados(self):
        return self._livros_emprestados

    
        
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")

        escolha = input("Digite o número da opção: ")
        if escolha == '1':
            titulo = input("titulo do livro: ")
            autor_nome = input("figite o nome do autor: ")
            autor_nacionalidade = input("figite a nacionalidade do autor: ")
            isbn = input("Digite o ISBN do livro: ")
            autor = Autor(autor_nome, autor_nacionalidade)
            livro = Livro(titulo,autor,isbn)
            Livro.adicionar(livro)

        elif escolha == '2':
            criterio = input('criterio do livro: ').strip().lower()
            valor =  input('valor do livro: ')
            livro = Livro.buscar(criterio,valor)
            if livro:
                print("livro encontrado")
            else:
                print("livro não encontradp")

if __name__ == "__main__":
    main()