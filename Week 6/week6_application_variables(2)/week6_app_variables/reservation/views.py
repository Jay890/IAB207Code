from flask import Blueprint,render_template
from .models import Hotel

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='In dynamic use of content'
    hotels123 = get_hotel_list()
    return render_template('index_list.html', tag_line=tag_line, hotelsTest=hotels123)


def get_hotel_list():
    brisbane_hotel = Hotel('Brisbane', '01.jpg',
    'As the capital of the Sunshine State, we are blessed with idyllic subtropical weather all year round.')

    sydney_hotel = Hotel('Sydney', 'sydney.jpg',
    'From splendid Sydney Harbour, idyllic beaches and great national parks, to the marvellous creativity of the Sydney Opera House, dazzling entertainment and fascinating heritage, discover all the things to do and see throughout the year.')

    melbourne_hotel = Hotel('Melbourne', 'melbourne.jpg',
     'A packed agenda of food, wine, sports and arts is your introduction to the best of Melbourne – from its creative, exciting city centre, to its buzzing neighbourhood hubs.')

    hlist = list()
    hlist.append(brisbane_hotel)
    hlist.append(sydney_hotel)
    hlist.append(melbourne_hotel)
    hlist.append(brisbane_hotel)
    hlist.append(sydney_hotel)
    hlist.append(melbourne_hotel)
        
    return hlist