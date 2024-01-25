# Дан несложный пример HTML-страницы: Sample Web Page.

# Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта 
# (они заключены в теги <h3>).

# Ожидаемый результат:
# ['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', 
#  '4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables', 
#  '9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet', '11. Where to go from here', 
#  '12. Postscript: Cell Phones']

import requests
from bs4 import BeautifulSoup


def get_subheadings(url):
	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html.parser')

	subheadings = [heading.text.strip() for heading in soup.find_all('h3')]

	return subheadings



url = 'http://www.columbia.edu/~fdc/sample.html'


subheadings = get_subheadings(url)


print(subheadings)