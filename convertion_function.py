#!/usr/bin/env python
# coding: utf-8

# # GROUP 2 homework
# ## [1] With package 'requests' and some websites
# ### Here we use "https://v6.exchangerate-api.com"
# Data is updated everyday at ~00:00:02
# 
# Nous allons utiliser le USD comme devise de reference pour effectuer nos conversions
# 
# By: (Goro, Barro, Koanda, Konseibo)

# In[12]:


def convert(d_source='EUR', d_destin='XOF', amount=10, precision=2):
    """ This is a currency convertion function.
        Usage: convert(source='EUR', destination='XOF', amount=10, precision=2)
    """
    import requests
    from datetime import datetime as dt

    # Let's try to read data from the saved file containing today exchange
    try:
        with open('.conversion_rates.txt', 'r') as f:
            mybckp = eval(f.readlines()[0])
            last_update = mybckp.get('Update_time')
            last_update_utc = dt.strptime(last_update, "%Y%m%d%H%M%S")
            
            # let's check if date in the saved file is the latest
            past = int(last_update_utc.strftime("%Y%m%d"))
            now = int(dt.now().strftime("%Y%m%d"))
            if now > past:
                raise Exception("The saved data is obsolete")
            conversion_rates = mybckp.get("conversion_rates")
            
            # except ValueError
    except:
        print("execpt")
        # Making a request to https://v6.exchangerate-api.com
        url = 'https://v6.exchangerate-api.com/v6/dea91294134d2f7b96e8c2b3/latest/USD'
        response = requests.get(url)
        data = response.json()
        conversion_rates = data.get('conversion_rates')
        last_update_utc = dt.strptime(data.get('time_last_update_utc'), "%a, %d %b %Y %H:%M:%S %z")
        #last_update_unix = data.get('time_last_update_unix')
        #last_update_unix_unit = "seconds since 1970-01-01 00:00:00 UTC"
        
        # let's update data in the backup file
        date_to_write_in_file = dt.strftime(last_update_utc, "'Update_time': '%Y%m%d%H%M%S'")
        #print(date_to_write_in_file)
        with open('.conversion_rates.txt', 'w') as f:
            f.write("{" + date_to_write_in_file + ", ")
            f.write("'conversion_rates':")
            f.write(str(conversion_rates))
            f.write("}")
        
    # data is in JSON format i.e a dictionary
    #print(data)
    last_update_date = dt.strftime(last_update_utc, "%d/%m/%Y")
    last_update_time = dt.strftime(last_update_utc, "%H:%M:%S UTC")
    
    # rate between USD and source/destination currencies
    rate_USD_source = conversion_rates.get(d_source)
    rate_USD_destin = conversion_rates.get(d_destin)
    
    # rate between source and destination currencies
    rate_source_destin = float(rate_USD_destin) / float(rate_USD_source)
    rate_source_destin_rounded = round(rate_source_destin, precision)
    amount_converted = amount * rate_source_destin
    amount_converted_rounded = round(amount_converted, precision)
    
    print(" 1", d_source, "=", rate_source_destin_rounded, d_destin, "\n")
    print(amount, d_source, "=", amount_converted_rounded, d_destin, "\n")
    print("Updated on", last_update_date, "at", last_update_time)
    
    return amount_converted, rate_source_destin, last_update_date, last_update_time
    #return amount_converted_rounded, rate_source_destin_rounded, last_update_date, last_update_time


# In[13]:


#hello1, hello2, hello3, hello4 = convert()
_ = convert('USD', 'XOF', 50, 5)
#print()


# In[16]:





# In[ ]:




