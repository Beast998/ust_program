from concurrent.futures import ThreadPoolExecutor
from word_count import compute_word_frequency
from read import read_input_file
from display import display_word_frequency

def main():
    filename = 'C:\\Users\\Admin\\PycharmProjects\\word_counter\\input_data\\input.txt'  # Path to the input file

    # Execute tasks in parallel
    with ThreadPoolExecutor() as executor:
        # Read input
        text_future = executor.submit(read_input_file, filename)
        text = text_future.result()

        # Compute frequency
        word_freq_future = executor.submit(compute_word_frequency, text)
        word_freq = word_freq_future.result()

        # Display output
        display_word_frequency(word_freq)

if __name__ == "__main__":
    main()
