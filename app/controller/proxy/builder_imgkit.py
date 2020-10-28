from concurrent.futures import ThreadPoolExecutor as executor
import imgkit
import tempfile
import os

def builder(**kwargs):
    
    def build(content='', fileout='', options={}, filecss=''):
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

    return executor().submit(
        build, 
        content=kwargs['content'],
        fileout=kwargs['fileout'],
        options=kwargs['options'],
        filecss=kwargs['filecss']
    )