from jinja2 import Template
from itertools import chain
from .builder_imgkit import builder as imgbuild
from .builder_selenium import builder as selbuild
from ...env import env, paths
from ..folder import folder

import os

def loader(proxy):
    contents = proxy()

    contents = contents if type(contents) == list else [contents]

    fileout = []

    render = env[proxy.__name__]['render']
    
    templates = []
    for content in contents:
        templates.append([
            template.render(content, image=os.path.abspath(paths['loader']['image'] + image)) for template, image in zip([
                        Template(open(file).read()) for file in [
                            (paths['loader']['model'] + model) for model in render['models'] if os.path.exists(paths['loader']['model'] + model)
                        ]
                    ], render['images'] if render['images'] != [] else ['' for empty in range(len(contents))]
                )
            ]
        )

    templates = list(chain(*templates)) if any(isinstance(i, list) for i in templates) else templates

    if(proxy.__name__ == 'alerts'):

        for content, template in zip(contents, templates):

            out = folder('Alerts', False) + '/' + 'Alert.png'.replace('.', '-{}.'.format(content['web']), -1)
            
            if(not os.path.isfile(out)):
                fileout.append(
                    selbuild(
                        template=template,
                        out=out,
                        content=content
                    ).result()
                )
    
    else:

        for index, template in enumerate(templates):

            out = folder() + render['out'].replace('.', '-{}.'.format(index), -1)
            options = render['options'][0] if len(render['options']) == 1 else render['options'][index]
            css = paths['loader']['css'] + render['styles'][0] if len(render['styles']) == 1 else paths['loader']['css'] + render['styles'][index]

            fileout.append(
                imgbuild(
                    mode=proxy.__name__,
                    content=template,
                    fileout=out,
                    options=options,
                    filecss=css
                ).result()
            )
           
    return fileout