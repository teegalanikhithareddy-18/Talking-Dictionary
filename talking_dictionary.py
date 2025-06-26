import pyttsx3
from nltk.corpus import wordnet as wn
import nltk

# Ensure WordNet data is downloaded
try:
    wn.synsets("test")
except LookupError:
    nltk.download("wordnet")
    nltk.download("omw-1.4")

def speak(text):
    print("🔊 Speaking:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_offline_meaning(word):
    synsets = wn.synsets(word)
    if not synsets:
        return None
    # Return the first definition found
    return synsets[0].definition()

def main():
    word = input("📥 Enter a word to get its meaning (offline): ").strip()
    meaning = get_offline_meaning(word)

    if meaning:
        print(f"📘 Meaning of '{word}': {meaning}")
        speak(meaning)
    else:
        print("❌ No definition found in offline dictionary.")
        speak("Sorry, I couldn't find a definition.")

if __name__ == "__main__":
    main()
