# ai engine guide

comprehensive guide to understanding and customizing the sophisticated ai engine

## engine overview

the sophisticated ai engine (`sophisticated_engine.py`) is the brain of the waste time bot. it analyzes scammer messages and dynamically selects optimal responses to maximize time waste and frustration.

### core components

1. **ScammerAnalyzer** - analyzes incoming scammer messages
2. **SophisticatedResponseEngine** - generates appropriate responses
3. **CSV Logging** - automatically tracks all interactions
4. **Strategy Selection** - picks best time-wasting approach

## scammer analysis system

### keyword scoring

the analyzer uses weighted keyword dictionaries to score different aspects:

```python
# urgency detection
urgency_keywords = {
    'immediately': 5, 'urgent': 4, 'now': 4, 'right now': 5,
    'asap': 4, 'quickly': 3, 'fast': 3, 'hurry': 4,
    'emergency': 5, 'critical': 4, 'final notice': 5
}

# authority claims
authority_keywords = {
    'police': 5, 'fbi': 5, 'irs': 4, 'government': 4,
    'microsoft': 3, 'apple': 3, 'bank': 4, 'security': 3
}

# payment requests
payment_keywords = {
    'gift card': 5, 'itunes': 4, 'google play': 4,
    'wire transfer': 5, 'bitcoin': 5, 'crypto': 5
}
```

### analysis metrics

for each scammer message, the engine calculates:

| metric | description | range |
|--------|-------------|-------|
| `urgency_score` | how urgent/desperate they sound | 0-20+ |
| `authority_score` | claims of official authority | 0-20+ |
| `payment_score` | payment/money requests | 0-20+ |
| `info_score` | personal information requests | 0-15+ |
| `frustration_score` | anger/frustration level | 0-15+ |
| `threat_score` | legal threats and intimidation | 0-10+ |
| `caps_ratio` | percentage of CAPS text | 0.0-1.0 |
| `exclamation_count` | number of ! marks | 0-n |
| `frustration_level` | composite frustration score | 0.0-5.0+ |

### boolean flags

the analyzer sets boolean flags for easy decision making:

```python
'is_high_urgency': urgency_score >= 8,
'is_authority_claim': authority_score >= 6,
'is_payment_scam': payment_score >= 8,
'is_info_phishing': info_score >= 8,
'is_highly_frustrated': frustration_level >= 1.5,
'is_escalating': escalation_score >= 5,
'is_threatening': threat_score >= 4
```

## strategy selection logic

### strategy hierarchy

the engine uses a sophisticated decision tree to pick the best response strategy:

```python
def _select_optimal_strategy(self, analysis):
    # priority order (higher priority first)
    
    # 1. maximum annoyance for highly frustrated scammers
    if analysis['is_highly_frustrated'] or self.scammer_frustration_level > 3:
        return 'maximum_time_waste'
    
    # 2. challenge authority claims
    if analysis['is_threatening'] or analysis['threat_score'] >= 4:
        return 'authority_challenge'
    
    # 3. escalation tactics for desperate scammers
    if analysis['is_escalating']:
        return random.choice(['hold_music', 'maximum_time_waste', 'physical_limitations'])
    
    # 4. slow down urgent scammers
    if analysis['is_high_urgency'] or analysis['urgency_score'] >= 8:
        return random.choice(['physical_limitations', 'technical_problems', 'hold_music'])
    
    # 5. confuse payment scams
    if analysis['is_payment_scam'] or analysis['payment_score'] >= 8:
        return 'payment_confusion'
    
    # ... continues with more specific conditions
```

### available strategies

| strategy | purpose | effectiveness | time waste |
|----------|---------|---------------|------------|
| `maximum_time_waste` | most annoying for angry scammers | very high | 300s |
| `hold_music` | put them on hold with music | high | 180s |
| `physical_limitations` | act old and slow | high | 150s |
| `payment_confusion` | confuse payment process | medium-high | 120s |
| `technical_problems` | pretend hearing/tech issues | medium-high | 120s |
| `authority_challenge` | question their authority | medium | 90s |
| `tangent` | go off on random stories | medium | 90s |
| `questions` | ask them questions | medium | 60s |
| `confusion` | act confused | low-medium | 30s |

## customizing the ai engine

### adding new keywords

```python
# add to existing keyword dictionaries
self.urgency_keywords.update({
    'rush': 3,
    'deadline': 4,
    'expires': 3
})

# create new keyword category
self.crypto_keywords = {
    'bitcoin': 5,
    'ethereum': 4,
    'wallet': 4,
    'blockchain': 3
}
```

### creating new strategies

```python
# 1. add strategy to __init__
self.strategies['new_strategy'] = self._generate_new_strategy_response

# 2. implement the strategy method
def _generate_new_strategy_response(self, analysis, scammer_input):
    # custom logic for new strategy
    if 'bitcoin' in scammer_input.lower():
        return "what's a bitcoin? is that like a chuck e cheese token?"
    return random.choice(SOME_RESPONSE_LIST)

# 3. add to strategy selection logic
if analysis['crypto_score'] >= 5:
    return 'new_strategy'

# 4. add time estimate
base_times['new_strategy'] = 90  # seconds
```

### adjusting thresholds

```python
# modify boolean flag thresholds
'is_high_urgency': urgency_score >= 6,  # lowered from 8
'is_payment_scam': payment_score >= 6,  # lowered from 8

# adjust strategy selection thresholds
if analysis['urgency_score'] >= 3:  # lowered from 4
    return random.choice(['physical_limitations', 'technical_problems'])
```

