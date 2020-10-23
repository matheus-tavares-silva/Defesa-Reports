from concurrent.futures import ThreadPoolExecutor as executor
import imgkit
import tempfile
import os

PATH_MODEL = './app/view/'
PATH_CSS = PATH_MODEL + 'static/css/'
PATH_IMAGE = PATH_MODEL + 'static/image/'
PATH_OUT = './out/'

def __build(content='', fileout='', options={}, filecss=''):

    try:
        file = tempfile.NamedTemporaryFile(mode='w', suffix='.html')

        file.write(content)
        
        file.flush()

        imgkit.from_file(
            filename=file.name,
            output_path=fileout,
            options=options,
            css=filecss,
        )

        file.close()
    except:
        pass
    else:
        return fileout
    
    return None

def builder(**kwargs):

    return executor().submit(
        __build, 
        content=kwargs['content'],
        fileout=kwargs['fileout'],
        options=kwargs['options'],
        filecss=kwargs['filecss']
    )