import random

facts = ['Sri Lanka has a sole Test win against the Aussies till date.', 'Sanath Jayasuriya has more ODI wickets than Shane Warne.', "Dhaka's Sher-e-Bangla stadium and Bangabandhu stadium have hosted more ODIs than Lord's.", "The highest number of runs scored in an over is not 36. It's 77.", 'Adam Gilchrist holds the record for playing the most number of Tests straight after debut.', 'Ishant Sharma is responsible for all the three highest scores made by a batsman against India in the 21st century.', 'On 12th January 1964, Indian spinner Bapu Nadkarni bowled 21 consecutive maiden overs vs England at Chennai.', 'Chris Martin and B.S Chandrasekhar have taken more Test wickets in their career than the test runs they scored.', 'Wilfred Rhodes took 4,204 wickets in First Class cricket.', ' Sir Jack Hobbs scored 199 centuries in his First Class career.', ' In a World Cup Match, chasing 335, Sunil Gavaskar scored an unbeaten 36 off 174 balls.', ' Jim Laker once took19 wickets in a Test match.', ' Saurav Ganguly is the only Indian player to score a century in the knock out stages of a World Cup.', " After Virat Kohli's debut, India has chased down 300+ targets five times.", ' Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.', ' The player with the most number of not outs in Test cricket is not Rahul Dravid, but Courtney Walsh.', ' Saurav Ganguly is the only player to win four consecutive Man of the Match awards in ODIs.', ' Dirk Nannes has represented both Australia and Netherlands in International Cricket.', ' Shahid Afridi used a bat borrowed from Waqar Younis to score the fastest century in a ODI match.', " In 1989, along with Sachin Tendulkar, 23 other cricketers made their International debuts. The last one to retire before Sachin, was New Zealand's Chris Cairns, who retired in 2004.", ' Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.', ' Sir Don Bradman has just hit 6 sixes in his entire career.', " Virender Sehwag's highest scores in T20, ODI and Tests are 119, 219 and 319 respectively.", " Wasim Akram's highest Test innings score of 257 is higher than that of Sachin Tendulkar's (who has 248 n.o. to his credit).", ' The England Cricket Team is the only team in ODI history to lose a 60 over ODI Final (1979 World Cup), a 50 over ODI Final (1992 World Cup and 2004 Champions Trophy) and a 20 over ODI Final (2013 Champions Trophy) in ICC tournaments.', ' Lance Klusener, Abdur Razzaq, Shoaib Malik and Hashan Tillakaratne are the only players to have batted in 10 different batting positions in ODIs.', ' MS Dhoni and Suresh Raina have never scored an ODI ton outside of Asia.', ' Graeme Smith is the only player in the history of cricket to have captained a team for more than 100 Test matches.', ' Sachin Tendulkar got out for a duck only once in his Ranji career. Bhuvaneshwar Kumar got him.', ' Saeed Ajmal has never won a Man of the Match award in One Day International Cricket.', " Shahid Afridi used Sachin Tendulkar's bat to hit the fastest ever ODI century.", ' Chris Gayle is the only batsman to hit a six off the first ball of a Test match. ', " Vinod Kambli's Test match average is better than his childhood friend Sachin Tendulkar. ",' Sunil Gavaskar was out off the first ball of a Test match thrice in his career. ', ' ML Jaisimha and Ravi Shastri are the only Indians to bat on all five days of a Test. ', " The only cricketer to play Test cricket for India and England is Saif Ali Khan's grandfather, Iftikhar Ali Khan Pataudi. ", ' Lala Amarnath is the only bowler to dismiss Don Bradman hit wicket in Test cricket. ', " There's an uncanny similarity between the Indo-Pak match at the Australasia Cup of 1986 and Asia Cup 2014, India won their second World Cup 28 years later in 2011 and remarkably won their second ever Test at Lord's three years later in 2014. ", ' India is the only country to win the 60-Over, 50-Over and 20-Over World Cup. ', ' Alec Stewart was born on 8-4-63 and he scored 8463Test runs. ', ' Asif Karim of Kenya has played International cricket and Davis Cup (Tennis) for his country. ', ' Wilfred Rhodes of England played Test cricket till he was 52. ', ' Allan Border played 153 consecutive Test matches.  ', ' Australia beat England by 45 runs in the first ever cricket Test as well as the Centenary Test in 1977. ', ' All four innings of a test on the same day. ', " There's only one person who witnessed Jim Laker and Anil Kumble taking 10 wickets in an innings. ", ' On the morning of 11/11/11 South Africa needed 111 runs to win at 11:11. ', " India's Mohinder Amarnath is the only cricketer to be dismissed for handling the ball and obstructing the field."]

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Cricket Facts. " \
                    "Various interesting and mind blowing facts about Cricket for you.  " \
                    "Say, tell me a fact about Cricket or just say fact."
                    
    reprompt_text = "If you want to hear another fact, say " \
                    "Fact! Now you try!" 
                    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    
    card_title = "Session Ended"
    speech_output = "Have a nice day! " \
                    "Come back for more facts! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))
		
		
def get_fact(intent, session):
    
    card_title = "Facts"
    should_end_session = False

    index = random.randint(0, len(facts))
    speech_output = "Did you know that " + facts[index]
    reprompt_text = "For another fact, just say fact!"
    session_attributes = {"fact": facts[index]}
    should_end_session = True
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    session_attributes = {}

def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    
    if intent_name == "TellFactIntent":
        return get_fact(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
        
def on_session_ended(session_ended_request, session):
    session_attributes = {}

# --------------- Main handler ------------------

session_attributes = {}

def lambda_handler(event, context):
    
    if event['session']['new']:
	    on_session_started({'requestId': event['request']['requestId']},event['session'])
		
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
