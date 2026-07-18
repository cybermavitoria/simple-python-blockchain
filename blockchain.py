import hashlib

def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

dados_b1 = "Vitoria recebeu 50 moedas"
hash_anterior_b1 = "0"
hash_b1 = gerar_hash(dados_b1 + hash_anterior_b1)

dados_b2 = "Vitoria gastou 20 moedas"
hash_anterior_b2 = hash_b1
hash_b2 = gerar_hash(dados_b2 + hash_anterior_b2)

print(f"Bloco 1: {dados_b1}")
print(f"Hash 1 : {hash_b1}\n")

print(f"Bloco 2: {dados_b2}")
print(f"Link   : {hash_anterior_b2}")
print(f"Hash 2 : {hash_b2}")
