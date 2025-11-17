"""Async usage examples for Zaban Python client."""

import asyncio
from zaban import AsyncZaban


async def single_translation():
    """Example: Single async translation."""
    print("=== Single Async Translation ===\n")
    
    async with AsyncZaban(api_key="Your_ZABAN_API_KEY") as client:
        result = await client.translation.create(
            text="Hello, world!",
            target_lang="hin_Deva",
            auto_detect=True
        )
        print(f"Original: Hello, world!")
        print(f"Translated: {result.translated_text}\n")


async def batch_translations():
    """Example: Batch translations with concurrent requests."""
    print("=== Batch Translations ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        # Prepare multiple texts
        texts = [
            "Hello",
            "Goodbye",
            "Thank you",
            "Good morning",
            "How are you?",
        ]
        
        # Create concurrent translation tasks
        tasks = [
            client.translation.create(
                text=text,
                target_lang="hin_Deva",
                auto_detect=True
            )
            for text in texts
        ]
        
        # Execute all tasks concurrently
        results = await asyncio.gather(*tasks)
        
        # Print results
        for original, result in zip(texts, results):
            print(f"{original:20} -> {result.translated_text}")
        
        print()


async def multi_language_translation():
    """Example: Translate one text to multiple languages."""
    print("=== Multi-Language Translation ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        text = "Good morning"
        target_languages = [
            ("hin_Deva", "Hindi"),
            ("tam_Taml", "Tamil"),
            ("ben_Beng", "Bengali"),
            ("tel_Telu", "Telugu"),
            ("guj_Gujr", "Gujarati"),
        ]
        
        # Create concurrent tasks
        tasks = [
            client.translation.create(
                text=text,
                target_lang=lang_code,
                auto_detect=True
            )
            for lang_code, _ in target_languages
        ]
        
        # Execute all tasks
        results = await asyncio.gather(*tasks)
        
        # Print results
        print(f"Original: {text}\n")
        for (_, lang_name), result in zip(target_languages, results):
            print(f"{lang_name:12} -> {result.translated_text}")
        
        print()


async def tts_async():
    """Example: Async text-to-speech."""
    print("=== Async Text-to-Speech ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        audio = await client.audio.speech.create(
            text="नमस्ते दुनिया",
            lang="hi",
            speaker="female"
        )
        
        audio.save("async_output.wav")
        print("Audio saved to: async_output.wav\n")


async def stt_async():
    """Example: Async speech-to-text."""
    print("=== Async Speech-to-Text ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        try:
            transcription = await client.audio.transcriptions.create(
                audio="audio.wav",
                lang="hi"
            )
            print(f"Transcribed: {transcription.text}\n")
        except Exception as e:
            print(f"Error: {e}")
            print("(Make sure you have an audio file at 'audio.wav')\n")


async def transliteration_async():
    """Example: Async transliteration."""
    print("=== Async Transliteration ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        words = ["namaste", "dhanyavaad", "shukriya"]
        
        tasks = [
            client.transliteration.create(
                text=word,
                source_script="latn",
                target_script="deva",
                lang="hi"
            )
            for word in words
        ]
        
        results = await asyncio.gather(*tasks)
        
        for original, result in zip(words, results):
            print(f"{original:15} -> {result.top}")
        
        print()


async def error_handling_async():
    """Example: Async error handling."""
    print("=== Async Error Handling ===\n")
    
    from zaban import ZabanError, AuthenticationError
    
    try:
        async with AsyncZaban(api_key="sk-invalid") as client:
            result = await client.translation.create(
                text="Hello",
                target_lang="hin_Deva"
            )
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
    except ZabanError as e:
        print(f"API error: {e}")
    
    print()


async def mixed_operations():
    """Example: Mix different operations concurrently."""
    print("=== Mixed Concurrent Operations ===\n")
    
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        # Create different types of tasks
        translation_task = client.translation.create(
            text="Hello",
            target_lang="hin_Deva",
            auto_detect=True
        )
        
        transliteration_task = client.transliteration.create(
            text="namaste",
            source_script="latn",
            target_script="deva",
            lang="hi"
        )
        
        # Execute concurrently
        translation, transliteration = await asyncio.gather(
            translation_task,
            transliteration_task
        )
        
        print(f"Translation: Hello -> {translation.translated_text}")
        print(f"Transliteration: namaste -> {transliteration.top}")
        print()


async def main():
    """Run all async examples."""
    print("Zaban Python Client - Async Usage Examples\n")
    print("=" * 50 + "\n")
    
    try:
        await single_translation()
        await batch_translations()
        await multi_language_translation()
        # await tts_async()
        # await stt_async()
        await transliteration_async()
        # await error_handling_async()
        await mixed_operations()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have set your API key:")
        print("  export ZABAN_API_KEY='sk-your-api-key'")


if __name__ == "__main__":
    asyncio.run(main())

