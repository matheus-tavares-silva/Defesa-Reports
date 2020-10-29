env = \
{
    'paths' : {
        'out' : './out/',
        'loader' : {
            'model' : './app/view/',
            'css' : './app/view/static/css/',
            'image' : './app/view/static/image/',
        }
    },
    'alerts': {
        'link': 'https://alerts.inmet.gov.br/cap_12/',
        'path': {
            'root': '/html/body/table/tr/td/a'
        },
        'default' : {
            'country' : 'Mato Grosso',
            'date' : None,
            'location' : [-12.38, -54.92]
        },
        'render' : {
            'models' : ['alerts-1.jinja'],
            'styles' : [],
            'images' : [],
            'out'    : [],
            'options' : []
        }
    },
    'cptec': {
        'api' : 'https://apiprevmet3.inmet.gov.br/',
        'link': 'https://www.cptec.inpe.br/previsao-tempo/mt/',
        'path': {
            'min': 'div.justify-content-md-center:nth-child(1) > span:nth-child(1)',
            'max': 'div.justify-content-md-center:nth-child(2) > span:nth-child(1)',
            'city': 'h2.text-center',
            'icon': 'div.col-md-auto:nth-child(3) > a:nth-child(1) > img:nth-child(1)'
        },
        'route' : {
            'geocode' : 'autocomplete/',
            'prevision' : 'previsao/'

        },
        'default': {'cities' : [['cuiaba', 'juina', 'alta_floresta', 'vila_rica', 'barra_do_garcas', 'rondonopolis'], ['caceres', 'tangara_da_serra', 'diamantino', 'sorriso', 'juara', 'sinop']]},
        'render' : {
            'models' : ['cptec-1.jinja'],
            'styles' : ['cptec-1.css'],
            'images' : ['cptec-1.png'],
            'out'    : 'cptec.jpg',
            'options' : [
                {
                    'width': '1080',
                    'height': '1920',
                    'xvfb': ''
                }
            ]
        }
    },
    'inmet' : {
        'api' : 'http://apitempo.inmet.gov.br/estacao',
        'stations' : {        
            'SAPEZAL'                           :'A911',
            'COTRIGUAÇÚ'                        :'A919',
            'APIACAS'                           :'A910',
            'JUÍNA'                             :'A920',
            'JUARA'                             :'A9114',
            'ALTA FLORESTA'                     :'A924',
            'CARLINDA'                          :'A926',
            'GUARANTÃ DO NORTE'                 :'A906',
            'MATUPA'                            :'83214',
            'SÃO JOSÉ DO XINGU'                 :'A942',
            'SÃO FELIX DO ARAGUAIA'             :'A921',
            'SERRA NOVA DOURADA'                :'A943',
            'QUERÊNCIA'                         :'A916',
            'CANARANA'                          :'83270',
            'ÁGUA BOA'                          :'A908',
            'NOVA XAVANTINA'                    :'83319',
            'GAUCHA DO NORTE'                   :'A930',
            'COMODORO'                          :'A913',
            'BRASNORTE'                         :'A927',
            'NOVA MARINGA'                      :'A928',
            'SÃO JOSÉ DO RIO CLARO'             :'A903',
            'CAMPO NOVO DOS PARECIS'            :'A905',
            'VILA BELA DA SANTÍSSIMA TRINDADE'  :'A922',
            'PONTES E LACERDA'                  :'A937',
            'SALTO DO CEU'                      :'A936',
            'TANGARÁ DA SERRA'                  :'A902',
            'PORTO ESTRELA'                     :'A935',
            'CACERES'                           :'A941',
            'DIAMANTINO'                        :'83309',
            'ROSARIO OESTE'                     :'A944',
            'CUIABÁ'                            :'A901',
            'SINOP'                             :'A917',
            'SORRISO'                           :'A904',
            'NOVA UBIRATÃ'                      :'A929',
            'PARANATINGA'                       :'A915',
            'SANTO ANTONIO DO LESTE'            :'A931',
            'PRIMAVERA DO LESTE'                :'A923',
            'POXOREO'                           :'83358',
            'CAMPO VERDE'                       :'A912',
            'RONDONÓPOLIS'                      :'A907',
            'ITIQUIRA'                          :'A933',
            'GUIRATINGA'                        :'A932',
            'ALTO TAQUARI'                      :'A934'
        }
    },
    'covid': {
        'link': 'https://app.powerbi.com/view?r=eyJrIjoiYjJhNjdhMGQtNWRmNy00ZTM4LWE3YmUtMjFmMTg3YzE5ZjAzIiwidCI6ImNkMWVlZGQ2LTgyMjktNDM1Zi05YmQ1LWM2OWFiZDgxNzMzNyJ9',
        'path': {
            'confirmed': 'visual-container-modern.visual-container-component:nth-child(3) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'interned': '.visualContainerHost > visual-container-repeat:nth-child(1) > visual-container-modern:nth-child(1) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'recovered': 'visual-container-modern.visual-container-component:nth-child(6) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'isolated': 'visual-container-modern.visual-container-component:nth-child(7) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'dead': 'visual-container-modern.visual-container-component:nth-child(5) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'table': {
                'cities': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(%)',
                'cases': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(%)'
            },
            'button': '/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[15]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[3]/div'
        },
        'render' : {
            'models' : ['corona-1.jinja', 'corona-2.jinja'],
            'styles' : ['corona-1.css', 'corona-2.css'],
            'images' : ['corona-1.png', 'corona-2.png'],
            'out'    : 'corona.jpg',
            'options' : [
                {
                    'width': '1080',
                    'height': '1080',
                    'xvfb': ''
                },
                {
                    'width': '1080',
                    'height': '1920',
                    'xvfb': ''
                }
            ]
        }
    },
    'telegram' : {
        'token' : open('token.txt').read(), 
        'messages' : {
            'welcome' : \
'''
Bem vindo gerador ao de relatários.

Escolha uma opção:

1 - Gerar Previsão do tempo
2 - Gerar Painel do Covid-19
3 - Situação Alertas
''',
            'generate' : {
                '1' : {
                    'service' : 'cptec', 
                    'warning' : 'Gerando arquivo de previsão do tempo, aguarde um momento...', 
                    'success' : 'Arquivo de previsão diária gerado com sucesso!',
                    'error'   : 'Opa! acho que algum problema está acontecendo... tenta de novo mais tarde, obrigado!'
                },
                '2' : {
                    'service' : 'covid', 
                    'warning' : 'Gerando arquivos do painel covid, aguarde um momento...',
                    'success' : 'Painel covid-19 gerado com sucesso!',
                    'error'   : 'Opa! acho que algum problema está acontecendo... tenta de novo mais tarde, obrigado!'
                },
                '3' : {
                    'service' : 'alerts', 
                    'warning' : 'Sistema de notificações de alerta: '
                }
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
    }
}