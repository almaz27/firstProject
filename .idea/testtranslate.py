import translators as ts

print(ts.translators_pool)
q_text = "«О ратификации Протокола о внесении изменений и дополнений в Договор между Кыргызской Республикой и Республикой Казахстан об оказании взаимной правовой помощи по гражданским и уголовным делам от 26 августа 1996 года, подписанного 26 мая 2022 года в городе Бишкек»"
print(ts.translate_text(q_text, translator='google', from_language='ru', to_language='en'))
# translate_text(query_text: str, translator: str = 'bing', from_language: str = 'auto', to_language: str = 'en', **kwargs)

