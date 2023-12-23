from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os
from langdetect import detect
from nltk.corpus import wordnet

class MyTranslator:
    def __init__(self):
        self.translator = Translator()
        self.recognizer = sr.Recognizer()
        self.translation_history = []
        self.favorites = {}
        self.target_language = 'en'  # Default target language

    def translate_text(self, text, target_language=None):
        target_language = target_language or self.target_language
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    def detect_language(self, text):
        return self.translator.detect(text).lang

    def get_synonyms_antonyms(self, word, lang='en'):
        synonyms = []
        antonyms = []

        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

        return synonyms, antonyms

    def add_to_history(self, original, translated, source_lang, target_lang):
        self.translation_history.append({
            'original': original,
            'translated': translated,
            'source_lang': source_lang,
            'target_lang': target_lang
        })

    def view_history(self):
        print("\nTranslation History:")
        for idx, entry in enumerate(self.translation_history, start=1):
            print(f"{idx}. {entry['original']} ({entry['source_lang']}) -> {entry['translated']} ({entry['target_lang']})")

    def add_to_favorites(self, key, value):
        self.favorites[key] = value
        print(f"\nAdded to Favorites: {key} -> {value}")

    def view_favorites(self):
        print("\nFavorite Translations:")
        for key, value in self.favorites.items():
            print(f"{key} -> {value}")

    def set_target_language(self, language_code):
        self.target_language = language_code
        print(f"\nDefault Target Language set to: {language_code}")

    def speak_text(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("output.mp3")
        os.system("start output.mp3")

    def pronounce_text(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("pronunciation.mp3")
        os.system("start pronunciation.mp3")

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Say something...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                print("Recognizing...")

                # Use RapidAPI key here
                rapid_api_key = "your key"
                text = self.recognizer.recognize_google(audio, key=rapid_api_key)

                print(f"Recognized Text: {text}")

                # Detect the language
                detected_language = detect(text)
                print(f"Detected Language: {detected_language}")

                # Translate the text
                translated_text = self.translate_text(text, self.target_language)

                # Output
                print(f"Translated Text ({self.target_language}): {translated_text}")

                # Other features (e.g., synonyms, antonyms, add to history, etc.)

            except sr.UnknownValueError:
                print("Speech recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    translator = MyTranslator()

    while True:
        print("\n===== My Translator =====")
        print("Enter 'exit' to quit.")

        # Input
        user_input = input("Do you want to enter text or use speech recognition? (text/speech): ")

        if user_input.lower() == 'text':
            text_to_translate = input("Enter the text to translate: ")
        elif user_input.lower() == 'speech':
            translator.recognize_speech()
            continue
        else:
            print("Invalid input. Please enter 'text' or 'speech'.")
            continue

        # Check for exit command
        if text_to_translate.lower() == 'exit':
            print("Exiting My Translator. Goodbye!")
            break

        # Language detection
        source_language = translator.detect_language(text_to_translate)
        print(f"Detected Source Language: {source_language}")

        # Target language input
        target_language = input("Enter the target language code (e.g., 'fr' for French): ")

        # Translation
        translated_text = translator.translate_text(text_to_translate, target_language)

        # Synonyms and Antonyms
        synonyms, antonyms = translator.get_synonyms_antonyms(text_to_translate, lang=target_language)
        print(f"\nSynonyms: {', '.join(synonyms) if synonyms else 'N/A'}")
        print(f"Antonyms: {', '.join(antonyms) if antonyms else 'N/A'}")

        # Add to history
        translator.add_to_history(text_to_translate, translated_text, source_language, target_language)

                # Output
        print(f"\nOriginal Text ({source_language}): {text_to_translate}")
        print(f"Translated Text ({target_language}): {translated_text}")

        # Additional features
        print("\nAdditional Features:")
        print("1. View Translation History")
        print("2. Add to Favorites")
        print("3. View Favorites")
        print("4. Set Default Target Language")
        print("5. Speak Translated Text")
        print("6. Pronounce Text")
        # Include other feature options here

        choice = input("Enter the number of the feature you want to use (or press Enter to skip): ")

        if choice == '1':
            translator.view_history()
        elif choice == '2':
            key = input("Enter a key for the favorite translation: ")
            translator.add_to_favorites(key, translated_text)
        elif choice == '3':
            translator.view_favorites()
        elif choice == '4':
            language_code = input("Enter the language code for the default target language: ")
            translator.set_target_language(language_code)
        elif choice == '5':
            translator.speak_text(translated_text, lang=target_language)
        elif choice == '6':
            translator.pronounce_text(translated_text, lang=target_language)
        # Include other feature cases here

if __name__ == "__main__":
    main()
