#Etapa1 e 2 - Cadastro de uma startup e projetos

startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("Startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])

bancadas = [
    [1, 0],
    [0, 1]
]

print("Bancadas:")
print("bancadas[0][0] =", bancadas[0][0], "(N1)")
print("bancadas[0][1] =", bancadas[0][1], "(N2)")
print("bancadas[1][0] =", bancadas[1][0], "(S1)")
print("bancadas[1][1] =", bancadas[1][1], "(S2)")
print("Legenda: 1 = Ocupado, 0 = Livre.")

# Etapa 3 - leitura do arquivo custos_cloud.csv sem laços de repetição
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_servidor_aws = arquivo.readline()
    linha_banco_postgres = arquivo.readline()
    linha_backup_cloud = arquivo.readline()
    linha_dominio_ssl = arquivo.readline()

print("Cabecalho lido:", cabecalho.strip())
print("Linha lida:", linha_servidor_aws.strip())
print("Linha lida:", linha_banco_postgres.strip())
print("Linha lida:", linha_backup_cloud.strip())
print("Linha lida:", linha_dominio_ssl.strip())

# Etapa 4 - consolidação e painel final
recurso_servidor, custo_servidor = linha_servidor_aws.strip().split(",")
recurso_banco, custo_banco = linha_banco_postgres.strip().split(",")
recurso_backup, custo_backup = linha_backup_cloud.strip().split(",")
recurso_dominio, custo_dominio = linha_dominio_ssl.strip().split(",")

custo_servidor_aws = float(custo_servidor.strip())
custo_banco_postgres = float(custo_banco.strip())
custo_backup_cloud = float(custo_backup.strip())
custo_dominio_ssl = float(custo_dominio.strip())

total = custo_servidor_aws + custo_banco_postgres + custo_backup_cloud + custo_dominio_ssl

print("\n=== Painel Final ===")
print("Startup:", startup["nome"])
print("Bancada alocada:", "Bancada N1")
print("Total de infraestrutura Cloud: R$ {:.2f}".format(total))
