# print("hello world")

# book = "books/frankenstein.txt"
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # words = file_contents.split()
        file_lower = file_contents.lower()
        print(file_lower)

main()
