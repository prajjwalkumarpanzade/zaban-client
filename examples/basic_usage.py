"""Basic usage examples for Zaban Python client."""

from zaban import Zaban

# Initialize client
# Option 1: Pass API key directly
client = Zaban(api_key="Your_ZABAN_API_KEY")

# Option 2: Use environment variable ZABAN_API_KEY
# client = Zaban()


def translation_example():
    """Example: Translate text between languages."""
    print("=== Translation Example ===\n")
    
    # English to Hindi
    result = client.translation.create(
        text="Hello, how are you?",
        source_lang="eng_Latn",
        target_lang="hin_Deva"
    )
    print(f"Original: Hello, how are you?")
    print(f"Translated: {result.translated_text}")
    print(f"Model: {result.model}\n")
    
    # With auto-detection
    result = client.translation.create(
        text="Good morning",
        target_lang="tam_Taml",
        auto_detect=True
    )
    print(f"Original: Good morning")
    print(f"Translated: {result.translated_text}")
    print(f"Detected language: {result.source_lang}\n")
    
    # Using convenience method
    result = client.translation.translate(
        "Thank you",
        to="hin_Deva",
        from_="eng_Latn"
    )
    print(f"Original: Thank you")
    print(f"Translated: {result.translated_text}\n")


def tts_example():
    """Example: Convert text to speech."""
    print("=== Text-to-Speech Example ===\n")
    
    audio = client.audio.speech.create(
        text="नमस्ते दुनिया",
        lang="hi",
        speaker="female",
        format="wav"
    )
    
    # Save to file
    audio.save("output.wav")
    print("Audio saved to: output.wav")
    
    # Or get bytes directly
    audio_bytes = audio.content
    print(f"Audio size: {len(audio_bytes) if audio_bytes else 0} bytes\n")


def stt_example():
    """Example: Transcribe speech to text."""
    print("=== Speech-to-Text Example ===\n")
    
    # From file path
    try:
        transcription = client.audio.transcriptions.create(
            audio="audio.wav",
            lang="hi"
        )
        print(f"Transcribed text: {transcription.text}")
        print(f"Language: {transcription.language}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("(Make sure you have an audio file at 'audio.wav')\n")


def transliteration_example():
    """Example: Transliterate text between scripts."""
    print("=== Transliteration Example ===\n")
    
    result = client.transliteration.create(
        text="namaste",
        source_script="latn",
        target_script="deva",
        lang="hi",
        topk=3
    )
    
    print(f"Original: namaste")
    print(f"Top result: {result.top}")
    print(f"All results: {result.results}\n")


def error_handling_example():
    """Example: Handle errors gracefully."""
    print("=== Error Handling Example ===\n")
    
    from zaban import (
        AuthenticationError,
        ValidationError,
        ZabanError
    )
    
    try:
        # This will fail with an invalid API key
        invalid_client = Zaban(api_key="sk-invalid")
        result = invalid_client.translation.create(
            text="Hello",
            target_lang="hin_Deva"
        )
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except ZabanError as e:
        print(f"API error: {e}")
    
    print()


def context_manager_example():
    """Example: Use client as context manager."""
    print("=== Context Manager Example ===\n")
    
    with Zaban(api_key="sk-your-api-key") as client:
        result = client.translation.create(
            text="Hello",
            target_lang="hin_Deva",
            auto_detect=True
        )
        print(f"Translated: {result.translated_text}")
    
    print("Client automatically closed\n")


if __name__ == "__main__":
    print("Zaban Python Client - Basic Usage Examples\n")
    print("=" * 50 + "\n")
    
    try:
        translation_example()
        # tts_example()
        # stt_example()
        transliteration_example()
        # error_handling_example()
        # context_manager_example()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have set your API key:")
        print("  export ZABAN_API_KEY='sk-your-api-key'")
        print("or pass it directly to Zaban(api_key='sk-your-api-key')")

