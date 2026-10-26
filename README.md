# Email to CSV

I built this to turn messy client messages into a clean spreadsheet. It reads the text, pulls out the important details with the Gemini API, and saves them as a CSV.

## Example

Input:

> Hi, this is Mike from Lone Star Print. Please send 40 flyers and 10 banners to Austin before March 3rd. Budget around $450. My number is (512) 555-0143. Thanks!

Output:

| company | city | items | date | budget | phone |
|---|---|---|---|---|---|
| Lone Star Print | Austin | 40 flyers and 10 banners | March 3rd | $450 | (512) 555-0143 |

## Run it

You need Python installed (python.org/downloads) and a free Gemini API key (aistudio.google.com).

1. Download this repo: click the green **Code** button, then **Download ZIP**, and unzip it
2. Open a terminal in that folder
3. Install what it needs: `pip install -r requirements.txt`
4. Create a file named `.env` in the folder, containing one line: `GEMINI_API_KEY=your_key`
5. Put your texts in `text.txt`, with `---` between them
6. Run: `python text_to_csv.py`
7. Your spreadsheet appears in the same folder as `orders.csv`
