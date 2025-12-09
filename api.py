import paralleldots
paralleldots.set_api_key("<KEY>")

def ner(text):
    ner=paralleldots.ner(text)
    return ner