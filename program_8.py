
# Program 8: Huffman Coding

import heapq
from itertools import count


# ---------- Node Class ----------
class Node:
    def __init__(self, char, freq, left=None, right=None):
        # Store character and its frequency
        self.char = char
        self.freq = freq

        # Store left and right child nodes
        self.left = left
        self.right = right


# ---------- Huffman Coding ----------
class HuffmanCoder:
    def build_tree(self, frequencies):
        # Create an empty priority queue
        heap = []
        unique_id = count()

        # Create a leaf node for each character
        for char, freq in frequencies.items():
            if freq <= 0:
                raise ValueError("Frequency must be positive")

            node = Node(char, freq)
            heapq.heappush(
                heap, (freq, next(unique_id), node)
            )

        # Combine nodes with the lowest frequencies
        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            # Create a parent node
            merged = Node(None, freq1 + freq2, left, right)

            heapq.heappush(
                heap, (merged.freq, next(unique_id), merged)
            )

        # Return the root of the Huffman tree
        return heap[0][2] if heap else None

    def generate_codes(self, root):
        # Dictionary to store binary codes
        codes = {}

        def traverse(node, code):
            if node is None:
                return

            # Save the code for a leaf node
            if node.char is not None:
                codes[node.char] = code if code else "0"
                return

            # Traverse left with 0 and right with 1
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(root, "")
        return codes


# ---------- Main Program ----------
print("PROGRAM 8")
print("Huffman Coding")

# Character frequencies
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

# Build tree and generate binary codes
coder = HuffmanCoder()
root = coder.build_tree(frequencies)
codes = coder.generate_codes(root)

# Display Huffman codes
print("\nHuffman Codes")
for char in sorted(codes):
    print(char, ":", codes[char])
