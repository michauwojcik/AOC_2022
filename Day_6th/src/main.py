"""
    Program which finds the starting point (index in string) of packet and message. 

    1. Reads input from textfile
    2. Initializes 'packet' and 'message' objects (packet starts after 4 unique characters, message after 14)
    3. Searches for window made up from 4 and 14 unique characters. Returns the character's index which follows that window.

"""


from datastream import DatastreamReceiver
import sys
sys.path.append("../../Common")
from text_file_manager import TextFileManager

datastream_path = sys.argv[1]

def main(datastream_path):
    input = TextFileManager(datastream_path)
    packet = DatastreamReceiver(input.content, window_size=4)
    message = DatastreamReceiver(input.content, window_size=14)
    
    packet_start_index = packet.find_starting_index()
    message_start_index = message.find_starting_index()

    print(f"Starting point for packet: {packet_start_index}. Starting point for message: {message_start_index}")


if __name__ == "__main__":
    main(datastream_path)