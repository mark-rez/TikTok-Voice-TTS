# author: Giorgio
# date: 19.03.2024
# topic: TikTok-Voice-TTS
# version: 1.1

import requests, base64, json, sys
from threading import Thread
from playsound import playsound

# Define a function to split the text into chunks of 300 characters or less
def split_string(string: str) -> list[str]:
    words: list[str] = string.split()

    result: list[str] = []
    current_chunk: str = ''

    for word in words:
        if len(current_chunk) + len(word) + 1 <= 300:  # Check if adding the word exceeds the chunk size
            current_chunk += ' ' + word
        else:
            if current_chunk:  # Append the current chunk if not empty
                result.append(current_chunk.strip())
            current_chunk = word
    if current_chunk:  # Append the last chunk if not empty
        result.append(current_chunk.strip())

    return result

# Load endpoint data from JSON file
with open("tts_json_data/endpoints.json", 'r') as f:
    ENDPOINT_DATA = json.load(f)

# Load voice data from JSON file
with open("tts_json_data/voices.json", 'r') as f:
    VOICES = json.load(f)

# Define the text-to-speech function
def tts(text: str, voice: str, output_filename: str = "output.mp3", play_sound: bool = False) -> None:
    # Check if the specified voice is valid
    if not voice in VOICES:
        raise ValueError("voice must be valid")
    
    # Check if the text is not empty
    if not text:
        raise ValueError("text must not be 'None'")
    
    # Iterate over each endpoint
    for entry in ENDPOINT_DATA:
        # Split the text into chunks
        chunks: list[str] = split_string(text)
        data: list[str] = ["" for i in range(len(chunks))]

        # Define a function to generate audio for each chunk in a separate thread
        def generate_audio_chunk(index: int, chunk: str) -> None:
            try:
                # Send a request to the endpoint to generate audio for the chunk
                response = requests.post(
                    entry["url"], 
                    json={
                        "text": chunk,
                        "voice": voice
                    }
                )
                # Store the audio data for the chunk
                data[index] = response.json()[entry["response"]]
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()

        # Create and start threads for generating audio for each chunk
        threads: list[Thread] = []
        for index, chunk in enumerate(chunks):
            thread: Thread = Thread(target=generate_audio_chunk, args=(index, chunk))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # Concatenate audio data from all chunks and decode from base64
        audio_bytes = base64.b64decode("".join(data))
        
        # Write the audio data to a file
        with open(output_filename, "wb") as file:
            file.write(audio_bytes)
            print(f"File '{output_filename}' has been generated successfully.")
        
        # Play the audio if specified
        if (play_sound) :
            playsound(output_filename)

        # Break after processing the first endpoint (remove this if you want to process all endpoints)
        break
