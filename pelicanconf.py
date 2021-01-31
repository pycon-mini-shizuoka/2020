#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'pycon-mini-shizuoka'
SITENAME = 'PyCon mini Shizuoka'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = "./pycon-mini-shizu-pelican-theme"

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# index.rst raw load html. exclude dir 
ARTICLE_EXCLUDES = ["rst_htmls"]

# save_as

ARTICLE_URL = '{category}/{author}/'
ARTICLE_SAVE_AS = '{category}/{author}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# github pages add CNAME

STATIC_PATHS = ['extra/front_img']
EXTRA_PATH_METADATA = {'extra/front_img': {'path': './front_img/'},
}


# =====[テーマ専用の設定をロード]=====

# フロントページの差し込み
COPYRIGHT_TEXT = "PyCon mini Shizuoka 実行委員会"
EVENT_FORNT_SUMMARY = "2020.02.29 SAT @藤枝 Biviキャン"

TWITTER_HASHTAG_URL= "https://twitter.com/hashtag/pycon_shizu"

# CFP_FROM_BOTTON_TEXT = "CfP応募終了しました"
# CFP_FORM_URL = "#cfp" # inner header link

CONNPASS_URL = "https://pycon-shizu.connpass.com/event/152678/"

# KYOSAN_INFO = "主催: PyCon mini Shizuoka 実行委員会 <br> 共催:藤枝ICTコンソーシアム 後援:藤枝市 / 静岡産業大学"

KYOSAN_INFO = "主催: PyCon mini Shizuoka 実行委員会 <br> 共催:藤枝ICTコンソーシアム 後援:藤枝市 / 静岡産業大学 / 一般社団法人PyCon JP"


# フロントページの移動用にidリンクをメニューに載せる
NAVMENU = (
    ("2020オンライン特設", "./2020_online/"),
    ("重要なお知らせ", "./important_notices/"),
    ("イベント情報", (
        ("キーノート", "./#keynote"),
        ("招待スピーカー", "./#guest_session"),
        ("セッション一覧", "./category/session/"),
        ("タイムテーブル", "./timetable/"),
    )),
    ("会場","./#access"),
    # ("スポンサー", "./sponsor/"),
    ("スタッフ", "./staff/"),
    ("行動規範", "./code-of-conduct/")
)

# カテゴリ名称のslugを置き換えする
CATEGORY_SLUG_EXCHANGE = {"session":"セッション", }

# キーノートスピーカーと招待セッションの情報

KEYNOTE_INFO = {
    "name":"からあげ",
    "theme":"""「ラズベリーパイの"パイ"とはなんのことだ」""",
    "description":"""からあげ氏は、ものづくり企業で20年近く働くかたわら、インターネットを使って情報発信を行っており、ブログサイト「karaage.」は特に有名です。その活動はインターネットのみならず、複数の書籍やメディアでの執筆やMakerとしても活躍し、2019年にAI x 愛知の勉強会「AIchi勉強会」を主催者として開催しています。""",
    "twittername":"karaage0703",
    "siteurl":"https://karaage.hatenadiary.jp/",
    "iconfilepath":"./front_img/icon_karaage0703.png",
}

GUEST_SESSION_INFO = {
    "name":"静岡産業大学情報学部教授 佐野典秀",
    "theme":"「いま、なぜPythonなのか？」<br>〜AI研究者（Python初心者）の視点から〜",
    "description": """東工大大学院卒、博士（工学）。静岡産業大学情報学部教授、ICT研究機構長、総合研究所副所長を兼務。専門は、ロボティックス、意思決定論、AI、3DCG等""",
    "iconfilepath":"./front_img/icon_Prof-Sano.png",
}

# タイムテーブルの時間一覧とセッション番号の対応リスト

TIMETABLE_ROOMS = [
    {"name":"部屋全体", "len":10},
    {"name":"講義室B(左)", "len":5},
    {"name":"講義室A(右)", "len":5},
]

TIMETABLE_COLUMHEADER = ["講義室B(左)", "講義室A(右)"]

