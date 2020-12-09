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
        'api' : 'http://apitempo.inmet.gov.br/',
        'route' : {
            'station' : 'estacao/'
        },
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
        },
        'render' : {
            'models' : ['inmet-1.jinja'],
            'styles' : ['inmet-1.css'],
            'images' : ['inmet-1.png'],
            'out'    : 'inmet.png',
            'options' : [
                {
                    'width': '1080',
                    'height': '1920',
                    'format' : 'png',
                    'quality' : 100,
                    'xvfb': ''
                }
            ]
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
                'cities': 'visual-container-modern.visual-container-component:nth-child(15) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(%)',
                'cases': 'visual-container-modern.visual-container-component:nth-child(15) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(%)'
            },
            'search' : {
                'cities' : '.bodyCells > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
            },
            'next' : '/html/body/div[1]/ui-view/div/div[2]/logo-bar/div/div/div/logo-bar-navigation/span/a[3]',
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
    'report' : {
        'api' : {
            'foco' : 'http://queimadas.dgi.inpe.br/queimadas/bdqueimadas/export-graphic-data?dateTimeFrom={}&dateTimeTo={}&satellites=AQUA_M-T&biomes=&risk=&continent=8&countries=33&states=03351&specialRegions=&id=firesByCity&protectedArea=&industrialFires=false'
        },
        'render' : {
            'models' : ['report-1.jinja'],
            'styles' : ['report-1.css'],
            'images' : ['report-1.png'],
            'out'    : 'report.png',
            'options' : [
                {
                    'width': '1080',
                    'height': '1920',
                    'javascript-delay' : 3000,
                    'xvfb': ''
                }
            ]
        }
    },
    'local_report' : {
        'api' : 'https://run.blockspring.com/api_v2/blocks/query-public-google-spreadsheet?=&flatten=true',
        'payload' : {
            "query":"SELECT A, B, C, D, E, F, G, H\r\n",
            "url":"https://docs.google.com/spreadsheets/d/1M_cCPE5J2JEsP1zmHt0_g9XjCehzrRPQ/edit#gid=588465278",
            "_blockspring_spec":r'true',
            "_blockspring_ui":r'true'
        },
        'render' : {
            'models' : ['local_report-1.jinja'],
            'styles' : ['local_report-1.css'],
            'images' : ['local_report-1.png'],
            'out'    : 'local_report.jpg',
            'options' : [
                {
                    'width': '1080',
                    'height': '1080',
                    'xvfb': ''
                }
            ]
        }
    },
    'telegram' : {
        'token' : open('token.txt', 'r').read().rstrip('\n'), 
        'messages' : {
            'welcome' : \
'''
Bem vindo gerador ao de relatários.

Escolha uma opção:

1 - Gerar Previsão do tempo
2 - Gerar Painel do Covid-19
3 - Situação Alertas
4 - Dados de Estações do Inmet 
5 - Gerar Boletim Diário
6 - Gerar Boletim Local Diário
''',
            'generate' : {
                '1' : {
                    'service' : 'cptec', 
                    'warning' : 'Gerando arquivo de previsão do tempo, aguarde um momento...', 
                    'success' : 'Arquivo de previsão diária gerado com sucesso!',
                    'error'   : 'Opa! algum problema está aconteceu... tenta de novo mais tarde, obrigado!'
                },
                '2' : {
                    'service' : 'covid', 
                    'warning' : 'Gerando arquivos do painel covid, aguarde um momento...',
                    'success' : 'Painel covid-19 gerado com sucesso!',
                    'error'   : 'Opa! algum problema está aconteceu... tenta de novo mais tarde, obrigado!'
                },
                '3' : {
                    'service' : 'alerts', 
                    'warning' : 'Sistema de notificações de alerta: '
                },
                '4' : {
                    'service' : 'inmet',
                    'warning' : 'Gerando documento solicitado, aguarde um momento...',
                    'success' : 'Documento com os dados solicitados gerado com sucesso!',
                    'error'   : 'Opa! algum problema está aconteceu... tenta de novo mais tarde, obrigado!',
                    'options' : {
                        'cities'    : 'Digite o nome da cidade a qual você deseja coletar os dados, ex:. \'Cuiabá\' ou \'Cáceres\':',
                        'start'     : 'Digite a data e o horário inicial por extenso separando o horário da data, ex:. \'01012020 10\' (01/01/2020 10:00) ou \'01012020 0\' (01/01/2020 00:00):',
                        'end'       : 'Agora a data e o horário final dos dados a serem coletados da mesma forma:',
                        'filter'    : 'Digite seria o tipo da informação que você deseja separado por espaços, ex:. \'chuva\' ou \'vento\' ou \'tudo\'(Para vento e chuva):',
                        'temperature' : 'Dejesa incluir dados sobre a temperatura, digite \'sim\' ou \'não\':',
                        'unknown'   : 'Desculpe, Não entendi a sua solicitação',
                        'info'      : 'Caso queira cancelar a operação apenas digite: \'cancelar\''
                    }
                },
                '5' : {
                    'service' : 'report', 
                    'warning' : 'Gerando arquivos do boletim diário, aguarde um momento...',
                    'success' : 'Boletim diário gerado com sucesso!',
                    'error'   : 'Opa! algum problema está aconteceu... tenta de novo mais tarde, obrigado!'
                },
                '6' : {
                    'service' : 'local_report', 
                    'warning' : 'Gerando arquivos do boletim local diário, aguarde um momento...',
                    'success' : 'Boletim local diário gerado com sucesso!',
                    'error'   : 'Opa! algum problema está aconteceu... tenta de novo mais tarde, obrigado!',
                    'options' : {
                        'cities'    : 'Digite o nome da cidade a qual você deseja coletar os dados, ex:. \'Cuiabá\' ou \'Cáceres\':',
                        'info'      : 'Caso queira cancelar a operação apenas digite: \'cancelar\'',
                        'unknown'   : 'Desculpe, Não entendi a sua solicitação',
                    }
                }
            },
            'unknown' : \
'''
Desculpe, não entedi sua solicitação.

Aqui estão algumas opções:

1 - Gerar Previsão do tempo
2 - Gerar Painel do Covid-19
3 - Situação Alertas
4 - Dados de Estações do Inmet 
5 - Gerar Boletim Diário
6 - Gerar Boletim Local Diário
'''
        }
    }
}
