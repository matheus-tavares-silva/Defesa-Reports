messages = {
    'welcome' : \
'''
Bem vindo gerador ao de relatários.

Escolha uma opção:

1 - Gerar Previsão do tempo
2 - Gerar Painel do Covid-19
3 - Situação Alertas
''',
'generate' : {
    '1' : {'function' : 'cptec', 'message' : 'Gerando arquivo de previsão do tempo, aguarde um momento...'},
    '2' : {'function' : 'covid', 'message' : 'Gerando arquivos do painel covid, aguarde um momento...'},
    '3' : {'function' : 'alerts', 'message' : 'Sistema de notificações de alerta: '}
},
'unknown' : \
'''
Desculpe, não entedi sua solicitação.

Aqui estão algumas opções:

1 - Gerar Previsão do tempo
2 - Gerar Painel do Covid-19
3 - Situação Alertas
'''
}