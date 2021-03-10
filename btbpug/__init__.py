class BytesToBits(object):
    try:
        from .word import word
        from .lyrics import lyrics
        from .madlibs import MadLibs
        from .speedtext import SpeedText
    except Exception as e:
        raise e
