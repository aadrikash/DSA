class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):

        # Store cells along with their Manhattan distance
        cells = []

        # Visit every row
        for r in range(rows):

            # Visit every column
            for c in range(cols):

                # Calculate Manhattan distance
                distance = abs(r - rCenter) + abs(c - cCenter)

                # Store distance and coordinates
                cells.append((distance, r, c))

        # Sort cells by distance
        cells.sort()

        # Return only the coordinates
        return [[r, c] for distance, r, c in cells]