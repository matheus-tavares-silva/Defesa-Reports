env = \
{
    'alert': {
        'link': 'https://alerts.inmet.gov.br/cap_12/',
        'path': {
            'root': '/html/body/table/tr/td/a'
        },
        'default' : {
            'country' : 'Mato Grosso',
            'date' : None
        }
    },
    'cptec': {
        'link': 'https://www.cptec.inpe.br/previsao-tempo/mt/',
        'path': {
            'min': 'div.justify-content-md-center:nth-child(1) > span:nth-child(1)',
            'max': 'div.justify-content-md-center:nth-child(2) > span:nth-child(1)',
            'city': 'h2.text-center',
            'icon': 'div.col-md-auto:nth-child(3) > a:nth-child(1) > img:nth-child(1)'
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
    'covid': {
        'link': 'http://www.saude.mt.gov.br/painelcovidmt2/',
        'path': {
            'panel': '/html/body/section/div/div/div/iframe',
            'confirmed': '.visualContainerHost > visual-container-repeat:nth-child(1) > visual-container-modern:nth-child(2) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'interned': 'visual-container-modern.visual-container-component:nth-child(32) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'recovered': 'visual-container-modern.visual-container-component:nth-child(5) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'isolated': 'visual-container-modern.visual-container-component:nth-child(6) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'dead': 'visual-container-modern.visual-container-component:nth-child(4) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
            'table': {
                'cities': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(%)',
                'cases': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(%)'
            },
            'button': '/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[14]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[3]'
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
    }
}