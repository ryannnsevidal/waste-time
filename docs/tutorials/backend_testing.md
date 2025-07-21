# backend testing guide

comprehensive guide for testing the waste time bot backend and ai engine

## quick start testing

### 1. basic flask api testing
test that the web server is running correctly:

```bash
# start the app (if not already running)
python app.py

# test main endpoint
curl http://localhost:5000/

# expected output:
# <h1>waste time bot</h1>
# <p>bot is running and ready to waste scammer time</p>
```

### 2. docker testing
test the containerized version:

```bash
# build and run with docker
docker-compose up --build

# test docker endpoint (note port 5001)
curl http://localhost:5001/

# should show same output as above
```

## ai engine testing

### 3. testing the sophisticated engine directly

create a test file or run directly in python:

```python
from sophisticated_engine import get_sophisticated_response, ScammerAnalyzer

# test scammer analysis
analyzer = ScammerAnalyzer()
analysis = analyzer.analyze_scammer_input("You need to buy gift cards NOW!")

print("scammer analysis:")
print(f"  urgency score: {analysis['urgency_score']}")
print(f"  payment score: {analysis['payment_score']}")
print(f"  threat score: {analysis['threat_score']}")
print(f"  is payment scam: {analysis['is_payment_scam']}")

# test full response generation
result = get_sophisticated_response("This is Microsoft tech support calling about your computer virus")

print("\nai response:")
print(f"  strategy chosen: {result['strategy']}")
print(f"  estimated time waste: {result['estimated_time_waste']} seconds")
print(f"  scammer frustration: {result['scammer_frustration']}")
print(f"  response: {result['response'][:100]}...")
```

### 4. batch testing multiple scenarios

```python
from sophisticated_engine import get_sophisticated_response

# test different scammer types
test_cases = [
    {
        'input': 'You need to buy gift cards immediately!',
        'expected_strategy': 'payment_confusion',
        'scam_type': 'gift_card'
    },
    {
        'input': 'This is the IRS, you owe taxes or police will arrest you',
        'expected_strategy': 'authority_challenge', 
        'scam_type': 'irs_threat'
    },
    {
        'input': 'Your computer has viruses, download this software now',
        'expected_strategy': 'technical_problems',
        'scam_type': 'tech_support'
    },
    {
        'input': 'Give me your social security number for verification',
        'expected_strategy': 'questions',
        'scam_type': 'info_phishing'
    }
]

print("batch testing ai responses")
print("="*50)

for i, test in enumerate(test_cases, 1):
    print(f"\ntest {i}: {test['scam_type']}")
    print(f"input: {test['input']}")
    
    result = get_sophisticated_response(test['input'])
    
    print(f"strategy: {result['strategy']}")
    print(f"expected: {test['expected_strategy']}")
    print(f"match: {'PASS' if result['strategy'] == test['expected_strategy'] else 'FAIL'}")
    print(f"time waste: {result['estimated_time_waste']}s")
    print(f"response preview: {result['response'][:80]}...")
```

## advanced testing with analytics

### 5. using the sophisticated demo suite

```bash
# run the full testing suite
python sophisticated_demo.py

# this provides interactive menu:
# 1. Advanced Scammer Profiling
# 2. ML Strategy Optimization  
# 3. Real-time Conversation Analyzer
# 4. Full Analytics Suite
# 5. Exit
```

### 6. programmatic analytics testing

```python
from sophisticated_demo import AdvancedAnalytics
from sophisticated_engine import get_sophisticated_response

# create analytics tracker
analytics = AdvancedAnalytics()

# run multiple tests
test_inputs = [
    "URGENT! Buy $500 gift cards now!",
    "This is Microsoft support, your computer is infected",
    "IRS final notice, pay now or face arrest",
    "Please verify your bank account information",
    "You won $1 million, just pay processing fees"
]

print("running analytics test suite...")

for input_text in test_inputs:
    result = get_sophisticated_response(input_text)
    analytics.record_test(input_text, result)
    print(f"processed: {input_text[:40]}... -> {result['strategy']}")

# generate comprehensive report
report = analytics.generate_report()
print("\n" + report)

# export data to csv
csv_file = analytics.export_to_csv()
print(f"\ndata exported to: {csv_file}")
```

## csv data analysis

### 7. viewing csv data

```bash
# check what csv files exist
ls -la analytics_data/

# view csv headers and first few rows
head -3 analytics_data/scammer_analysis_20250720.csv

# count total responses by strategy
cut -d, -f3 analytics_data/scammer_analysis_20250720.csv | sort | uniq -c

# view high urgency scams
grep "True.*True" analytics_data/scammer_analysis_20250720.csv
```

### 8. analyzing effectiveness

```python
import pandas as pd

# load csv data for analysis
df = pd.read_csv('analytics_data/scammer_analysis_20250720.csv')

# strategy effectiveness analysis
strategy_stats = df.groupby('strategy').agg({
    'estimated_time_waste': ['mean', 'sum', 'count'],
    'scammer_frustration': 'mean',
    'urgency_score': 'mean'
}).round(2)

print("strategy effectiveness:")
print(strategy_stats)

# scam type detection accuracy
scam_detection = df[['is_payment_scam', 'is_authority_claim', 'is_info_phishing', 'is_threatening']].sum()
print("\nscam detection counts:")
print(scam_detection)

# time waste distribution
print(f"\ntotal time wasted: {df['estimated_time_waste'].sum()} seconds")
print(f"average per call: {df['estimated_time_waste'].mean():.1f} seconds")
print(f"most effective strategy: {df.loc[df['estimated_time_waste'].idxmax(), 'strategy']}")
```

## performance testing

### 9. stress testing the engine

```python
import time
from sophisticated_engine import get_sophisticated_response

# measure response time under load
test_input = "You need to pay taxes immediately or police will arrest you!"

start_time = time.time()
for i in range(100):
    result = get_sophisticated_response(test_input)
    if i % 10 == 0:
        print(f"completed {i+1} responses...")

end_time = time.time()
avg_response_time = (end_time - start_time) / 100

print(f"\nperformance results:")
print(f"average response time: {avg_response_time*1000:.2f}ms")
print(f"responses per second: {1/avg_response_time:.1f}")
```

### 10. memory usage testing

```python
import psutil
import os
from sophisticated_engine import SophisticatedResponseEngine

# measure memory usage
process = psutil.Process(os.getpid())
initial_memory = process.memory_info().rss / 1024 / 1024  # MB

# create engine and run tests
engine = SophisticatedResponseEngine()

for i in range(1000):
    result = engine.generate_response(f"Test message number {i}")

final_memory = process.memory_info().rss / 1024 / 1024  # MB
memory_growth = final_memory - initial_memory

print(f"memory usage:")
print(f"initial: {initial_memory:.1f} MB")
print(f"final: {final_memory:.1f} MB") 
print(f"growth: {memory_growth:.1f} MB")
```

## troubleshooting

### common issues

1. **import errors**: make sure you're in the right directory and have installed requirements
2. **csv permission errors**: check that analytics_data directory is writable
3. **memory issues**: the engine keeps conversation history, restart for long tests
4. **response inconsistency**: the ai uses randomness, expect variation in responses

### debug mode

```python
# enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

from sophisticated_engine import get_sophisticated_response

# run with debug info
result = get_sophisticated_response("debug test message")
```
