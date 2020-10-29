from jinja2 import Template
from itertools import chain
from .builder import builder
from ...env import env, paths
from ..folder import folder
from ...utils import folium
import os

def render(proxy):
    contents = proxy()

    contents = contents if type(contents) == list else [contents]

    fileout = []

    options = env[proxy.__name__]['render']
    
    templates = []
    for content in contents:
        templates.append([
            template.render(content, image=os.path.abspath(paths['loader']['image'] + image)) for template, image in zip([
                        Template(open(file).read()) for file in [
                            (paths['loader']['model'] + model) for model in options['models'] if os.path.exists(paths['loader']['model'] + model)
                        ]
                    ], options['images'] if options['images'] != [] else ['' for empty in range(len(contents))]
                )
            ]
        )

    templates = list(chain(*templates)) if any(isinstance(i, list) for i in templates) else templates

    if(proxy.__name__ == 'alerts'):

        for content, template in zip(contents, templates):

            out = folder('Alerts', False) + '/' + 'Alert.png'.replace('.', '-{}.'.format(content['web']), -1)
            
            if(not os.path.isfile(out)):
                fileout.append(
                    {
                       'file': builder(file_out=out).build_by_selenium(
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
                builder(template=template, file_out=out).build_by_imgkit(options=config, file_css=css).result()
            )
           
    return fileout