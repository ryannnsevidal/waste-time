#!/usr/bin/env python3

# ai powered engine that figures out what scammers are saying 
# and picks the best way to waste their time

import random
import re
import csv
import os
import datetime
from massive_responses import *
from gift_card_numbers import *

# import app tracking functions if available
try:
    from app import start_call_tracking, active_calls
    APP_INTEGRATION = True
except ImportError:
    APP_INTEGRATION = False

class ScammerAnalyzer:
    # looks at scammer messages and figures out what type of scam theyre running
    
    def __init__(self):
        # words that make scammers sound urgent (higher number = more urgent)
        self.urgency_keywords = {
            'immediately': 5, 'urgent': 4, 'now': 4, 'right now': 5,
            'asap': 4, 'quickly': 3, 'fast': 3, 'hurry': 4,
            'emergency': 5, 'critical': 4, 'final notice': 5,
            'last chance': 5, 'expire': 3, 'deadline': 4,
            'minutes': 4, 'seconds': 5, 'hours': 3, 'time': 2
        }
        
        # words scammers use to sound official (higher = more suspicious)
        self.authority_keywords = {
            'police': 5, 'fbi': 5, 'irs': 4, 'government': 4,
            'microsoft': 3, 'apple': 3, 'bank': 4, 'security': 3,
            'agent': 4, 'officer': 4, 'department': 3, 'official': 4,
            'federal': 5, 'arrest': 5, 'warrant': 5, 'legal': 4,
            'court': 4, 'judge': 4, 'attorney': 4, 'lawyer': 4
        }
        
        # payment stuff scammers ask for (higher = more sketchy)
        self.payment_keywords = {
            'gift card': 5, 'itunes': 4, 'google play': 4, 'amazon': 3,
            'target': 4, 'walmart': 4, 'steam': 4, 'visa': 3,
            'prepaid': 4, 'wire transfer': 5, 'bitcoin': 5, 'crypto': 5,
            'western union': 5, 'moneygram': 5, 'cash': 2, 'money': 2,
            'pay': 2, 'payment': 3, 'purchase': 3, 'buy': 3
        }
        
        # personal info they try to steal (higher = more sensitive)
        self.info_keywords = {
            'social security': 5, 'ssn': 5, 'credit card': 5, 'bank account': 5,
            'password': 5, 'pin': 4, 'date of birth': 4, 'address': 3,
            'full name': 2, 'phone number': 2, 'email': 2, 'verification': 3,
            'confirm': 2, 'verify': 3, 'account number': 4, 'routing': 4
        }
        
        # when scammers get mad (positive numbers = more frustrated)
        self.frustration_keywords = {
            'stupid': 3, 'idiot': 3, 'damn': 2, 'hell': 2, 'shit': 3,
            'listen': 2, 'understand': 2, 'why': 2, 'what': 1,
            'sir': 1, 'madam': 1, 'please': -1  # saying please actually makes them less frustrated
        }
        
        # phrases that show theyre getting desperate
        self.escalation_keywords = {
            'final warning': 5, 'last time': 4, 'not listening': 3,
            'wasting time': 4, 'hanging up': 3, 'transfer': 2,
            'supervisor': 3, 'manager': 3, 'cooperate': 3
        }
    
    def analyze_scammer_input(self, text):
        # looks at what scammer said and figures out how suspicious/frustrated they are
        text_lower = text.lower()
        
        # check for different types of scammer keywords
        urgency_score = self._calculate_score(text_lower, self.urgency_keywords)
        authority_score = self._calculate_score(text_lower, self.authority_keywords)
        payment_score = self._calculate_score(text_lower, self.payment_keywords)
        info_score = self._calculate_score(text_lower, self.info_keywords)
        frustration_keywords_score = self._calculate_score(text_lower, self.frustration_keywords)
        escalation_score = self._calculate_score(text_lower, self.escalation_keywords)
        
        # count questions and commands
        question_count = text.count('?')
        command_patterns = len(re.findall(r'\b(go|buy|get|give|tell|read|say|do|download|click|type|enter)\b', text_lower))
        
        # look for signs theyre getting mad
        caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
        exclamation_count = text.count('!')
        all_caps_words = len([word for word in text.split() if word.isupper() and len(word) > 2])
        
        # calculate how frustrated they are based on multiple things
        frustration_level = (
            caps_ratio * 2 +                    # TYPING IN CAPS = mad
            (exclamation_count * 0.2) +         # lots of !!! = frustrated
            (frustration_keywords_score * 0.3) + # swearing and anger words
            (all_caps_words * 0.1) +            # WORDS IN ALL CAPS
            (escalation_score * 0.2)            # escalation phrases
        )
        
        # check if theyre making threats
        threat_score = 0
        threat_patterns = ['arrest', 'jail', 'police', 'warrant', 'legal action', 'lawsuit', 'court']
        for pattern in threat_patterns:
            if pattern in text_lower:
                threat_score += 2
        
        # add everything up to get total suspicion level
        total_suspicion = urgency_score + authority_score + payment_score + info_score + threat_score
        
        return {
            'urgency_score': urgency_score,
            'authority_score': authority_score,
            'payment_score': payment_score,
            'info_score': info_score,
            'frustration_score': frustration_keywords_score,
            'escalation_score': escalation_score,
            'threat_score': threat_score,
            'question_count': question_count,
            'command_count': command_patterns,
            'caps_ratio': caps_ratio,
            'exclamation_count': exclamation_count,
            'all_caps_words': all_caps_words,
            'frustration_level': frustration_level,
            'total_suspicion': total_suspicion,
            # these tell us when to trigger different response strategies
            'is_high_urgency': urgency_score >= 8,
            'is_authority_claim': authority_score >= 6,
            'is_payment_scam': payment_score >= 8,
            'is_info_phishing': info_score >= 8,
            'is_highly_frustrated': frustration_level >= 1.5,
            'is_escalating': escalation_score >= 5,
            'is_threatening': threat_score >= 4
        }
    
    def _calculate_score(self, text, keyword_dict):
        # adds up points for each keyword found in the text
        score = 0
        for keyword, weight in keyword_dict.items():
            if keyword in text:
                score += weight
        return score

