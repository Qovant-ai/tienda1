"""Arma los archivos del tema "Gift List Co v1" a partir de los del tema Pawlet v4 (carpeta theme/).

Uso: python3 brand/tools/build_giftlist_theme.py theme theme-giftlist
Solo escribe los archivos que cambian; el resto del tema queda igual que en la copia de v4.
"""
import json
import os
import re
import sys

SRC, OUT = sys.argv[1], sys.argv[2]

PALETTE = {  # Pawlet -> Gift List Co
    "#1b2b48": "#24203f", "#1B2B48": "#24203f",
    "#ff9f6e": "#f2675f", "#FF9F6E": "#f2675f",
    "#fff3ea": "#fff6f0",
    "#ffe7d6": "#ffe4e1",
    "#3b4a66": "#4b4766",
    "#e7dfd6": "#ece1da",
    "#f6efe8": "#f7eee9",
}


def recolor(text):
    for a, b in PALETTE.items():
        text = text.replace(a, b)
    return text


def read(rel):
    with open(os.path.join(SRC, rel), encoding="utf-8") as fh:
        return fh.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote", rel)


def write_json(rel, data):
    write(rel, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def load_json(rel):
    return json.loads(re.sub(r"/\*.*?\*/", "", read(rel), flags=re.S))


TRUST = {
    "trust_shipping": {"type": "item", "settings": {"icon": "truck", "title": "Free US shipping", "text": "On every order, no minimum"}},
    "trust_returns": {"type": "item", "settings": {"icon": "refresh", "title": "30-day returns", "text": "Easy returns, no fuss"}},
    "trust_checkout": {"type": "item", "settings": {"icon": "lock", "title": "Secure checkout", "text": "Pay safely with PayPal"}},
    "trust_help": {"type": "item", "settings": {"icon": "chat", "title": "Real humans", "text": "Support in English & español"}},
}
TRUST_LABEL = "Why shop with Gift List Co"

# --- config/settings_data.json -------------------------------------------------
settings = load_json("config/settings_data.json")
cur = settings["current"]
cur["logo"] = "shopify://shop_images/giftlist-logo-horizontal.png"
cur["logo_inverse"] = "shopify://shop_images/giftlist-logo-horizontal-white.png"
cur["favicon"] = "shopify://shop_images/giftlist-favicon.png"
write("config/settings_data.json", recolor(json.dumps(settings, indent=2, ensure_ascii=False)) + "\n")

# --- templates/index.json -------------------------------------------------------
index = load_json("templates/index.json")
S = index["sections"]

hero = S["hero"]["settings"]
hero.update({
    "background_color": "#fff6f0",
    "eyebrow": "Holiday gift guide 2026",
    "heading": "Find the perfect gift for",
    "heading_highlight": "everyone you love.",
    "text": "<p>Shop by who you’re buying for: mom, dad, the kids, your partner, grandparents, best friends and even the dog. Every gift ships free from US warehouses.</p>",
    "button_1_label": "Shop all gifts",
    "button_1_link": "shopify://collections/gifts",
    "button_2_label": "Gifts for Mom",
    "button_2_link": "shopify://collections/gifts-for-mom",
    "check_1": "Free US shipping on every order",
    "check_2": "Arrives in 4–8 business days",
    "check_3": "30-day returns",
    "image": "shopify://shop_images/giftlist-hero.jpg",
    "badge_top": "Shipping",
    "badge_price": "$0",
    "badge_bottom": "every US order",
})

S["trust"]["blocks"] = TRUST
S["trust"]["settings"]["label"] = TRUST_LABEL

RECIPIENTS = [
    ("for_daughter", "gifts-for-daughter", "For Your Daughter", "giftlist-for-daughter.jpg", "#fce1ec"),
    ("for_son", "gifts-for-son", "For Your Son", "giftlist-for-son.jpg", "#dceafa"),
    ("for_mom", "gifts-for-mom", "For Mom", "giftlist-for-mom.jpg", "#ffe4dc"),
    ("for_dad", "gifts-for-dad", "For Dad", "giftlist-for-dad.jpg", "#e2e7ef"),
    ("for_girlfriend", "gifts-for-girlfriend", "For Your Girlfriend", "giftlist-for-girlfriend.jpg", "#fbe0e3"),
    ("for_boyfriend", "gifts-for-boyfriend", "For Your Boyfriend", "giftlist-for-boyfriend.jpg", "#dff0ea"),
    ("for_grandma", "gifts-for-grandma", "For Grandma", "giftlist-for-grandma.jpg", "#f3e6f5"),
    ("for_grandpa", "gifts-for-grandpa", "For Grandpa", "giftlist-for-grandpa.jpg", "#ece6dc"),
    ("for_bestie_her", "gifts-for-best-friend-her", "For Your Best Friend (Her)", "giftlist-for-bestie-her.jpg", "#ffe9d6"),
    ("for_bestie_him", "gifts-for-best-friend-him", "For Your Best Friend (Him)", "giftlist-for-bestie-him.jpg", "#e6e3f7"),
    ("for_pet", "gifts-for-pets", "For Your Pet", "giftlist-for-pet.jpg", "#fff1c7"),
    ("all", "gifts", "All Gifts", "giftlist-all.jpg", "#24203f"),
]
cats = S["categories"]
cats["settings"].update({
    "background_color": "#ffffff",
    "eyebrow": "Shop by recipient",
    "heading": "Who are you shopping for?",
    "text": "<p>Pick a person and we’ll show you gifts they’ll actually use.</p>",
    "product_label_one": "gift",
    "product_label_other": "gifts",
})
cats["blocks"] = {
    key: {"type": "category", "settings": {
        "collection": handle, "title": title, "text": "", "image": f"shopify://shop_images/{img}",
        "link": "", "size": "small", "button_label": "", "style": "photo", "card_color": color}}
    for key, handle, title, img, color in RECIPIENTS
}
cats["block_order"] = [r[0] for r in RECIPIENTS]

bs = S["best_sellers"]
bs["settings"]["collection"] = "gifts"
bs["settings"]["background_color"] = "#fff6f0"
head = bs["blocks"]["static-header"]["blocks"]
head["product_list_text"]["settings"]["text"] = "<h2>Best-selling gifts</h2>"
head["product_list_button"]["settings"]["label"] = "Shop all gifts"

why = S["why"]["settings"]
why.update({
    "background_color": "#24203f",
    "image": "shopify://shop_images/giftlist-why.jpg",
    "eyebrow": "Why Gift List Co",
    "heading": "Gift-giving, solved",
    "text": "<p>We pick gifts that are useful, well made and fairly priced, then sort them by who they’re for. Find the right one in minutes, not hours.</p>",
    "point_1": "Gifts sorted by recipient, so you skip the endless scrolling",
    "point_2": "Free US shipping on every order, from US warehouses",
    "point_3": "30-day returns if it’s not quite right",
    "button_label": "Shop all gifts",
    "button_link": "shopify://collections/gifts",
    "sticker_icon": "gift",
})

S.pop("club", None)
faq = S["faq"]
faq["blocks"] = {
    "q_shipping": {"type": "question", "settings": {"question": "How long does shipping take?", "answer": "<p>Orders ship from US warehouses and usually arrive in 4–8 business days. Shipping is free on every US order, and you’ll get tracking by email.</p>"}},
    "q_gift": {"type": "question", "settings": {"question": "Can I send a gift straight to them?", "answer": "<p>Yes. At checkout, enter their name and address as the shipping address and we’ll deliver it to their door.</p>"}},
    "q_returns": {"type": "question", "settings": {"question": "What if they don’t love it?", "answer": "<p>Return unused items within 30 days of delivery. If something arrives damaged, send us a photo and we’ll replace it or refund you.</p>"}},
    "q_pay": {"type": "question", "settings": {"question": "How do I pay?", "answer": "<p>We accept PayPal. Your payment is processed securely by PayPal, and we never see your card details.</p>"}},
    "q_spanish": {"type": "question", "settings": {"question": "¿Hablan español?", "answer": "<p>¡Sí! Escríbenos en español cuando quieras.</p>"}},
}
faq["block_order"] = ["q_shipping", "q_gift", "q_returns", "q_pay", "q_spanish"]
faq["settings"]["heading"] = "Good questions, honest answers"

index["order"] = ["hero", "trust", "categories", "best_sellers", "why", "faq"]
write("templates/index.json", recolor(json.dumps(index, indent=2, ensure_ascii=False)) + "\n")

# --- templates/product.json -----------------------------------------------------
product = load_json("templates/product.json")
def find_block(node, key):
    """Busca un bloque por su clave en cualquier nivel (los bloques pueden ir dentro de grupos)."""
    if isinstance(node, dict):
        if key in node.get("blocks", {}):
            return node["blocks"][key]
        for value in node.get("blocks", {}).values():
            found = find_block(value, key)
            if found:
                return found
    return None


main = product["sections"]["main"]
blocks = {"perks": find_block(main, "perks"), "info": find_block(main, "info")}
perks = blocks["perks"]["settings"]
perks.update({"free_shipping_threshold": 0, "shipping_text": "Free US shipping", "shipping_free_text": "Free US shipping"})
blocks["info"]["settings"]["content_1"] = (
    "<p>Free US shipping on every order. Ships from a US warehouse and usually arrives in 4–8 business days, "
    "with tracking by email.</p><p><a href=\"/pages/shipping-policy\" title=\"Shipping Policy\">Shipping policy</a></p>")
blocks["info"]["settings"]["title_2"] = "Returns"
blocks["info"]["settings"]["content_3"] = (
    "<p>We’re happy to help in English or Spanish. Check our <a href=\"/pages/faqs\" title=\"FAQ\">FAQ</a> or "
    "<a href=\"/pages/contact\" title=\"Contact\">send us a message</a>.</p>")
product["sections"]["trust"]["blocks"] = TRUST
product["sections"]["trust"]["settings"]["label"] = TRUST_LABEL
write("templates/product.json", recolor(json.dumps(product, indent=2, ensure_ascii=False)) + "\n")

# --- templates/collection.json --------------------------------------------------
collection = load_json("templates/collection.json")
collection["sections"]["trust"]["blocks"] = TRUST
collection["sections"]["trust"]["settings"]["label"] = TRUST_LABEL
write("templates/collection.json", recolor(json.dumps(collection, indent=2, ensure_ascii=False)) + "\n")

# --- sections/footer-group.json -------------------------------------------------
footer = read("sections/footer-group.json")
footer = footer.replace(
    "<p>New arrivals, member offers and a sneak peek at each month's Club box. No spam, unsubscribe anytime.</p>",
    "<p>New gift ideas, holiday deals and last-day-to-order reminders. No spam, unsubscribe anytime.</p>")
footer = footer.replace(
    "<p><strong>Pawlet Club</strong></p><p>Hand-picked favorites for dogs and cats, shipped from US warehouses, plus monthly Club boxes. Hablamos español.</p>",
    "<p><strong>Gift List Co</strong></p><p>Thoughtful gifts sorted by who you’re shopping for, with free shipping from US warehouses. Hablamos español.</p>")
footer = footer.replace('"heading": "Pawlet Club"', '"heading": "Shop"')
write("sections/footer-group.json", recolor(footer))

# --- sections and snippets (icons, colors, block limit) -------------------------
for rel in ("sections/pawlet-hero.liquid", "sections/pawlet-gift.liquid", "sections/pawlet-categories.liquid"):
    text = read(rel)
    text = text.replace("{% render 'pawlet-icon', icon: 'paw' %}{{ s.eyebrow", "{% render 'pawlet-icon', icon: 'gift' %}{{ s.eyebrow")
    text = text.replace("icon: 'paw', class: 'pc-paw-deco", "icon: 'gift', class: 'pc-paw-deco")
    text = text.replace("{% render 'pawlet-icon', icon: 'paws' %}", "{% render 'pawlet-icon', icon: 'sparkle' %}")
    text = text.replace('"max_blocks": 10', '"max_blocks": 16')
    write(rel, recolor(text))

for rel in ("sections/pawlet-ship-notice.liquid", "snippets/pawlet-styles.liquid", "sections/header-group.json"):
    write(rel, recolor(read(rel)))
