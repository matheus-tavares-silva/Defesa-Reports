from jinja2 import Template
from itertools import chain
from glob import glob
from ...env import env
from ..folder import folder
import os

PATH_MODEL = './app/view/'
PATH_CSS = PATH_MODEL + 'static/css/'
PATH_IMAGE = PATH_MODEL + 'static/image/'

def loader(proxy, builder):
    contents = proxy()

    contents = contents if type(contents) == list else [contents]

    fileout = []

    render = env[proxy.__name__]['render']
    
    templates = []
    for content in contents:
        templates.append([template.render(content, image=os.path.abspath(PATH_IMAGE + image)) for template, image in zip([Template(open(file).read()) for file in [(PATH_MODEL + model) for model in render['models'] if os.path.exists(PATH_MODEL + model)]], render['images'])])

    templates = list(chain(*templates)) if any(isinstance(i, list) for i in templates) else templates

    for index, template in enumerate(templates):
    
        out = folder() + render['out'].replace('.', '-{}.'.format(index), -1)
        options = render['options'][0] if len(render['options']) == 1 else render['options'][index]
        css = PATH_CSS + render['styles'][0] if len(render['styles']) == 1 else PATH_CSS + render['styles'][index]

        fileout.append(
            builder(
                content=template,
                fileout=out,
                options=options,
                filecss=css
            ).result()
        )

    return fileout