TIMETABLE_MAP = [
    {"time":"9:30〜9:50","sessions":[
        {"title":"受付", "room":"講義室B(左)"},
        {"title":None, "room":"講義室A(右)"}
        ]
    },
    {"time":"9:50〜10:00","sessions":[
        {"title":"オープニング","room":"部屋全体"}
        ]
    },
    {"time":"10:00〜10:45","sessions":[
        {"title":"キーノート","room":"部屋全体",
        "speaker_name":KEYNOTE_INFO["name"],
        "theme":KEYNOTE_INFO["theme"]}
        ]
    },
    {"time":"10:55〜11:40","sessions":[
        {"title":"招待セッション","room":"部屋全体",
        "speaker_name":GUEST_SESSION_INFO["name"],
        "theme":GUEST_SESSION_INFO["theme"]}
        ]
    },
    {"time":"12:00〜13:00","sessions":[
        {"title":"昼食","room":"部屋全体"}
        ]
    },
    # セッションはsession_number指定でセッション情報を呼び出す
    {"time":"13:15〜13:45","sessions":[
        {"session_number":"01","room":"講義室B(左)"},
        {"session_number":"07","room":"講義室A(右)"}
        ]
    },
    {"time":"13:55〜14:25","sessions":[
        {"session_number":"02","room":"講義室B(左)"},
        {"session_number":"16","room":"講義室A(右)"}
        ]
    },
    {"time":"14:35〜15:05","sessions":[
        {"session_number":"10","room":"講義室B(左)"},
        {"session_number":"13","room":"講義室A(右)"}
        ]
    },
    
    {"time":"15:05～15:25","sessions":[
        {"title":"おやつ休憩","room":"部屋全体"}
        ]
    },

    {"time":"15:25〜15:55","sessions":[
        {"session_number":"12","room":"講義室B(左)"},
        {"session_number":"03","room":"講義室A(右)"}
        ]
    },
    {"time":"16:05〜16:35","sessions":[
        {"session_number":"04","room":"講義室B(左)"},
        {"session_number":"11","room":"講義室A(右)"}
        ]
    },
    {"time":"16:45〜17:15","sessions":[
        {"session_number":"06","room":"講義室B(左)"},
        {"session_number":"17","room":"講義室A(右)"}
        ]
    },
    
    # 終盤
    {"time":"17:30〜17:50","sessions":[
        {"title":"LT大会","room":"講義室B(左)"},{"title":"懇親会準備","room":"講義室A(右)"}
        ]
    },
    {"time":"17:50〜18:00","sessions":[
        {"title":"クロージング","room":"講義室B(左)"}, {"title":"懇親会準備","room":"講義室A(右)"}
        ]
    },
    {"time":"18:00〜19:30","sessions":[
        {"title":"懇親会 + LT大会","room":"部屋全体"}
        ]
    },

]

# スポンサー

SPONSORS = [
    {"corpname":"スポンサー名ABC", "siteurl":"/#page-top", 
    "logo_path":"front_img/proto_sponsor_logo.png",
    "description":"""スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。""",
    },
    {"corpname":"スポンサー名ABC", "siteurl":"/#page-top", 
    "logo_path":"front_img/proto_sponsor_logo.png",
    "description":"""スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。""",
    },
    {"corpname":"スポンサー名ABC", "siteurl":"/#page-top", 
    "logo_path":"front_img/proto_sponsor_logo.png",
    "description":"""スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。スポンサーの紹介文です。""",
    },
]

# パトロン

PATRONS = [
    {"name":"Patron Name", "twittername":"a", "siteurl":"/#page-top", 
    "logo_path":"front_img/proto_sponsor_logo.png"},
    {"name":"Patron Name", "siteurl":"/#page-top", 
    "logo_path":"front_img/proto_sponsor_logo.png"},
    {"name":"Patron Name", "twittername":"a",  
    "logo_path":"front_img/proto_sponsor_logo.png"},
]

# スタッフ一覧
STAFF_INFOS = [
    {"name":"b7craft"},
    {"name":"Chuui","twittername":"es_chuui"},
    {"name":"Hikaru",},
    {"name":"hrsano645","twittername":"hrs_sano645", "siteurl":"hr-sano.net"},
    {"name":"th.aoyagi.dg7"},
    {"name":"yoshi-corleone","twittername":"yoshi_corleone"},
    {"name":"やな","twittername":"chihiro_yy"},
    # {"name":"**","twittername":"**", "siteurl":"**"},
]