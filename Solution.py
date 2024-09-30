class Solution:
    def findContentChildren(self, greed_factors, cookie_sizes):
        # Sort the greed factors of the children and the sizes of the cookies
        greed_factors.sort()
        cookie_sizes.sort()

        # Initialize the cookie index
        cookie_index = 0

        # Iterate through each greed factor
        for child_index, greed in enumerate(greed_factors):
            # Move through the cookie sizes until we find a cookie that satisfies the current greed factor
            while cookie_index < len(cookie_sizes) and cookie_sizes[cookie_index] < greed:
                cookie_index += 1

            # If there are no more cookies left, return the number of content children so far
            if cookie_index >= len(cookie_sizes):
                return child_index

            # Move to the next cookie index assuming the current cookie has been used
            cookie_index += 1

        # All children have been content, return the total number of children
        return len(greed_factors)
