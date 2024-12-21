import os
import subprocess

# Define the directories containing audio files
genre_dirs = [
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//blues',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//classical',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//country',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//disco',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//hiphop',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//jazz',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//metal',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//pop',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//reggae',
    'C://Users//Deepak//Desktop//Audio//archive//Data//genres_original//rock'
]

for genre_dir in genre_dirs:
    # List files in the directory before conversion
    print(f"Contents of {genre_dir} before conversion:")
    before_conversion = os.listdir(genre_dir)
    print(before_conversion)

    # Convert .au files to .wav
    for root, _, files in os.walk(genre_dir):
        for file in files:
            if file.endswith('.au'):
                source_file = os.path.join(root, file)
                output_file = os.path.join(root, file[:-3] + "wav")
                subprocess.run(['sox', source_file, output_file], check=True)

    # Remove .au files after conversion
    for root, _, files in os.walk(genre_dir):
        for file in files:
            if file.endswith('.au'):
                os.remove(os.path.join(root, file))

    # List files in the directory after conversion
    print(f"Contents of {genre_dir} after conversion:")
    after_conversion = os.listdir(genre_dir)
    print(after_conversion)
    print("\n")

print("Conversion complete. Check respective directories.")
