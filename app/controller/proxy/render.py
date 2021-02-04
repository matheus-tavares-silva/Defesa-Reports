from jinja2 import Template
from itertools import chain
from ...env import env, paths
from ..folder import folder
from ...utils import folium
import os

from .builder import Builder 
class Render(Builder):
    def __init__(self, reponse=list, name=str, **kwargs):
        self.__reponse   = reponse if type(reponse) == list else [reponse]
        self.__name      = name
        self.__overwrite = kwargs.get('overwrite', False)
        self.__method    = kwargs.get('method', 'wkhtml')
        self.__use_temp  = kwargs.get('use_temp', False)
        self.__page_size = kwargs.get('page_size', {'width' : 1920, 'height' : 1080})
        self.__folium_zoom = kwargs.get('folium_zoom', 6)
        self.content       = self.__transfer()
        

    def __transfer(self):
        fileout = []
        templates = []
        get_abspath = lambda f : os.path.abspath(f)


        options = env[self.__name]['render']
        
        for content in self.__reponse:
            templates.append([
                template.render(content, image=get_abspath(paths['loader']['image'] + image)) for template, image in zip([
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

                file_out = get_abspath(
                    Builder(file_out=out)._build_by_selenium(
                        link=folium(data=content, zoom=self.__folium_zoom),
                    ).result()
                ) if not os.path.isfile(out) else get_abspath(out) if self.__overwrite else None, 

                message  = template if not self.__overwrite else {
                    'type'         : content['type'],
                    'event'        : content['event'],
                    'onset'        : content['onset'],
                    'headline'     : content['headline'],
                    'expires'      : content['expires'],
                    'web'          : content['web'],
                    'description'  : '.'.join(content['description'].split('.')[1:]),
                    'color'        : content['color']
                }

                if(not None in file_out and message):
                    fileout.append(
                        {
                            'file': file_out[0] if type(file_out) == tuple else file_out,
                            'message': message
                        }
                    )
               
        else:
            for index, template in enumerate(templates):

                out     = folder() + options['out'].replace('.', '-{}.'.format(index), -1)
                config  = options['options'][0] if len(options['options']) == 1 else options['options'][index]
                css     = paths['loader']['css'] + options['styles'][0] if len(options['styles']) == 1 else paths['loader']['css'] + options['styles'][index]

                if(self.__method == 'selenium'):
                    fileout.append(
                        Builder(
                            template=template, 
                            file_out=out
                        )._build_by_selenium(
                            use_temp=self.__use_temp, 
                            size=self.__page_size
                        ).result()
                    )
                elif(self.__method == 'wkhtml'):
                    fileout.append(
                        Builder(
                            template=template, 
                            file_out=out
                        )._build_by_imgkit(
                            options=config, 
                            file_css=css
                        ).result()
                    )
            
        return fileout