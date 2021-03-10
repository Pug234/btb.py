class BytesToBits(object):
    try:
        from .word import word
        from .lyrics import lyrics
        from .madlibs import MadLibs
        from .speedtext import SpeedText
        from .reddit import reddit
        from .meme import meme
    except Exception as e:
        raise e
