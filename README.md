MyTranslator
Overview:

MyTranslator is a versatile Python-based translation tool that leverages Google Translate and various language processing libraries to provide a seamless translation experience. This project is designed to cater to both text and speech inputs, making it an ideal choice for users who prefer different modes of interaction.

Features:

Text Translation: Translate written text from one language to another using the powerful Google Translate API.

Speech Recognition: Employ speech recognition capabilities to allow users to input text through spoken words.

Language Detection: Automatically detect the language of the input text, ensuring accurate translations.

Synonyms and Antonyms: Explore the synonyms and antonyms of translated words using WordNet.

Translation History: Keep track of translations with a comprehensive history log, including source and target languages.

Favorites: Save your favorite translations for quick access in the future.

Target Language Setting: Set a default target language for translation to streamline the process.

Text-to-Speech (TTS): Listen to the translated text and learn pronunciation with the TTS feature.

Pronunciation: Get the pronunciation of translated text using text-to-speech capabilities.

Speech-to-Text (STT): Convert spoken words into text using the Google Speech Recognition API via RapidAPI.

Dependencies:

googletrans: Google Translate API wrapper for Python.
speech_recognition: Library for performing speech recognition with support for various engines.
gtts: Google Text-to-Speech API wrapper for Python.
nltk: Natural Language Toolkit for language processing.
langdetect: Language detection library for Python.
How to Use:

Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Obtain a RapidAPI key for the Google Speech Recognition API and replace "YOUR_RAPID_API_KEY" in the code.
Run the MyTranslator.py script to launch the translation tool.
Choose between entering text or using speech recognition and follow the on-screen prompts.
Contributing:

Contributions are welcome! If you have ideas for new features, bug fixes, or improvements, feel free to open an issue or submit a pull request.

