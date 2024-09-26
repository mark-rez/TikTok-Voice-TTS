# Python standard modules
import os
import requests
import base64
import re
from json import load
from threading import Thread
from typing import Dict, List, Optional

# Downloaded modules
from playsound import playsound

# Local files
from .voice import Voice

import logging
# Setup logging configuration
logging.basicConfig(level=logging.INFO)

def tts(
    text: str,
    voice: Voice,
    output_file_path: str = "output.mp3",
    play_sound: bool = False
):
    """Main function to convert text to speech and save to a file."""
    
    # Validate input arguments
    _validate_args(text, voice)

    # Load endpoint data from the endpoints.json file
    endpoint_data: List[Dict[str, str]] = _load_endpoints()
    success: bool = False    

    # Iterate over endpoints to find a working one
    for endpoint in endpoint_data:
        # Generate audio bytes from the current endpoint
        audio_bytes: bytes = _fetch_audio_bytes(endpoint, text, voice)
        
        if audio_bytes:
            # Save the generated audio to a file
            _save_audio_file(output_file_path, audio_bytes)
        
            # Optionally play the audio file
            if play_sound:
                playsound(output_file_path)
            
            success = True
            # Stop after processing a valid endpoint
            break

    if not success:
        raise Exception("failed to generate audio")

def _save_audio_file(output_file_path: str, audio_bytes: bytes):
    """Write the audio bytes to a file."""
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        
    with open(output_file_path, "wb") as file:
        file.write(audio_bytes)

def _fetch_audio_bytes(
    endpoint: Dict[str, str],
    text: str,
    voice: Voice
) -> Optional[bytes]:
    """Fetch audio data from an endpoint and decode it."""
    
    # Initialize variables for endpoint validity and audio data
    text_chunks: List[str] = _split_text(text)
    audio_chunks: List[str] = ["" for _ in range(len(text_chunks))]

    # Function to generate audio for each text chunk
    def generate_audio_chunk(index: int, text_chunk: str):
        try:
            response = requests.post(endpoint["url"], json={"text": text_chunk, "voice": voice.value})
            response.raise_for_status()
            audio_chunks[index] = response.json()[endpoint["response"]]
        except (requests.RequestException, KeyError):
            return

    # Start threads for generating audio for each chunk
    threads = [Thread(target=generate_audio_chunk, args=(i, chunk)) for i, chunk in enumerate(text_chunks)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    if any(not chunk for chunk in audio_chunks):
        return None

    # Concatenate and decode audio data from all chunks
    return base64.b64decode("".join(audio_chunks))

def _load_endpoints() -> List[Dict[str, str]]:
    """Load endpoint configurations from a JSON file."""
    script_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(script_dir, '../data', 'config.json')
    with open(json_file_path, 'r') as file:
        return load(file)

def _validate_args(text: str, voice: Voice):
    """Validate the input arguments."""
    
    # Check if the voice is of the correct type
    if not isinstance(voice, Voice):
        raise TypeError("'voice' must be of type Voice")
    
    # Check if the text is not empty
    if not text:
        raise ValueError("text must not be empty")

def _split_text(text: str, byte_limit: int = 300) -> List[str]:
    """
    Split text into chunks where each chunk's UTF-8 byte length is <= byte_limit.
    
    Args:
        text (str): The input text to be split.
        byte_limit (int): The maximum byte size per chunk.
        
    Returns:
        List[str]: A list of text chunks.
    """
    merged_chunks = []
    current_chunk = ""
    current_byte_length = 0
    
    # Extended punctuation and symbols for chunk splitting
    punctuation_regex = r'.*?[.,!?:;\-—…“”‘’\'"「」『』（）【】《》{}<>\[\]‥、。！？\n]|.+'

    # Split text based on punctuation and symbols to maintain natural pauses
    separated_chunks = re.findall(punctuation_regex, text)
    
    for chunk in separated_chunks:
        chunk_byte_length = len(chunk.encode('utf-8'))
        
        if chunk_byte_length > byte_limit:
            # Split the chunk further if it exceeds byte limit
            words = chunk.split()
            for word in words:
                word_byte_length = len(word.encode('utf-8'))
                if current_byte_length + word_byte_length + 1 > byte_limit:
                    if current_chunk:
                        merged_chunks.append(current_chunk)
                        logging.info(f"Chunk created: {current_chunk} (Bytes: {current_byte_length})")
                    current_chunk = word
                    current_byte_length = word_byte_length
                else:
                    if current_chunk:
                        current_chunk += ' ' + word
                        current_byte_length += word_byte_length + 1  # +1 for space
                    else:
                        current_chunk = word
                        current_byte_length = word_byte_length
        else:
            if current_byte_length + chunk_byte_length > byte_limit:
                if current_chunk:
                    merged_chunks.append(current_chunk)
                    logging.info(f"Chunk created: {current_chunk} (Bytes: {current_byte_length})")
                current_chunk = chunk
                current_byte_length = chunk_byte_length
            else:
                current_chunk += chunk
                current_byte_length += chunk_byte_length
    
    if current_chunk:
        merged_chunks.append(current_chunk)
        logging.info(f"Chunk created: {current_chunk} (Bytes: {current_byte_length})")
    
    return merged_chunks
