from pathlib import Path
import shutil

class Organizador():

    def __init__(self,pasta_origem,pastas):
        self.pasta_origem = pasta_origem
        self.pastas = pastas

    
    def mover_arquivos(self, origem, destino):
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

    def organizar_pasta(self):
        """
        Organiza os arquivos de uma pasta de acordo com suas extensões.

        Cria as pastas de destino quando necessário e move os arquivos
        para suas categorias.

        :param self.pasta_origem: Caminho da pasta que será organizada.
        """
        #Cria um loop que vai usar o .interdir() para percorrer a pasta
        for item in self.pasta_origem.iterdir():
            if item.is_file():#verifica se é um arquivo // item.suffix é para ler apenas a extensão do arquivo
                if item.suffix in self.pastas: #ignora as pastas, pois devemos organizar apenas arquivos
                    print(f"{item.suffix} -> {self.pastas[item.suffix]}")

                    pasta_destino = self.pasta_origem / self.pastas[item.suffix] 
                    if not pasta_destino.exists():
                        pasta_destino.mkdir(parents=True, exist_ok=True) #cria a pasta destino caso não exista
                        print("Pasta foi criada.")
                    else:
                        print("Pasta ja existente.")
                    self.mover_arquivos(item,pasta_destino)

                else:
                    print("Extensão não cadastrada")#se n tiver, ele avisa

            else:
                print(f"Foi encontrado uma pasta")
            #Vai avaliar se a pasta com o nome item do dicionario existe, se existir retornar true,se não: false



#programa principal
print("=-=" * 10)
print("    Organizador de codigo")
print("=-=" * 10)
caminho = input("Digite o caminho da pasta que deseja organizar: ")
pasta_origem = Path(caminho)
org1 = Organizador(
    pasta_origem,
    {
        ".pdf": "PDFs",
        ".mp3": "Musicas",
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".txt": "Textos",
        ".mp4": "Videos",
        ".xlsx": "Planilhas"
    }
) # Cria o objeto, define a pasta de origem e as categorias de arquivos.

org1.organizar_pasta()


#Path(r"C:\Users\SEPOF\Desktop\pasta_organizar_teste") pasta utilizada