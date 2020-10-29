from concurrent.futures import ThreadPoolExecutor as executor
from selenium import webdriver
from time import sleep
from ...env import gecko
import imgkit
import tempfile

class builder:
    def __init__(self, template='', file_out='', **kwargs):
        self.template = template
        self.file_out = file_out

        self.__execute = lambda function: executor().submit(function)

    def build_by_imgkit(self, options='', file_css=''):

        def build():
            try:
                with tempfile.NamedTemporaryFile(mode='w', suffix='.html') as file_temp:
                    file_temp.write(self.template)
                    
                    file_temp.flush()

                    imgkit.from_file(
                        filename=file_temp.name,
                        output_path=self.file_out,
                        options=options,
                        css=file_css,
                    )
            except:
                pass
            else:
                return self.file_out
        
        return self.__execute(build)
    
    def build_by_selenium(self, link, size={'width' : 1920, 'height' : 1080}, get_by_file=True, wait_javascript=10):

        def build():
            try:
                driver = webdriver.Firefox(executable_path=gecko)

                driver.set_window_size(size['width'], size['height'])

                driver.get('file:///' + link) if get_by_file else driver.get(link)

                sleep(wait_javascript)

                driver.save_screenshot(self.file_out)    
            except:
                return None
            finally:
                driver.quit()
                        
            return self.file_out

        return self.__execute(build)
    