# Compatibility Factors between ISTP and INTJ Personality Types

compatibility_data = {
    "Factor": [
        "Communication Style",
        "Approach to Problem-Solving",
        "Emotional Expression",
        "Interest in Routine",
        "Need for Personal Space",
        "Long-Term Planning",
        "Approach to Change",
        "Risk-Taking"
    ],
    "ISTP": [
        "Direct, factual, prefers action over discussion",
        "Practical, prefers hands-on solutions",
        "Reserved, not highly expressive",
        "Dislikes routine, prefers spontaneity",
        "High, values independence",
        "Not highly focused, prefers to live in the moment",
        "Adaptable, comfortable with unexpected changes",
        "Willing to take risks, enjoys new experiences"
    ],
    "INTJ": [
        "Strategic, values efficiency and logic",
        "Analytical, looks for systematic solutions",
        "Reserved, values privacy and internal reflection",
        "Likes structure, but can adapt if needed",
        "High, values autonomy and self-sufficiency",
        "Highly focused, plans for the future",
        "Prefers controlled change, can be inflexible",
        "Calculated risks, prefers well-thought-out plans"
    ]
}

# Creating a DataFrame for Compatibility Factors
compatibility_df = pd.DataFrame(compatibility_data)
compatibility_df
