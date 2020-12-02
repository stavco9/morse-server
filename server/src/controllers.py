import socket
import os
import morse_talk as morse

def translate_text_to_morse(text):
    try:
        text_translated = morse.encode(text)
    except:
        return None

    return text_translated