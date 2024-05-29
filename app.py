from flask import Flask, render_template, request, abort
from picport import picport

app = Flask(__name__)
picport = picport()

ALLOWED_HOSTS = ['mwfbiz.com', 'mastrowall.in', 'amrit-corp.com','onrender.com']
DISALLOWED_WORDS = [
    'adult', 'xxx', 'sex', 'nude', 'fuck', 'porn', 'porno', 'pornography',
    'sexual', 'erotic', 'naked', 'nudes', 'fucking', 'blowjob', 'handjob', 'anal',
    'orgy', 'strip', 'striptease', 'ass', 'boobs', 'tits', 'pussy', 'vagina', 'dick',
    'penis', 'whore', 'slut', 'bitch', 'cock', 'cum', 'ejaculation', 'sperm', 'lesbian', 'gay',
    'homosexual', 'bisexual', 'transsexual', 'transgender', 'prostitute', 'escort', 'dominatrix',
    'bdsm', 'bondage', 'fetish', 'masturbate', 'masturbation', 'orgasm', 'clitoris', 'genitals',
    'aroused', 'arousal', 'penetration', 'rape', 'incest', 'molest', 'paedophile', 'paedophilia',
    'hentai', 'incesto', 'bestiality', 'bestial', 'zoophilia', 'zoophile', 'cumshot',
    'hardcore', 'softcore', 'voyeur', 'voyeurism', 'submissive', 'dominant', 'sub', 'dom',
    'bareback', 'smut', 'carnal', 'fellation', 'sodomie', 'débauche', 'putain', 'pute', 'putes',
    'teufel', 'ficken', 'schwanz', 'hure', 'vergewaltigung', 'brüste', 'vulva', 'scheide',
    'coito', 'copulare', 'escort', 'scopare', 'tette', 'fica', 'pene', 'vagina', 'peitos',
    'bunda', 'buceta', 'penis', 'prostituta', 'safada', 'transa', 'sexo', 'putaria', 'erotico',
    'сачок', 'секс', 'порно', 'сиськи', 'член', 'хуи', 'ебать', 'ебля', 'трахать', 'трах', 'сперм',
    'гей', 'лесбиянка', 'гомосексуал', 'педофил', 'педофилия', 'инцест', 'насилие', 'насиловать',
    '强奸', '性交', '色情', '裸体', '成人', '黄色', '性虐', '淫秽', '强暴', '卖淫', '嫖娼'
]

def check_host():
    host = request.host.split(':')[0]
    if host not in ALLOWED_HOSTS:
        abort(502)

def check_query(query):
    for word in DISALLOWED_WORDS:
        if word in query.lower():
            return False
    return True

@app.route('/')
def index():
    check_host()
    return render_template('index.html')

@app.route('/search')
def search():
    check_host()
    query = request.args.get('query', 'hd wallpaper')
    if not check_query(query):
        error_message = "🚫 The search query contains disallowed words or phrases. 🚫"
        return render_template('index.html', error=error_message)
    images = picport.search_google_images(query)
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
