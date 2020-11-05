from jinja2 import Template
from itertools import chain
from ...env import env, paths
from ..folder import folder
from ...utils import folium
import os

from .builder import Builder 
class Render(Builder):
    def __init__(self, reponse=[], name=''):
        self.__reponse = reponse if type(reponse) == list else [reponse]
        self.__name = name

        self.content = self.__transfer()

    def __transfer(self):
        fileout = []
        templates = []

        options = env[self.__name]['render']
        
        for content in self.__reponse:
            templates.append([
                template.render(content, image=os.path.abspath(paths['loader']['image'] + image)) for template, image in zip([
                            Template(open(file).read()) for file in [
                                (paths['loader']['model'] + model) for model in options['models'] if os.path.exists(paths['loader']['model'] + model)
                            ]
                        ], options['images'] if options['images'] != [] else ['' for empty in range(len(self.__reponse))]
                    )
                ]
            )

        templates = list(chain(*templates)) if any(isinstance(i, list) for i in templates) else templates

        if(self.__name == 'alerts'):

            for content, template in zip(self.__reponse, templates):

                out = folder('Alerts', False) + '/' + 'Alert.png'.replace('.', '-{}.'.format(content['web']), -1)
                
                if(not os.path.isfile(out)):
                    fileout.append(
                        {
                        'file': Builder(file_out=out)._build_by_selenium(
                                        link=folium(data=content),
                                    ).result(), 
                        'message': template
                        }
                    )
        
        else:

            for index, template in enumerate(templates):

                out = folder() + options['out'].replace('.', '-{}.'.format(index), -1)
                config = options['options'][0] if len(options['options']) == 1 else options['options'][index]
                css = paths['loader']['css'] + options['styles'][0] if len(options['styles']) == 1 else paths['loader']['css'] + options['styles'][index]

                fileout.append(
                    Builder(template=template, file_out=out)._build_by_imgkit(options=config, file_css=css).result()
                )
            
        return fileout