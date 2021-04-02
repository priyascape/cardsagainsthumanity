
# Create your views here.
from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import *
from .models import WhiteCard
from .models import BlackCard
import json
import random
import time

# ----------------------------------------------------------------------------
# Route to index - get all WhiteCard BlackCard
# ----------------------------------------------------------------------------

def index(request):
    context = {
        'whitecards' : WhiteCard.objects.all(),
        'blackcards' : BlackCard.objects.all()
        }
    return render(request,'index.html', context)

# ----------------------------------------------------------------------------
# Route to example - show the vision
# ----------------------------------------------------------------------------
def example(request):
        return render(request,'example.html')
    
# ----------------------------------------------------------------------------
# Route to start game, create player and render
# ----------------------------------------------------------------------------

def start(request):
    if request.method == 'POST':
        num_of_players = int(request.POST['form_select'])
        counter = 0
        num = 1
        for i in range(num_of_players):
            if counter == 0:
                number_of_players = Player.objects.create(name=request.POST['name'],
                    is_human=True)
                counter += 1
            else:
                number_of_players = Player.objects.create(name=f"computer {num}",is_human=False)
                num += 1
        return redirect ('/question')
    else:
        return render(request, "start.html")

# ----------------------------------------------------------------------------
# Route to loading JSon strings
# ----------------------------------------------------------------------------


def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj

json_str = json.dumps(set([1,2,3]), default=serialize_sets)
print(json_str)

def load_json_into_db(request):
    with open('/Users/richardconstellation/Desktop/codingdojo/python_stack/django/django_fullstack/cards-against-humanity-api/data/official/packs/main_deck.json') as f:
        main_deck_as_dict = json.load(f)
    # for answer in main_deck_as_dict['white']:
    #     WhiteCard.objects.create(answer=answer)
    # for question in main_deck_as_dict['black']:
    #     BlackCard.objects.create(question=question)
    # return redirect('/')
    for i in range (len(main_deck_as_dict['black'])):
        BlackCard.objects.create(question=main_deck_as_dict['black'][i]["content"])

    return redirect('/')

#Black.objects.get(id = blc.id)
# def player(request.session):
#     context ={ hand[array]
        
#     }
# ----------------------------------------------------------------------------
# Route to randomly select question
# ----------------------------------------------------------------------------                 

def question(request):
    whiteCardList = WhiteCard.objects.all()
    whiteCardArr = []
    #for x in range(len(whiteCardList)):
        #WhiteCard.objects.create(answer= whiteCardList[x])
 
    for j in range(10):
        whiteCardArr.append(whiteCardList[random.randint(0, len(whiteCardList))])

    blClist = BlackCard.objects.all()
    blcard = blClist[random.randint(0, len(blClist))]
    request.session['blcard'] = blcard.question
    print(blcard.question)
    context = {
        'whiteCardArr': whiteCardArr
    }
    
    return render(request,'question.html', context)

# ----------------------------------------------------------------------------
# Route to draw a card (10)
# ----------------------------------------------------------------------------

def choose_card(request):
    return render(request,'choose_card.html')
# ----------------------------------------------------------------------------
# Route to render result
# ----------------------------------------------------------------------------
def result(request):
    return render(request,'result.html')

# ---
#  hit start game
#  create a function to create the player
# import random
# #  def rendering_template(request):
#     arr = ["pic1","pic2", "pic3"]
#     context={
#         "selected_pic": random.randint(0, 2)
#     }
    
    # import JSon
    # Read the Json file
    # put the contenst of the file into 1 variable - set as Json , set into the variable I define
    #  eg for whitecard in whitecards 
    # WhiteCard.objects.create(answer=whitecard ["white"])
    
# ----------------------------------------------------------------------------
# Route to reset flush
# ----------------------------------------------------------------------------
     
def reset(request):
    request.session.flush()
    return redirect('/')
    
    
