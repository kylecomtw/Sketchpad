
pursue_templates = [
    "剛剛有提過{key}。我找到一個和{title}有關的東西{content}",
    "說到{key}.....維基有相關的東西：{content}"    
]

spread_templates = [
    "至於{key}...",
    "{key}！"
]

reflection_templates = [
    "你好像對{key}很有興趣。我找到一個和{title}有關的東西{content}"
]

elicit_templates = [
    "對了，我昨天發現有個東西在介紹{title}。{content}。",
    "你知道{title}嗎？{content}"
]

connectives_templates = [
    "而且", "還有", "也", "還是"
]

script_templates = {
    "pursue": pursue_templates,
    "spread": spread_templates,    
    "psychoanalysis": reflection_templates,
    "random": elicit_templates,
    "connectives": connectives_templates
}
