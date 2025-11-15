# Entrega el libro como un string
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def conteo(book):  
    texto = book.lower()
    dicc = {}
    for t in texto:
        if t in dicc:
            dicc[t] += 1
        else:
            dicc[t] = 1
    return dicc

def sort_on(items):
    return items["num"]

def order_count(chars):
    lista = []   
    for ch, count in chars.items():
        if ch.isalpha():
            lista.append({"char":ch, "num":count})
    lista.sort(reverse=True, key=sort_on)
    return lista