## response generation

### contextual responses

the engine selects responses based on scammer input context:

```python
def _generate_confusion_response(self, analysis, scammer_input):
    if 'computer' in scammer_input.lower():
        return random.choice(TECH_SUPPORT_DEEP)
    elif any(word in scammer_input.lower() for word in ['gift card', 'target', 'walmart']):
        return random.choice(GIFT_CARD_RESPONSES)
    else:
        return get_contextual_response(scammer_input)
```

### response databases

responses are stored in `massive_responses.py`:

```python
# tech support responses
TECH_SUPPORT_DEEP = [
    "hold on, let me unplug my computer... *sounds of struggle* ok it's unplugged. now what?",
    "my computer is the black rectangle thing, right? or is that the tv?",
    "i tried downloading more ram but my cup holder broke"
]

# gift card confusion
GIFT_CARD_RESPONSES = [
    "gift cards? like for birthdays? how much gift can fit on such a small card?",
    "do i need to wrap the gift card? i have nice wrapping paper with little flowers",
    "can i use my library card instead? it has my picture on it"
]
```

## advanced features

### conversation memory

the engine tracks conversation state:

```python
self.conversation_history = []  # stores all inputs
self.scammer_frustration_level = 0  # cumulative frustration
self.time_wasted = 0  # total time wasted
```

### dynamic adaptation

responses adapt based on conversation history:

```python
# frustration builds over time
self.scammer_frustration_level += analysis['frustration_level']

# longer conversations get more aggressive strategies
if len(self.conversation_history) > 5:
    strategy_preference = 'maximum_time_waste'
```

### effectiveness tracking

each strategy tracks its effectiveness:

```python
def _estimate_time_waste(self, strategy, analysis):
    base_time = base_times.get(strategy, 60)
    
    # bonus time for frustrated scammers (they stay longer)
    if analysis['frustration_level'] > 2:
        base_time *= 1.5
    elif analysis['frustration_level'] > 1:
        base_time *= 1.2
        
    return base_time
```

## testing and debugging

### debug mode

```python
# enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# test with debug output
from sophisticated_engine import get_sophisticated_response

result = get_sophisticated_response("test message")
print(f"analysis: {result['analysis']}")
print(f"strategy reasoning: {result['strategy']}")
```

### custom test scenarios

```python
def test_engine_behavior():
    from sophisticated_engine import SophisticatedResponseEngine
    
    engine = SophisticatedResponseEngine()
    
    # test escalation
    messages = [
        "hello this is microsoft",
        "your computer has virus",
        "you need to download our software now",
        "WHY AREN'T YOU LISTENING TO ME!",
        "I WILL TRANSFER YOU TO MY SUPERVISOR!"
    ]
    
    for msg in messages:
        result = engine.generate_response(msg)
        print(f"input: {msg}")
        print(f"strategy: {result['strategy']}")
        print(f"frustration: {result['scammer_frustration']:.2f}")
        print(f"time waste: {result['estimated_time_waste']}s")
        print("---")

test_engine_behavior()
```

### performance monitoring

```python
import time
from sophisticated_engine import get_sophisticated_response

def benchmark_engine():
    start_time = time.time()
    
    for i in range(100):
        result = get_sophisticated_response(f"test message {i}")
    
    end_time = time.time()
    avg_time = (end_time - start_time) / 100
    
    print(f"average response time: {avg_time*1000:.2f}ms")
    print(f"responses per second: {1/avg_time:.1f}")

benchmark_engine()
```

## advanced customization examples

### regional scam detection

```python
# add region-specific scam patterns
self.region_keywords = {
    'usa': {
        'irs': 5, 'social security': 5, 'medicare': 4,
        'police department': 4, 'sheriff': 4
    },
    'uk': {
        'hmrc': 5, 'nhs': 4, 'council tax': 4,
        'tv licence': 3, 'dvla': 3
    },
    'australia': {
        'ato': 5, 'centrelink': 4, 'medicare': 4,
        'afp': 4  # australian federal police
    }
}

def detect_region_specific_scam(self, text):
    for region, keywords in self.region_keywords.items():
        score = self._calculate_score(text.lower(), keywords)
        if score >= 5:
            return region
    return 'generic'
```

### machine learning integration

```python
# add ml-based sentiment analysis
def analyze_sentiment_ml(self, text):
    from textblob import TextBlob
    
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # -1 to 1
    
    # convert to scammer frustration indicator
    if sentiment_score < -0.3:
        return 'highly_negative'  # angry scammer
    elif sentiment_score < -0.1:
        return 'negative'  # frustrated
    else:
        return 'neutral'  # calm/professional
```

### adaptive learning

```python
# track strategy success rates
self.strategy_success = defaultdict(list)

def record_strategy_outcome(self, strategy, success_score):
    self.strategy_success[strategy].append(success_score)
    
def get_best_strategies(self):
    best_strategies = {}
    for strategy, scores in self.strategy_success.items():
        if scores:
            avg_score = sum(scores) / len(scores)
            best_strategies[strategy] = avg_score
    
    return sorted(best_strategies.items(), key=lambda x: x[1], reverse=True)
```

this guide provides everything needed to understand, customize, and extend the ai engine. the modular design makes it easy to add new detection patterns, response strategies, and optimization techniques.
