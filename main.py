from bs4 import BeautifulSoup
import requests 
import pandas as pd
import lxml

def main():
    course_list = []
    uni_list = []
    links = []
    for page in range(201):
        link = f'https://www.studienwahl.at/studies/engineering-sciences/?page={page}&per-page=10'  
        http_request = requests.get(link).text
        soup = BeautifulSoup(http_request, 'lxml')
        boxes_even = soup.find_all('div', class_ = 'course even')
        boxes_odd = soup.find_all('div', class_ = 'course odd')
        for box in boxes_even:
            course = box.find('h2').text
            course_list.append(course)
            uni = box.find('p').text
            uni_list.append(uni)
        for box in boxes_odd:
            course = box.find('h2').text
            course_list.append(course)
            uni = box.find('p').text
            uni_list.append(uni)
        print(f'Scrapped page {page} of 200') 

    data_panda = {'Course' : course_list, 'University' : uni_list}
    df = pd.DataFrame(data_panda)
    df.to_csv('austria_course_list.csv')
    print('Completed, Saved Succesfully on hard disk')

if __name__ == '__main__':
    main()




