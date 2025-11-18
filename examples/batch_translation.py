"""Batch translation examples for processing large amounts of text."""

import asyncio
import io
import sys
import time
from typing import List, Tuple

from zaban import AsyncZaban

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# API Key - Option 1: Set directly here
API_KEY = "Your_ZABAN_API_KEY"
# Option 2: Use environment variable (set ZABAN_API_KEY)
# API_KEY = None


async def translate_file(
    client: AsyncZaban, input_file: str, output_file: str, target_lang: str, batch_size: int = 10
):
    """Translate a text file line by line.

    Args:
        client: AsyncZaban client
        input_file: Path to input file
        output_file: Path to output file
        target_lang: Target language code
        batch_size: Number of concurrent translations
    """
    print(f"Translating {input_file} to {target_lang}...\n")

    # Read input file
    with open(input_file, encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    translated_lines = []

    # Process in batches
    for i in range(0, total_lines, batch_size):
        batch = lines[i : i + batch_size]

        # Create tasks for batch
        tasks = [
            client.translation.create(text=line.strip(), target_lang=target_lang, auto_detect=True)
            for line in batch
            if line.strip()
        ]

        # Execute batch
        results = await asyncio.gather(*tasks)

        # Collect results
        for result in results:
            translated_lines.append(result.translated_text + "\n")

        print(f"Processed {min(i + batch_size, total_lines)}/{total_lines} lines")

    # Write output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

    print(f"\nTranslation complete! Output saved to {output_file}\n")


async def translate_dataset(
    texts: List[str], target_langs: List[str], batch_size: int = 10
) -> List[Tuple[str, str, str]]:
    """Translate a dataset to multiple languages.

    Args:
        texts: List of texts to translate
        target_langs: List of target language codes
        batch_size: Number of concurrent translations

    Returns:
        List of tuples (original_text, target_lang, translated_text)
    """
    async with AsyncZaban(api_key=API_KEY) as client:
        results = []
        total = len(texts) * len(target_langs)
        processed = 0

        print(f"Translating {len(texts)} texts to {len(target_langs)} languages...")
        print(f"Total translations: {total}\n")

        start_time = time.time()

        # Process in batches
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i : i + batch_size]

            # Create tasks for all language combinations in batch
            tasks = []
            task_metadata = []

            for text in batch_texts:
                for target_lang in target_langs:
                    tasks.append(
                        client.translation.create(
                            text=text, target_lang=target_lang, auto_detect=True
                        )
                    )
                    task_metadata.append((text, target_lang))

            # Execute batch
            batch_results = await asyncio.gather(*tasks)

            # Collect results
            for (text, target_lang), result in zip(task_metadata, batch_results):
                results.append((text, target_lang, result.translated_text))
                processed += 1

            print(f"Processed {processed}/{total} translations")

        elapsed_time = time.time() - start_time
        print(f"\nCompleted in {elapsed_time:.2f} seconds")
        print(f"Average: {elapsed_time/total:.2f} seconds per translation\n")

        return results


async def compare_translations():
    """Compare translations across multiple target languages."""
    print("=== Translation Comparison ===\n")

    async with AsyncZaban(api_key=API_KEY) as client:
        text = "Artificial intelligence is transforming the world"

        target_langs = [
            ("hin_Deva", "Hindi"),
            ("tam_Taml", "Tamil"),
            ("ben_Beng", "Bengali"),
            ("tel_Telu", "Telugu"),
            ("mar_Deva", "Marathi"),
        ]

        print(f"Original: {text}\n")

        # Translate to all languages concurrently
        tasks = [
            client.translation.create(text=text, target_lang=lang_code, auto_detect=True)
            for lang_code, _ in target_langs
        ]

        results = await asyncio.gather(*tasks)

        # Display results
        for (_, lang_name), result in zip(target_langs, results):
            print(f"{lang_name:12} | {result.translated_text}")

        print()


async def progressive_translation():
    """Translate text progressively through multiple languages."""
    print("=== Progressive Translation ===\n")

    async with AsyncZaban(api_key=API_KEY) as client:
        # Start with English
        current_text = "Knowledge is power"
        current_lang = "eng_Latn"

        # Translation chain
        chain = [
            ("hin_Deva", "Hindi"),
            ("ben_Beng", "Bengali"),
            ("tam_Taml", "Tamil"),
            ("eng_Latn", "English (back)"),
        ]

        print(f"Original: {current_text} ({current_lang})\n")

        for target_lang, lang_name in chain:
            result = await client.translation.create(
                text=current_text, source_lang=current_lang, target_lang=target_lang
            )

            print(f"-> {lang_name:20} | {result.translated_text}")

            current_text = result.translated_text
            current_lang = target_lang

        print()


async def main():
    """Run batch translation examples."""
    print("Zaban Python Client - Batch Translation Examples\n")
    print("=" * 50 + "\n")

    try:
        # Example 1: Compare translations
        await compare_translations()

        # Example 2: Progressive translation
        await progressive_translation()

        # Example 3: Translate dataset
        sample_texts = [
            "Hello, world!",
            "Good morning",
            "Thank you",
            "How are you?",
            "Nice to meet you",
        ]

        sample_langs = ["hin_Deva", "tam_Taml"]

        results = await translate_dataset(sample_texts, sample_langs, batch_size=5)

        print("=== Dataset Translation Results ===\n")
        for text, lang, translation in results[:5]:  # Show first 5
            print(f"{text:25} ({lang}) -> {translation}")
        print(f"... and {len(results) - 5} more\n")

        # Example 4: File translation (uncomment if you have a file)
        # async with AsyncZaban() as client:
        #     await translate_file(
        #         client,
        #         "input.txt",
        #         "output_hindi.txt",
        #         "hin_Deva",
        #         batch_size=10
        #     )

    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have set your API key:")
        print("  export ZABAN_API_KEY='Your_ZABAN_API_KEY'")


if __name__ == "__main__":
    asyncio.run(main())
