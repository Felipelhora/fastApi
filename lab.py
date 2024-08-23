

'''
dict_1 = { "nome": "felipe"

}
dict_2 = {"idade": "37",
          **dict_1
          }


print (dict_2)


# breackpoint sem precisar do visual studio code
#breakpoint()


try:
    assert 1 == 1
    print ('\n\n\n\n\n\n\n\n\n\n\n------- deu certo ------------\n\n\n\n\n\n')
    raise ('É possivel forçar um erro mesmo com sucesso usando raise, assim essa mensagem é enviada e direcionada para exception')
except:
    raise ('aqui eu coloco o erro que eu quero colocar com minha mensagem personalizada')
'''

### yeld

# objeto gerador
# tem yield se chama um gerador e não uma função
## pode se iterar

# next() função para gerar o proximo | caso não tenha mais gera exception | só vai para frente


def funcao_geradora():
    yield 1
    yield 2
    yield 3


gerador  = funcao_geradora()

next(gerador)
next(gerador)
next(gerador)
next(gerador)


