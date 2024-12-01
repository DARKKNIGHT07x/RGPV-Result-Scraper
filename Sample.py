# res = driver.find_elements(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_pnlGrading"]/table/tbody/tr[3]/td/table')
# print(len(res))

# for i in range(2, len(res) + 1):
#     spa = '/html/body/form/div[3]/div/div[2]/table/tbody/tr[8]/td/div/table/tbody/tr[3]/td/table[' + str(i) + ']/tbody/tr'
#     sub1 = driver.find_element(By.XPATH, spa).text.replace(' ', '')
#     vpa = '/html/body/form/div[3]/div/div[2]/table/tbody/tr[8]/td/div/table/tbody/tr[3]/td/table[' + str(i) + ']/tbody/tr'
#     gra1 = driver.find_element(By.XPATH, vpa).text
#     tempList.update({sub1: gra1})

# tempList.update({"Result": (driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblResultNewGrading").text)})
# tempList.update({"SGPA": (driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblSGPA").text)})
# tempList.update({"CGPA": (driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblcgpa").text)})
# try:
#     tempList.update({"Division": (driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblDiv_Ssem").text)})
# except:
#     pass

# print(tempList)
