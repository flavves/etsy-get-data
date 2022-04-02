# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 03:01:10 2022

@author: okmen
"""

#https://www.etsy.com/listing/1160227254/leather-car-mats-for-mercedes?variation0=2475232049&variation1=2475232051

variant_1_uzunluk=driver.find_element_by_xpath('//*[@id="variation-selector-0"]').text
variant_1_uzunluk=variant_1_uzunluk.split("\n")
variant_1_uzunluk.pop(0)
variant_1_uzunluk.pop(-1)
variant_1_uzunluk=len(variant_1_uzunluk)


variant_2_uzunluk=driver.find_element_by_xpath('//*[@id="variation-selector-1"]').text
variant_2_uzunluk=variant_2_uzunluk.split("\n")
variant_2_uzunluk.pop(0)
variant_2_uzunluk.pop(-1)
variant_2_uzunluk=len(variant_2_uzunluk)






        try:                                                                    
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/p'))
            )
        finally:
            pass
        
        
        try:
            try:
                element = WebDriverWait(driver, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/p'))
                )
            finally:
                pass
            
            driver.find_element_by_xpath('//*[@id="variation-selector-0"]/option['+varyasyon1_sayac+']').click()
            variant_1=driver.find_element_by_xpath('//*[@id="variation-selector-0"]/option['+varyasyon1_sayac+']').text
        except:
            varyasyon2_sayac=varyasyon2_sayac+1
            varyasyon1_sayac=2
        
        varyasyon1_sayac=varyasyon1_sayac+1
        
        
        try:
            element = WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="variation-selector-1"]/option['+varyasyon2_sayac+']'))
            )
            varyasyon2_var_mi=True
        finally:
            pass
        
        if varyasyon2_var_mi==True:
            try:
                
                    
                driver.find_element_by_xpath('//*[@id="variation-selector-1"]/option['+varyasyon2_sayac+']').click()
                variant_2=driver.find_element_by_xpath('//*[@id="variation-selector-1"]/option['+varyasyon2_sayac+']').text
            except:
                varyasyon2_sayac=2
                
        