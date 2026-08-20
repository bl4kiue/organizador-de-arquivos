from pathlib import Path
import shutil

pasta_origem = Path("C:/Users/Miche/OneDrive/Desktop/minha pasta(caua)")

pastas = {
    ".pdf": "PDFs",
    ".mp3": "Musicas",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".txt": "Textos",
    ".mp4": "Videos"
}

def mover_arquivos(origem, destino):
    """
    Move um arquivo da origem para o destino.

    :param origem: Caminho do arquivo que será movido.
    :param destino: Caminho da pasta para onde o arquivo será movido.
    """
    try:
        shutil.move(origem, destino)
        print(f"Arquivo movido com sucesso para: {destino}")
    except Exception as erro:
        print(f"Não foi possivel mover o arquivo. {erro}")



def organizar_pasta(minhapasta):
    """
    Organiza os arquivos de uma pasta de acordo com suas extensões.

    Cria as pastas de destino quando necessário e move os arquivos
    para suas categorias.

    :param minhapasta: Caminho da pasta que será organizada.
    """
    #Cria um loop que vai usar o .interdir() para percorrer a pasta
    for item in minhapasta.iterdir():
        if item.is_file():#verifica se é um arquivo // item.suffix é para ler apenas a extensão do arquivo
            if item.suffix in pastas: #ignora as pastas, pois devemos organizar apenas arquivos
                print(f"{item.suffix} -> {pastas[item.suffix]}")

                pasta_destino = minhapasta / pastas[item.suffix] 
                if not pasta_destino.exists():
                    pasta_destino.mkdir(parents=True, exist_ok=True) #cria a pasta destino caso não exista
                    print("Pasta foi criada.")
                else:
                    print("Pasta ja existente.")
                mover_arquivos(item,pasta_destino)

            else:
                print("Extensão não cadastrada")#se n tiver, ele avisa

        else:
            print(f"Foi encontrado uma pasta")
        #Vai avaliar se a pasta com o nome item do dicionario existe, se existir retornar true,se não: false

#programa principal
print("=-=" * 10)
print("    Organizador de codigo")
print("=-=" * 10)