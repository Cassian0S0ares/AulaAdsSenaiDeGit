import webbrowser
import psutil

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
chrome_esta_aberto = False

while True:
    esta_rodando = any(p.name().lower() == 'chrome.exe' for p in psutil.process_iter())
    webbrowser.open(url)
    if not esta_rodando and chrome_esta_aberto:
        print('Chrome fechado. Abrindo nova aba...')
        webbrowser.open(url)
        chrome_esta_aberto = True
    elif not esta_rodando and not chrome_esta_aberto:
        print('Chrome não está aberto. Abrindo URL pela primeira vez...')
        webbrowser.open(url)
        chrome_esta_aberto = True
    elif esta_rodando:
        chrome_esta_aberto = True


