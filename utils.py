def open_html(file):
    with open(file, 'r', encoding='utf-8') as file:
        result = file.read()
        return result
