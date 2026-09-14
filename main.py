#Etapa1 - Cadastro de uma startup e projetos

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
