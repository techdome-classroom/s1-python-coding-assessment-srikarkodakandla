def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Initialize DP table, with dimensions (m + 1) x (n + 1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty pattern matches empty message
    dp[0][0] = True
    
    # If the pattern starts with stars, it can match an empty message
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?':
                # '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                # Characters must match exactly
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]

    # The result is stored in dp[m][n], which represents the match for the entire string and pattern
    return dp[m][n]