class SophisticatedResponseEngine:
    # picks the best response to waste the most time based on what scammer said
    
    def __init__(self, caller_phone=None):
        self.analyzer = ScammerAnalyzer()
        self.conversation_history = []
        self.scammer_frustration_level = 0
        self.time_wasted = 0
        self.caller_phone = caller_phone
        self.call_id = None
        
        # csv logging setup
        self.csv_dir = "analytics_data"
        self.csv_file = f"{self.csv_dir}/scammer_analysis_{datetime.datetime.now().strftime('%Y%m%d')}.csv"
        self._setup_csv_logging()
        
        # start call tracking for dashboard if available
        if APP_INTEGRATION and caller_phone:
            import uuid
            self.call_id = str(uuid.uuid4())
            # detect scam type from first analysis
            scam_type = "Unknown"
            try:
                start_call_tracking(self.call_id, caller_phone, scam_type)
            except Exception as e:
                print(f"couldnt start call tracking: {e}")
        
        # different ways to waste scammer time (ranked by how effective they are)
        self.strategies = {
            'confusion': self._generate_confusion_response,
            'hold_music': self._generate_hold_response,
            'questions': self._generate_question_response,
            'tangent': self._generate_tangent_response,
            'technical_problems': self._generate_technical_problems,
            'physical_limitations': self._generate_physical_limitations,
            'authority_challenge': self._generate_authority_challenge,
            'payment_confusion': self._generate_payment_confusion,
            'maximum_time_waste': self._generate_maximum_time_waste
        }
    
    def generate_response(self, scammer_input):
        # figures out the best response to waste the most time
        
        # analyze what the scammer just said
        analysis = self.analyzer.analyze_scammer_input(scammer_input)
        
        # keep track of conversation and how frustrated they are
        self.conversation_history.append(scammer_input)
        self.scammer_frustration_level += analysis['frustration_level']
        
        # pick the best strategy to annoy them
        strategy = self._select_optimal_strategy(analysis)
        
        # generate the actual response
        response = self.strategies[strategy](analysis, scammer_input)
        
        # keep track of how much time were wasting
        self.time_wasted += self._estimate_time_waste(strategy, analysis)
        
        # log to csv for analytics
        result = {
            'response': response,
            'strategy': strategy,
            'analysis': analysis,
            'estimated_time_waste': self._estimate_time_waste(strategy, analysis),
            'total_time_wasted': self.time_wasted,
            'scammer_frustration': self.scammer_frustration_level
        }
        self._log_to_csv(scammer_input, result)
        
        return result
    
    def _select_optimal_strategy(self, analysis):
        # picks the best way to waste time based on what scammer said and how mad they are
        
        # if theyre really pissed off, go for maximum time waste
        if analysis['is_highly_frustrated'] or self.scammer_frustration_level > 3:
            return 'maximum_time_waste'
        
        # if theyre making serious threats, challenge their authority
        if analysis['is_threatening'] or analysis['threat_score'] >= 4:
            return 'authority_challenge'
        
        # if theyre getting desperate, use the most annoying tactics
        if analysis['is_escalating']:
            return random.choice(['hold_music', 'maximum_time_waste', 'physical_limitations'])
        
        # if they claim to be from government/microsoft/etc, call them out
        if analysis['is_authority_claim'] or analysis['authority_score'] >= 6:
            return 'authority_challenge'
        
        # if theyre being super urgent, be really slow and have problems
        if analysis['is_high_urgency'] or analysis['urgency_score'] >= 8:
            return random.choice(['physical_limitations', 'technical_problems', 'hold_music'])
        
        # if they want payment, confuse the hell out of the process
        if analysis['is_payment_scam'] or analysis['payment_score'] >= 8:
            return 'payment_confusion'
        
        # if they want personal info, ask them questions instead
        if analysis['is_info_phishing'] or analysis['info_score'] >= 8:
            return 'questions'
        
        # for medium urgency, use delays and confusion
        if analysis['urgency_score'] >= 4:
            return random.choice(['physical_limitations', 'technical_problems', 'confusion'])
        
        # for medium authority claims, lightly challenge or confuse
        if analysis['authority_score'] >= 3:
            return random.choice(['authority_challenge', 'questions', 'confusion'])
        
        # for payment requests, create confusion
        if analysis['payment_score'] >= 4:
            return 'payment_confusion'
        
        # for info requests, deflect with questions or stories
        if analysis['info_score'] >= 3:
            return random.choice(['questions', 'tangent'])
        
        # if they give lots of commands, act confused
        if analysis['command_count'] >= 3:
            return 'confusion'
        
        # if theyre yelling (caps/exclamations), pretend you cant hear
        if analysis['caps_ratio'] > 0.3 or analysis['exclamation_count'] >= 3:
            return 'technical_problems'  
        
        # default to mix of annoying strategies
        default_strategies = ['confusion', 'questions', 'tangent', 'technical_problems']
        return random.choice(default_strategies)
    
    def _generate_confusion_response(self, analysis, scammer_input):
        # act confused based on what they said
        if 'computer' in scammer_input.lower():
            return random.choice(TECH_SUPPORT_DEEP)
        elif any(word in scammer_input.lower() for word in ['gift card', 'target', 'walmart']):
            return random.choice(GIFT_CARD_RESPONSES)
        else:
            return get_contextual_response(scammer_input)
    
    def _generate_hold_response(self, analysis, scammer_input):
        # put them on hold with annoying music
        return random.choice(HOLD_MUSIC_RESPONSES)
    
    def _generate_question_response(self, analysis, scammer_input):
        # ask them questions to waste time
        return random.choice(COMBO_RESPONSES)
    
    def _generate_tangent_response(self, analysis, scammer_input):
        # go off on random stories
        return random.choice(COMBO_RESPONSES)
    
    def _generate_technical_problems(self, analysis, scammer_input):
        # pretend to have hearing/tech problems
        return random.choice(TECH_SUPPORT_DEEP)
    
    def _generate_physical_limitations(self, analysis, scammer_input):
        # act old and slow
        return random.choice(COMBO_RESPONSES)
    
    def _generate_authority_challenge(self, analysis, scammer_input):
        # question their authority
        return random.choice(IRS_AUTHORITY_DEEP)
    
    def _generate_payment_confusion(self, analysis, scammer_input):
        # confuse payment process
        if 'gift card' in scammer_input.lower():
            return random.choice(GIFT_CARD_RESPONSES)
        return random.choice(COMBO_RESPONSES)
    
    def _generate_maximum_time_waste(self, analysis, scammer_input):
        # use the most time wasting responses when theyre really mad
        return random.choice(HOLD_MUSIC_RESPONSES)
    
    def _estimate_time_waste(self, strategy, analysis):
        # estimates how much time each strategy wastes
        base_times = {
            'confusion': 30,
            'hold_music': 180,  # 3 minutes of hold music
            'questions': 60,
            'tangent': 90,
            'technical_problems': 120,
            'physical_limitations': 150,
            'authority_challenge': 90,
            'payment_confusion': 120,
            'maximum_time_waste': 300  # 5 minutes when theyre really mad
        }
        
        base_time = base_times.get(strategy, 60)
        
        # add extra time if theyre really frustrated (they stay on longer when mad)
        if analysis['frustration_level'] > 2:
            base_time *= 1.5
        elif analysis['frustration_level'] > 1:
            base_time *= 1.2
            
        return base_time
    
    def _setup_csv_logging(self):
        # creates analytics directory and csv file if they dont exist
        if not os.path.exists(self.csv_dir):
            os.makedirs(self.csv_dir)
        
        # create csv file with headers if it doesnt exist
        if not os.path.exists(self.csv_file):
            headers = [
                'timestamp', 'scammer_input', 'strategy', 'response_preview',
                'urgency_score', 'authority_score', 'payment_score', 'info_score',
                'frustration_score', 'threat_score', 'caps_ratio', 'exclamation_count',
                'estimated_time_waste', 'total_time_wasted', 'scammer_frustration',
                'is_high_urgency', 'is_authority_claim', 'is_payment_scam',
                'is_info_phishing', 'is_threatening'
            ]
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
    
    def _log_to_csv(self, scammer_input, result):
        # logs conversation data to csv for analytics
        try:
            timestamp = datetime.datetime.now().isoformat()
            analysis = result['analysis']
            
            # truncate response for preview
            response_preview = result['response'][:100] + "..." if len(result['response']) > 100 else result['response']
            
            row = [
                timestamp,
                scammer_input[:200],  # truncate long inputs
                result['strategy'],
                response_preview,
                analysis['urgency_score'],
                analysis['authority_score'],
                analysis['payment_score'],
                analysis['info_score'],
                analysis['frustration_score'],
                analysis['threat_score'],
                round(analysis['caps_ratio'], 3),
                analysis['exclamation_count'],
                result['estimated_time_waste'],
                result['total_time_wasted'],
                round(result['scammer_frustration'], 3),
                analysis['is_high_urgency'],
                analysis['is_authority_claim'],
                analysis['is_payment_scam'],
                analysis['is_info_phishing'],
                analysis['is_threatening']
            ]
            
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        except Exception as e:
            # dont crash if csv logging fails
            print(f"csv logging error: {e}")

# main engine instance
response_engine = SophisticatedResponseEngine()

def get_sophisticated_response(scammer_input):
    # main function to get ai response
    return response_engine.generate_response(scammer_input)
