from itertools import chain
from concurrent.futures import ThreadPoolExecutor as executor

def parallel(load):
    from .render import render
    from .proxy import covid, cptec, alerts

    load = [load] if type(load != list) else load

    results = [future.result() for future in [executor().submit(render, worker) for worker in [covid, cptec, alerts] if worker.__name__ in load]]

    return list(chain(*results)) if len(results) <= 1 else results
