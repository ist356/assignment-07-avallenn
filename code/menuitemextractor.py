if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    # $9.99 -> 9.99 float
    price = price.replace('$','')
    price = price.replace(',','')
    return float(price)

def clean_scraped_text(scraped_text: str) -> list[str]:
    # remove empty lines, lines that are "NEW!" or "NEW", lines that say "S", "V", "GS", "GF", or "P"
    # split the text on a newline
    # return the list of lines
    texts = scraped_text.split('\n')
    cleaned_text = []
    for text in texts:
        if text in ['GS',"V","S","P"]:
            continue
        if text.startswith("NEW"):
            continue
        if len(text.strip()) == 0:
            continue

        cleaned_text.append(text)
    return cleaned_text

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned_text = clean_scraped_text(scraped_text)
    name = cleaned_text[0]
    price = clean_price(cleaned_text[1])
    if len(cleaned_text) > 2:
        description = cleaned_text[2]
    if len(cleaned_text) == 2:
        description = 'No description available.'
    item = MenuItem(name=name, price=price, category=title, description=description)
    return item



if __name__=='__main__':
    pass
