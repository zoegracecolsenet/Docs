{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zoegracecolsenet/Docs/blob/main/Assignment1_Part1_Regex.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HvTPA2gRIRs4"
      },
      "source": [
        "# Assignment 1 - Part 1: Regular Expressions and Date Extraction\n",
        "\n",
        "**Course:** Natural Language Processing\n",
        "\n",
        "**Total Points:** 10 points (contributes to 50% of Assignment 1)\n",
        "\n",
        "---\n",
        "\n",
        "## Instructions\n",
        "\n",
        "1. Complete all the functions marked with `# YOUR CODE HERE`\n",
        "2. **DO NOT** change the function names or their signatures\n",
        "3. Each function must return the exact type specified\n",
        "4. Test your functions by running the test cells\n",
        "5. When finished:\n",
        "   - Export this notebook as a Python file (.py)\n",
        "   - **Name the file:** `LASTNAME_FIRSTNAME_assignment1_part1.py`\n",
        "   - Example: `DUPONT_Jean_assignment1_part1.py`\n",
        "   - Push to your GitHub repository\n",
        "   - Send the .py file by email to: **yoroba93@gmail.com**\n",
        "\n",
        "---\n",
        "\n",
        "## Assignment Overview\n",
        "\n",
        "In this assignment, you'll work with messy medical data and use regex to extract relevant information.\n",
        "\n",
        "Each line of the `dates.txt` file corresponds to a medical note. Each note has a date that needs to be extracted, but dates are encoded in many different formats.\n",
        "\n",
        "**Date formats you may encounter:**\n",
        "- `04/20/2009; 04/20/09; 4/20/09; 4/3/09`\n",
        "- `Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009`\n",
        "- `20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009`\n",
        "- `Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009`\n",
        "- `Feb 2009; Sep 2009; Oct 2010`\n",
        "- `6/2008; 12/2009`\n",
        "- `2009; 2010`\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "E88un-pHIRs8"
      },
      "source": [
        "## Setup"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xBatPgdhIRs9",
        "outputId": "88f5130b-bda8-40e6-c603-b509c03a568a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Loaded 500 medical notes\n",
            "\n",
            "First 5 notes:\n",
            "0         03/25/93 Total time of visit (in minutes):\\n\n",
            "1                       6/18/85 Primary Care Doctor:\\n\n",
            "2    sshe plans to move as of 7/8/71 In-Home Servic...\n",
            "3                7 on 9/27/75 Audit C Score Current:\\n\n",
            "4    2/6/96 sleep studyPain Treatment Pain Level (N...\n",
            "dtype: object\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import re\n",
        "from datetime import datetime\n",
        "\n",
        "# Load the data\n",
        "doc = []\n",
        "with open('dates.txt') as file:\n",
        "    for line in file:\n",
        "        doc.append(line)\n",
        "\n",
        "df = pd.Series(doc)\n",
        "print(f\"Loaded {len(df)} medical notes\")\n",
        "print(\"\\nFirst 5 notes:\")\n",
        "print(df.head())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k0T5SkI0IRs-"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 1 (1 point)\n",
        "\n",
        "**Write a regex pattern to extract dates in the format `MM/DD/YY` or `MM/DD/YYYY`.**\n",
        "\n",
        "Examples: `03/25/93`, `6/18/85`, `5/24/1990`, `1/25/2011`\n",
        "\n",
        "*This function should return a list of all matched date strings.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "igVIoT5NIRs-",
        "outputId": "1f7559f3-6f73-45c2-9e4f-9e021dece4c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 120 dates\n",
            "First 10: ['03/25/93', '6/18/85', '7/8/71', '9/27/75', '2/6/96', '7/06/79', '5/18/78', '10/24/89', '3/7/86', '4/10/71']\n"
          ]
        }
      ],
      "source": [
        "def question_one():\n",
        "    \"\"\"\n",
        "    Extract all dates in MM/DD/YY or MM/DD/YYYY format.\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b\\d{1,2}/\\d{1,2}/(?:\\d{2}|\\d{4})\\b'\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q1_result = question_one()\n",
        "print(f\"Found {len(q1_result)} dates\")\n",
        "print(f\"First 10: {q1_result[:10]}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_r76vw_iIRs-"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 2 (1 point)\n",
        "\n",
        "**Write a regex pattern to extract dates with month names.**\n",
        "\n",
        "Examples: `Mar-20-2009`, `March 20, 2009`, `Mar 20 2009`, `Mar. 20, 2009`\n",
        "\n",
        "*This function should return a list of all matched date strings.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dg-TNHanIRs_",
        "outputId": "80f7ac30-f5ca-43af-c60f-17c97d1e5376"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 34 dates\n",
            "First 10: ['April 11, 1990', 'May 30, 2001', 'Feb 18, 1994', 'February 18, 1981', 'October. 11, 2013', 'Jan 24 1986', 'July 26, 1978', 'December 23, 1999', 'May 15, 1989', 'September 06, 1995']\n"
          ]
        }
      ],
      "source": [
        "def question_two():\n",
        "    \"\"\"\n",
        "    Extract all dates with month names (e.g., Mar 20, 2009).\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\\.?\\s?-?\\s?\\d{1,2},?\\s?\\d{4}\\b'\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q2_result = question_two()\n",
        "print(f\"Found {len(q2_result)} dates\")\n",
        "print(f\"First 10: {q2_result[:10]}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "erP15jvyIRs_"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 3 (1 point)\n",
        "\n",
        "**Write a regex pattern to extract dates in the format `DD Month YYYY`.**\n",
        "\n",
        "Examples: `20 Mar 2009`, `20 March 2009`, `20 Mar. 2009`\n",
        "\n",
        "*This function should return a list of all matched date strings.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p9hfXCNXIRs_",
        "outputId": "34c24ed5-8984-4715-a5b3-5bf45abcb58c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 69 dates\n",
            "First 10: ['24 Jan 2001', '10 Sep 2004', '26 May 1982', '28 June 2002', '06 May 1972', '25 Oct 1987', '14 Oct 1996', '30 Nov 2007', '28 June 1994', '14 Jan 1981']\n"
          ]
        }
      ],
      "source": [
        "def question_three():\n",
        "    \"\"\"\n",
        "    Extract all dates in DD Month YYYY format.\n",
        "\n",
        "    Returns:\n",
        "        list: List of matched date strings\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b\\d{1,2}\\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\\.?\\s\\d{4}\\b'\n",
        "\n",
        "    results = []\n",
        "    for note in df:\n",
        "        matches = re.findall(pattern, note)\n",
        "        results.extend(matches)\n",
        "\n",
        "    return results\n",
        "\n",
        "# Test your function\n",
        "q3_result = question_three()\n",
        "print(f\"Found {len(q3_result)} dates\")\n",
        "print(f\"First 10: {q3_result[:10]}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EaX2U57eIRs_"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 4 (1 point)\n",
        "\n",
        "**Write a function that uses regex to extract all email addresses from a given text.**\n",
        "\n",
        "Test text is provided below.\n",
        "\n",
        "*This function should return a list of email addresses.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "POpwt6LGIRtA",
        "outputId": "7b954649-1a32-42a1-b6a3-b67f06b0f0a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found emails: ['support@company.com', 'sales@company.org', 'john.doe@email.co.uk', 'jane_doe123@university.edu']\n"
          ]
        }
      ],
      "source": [
        "def question_four(text):\n",
        "    \"\"\"\n",
        "    Extract all email addresses from text.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        list: List of email addresses\n",
        "    \"\"\"\n",
        "    # YOUR CODE HERE\n",
        "    pattern = r'\\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\\b'\n",
        "\n",
        "    return re.findall(pattern, text)\n",
        "\n",
        "# Test your function\n",
        "test_text = \"\"\"\n",
        "Contact us at support@company.com or sales@company.org.\n",
        "You can also reach john.doe@email.co.uk or jane_doe123@university.edu.\n",
        "Invalid emails: @invalid.com, user@, not-an-email\n",
        "\"\"\"\n",
        "\n",
        "q4_result = question_four(test_text)\n",
        "print(f\"Found emails: {q4_result}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "s4LfW6L_IRtA"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 5 (1 point)\n",
        "\n",
        "**Write a function that uses regex to clean text by:**\n",
        "1. Removing all digits\n",
        "2. Removing all punctuation except spaces\n",
        "3. Converting to lowercase\n",
        "4. Removing extra whitespace\n",
        "\n",
        "*This function should return the cleaned string.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rznrbM-TIRtA",
        "outputId": "ada7d87f-2862-45ae-b192-97c86d381d7a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original: 'Hello, World! 123 This is a TEST... with 456 numbers!!!'\n",
            "Cleaned:  'hello world this is a test with numbers'\n"
          ]
        }
      ],
      "source": [
        "def question_five(text):\n",
        "    \"\"\"\n",
        "    Clean text by removing digits, punctuation, and normalizing whitespace.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        str: Cleaned text\n",
        "    \"\"\"\n",
        "    text = re.sub(r'\\d+', '', text) # removing the digits\n",
        "\n",
        "    text = re.sub(r'[^\\w\\s]', '', text)# removing the punctuation\n",
        "\n",
        "    text = text.lower() # converting to lowercase\n",
        "\n",
        "    text = re.sub(r'\\s+', ' ', text).strip() # removing extra whitespace\n",
        "\n",
        "    return text  # Return cleaned text\n",
        "\n",
        "# Test your function\n",
        "test_text = \"Hello, World! 123 This is a TEST... with 456 numbers!!!\"\n",
        "q5_result = question_five(test_text)\n",
        "print(f\"Original: '{test_text}'\")\n",
        "print(f\"Cleaned:  '{q5_result}'\")\n",
        "# Expected: 'hello world this is a test with numbers'"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GyGPt3NKIRtA"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 6 (2 points)\n",
        "\n",
        "**Write a function that extracts and validates phone numbers.**\n",
        "\n",
        "Valid formats:\n",
        "- `XXX-XXX-XXXX`\n",
        "- `(XXX) XXX-XXXX`\n",
        "- `XXX.XXX.XXXX`\n",
        "- `XXX XXX XXXX`\n",
        "\n",
        "*This function should return a list of phone numbers in standardized format `XXX-XXX-XXXX`.*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iHFmz-ryIRtA",
        "outputId": "707967f8-5c54-4814-e1f4-3a5c76befbd8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found phones: ['123-456-7890', '555-123-4567', '888-555-1234', '999-888-7777']\n"
          ]
        }
      ],
      "source": [
        "def question_six(text):\n",
        "    \"\"\"\n",
        "    Extract phone numbers and return them in XXX-XXX-XXXX format.\n",
        "\n",
        "    Args:\n",
        "        text (str): Input text\n",
        "\n",
        "    Returns:\n",
        "        list: List of phone numbers in XXX-XXX-XXXX format\n",
        "    \"\"\"\n",
        "    def question_six(text):\n",
        "      \"\"\"\n",
        "    Extract phone numbers and return them in XXX-XXX-XXXX format.\n",
        "    \"\"\"\n",
        "\n",
        "    pattern = r'\\b\\d{3}-\\d{3}-\\d{4}\\b|\\(\\d{3}\\)\\s\\d{3}-\\d{4}|\\b\\d{3}\\.\\d{3}\\.\\d{4}\\b|\\b\\d{3}\\s\\d{3}\\s\\d{4}\\b'\n",
        "\n",
        "    matches = re.findall(pattern, text)\n",
        "\n",
        "    results = []\n",
        "    for m in matches:\n",
        "        digits = re.sub(r'\\D', '', m)\n",
        "        if len(digits) == 10:\n",
        "            results.append(f\"{digits[:3]}-{digits[3:6]}-{digits[6:]}\")\n",
        "\n",
        "    return results  # Return list of standardized phone numbers\n",
        "\n",
        "# Test your function\n",
        "test_text = \"\"\"\n",
        "Call us at 123-456-7890 or (555) 123-4567.\n",
        "You can also reach us at 888.555.1234 or 999 888 7777.\n",
        "Invalid: 12-34-5678, 1234567890\n",
        "\"\"\"\n",
        "\n",
        "q6_result = question_six(test_text)\n",
        "print(f\"Found phones: {q6_result}\")\n",
        "# Expected: ['123-456-7890', '555-123-4567', '888-555-1234', '999-888-7777']"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iNvbLSH2IRtB"
      },
      "source": [
        "---\n",
        "\n",
        "## Question 7 (3 points)\n",
        "\n",
        "**This is the main challenge: Extract all dates from the medical notes and sort them chronologically.**\n",
        "\n",
        "**Rules:**\n",
        "- Assume all dates in `xx/xx/xx` format are `mm/dd/yy`\n",
        "- Assume all 2-digit years are from the 1900s (e.g., `1/5/89` is January 5th, 1989)\n",
        "- If the day is missing (e.g., `9/2009`), assume it is the 1st day of the month\n",
        "- If the month is missing (e.g., `2010`), assume it is January 1st\n",
        "\n",
        "*This function should return a pandas Series of length 500, where the values are the original indices sorted by date in ascending chronological order.*\n",
        "\n",
        "**Example:**\n",
        "```python\n",
        "# If original series was:\n",
        "#    0    1999\n",
        "#    1    2010\n",
        "#    2    1978\n",
        "# Your function should return:\n",
        "#    0    2    (1978 is earliest)\n",
        "#    1    0    (1999 is second)\n",
        "#    2    1    (2010 is latest)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 46,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8zgU4OOTIRtB",
        "outputId": "e7f7dff7-c300-47ec-b922-4c3294a08aa7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result length: 500\n",
            "First 10 indices: [25, 39, 40, 71, 99, 466, 470, 481, 493, 9]\n",
            "Last 10 indices: [257, 152, 464, 253, 231, 427, 141, 186, 161, 413]\n"
          ]
        }
      ],
      "source": [
        "def question_seven():\n",
        "    \"\"\"\n",
        "    Extract dates from all medical notes and return indices sorted chronologically.\n",
        "\n",
        "    Returns:\n",
        "        pd.Series: Series of length 500 with original indices sorted by date\n",
        "    \"\"\"\n",
        "def question_seven():\n",
        "    month_re = r'(?:Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|Sept|September|Oct|October|Nov|November|Dec|December)'\n",
        "\n",
        "    patterns = [\n",
        "        ('mdy', re.compile(r'\\b\\d{1,2}/\\d{1,2}/\\d{2,4}\\b')),\n",
        "        ('my_num', re.compile(r'\\b\\d{1,2}/\\d{4}\\b')),\n",
        "        ('month_day_year', re.compile(rf'\\b{month_re}\\.?(?:[-\\s]+)\\d{{1,2}}(?:,)?(?:[-\\s]+)\\d{{4}}\\b', re.I)),\n",
        "        ('day_month_year', re.compile(rf'\\b\\d{{1,2}}(?:[-\\s]+){month_re}\\.?(?:,)?(?:[-\\s]+)\\d{{4}}\\b', re.I)),\n",
        "        ('month_year', re.compile(rf'\\b{month_re}\\.?(?:[-\\s]+)\\d{{4}}\\b', re.I)),\n",
        "        ('year', re.compile(r'\\b(?:19|20)\\d{2}\\b'))\n",
        "    ]\n",
        "\n",
        "    month_map = {\n",
        "        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,\n",
        "        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12\n",
        "    }\n",
        "\n",
        "    def parse_date(text, kind):\n",
        "        if kind == 'mdy':\n",
        "            m, d, y = text.split('/')\n",
        "            m, d, y = int(m), int(d), int(y)\n",
        "            if y < 100:\n",
        "                y += 1900\n",
        "            return datetime(y, m, d)\n",
        "\n",
        "        elif kind == 'my_num':\n",
        "            m, y = text.split('/')\n",
        "            return datetime(int(y), int(m), 1)\n",
        "\n",
        "        elif kind == 'month_day_year':\n",
        "            cleaned = re.sub(r'[,.]', '', text).replace('-', ' ')\n",
        "            parts = cleaned.split()\n",
        "            return datetime(int(parts[2]), month_map[parts[0][:3].lower()], int(parts[1]))\n",
        "\n",
        "        elif kind == 'day_month_year':\n",
        "            cleaned = re.sub(r'[,.]', '', text).replace('-', ' ')\n",
        "            parts = cleaned.split()\n",
        "            return datetime(int(parts[2]), month_map[parts[1][:3].lower()], int(parts[0]))\n",
        "\n",
        "        elif kind == 'month_year':\n",
        "            cleaned = re.sub(r'[,.]', '', text).replace('-', ' ')\n",
        "            parts = cleaned.split()\n",
        "            return datetime(int(parts[1]), month_map[parts[0][:3].lower()], 1)\n",
        "\n",
        "        else:\n",
        "            return datetime(int(text), 1, 1)\n",
        "\n",
        "    parsed = []\n",
        "\n",
        "    for idx, note in df.items():\n",
        "        matches = []\n",
        "\n",
        "        for order, (kind, pattern) in enumerate(patterns):\n",
        "            for match in pattern.finditer(note):\n",
        "                matches.append((match.start(), order, kind, match.group()))\n",
        "\n",
        "        if matches:\n",
        "            matches.sort(key=lambda x: (x[0], x[1]))\n",
        "            best_match = matches[0]\n",
        "            date_obj = parse_date(best_match[3], best_match[2])\n",
        "        else:\n",
        "            date_obj = datetime(1900, 1, 1)\n",
        "\n",
        "        parsed.append((idx, date_obj))\n",
        "\n",
        "    result = pd.DataFrame(parsed, columns=['index', 'date'])\n",
        "    result = result.sort_values('date', kind='mergesort')\n",
        "\n",
        "    return result['index'].reset_index(drop=True)# Return the sorted indices\n",
        "\n",
        "# Test your function\n",
        "q7_result = question_seven()\n",
        "print(f\"Result length: {len(q7_result)}\")\n",
        "print(f\"First 10 indices: {list(q7_result.head(10))}\")\n",
        "print(f\"Last 10 indices: {list(q7_result.tail(10))}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XV_yBuXhIRtB"
      },
      "source": [
        "---\n",
        "\n",
        "## Summary of Functions for Grading\n",
        "\n",
        "Make sure all these functions are properly implemented before exporting:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 47,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UnJQKJFSIRtB",
        "outputId": "a9497fff-7a1d-47af-d2a3-6a7446aac932"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Checking functions...\n",
            "✓ question_one: OK\n",
            "✓ question_two: OK\n",
            "✓ question_three: OK\n",
            "✓ question_four: OK\n",
            "✓ question_five: OK\n",
            "✓ question_six: OK\n",
            "✓ question_seven: OK\n",
            "\n",
            "Done! Export this notebook as .py file when all functions pass.\n"
          ]
        }
      ],
      "source": [
        "# Run this cell to verify all functions exist and return correct types\n",
        "print(\"Checking functions...\")\n",
        "\n",
        "try:\n",
        "    r1 = question_one()\n",
        "    assert isinstance(r1, list), \"question_one should return a list\"\n",
        "    print(\"✓ question_one: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_one: {e}\")\n",
        "\n",
        "try:\n",
        "    r2 = question_two()\n",
        "    assert isinstance(r2, list), \"question_two should return a list\"\n",
        "    print(\"✓ question_two: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_two: {e}\")\n",
        "\n",
        "try:\n",
        "    r3 = question_three()\n",
        "    assert isinstance(r3, list), \"question_three should return a list\"\n",
        "    print(\"✓ question_three: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_three: {e}\")\n",
        "\n",
        "try:\n",
        "    r4 = question_four(\"test@email.com\")\n",
        "    assert isinstance(r4, list), \"question_four should return a list\"\n",
        "    print(\"✓ question_four: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_four: {e}\")\n",
        "\n",
        "try:\n",
        "    r5 = question_five(\"Hello World 123\")\n",
        "    assert isinstance(r5, str), \"question_five should return a string\"\n",
        "    print(\"✓ question_five: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_five: {e}\")\n",
        "\n",
        "try:\n",
        "    r6 = question_six(\"123-456-7890\")\n",
        "    assert isinstance(r6, list), \"question_six should return a list\"\n",
        "    print(\"✓ question_six: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_six: {e}\")\n",
        "\n",
        "try:\n",
        "    r7 = question_seven()\n",
        "    assert isinstance(r7, pd.Series), \"question_seven should return a pandas Series\"\n",
        "    print(\"✓ question_seven: OK\")\n",
        "except Exception as e:\n",
        "    print(f\"✗ question_seven: {e}\")\n",
        "\n",
        "print(\"\\nDone! Export this notebook as .py file when all functions pass.\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x0_PsKmGIRtC"
      },
      "source": [
        "---\n",
        "\n",
        "## Submission Checklist\n",
        "\n",
        "- [ ] All 7 functions are implemented\n",
        "- [ ] All functions return the correct type\n",
        "- [ ] Notebook exported as Python file\n",
        "- [ ] File named: `LASTNAME_FIRSTNAME_assignment1_part1.py`\n",
        "- [ ] Pushed to GitHub repository\n",
        "- [ ] Sent to **yoroba93@gmail.com**"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "nlp-course",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.11.7"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}