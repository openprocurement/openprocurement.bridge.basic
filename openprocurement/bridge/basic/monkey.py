import traceback
import logging

exception_logger = logging.getLogger('exception_logger')


def print_exception(etype, value, tb, **kwargs):
    '''
    Monkey patching for handle Greenlets exception (gevent.hub.Hub#handle_error)
    '''
    try:
        exception_logger.error(''.join(traceback.format_exception(etype, value, tb)))
    except Exception as e:
        exception_logger.error('Exception logging error: {}'.format(repr(e)))
    return traceback.original_print_exception(etype, value, tb, **kwargs)


def patch_traceback():
    traceback.original_print_exception = traceback.print_exception
    traceback.print_exception = print_exception

