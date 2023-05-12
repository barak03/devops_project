import MainScores
from bs4 import BeautifulSoup


def test_scores_service():
    soup = BeautifulSoup(MainScores.score_server(), 'html.parser')
    element = soup.find(id='score')
    if element:
        element_text = int(element.text)
        return 1 <= element_text <= 1000


def main_function():
    return 0 if test_scores_service() else -1


main_function()
