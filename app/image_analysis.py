from transformers import pipeline

def analisar_imagens(lista_imagens):
    analisador = pipeline("image-classification", model="facebook/imagebind")

    resultados = []
    for imagem in lista_imagens:
        resultado = analisador(imagem)
        resultados.append({
            "imagem": imagem,
            "descricao": resultado
        })
    
    return resultados