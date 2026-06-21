import random
import re
from itertools import product

# Simple offline chatbot using large rule-based pattern matching.
# This is the previous version with direct response selection.

default_responses = [
    "That's interesting! Tell me more.",
    "I see. Can you elaborate?",
    "That sounds cool!",
    "Interesting point! Anything else?",
    "I understand. What else?",
    "Got it! Tell me more about that.",
    "I'm listening! Continue...",
    "Thanks for sharing. What else is on your mind?",
    "Nice! Keep going.",
    "I hear you. Tell me more.",
]

patterns = {}


def add_patterns(base_phrases, reply_list, prefixes=None, suffixes=None):
    prefixes = prefixes or [""]
    suffixes = suffixes or [""]

    for prefix, base, suffix in product(prefixes, base_phrases, suffixes):
        phrase = " ".join(filter(None, [prefix.strip(), base.strip(), suffix.strip()]))
        phrase = re.sub(r"\s+", " ", phrase).strip()
        if phrase:
            patterns[phrase] = reply_list


def create_patterns():
    greeting_responses = [
        "Hi there! How can I help you?",
        "Hello! Nice to meet you!",
        "Hey! What's up?",
        "Hi! I'm ready to chat.",
        "Hello! How can I support you today?",
    ]

    thanks_responses = [
        "You're welcome!",
        "Happy to help!",
        "Anytime!",
        "Glad I could help!",
        "No problem at all!",
    ]

    farewell_responses = [
        "Goodbye! See you later!",
        "Bye! Have a great day!",
        "See you soon!",
        "Take care!",
        "Catch you later!",
    ]

    identity_responses = [
        "I'm ChatBot, your AI assistant!",
        "You can call me ChatBot!",
        "I'm an AI chatbot here to talk with you.",
    ]

    help_responses = [
        "I'm here to help! Ask me anything.",
        "What do you need help with?",
        "I'm ready to assist!",
        "Tell me what you need and I'll do my best.",
    ]

    mood_responses = [
        "I'm doing great, thanks for asking!",
        "I'm feeling good and ready to chat!",
        "All good here. How are you?",
    ]

    weather_responses = [
        "I can't check the weather, but you can check a weather app!",
        "Sorry, I don't have weather data right now.",
        "I hope the weather is nice where you are!",
    ]

    time_responses = [
        "I don't have access to the current time, but you can check your system clock!",
        "Check your system time!",
        "I can't tell the exact time, but I'm here to chat.",
    ]

    joke_responses = [
        "Why did the programmer quit his job? Because he didn't get arrays! 😄",
        "What do you call a programmer from Finland? Nerdic! 😄",
        "I would tell you a UDP joke, but you might not get it. 😅",
    ]

    feeling_responses = [
        "I hear you. That matters.",
        "Thanks for telling me how you feel.",
        "I'm here for you.",
        "That sounds important.",
    ]

    favorite_responses = [
        "I have many favorite things, but I love chatting the most.",
        "That's a great question! I enjoy talking with you.",
        "I like learning new things from our conversation.",
    ]

    opinion_responses = [
        "I think that's a great topic!",
        "That's interesting. I enjoy that idea.",
        "I have a curious view on that, and I'm happy to discuss it.",
    ]

    activity_responses = [
        "That sounds like fun!",
        "I enjoy talking about that.",
        "Tell me more about it.",
    ]

    general_responses = [
        "I like that.",
        "That's an interesting thought.",
        "I hear you.",
        "Tell me more.",
    ]

    # Core phrase categories
    add_patterns(
        [
            "hello",
            "hi",
            "hey",
            "hiya",
            "howdy",
            "greetings",
            "what's up",
            "what is up",
            "good morning",
            "good afternoon",
            "good evening",
            "yo",
            "hi there",
            "hello there",
            "hey there",
        ],
        greeting_responses,
        suffixes=["", " there", " friend", " buddy", " mate", " everyone", " all", " today", " now"],
    )

    add_patterns(
        [
            "thanks",
            "thank you",
            "thx",
            "cheers",
            "much appreciated",
            "thanks a lot",
            "thank you so much",
            "thank you very much",
        ],
        thanks_responses,
        suffixes=["", " for your help", " for your support", " so much", " a lot", " buddy", " friend"],
    )

    add_patterns(
        [
            "bye",
            "goodbye",
            "see you",
            "see you later",
            "see you soon",
            "later",
            "take care",
            "talk to you later",
            "got to go",
            "i'm leaving",
            "i have to go",
            "good night",
        ],
        farewell_responses,
        suffixes=["", " friend", " buddy", " mate", " everyone", " all", " now", " soon", " tonight"],
    )

    add_patterns(
        [
            "what is your name",
            "what's your name",
            "who are you",
            "your name",
            "tell me your name",
            "may i know your name",
        ],
        identity_responses,
    )

    add_patterns(
        [
            "help",
            "help me",
            "can you help",
            "could you help",
            "i need help",
            "i need assistance",
            "i need support",
            "assist me",
            "please help",
            "please assist me",
            "can i get help",
        ],
        help_responses,
        suffixes=["", " please", " now", " with this", " with that", " with something"],
    )

    add_patterns(
        [
            "how are you",
            "how are you doing",
            "how is it going",
            "how is everything",
            "how is your day",
            "how are things",
            "how is life",
            "how do you do",
            "how you doing",
            "how's it going",
            "how are you today",
        ],
        mood_responses,
    )

    add_patterns(
        [
            "weather",
            "what is the weather",
            "what's the weather",
            "how is the weather",
            "is it raining",
            "is it sunny",
            "is it hot",
            "is it cold",
            "will it rain",
            "weather today",
            "weather now",
        ],
        weather_responses,
    )

    add_patterns(
        [
            "time",
            "what time is it",
            "what's the time",
            "tell me the time",
            "current time",
            "time now",
            "do you know the time",
        ],
        time_responses,
    )

    add_patterns(
        [
            "joke",
            "tell me a joke",
            "make me laugh",
            "say something funny",
            "do you know a joke",
            "give me a joke",
            "funny joke",
            "tell me something funny",
        ],
        joke_responses,
    )

    add_patterns(
        [
            "i am",
            "i'm",
            "i feel",
            "i feel very",
            "i am feeling",
            "i'm feeling",
            "i have been",
            "i was",
        ],
        feeling_responses,
        suffixes=[
            "happy",
            "sad",
            "excited",
            "bored",
            "tired",
            "angry",
            "nervous",
            "lonely",
            "stressed",
            "relaxed",
            "confused",
            "curious",
            "surprised",
            "content",
            "motivated",
            "sleepy",
            "hungry",
            "anxious",
            "distracted",
            "hopeful",
        ],
    )

    add_patterns(
        [
            "what is your favorite",
            "what's your favorite",
            "tell me your favorite",
            "do you have a favorite",
            "which is your favorite",
        ],
        favorite_responses,
        suffixes=[
            "color",
            "food",
            "movie",
            "song",
            "book",
            "hobby",
            "game",
            "sport",
            "animal",
            "place",
            "subject",
            "drink",
            "city",
            "movie genre",
            "music genre",
        ],
    )

    add_patterns(
        [
            "what do you think about",
            "what do you think of",
            "tell me what you think about",
            "tell me your opinion about",
            "do you like",
            "do you love",
            "are you okay with",
            "are you sure about",
        ],
        opinion_responses,
        suffixes=[
            "music",
            "movies",
            "books",
            "sports",
            "coding",
            "programming",
            "art",
            "travel",
            "technology",
            "fashion",
            "science",
            "food",
            "games",
            "chatbots",
            "AI",
            "nature",
            "space",
            "history",
            "school",
            "work",
        ],
    )

    add_patterns(
        [
            "i want to",
            "i would like to",
            "i wish to",
            "i hope to",
            "i need to",
            "i want",
            "i would like",
            "i wish",
            "i hope",
        ],
        activity_responses,
        suffixes=[
            "learn",
            "play",
            "eat",
            "sleep",
            "relax",
            "travel",
            "study",
            "work",
            "laugh",
            "chat",
            "talk",
            "code",
            "read",
            "write",
            "create",
            "draw",
            "exercise",
            "watch a movie",
            "have fun",
            "explore",
        ],
    )

    add_patterns(
        [
            "do you",
            "can you",
            "will you",
            "would you",
            "could you",
            "should you",
        ],
        general_responses,
        suffixes=[
            "help me",
            "tell me a joke",
            "give me advice",
            "answer a question",
            "teach me something",
            "solve this",
            "chat with me",
            "play a game",
            "suggest something",
            "share a story",
            "say hello",
        ],
    )

    subjects = ["i", "you", "we", "they", "he", "she", "it"]
    verbs = ["like", "love", "hate", "enjoy", "need", "want", "know", "understand", "prefer", "miss", "remember", "see", "find", "choose", "need to", "want to"]
    objects = [
        "music",
        "movies",
        "sports",
        "coding",
        "programming",
        "chatbots",
        "games",
        "books",
        "food",
        "travel",
        "science",
        "art",
        "history",
        "math",
        "technology",
        "fashion",
        "animals",
        "nature",
        "weather",
        "space",
        "school",
        "work",
        "coffee",
        "tea",
        "pizza",
        "sleep",
        "dance",
        "music videos",
        "stories",
        "memes",
    ]

    for subject, verb, obj in product(subjects, verbs, objects):
        phrase = f"{subject} {verb} {obj}".strip()
        patterns[phrase] = general_responses

    feeling_prefixes = [
        "i am",
        "i'm",
        "i feel",
        "i feel very",
        "i am feeling",
        "i've been",
        "i have been",
        "i was",
    ]
    feeling_words = [
        "happy",
        "sad",
        "excited",
        "bored",
        "tired",
        "angry",
        "nervous",
        "lonely",
        "stressed",
        "relaxed",
        "confused",
        "curious",
        "surprised",
        "content",
        "motivated",
        "sleepy",
        "hungry",
        "anxious",
        "distracted",
        "hopeful",
        "grateful",
        "sad today",
        "happy today",
        "excited today",
        "worried",
        "joyful",
        "angry today",
        "tired today",
        "ready",
        "nervous about school",
        "nervous about work",
        "excited about life",
        "happy about this",
        "sad about that",
        "curious about everything",
        "stressed about exams",
        "stressed about work",
    ]

    for prefix, word in product(feeling_prefixes, feeling_words):
        phrase = f"{prefix} {word}".strip()
        patterns[phrase] = feeling_responses

    topic_prefixes = [
        "tell me about",
        "what do you know about",
        "do you know about",
        "what is",
        "what are",
        "why is",
        "how do",
        "how can",
    ]
    topics = [
        "AI",
        "machine learning",
        "python",
        "chatbots",
        "technology",
        "space",
        "science",
        "coding",
        "travel",
        "music",
        "movies",
        "books",
        "history",
        "sports",
        "food",
        "weather",
        "nature",
        "animals",
        "games",
        "art",
    ]

    for prefix, topic in product(topic_prefixes, topics):
        phrase = f"{prefix} {topic}".strip()
        patterns[phrase] = activity_responses

    extra_prefixes = ["please", "hey", "ok", "okay", "so", "well", "actually", "honestly"]
    extra_bases = [
        "tell me something",
        "share something",
        "say something",
        "give me advice",
        "give me an idea",
        "give me a suggestion",
        "tell me a story",
        "share a story",
        "recommend something",
        "help me understand",
        "help me decide",
        "make a choice",
    ]
    for prefix, base in product(extra_prefixes, extra_bases):
        phrase = f"{prefix} {base}".strip()
        patterns[phrase] = activity_responses

    return patterns

patterns = create_patterns()
sorted_keywords = sorted(patterns.keys(), key=len, reverse=True)


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def get_response(user_input):
    clean_text = normalize_text(user_input)
    for keyword in sorted_keywords:
        if keyword in clean_text:
            return random.choice(patterns[keyword])
    return random.choice(default_responses)

print("=" * 50)
print("🤖 Offline Chatbot Started!")
print("=" * 50)
print(f"Loaded patterns: {len(patterns)}")
print("(Type 'exit' to quit)\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Thanks for chatting! 👋")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

    except KeyboardInterrupt:
        print("\n\nChatbot: Goodbye! Thanks for chatting! 👋")
        break
    except Exception as e:
        print(f"Error: {str(e)}\n")