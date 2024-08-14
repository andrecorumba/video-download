from pytube import YouTube
import yt_dlp

def download_with_pytube(url, output_path='.'):
    try:
        # Cria o objeto YouTube
        yt = YouTube(url)
        
        # Seleciona o stream de maior resolução disponível
        stream = yt.streams.get_highest_resolution()
        
        # Faz o download do vídeo
        stream.download(output_path)
        
        print(f'Vídeo baixado com sucesso: {yt.title}')
    except Exception as e:
        print(f'Ocorreu um erro ao tentar baixar o vídeo: {e}')


def download_with_yt_dlp(url, output_path='.'):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Vídeo baixado com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro ao tentar baixar o vídeo: {e}')

if __name__ == '__main__':
    print("Fazendo Download do Vídeo")
    download_with_yt_dlp(
        # 'https://www.youtube.com/watch?v=78_1tqjRLPE',
        "https://www.youtube.com/watch?v=0TdHj9vruwU",
        '/Users/andrelmr/python-projects/youtube-download'
        )
    print("Download Completo!")