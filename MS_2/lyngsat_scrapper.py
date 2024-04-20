import re
import requests
from bs4 import BeautifulSoup
import csv
from faker import Faker
import random
import time
import pandas as pd

# ----- HELPER FUNCTIONS ------
def scrape_region_link():
    # URL of the Lyngsat page containing satellite information
    url = 'https://www.lyngsat.com'

    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    Main_table = soup.find('table', {'width': '468', 'cellspacing': '0', 'border': '1', 'cellpadding': '2',
                                          'bgcolor': 'lightyellow'})
    if Main_table:
        second_row = Main_table.find_all('tr')[1]  # Select the second row
        cells = second_row.find_all('td')[1:5]  # Select the first four cells starting from the second column
        links = []  # List to store the extracted links
        for cell in cells:
            link = cell.find('a')
            if link:
                link_href = link.get('href')  # Extract the value of the 'href' attribute
                links.append(link_href)
        return links
    else:
        print("Satellite table not found.")
        return []
def scrape_Sattrack_link():
    # URL of the Lyngsat page containing satellite information
    links = scrape_region_link()
    all_sat_links = []  # List to store all satellite links

    # Iterate through each link
    for link in links:
        # URL of the Lyngsat page containing satellite information for the current region
        sat_url = f'https://www.lyngsat.com/tracker/{link}'


        response = requests.get(sat_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        Sat_table = soup.find('table', {'align': 'center', 'width': '720'})

        if Sat_table:
            nested_tables = Sat_table.find_all('td', {'align': 'center', 'valign': 'top'})

            # If the nested table is found
            for nested_table in nested_tables:
                child_table = nested_table.find('table', {'cellspacing': '0'})
                rows = child_table.find_all('tr')
                # Iterate through each row
                for row_index, row in enumerate(rows):
                    # Extract cells within the row
                    cells = row.find_all('td')
                    # Check if the number of cells is greater than 1 to ensure there is a second column
                    if len(cells) > 1:
                        rowspan = int(cells[0].get('rowspan', 1))
                        # Extract link from the second column
                        link_cell = cells[1].find('a')
                        if link_cell:
                            link_href = link_cell.get('href')  # Extract the value of the 'href' attribute
                            all_sat_links.append(link_href)
                        if rowspan > 1:
                            for idx in range(row_index + 1, row_index + rowspan):
                                next_row = rows[idx]
                                next_cell = next_row.find_all('td')[0]
                                link_cell = next_cell.find('a')
                                if link_cell:
                                    link_href = link_cell.get('href')  # Extract the value of the 'href' attribute
                                    all_sat_links.append(link_href)


    return all_sat_links
def scrape_Sat_link():
    # URL of the Lyngsat page containing satellite information
    links = scrape_region_link()
    all_sat_links = []  # List to store all satellite links

    # Iterate through each link
    for link in links:
        # URL of the Lyngsat page containing satellite information for the current region
        sat_url = f'https://www.lyngsat.com/{link}'

        response = requests.get(sat_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        Sat_table = soup.find('table', {'align': 'center', 'width': '720'})

        if Sat_table:
            nested_tables = Sat_table.find_all('td', {'align': 'center', 'valign': 'top'})

            # If the nested table is found
            for nested_table in nested_tables:
                child_table = nested_table.find('table', {'cellspacing': '0'})
                rows = child_table.find_all('tr')
                # Iterate through each row
                for row_index, row in enumerate(rows):
                    # Extract cells within the row
                    cells = row.find_all('td')
                    # Check if the number of cells is greater than 1 to ensure there is a second column
                    if len(cells) > 1:
                        rowspan = int(cells[0].get('rowspan', 1))
                        # Extract link from the second column
                        link_cell = cells[1].find('a')
                        if link_cell:
                            link_href = link_cell.get('href')  # Extract the value of the 'href' attribute
                            all_sat_links.append(link_href)
                        if rowspan > 1:
                            for idx in range(row_index + 1, row_index + rowspan):
                                next_row = rows[idx]
                                next_cell = next_row.find_all('td')[0]
                                link_cell = next_cell.find('a')
                                if link_cell:
                                    link_href = link_cell.get('href')  # Extract the value of the 'href' attribute
                                    all_sat_links.append(link_href)


    return all_sat_links
def get_package():
    package_links = set()
    region_link = scrape_region_link()
    for r_link in region_link:
        pack_link = f'https://www.lyngsat.com/packages/{r_link}'
        # Fetch the webpage
        response = requests.get(pack_link)

        soup = BeautifulSoup(response.text, 'html.parser')

        target_table = soup.find('table', {'align': 'center', 'width': '720'})
        if target_table:
            table = target_table.find('td', {'valign' : 'top', 'align' : 'center'})
            if table:
                rows = table.find_all('tr')
                if rows:
                    for row in rows:
                        # Find all <a> tags with 'href' attribute containing 'packages'
                        a_tags = row.find_all('a', href=lambda href: href and 'packages' in href.lower())
                        for a_tag in a_tags:
                            link = a_tag.get('href')
                            if link not in package_links:
                                package_links.add(link)
    return package_links
def get_channel_link():
    channel_links = set()
    sat_links = scrape_Sat_link()
    for link in sat_links:
        sat_url = f'https://www.lyngsat.com/{link}'

        # Fetch the webpage
        response = requests.get(sat_url)

        soup = BeautifulSoup(response.text, 'html.parser')
        # Search for tables with certain attributes
        tables = soup.find_all('table', {'width': '720', 'cellspacing': '0', 'cellpadding': '0'})

        if tables:
            for table in tables:
                rows = table.find_all('tr')
                if len(rows) > 2:
                    for row in rows[2:]:
                        cols = row.find_all('td')
                        if len(cols) >= 4:
                            # Find all <a> tags with 'href' attribute containing 'tvchannel'
                            a_tags = row.find_all('a', href=lambda href: href and 'tvchannel' in href.lower())
                            for a_tag in a_tags:
                                link = a_tag.get('href')
                                if link not in channel_links:
                                    channel_links.add(link)
    return channel_links
def get_channel_package_links():
    channel_links = set()
    pack_links = get_package()
    for p_link in pack_links:
        response = requests.get(p_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', {'width': '720', 'cellspacing': '0', 'cellpadding': '0'})
        if tables:
            for table in tables:
                rows = table.find_all('tr')
                if len(rows) > 2:
                    for row in rows[2:]:
                        cols = row.find_all('td')
                        if len(cols) >= 4:
                            # Find all <a> tags with 'href' attribute containing 'tvchannel'
                            a_tags = row.find_all('a', href=lambda href: href and 'tvchannel' in href.lower())
                            for a_tag in a_tags:
                                link = a_tag.get('href')
                                if link not in channel_links:
                                    channel_links.add(link)
    return channel_links

# ----- SCRAPPING FUNCTIONS ------
def scrape_satellite():
    # Get the extracted links
    links = scrape_region_link()
    sat_links = scrape_Sattrack_link()
    rockets = []
    dates = []
    sat_info_list = []
    for link in sat_links:
        sat_url = link

        # Fetch the webpage for the current region
        response = requests.get(sat_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        font_tags = soup.find_all('font', face='Arial', size='2')

        for font_tag in font_tags:
            text = font_tag.get_text().strip()
            if 'was launched with' in text:
                # Extracting the rocket name
                rocket_match = re.search(r'was launched with (.+?) (\d{4}-\d{2}-\d{2})', text)
                if rocket_match:
                    rocket_name = re.sub(r'/.*', '', rocket_match.group(1))
                    launch_date = rocket_match.group(2)
                    rockets.append(rocket_name)
                    dates.append(launch_date)
    # Open a CSV file to store the data
    with open('Satellite.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['Satellite Position Longitude', 'Satellite Position Hemisphere', 'Satellite Name', 'Region', 'Launch Date',
             'Launching Rocket'])

        # Iterate through each link
        for link in links:
            # URL of the Lyngsat page containing satellite information for the current region
            region_url = f'https://www.lyngsat.com/tracker/{link}'

            # Fetch the webpage for the current region
            response = requests.get(region_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the target <td> tag containing the desired table
            target_td = soup.find('table', {'align': 'center', 'width': '720'})

            # If the target <td> tag is found
            if target_td:
                # Find the nested table within the target <td> tag
                nested_tables = target_td.find_all('td', {'align': 'center', 'valign': 'top'})

                # If the nested table is found
                for nested_table in nested_tables:

                    child_table = nested_table.find('table', {'cellspacing': '0'})
                    # Find all rows within the nested table
                    rows = child_table.find_all('tr')

                    # Find the region
                    region_font = soup.find('font', {'face': 'Arial', 'size': '5'})
                    if region_font:
                        region_txt = region_font.text.strip().split('-')
                        region = region_txt[1].replace(',', ' &')
                    else:
                        region = "NULL"

                    # Iterate through each row
                    for row_index, row in enumerate(rows):
                        # Extract cells within the row
                        cells = row.find_all('td')
                        if len(cells) == 4:
                            # Extract satellite position and name
                            position_cell = cells[0]
                            rowspan = int(position_cell.get('rowspan', 1))  # Get rowspan attribute, default to 1
                            position_info = position_cell.text.strip().replace('°', '°,').split(',')
                            position_longitude = position_info[0]
                            position_hemisphere = position_info[1].strip() if len(position_info) > 1 else ''

                            name_cell = cells[1]
                            name_notclean = name_cell.text.strip()
                            name_clean = re.sub(r' \(incl\..*?\)', '', name_notclean)  # removing incline information
                            if '/' in name_clean:
                                name = name_clean.replace('/',
                                                          ' (') + ')'  # replacing / so all names follow the same format
                            else:
                                name = name_clean  # name attribute containts the name and other names in ()

                            sat_info = (position_longitude, position_hemisphere, name, region)
                            sat_info_list.append(sat_info)

                            # If rowspan is greater than 1, get names from subsequent rows
                            if rowspan > 1:
                                for idx in range(row_index + 1, row_index + rowspan):
                                    next_row = rows[idx]
                                    next_name_cell = next_row.find_all('td')[0]
                                    name_notclean = next_name_cell.text.strip()
                                    name_clean = re.sub(r' \(incl\..*?\)', '',
                                                        name_notclean)  # removing incline information
                                    if '/' in name_clean:
                                        name = name_clean.replace('/',
                                                                  ' (') + ')'  # replacing / so all names follow the same format
                                    else:
                                        name = name_clean  # name attribute containts the name and other names in ()

                                    sat_info = (position_longitude, position_hemisphere, name, region)
                                    sat_info_list.append(sat_info)

        for sat_info, date, rocket in zip(sat_info_list, dates, rockets):
            # Write each sat_info tuple along with date and rocket to CSV
            writer.writerow(sat_info + (date, rocket))
def scrape_Network():
    sat_links = scrape_Sat_link()
    unique_providers = set()

    with open('Networks.csv', 'w', newline='', encoding='utf-8') as csvfile_network:
        writer_network = csv.writer(csvfile_network)
        writer_network.writerow(['Network Name'])

        for link in sat_links:
            sat_url = f'https://www.lyngsat.com/{link}'
            # Fetch the webpage for the current region
            response = requests.get(sat_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for tables with certain attributes
            tables = soup.find_all('table', {'width': '720', 'cellspacing': '0', 'cellpadding': '0'})

            if tables:
                for table in tables:
                    rows = table.find_all('tr')
                    if len(rows) > 2:
                        for row in rows[2:]:
                            cols = row.find_all('td')[3:]
                            if len(cols) >= 4:
                                # Find all <a> tags within the current row
                                a_tags = row.find_all('a')
                                for a_tag in a_tags:
                                    if 'provider' in a_tag.get('href', '').lower():
                                        provider_name = a_tag.text.strip()
                                        if provider_name and provider_name not in unique_providers:
                                            unique_providers.add(provider_name)
                                            writer_network.writerow([provider_name])
def scrape_channel_network():
    channels = set()
    sat_links = scrape_Sat_link()
    print('start1')
    with open('Channels.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer_channels = csv.writer(csvfile)
        writer_channels.writerow(['Channel Name', 'Network Name'])

        for link in sat_links:
            sat_url = f'https://www.lyngsat.com/{link}'

            # Fetch the webpage
            response = requests.get(sat_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for tables with certain attributes
            tables = soup.find_all('table', {'width': '720', 'cellspacing': '0', 'cellpadding': '0'})

            if tables:
                for table in tables:
                    rows = table.find_all('tr')
                    if len(rows) > 2:
                        for row_idx, row in enumerate(rows):
                            cols = row.find_all('td')
                            cols_tst = row.find('td', {'width': '52'})
                            if len(cols) >= 4:
                                if cols[0] == cols_tst:
                                    # Rowspan exists, find the provider
                                    if row_idx > 0:
                                        prev_row = rows[row_idx - 1]
                                        provider_tag = prev_row.find('a',
                                                                     href=lambda href: href and 'provider' in href.lower())
                                        if provider_tag:
                                            provider_name = provider_tag.text.strip()
                                else:
                                    provider_name = ''
                                    # Write the channel and its network name to the CSV file

                                # Find all <a> tags within the current row
                                a_tags = row.find_all('a')
                                for a_tag in a_tags:
                                    if 'tvchannel' in a_tag.get('href', '').lower():
                                        channel_name = a_tag.text.strip()
                                        if channel_name:
                                            if channel_name not in channels:
                                                channels.add(channel_name)
                                                print('benekteb 1')
                                                writer_channels.writerow([channel_name, provider_name])
    return channels
def scrape_channel_network_2(channels):
    package_links = get_package()
    with open('Channels.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer_channels = csv.writer(csvfile)

        print('start2')

        for link in package_links:
            print('channel network')
            # Fetch the webpage
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for tables with certain attributes
            tables = soup.find_all('table', {'width': '720', 'cellspacing': '0', 'cellpadding': '0'})

            if tables:
                for table in tables:
                    rows = table.find_all('tr')
                    if len(rows) > 2:
                        for row in rows[2:]:
                            cols = row.find_all('td')
                            if len(cols) >= 4:
                                # Find all <a> tags within the current row
                                a_tags = row.find_all('a')
                                for a_tag in a_tags:
                                    if 'tvchannel' in a_tag.get('href', '').lower():
                                        channel_name = a_tag.text.strip()
                                        if channel_name:
                                            if channel_name not in channels:
                                                channels.add(channel_name)
                                                #package channels do not have a provider
                                                print('benekteb2')
                                                writer_channels.writerow([channel_name, ''])
def scrape_channel_1():

    unique_channels = set()
    channel_links = get_channel_link()
    count = 0

    print('started...')

    with open('Broadcast.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer_broadcast = csv.writer(csvfile)
        writer_broadcast.writerow(['Satellite Name', 'Channel Name', 'Beam', 'Freq. Num', 'Freq. Polarisation', 'SR', 'FEC','System Standard', 'System Modulation', 'Video Compression', 'Video Definition'])

        with open('Channel_Language.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer_lang = csv.writer(csvfile)
            writer_lang.writerow(['Satellite Name', 'Channel Name', 'Language'])

            with open('Channel_Encryption.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer_enc = csv.writer(csvfile)
                writer_enc.writerow(['Satellite Name', 'Channel Name', 'Encryption'])

                for link in channel_links:
                    print('loop')
                    response = requests.get(link)
                    soup = BeautifulSoup(response.text, 'html.parser')



                    # Check if link count is a multiple of 10,000
                    if count % 10000 == 0:
                        time.sleep(random.randint(1, 3))  # Add sleep after every 10,000 links

                    # Get the channel
                    channel_font = soup.find('font', {'face': 'Arial', 'size': '5'})
                    if channel_font:
                        channel_name = channel_font.text.strip().replace(',', ' &')
                    else:
                        channel_name = "NULL"
                    table = soup.find('table',{'width' : '700', 'cellpadding' : '0', 'cellspacing' : '0', 'border' : '1'})
                    if table:
                        rows = table.find_all('tr')
                        if len(rows) > 2:
                            for row in rows[2:]:
                                cols = row.find_all('td')
                                if len(cols) >= 4:

                                    name_notclean = cols[1].text.strip()
                                    name_clean = re.sub(r' \(incl\..*?\)', '',
                                                        name_notclean)  # removing incline information
                                    if '/' in name_clean:
                                        sat_name = name_clean.replace('/',
                                                                      ' (') + ')'  # replacing / so all names follow the same format
                                    else:
                                        sat_name = name_clean  # name attribute containts the name and other names in ()
                                    beam_txt = cols[2]
                                    beam_t = beam_txt.find_all('br')
                                    for br in beam_t:
                                        br.replace_with('\n')
                                    beams = beam_txt.text.strip().split('\n')
                                    beam = beams[0]
                                    freq_txt = cols[3]
                                    freq = freq_txt.text.strip().split()
                                    if freq[0].isdigit():
                                        freq_num = freq[0]
                                    else:
                                        continue
                                    if len(freq) >= 2:
                                        freq_pol = freq[1]
                                    else:
                                        freq_pol = ''
                                    sys_txt = cols[4]
                                    system_txt = sys_txt.find_all('br')
                                    for br in system_txt:
                                        br.replace_with('\n')
                                    system = sys_txt.text.strip().split('\n')
                                    sys_stand = system[0]
                                    if len(system) >= 2:
                                        sys_mod = system[1]
                                    else:
                                        sys_mod = ''

                                    video_txt = cols[6]
                                    video_new = video_txt.find_all('br')
                                    for br in video_new:
                                        br.replace_with('/')
                                    video = video_txt.text.strip().split('/')
                                    video_comp = video[0]
                                    if len(video) >= 2:
                                        video_def = video[1]
                                    else:
                                        video_def = ''

                                    sr_fec_txt = cols[5]
                                    srfec_txt = sr_fec_txt.find_all('br')
                                    for br in srfec_txt:
                                        br.replace_with('\n')
                                    sr_fec = sr_fec_txt.text.strip().split('\n')
                                    sr = sr_fec[0]
                                    if len(sr_fec) >= 2:
                                        fec = sr_fec[1]
                                    else:
                                        fec = ''

                                    # Check for duplicates
                                    channel_key = (sat_name, channel_name, freq_num, freq_pol, video_comp, video_def)
                                    if channel_key in unique_channels:
                                        continue  # Skip duplicate channel
                                    unique_channels.add(channel_key)

                                    print('write broadcast')
                                    # Increment link count
                                    count += 1
                                    writer_broadcast.writerow(
                                        [sat_name, channel_name, beam, freq_num, freq_pol, sr, fec, sys_stand, sys_mod,
                                         video_comp, video_def])

                                    print('write el ba2y..')

                                    lang_txt = cols[7]
                                    lang_l = lang_txt.find_all('br')
                                    for br in lang_l:
                                        br.replace_with('\n')
                                    lang_not_clean = lang_txt.text.strip()
                                    lang_p = re.sub(r'\d+', '', lang_not_clean)
                                    for lang_part in re.findall(r'\w+', lang_p):
                                        lang = lang_part.capitalize()
                                        writer_lang.writerow([sat_name, channel_name, lang])

                                    encry = cols[8]
                                    # Split encryption text by <br> tag
                                    encryption_lines = encry.find_all('br')
                                    for br in encryption_lines:
                                        br.replace_with('\n')
                                    encryption = encry.text.strip()
                                    # Split encryption text by newline characters
                                    encryption_types = encryption.split('\n')
                                    for enc_type in encryption_types:
                                        enc_type = re.sub(r'\W+', '', enc_type)
                                        if enc_type:
                                            writer_enc.writerow([sat_name, channel_name, enc_type])
def scrape_channel_2():

    unique_channels = set()
    channel_links = get_channel_package_links()
    count = 0

    print('started..2.')

    with open('Broadcast.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer_broadcast = csv.writer(csvfile)

        with open('Channel_Language.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer_lang = csv.writer(csvfile)

            with open('Channel_Encryption.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer_enc = csv.writer(csvfile)

                for link in channel_links:
                    print('loop2')
                    response = requests.get(link)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Increment link count


                    # Check if link count is a multiple of 10,000
                    if count % 10000 == 0:
                        time.sleep(random.randint(2, 3))  # Add sleep after every 10,000 links

                    # Get the channel
                    channel_font = soup.find('font', {'face': 'Arial', 'size': '5'})
                    if channel_font:
                        channel_name = channel_font.text.strip().replace(',', ' &')
                    else:
                        channel_name = "NULL"
                    table = soup.find('table',{'width' : '700', 'cellpadding' : '0', 'cellspacing' : '0', 'border' : '1'})
                    if table:
                        rows = table.find_all('tr')
                        if len(rows) > 2:
                            for row in rows[2:]:
                                cols = row.find_all('td')
                                if len(cols) >= 4:

                                    name_notclean = cols[1].text.strip()
                                    name_clean = re.sub(r' \(incl\..*?\)', '',
                                                        name_notclean)  # removing incline information
                                    if '/' in name_clean:
                                        sat_name = name_clean.replace('/',
                                                                      ' (') + ')'  # replacing / so all names follow the same format
                                    else:
                                        sat_name = name_clean  # name attribute containts the name and other names in ()
                                    beam_txt = cols[2]
                                    beam_t = beam_txt.find_all('br')
                                    for br in beam_t:
                                        br.replace_with('\n')
                                    beams = beam_txt.text.strip().split('\n')
                                    beam = beams[0]
                                    freq_txt = cols[3]
                                    freq = freq_txt.text.strip().split()
                                    if freq[0].isdigit():
                                        freq_num = freq[0]
                                    else:
                                        continue
                                    if len(freq) >= 2:
                                        freq_pol = freq[1]
                                    else:
                                        freq_pol = ''
                                    sys_txt = cols[4]
                                    system_txt = sys_txt.find_all('br')
                                    for br in system_txt:
                                        br.replace_with('\n')
                                    system = sys_txt.text.strip().split('\n')
                                    sys_stand = system[0]
                                    if len(system) >= 2:
                                        sys_mod = system[1]
                                    else:
                                        sys_mod = ''

                                    video_txt = cols[6]
                                    video_new = video_txt.find_all('br')
                                    for br in video_new:
                                        br.replace_with('/')
                                    video = video_txt.text.strip().split('/')
                                    video_comp = video[0]
                                    if len(video) >= 2:
                                        video_def = video[1]
                                    else:
                                        video_def = ''

                                    sr_fec_txt = cols[5]
                                    srfec_txt = sr_fec_txt.find_all('br')
                                    for br in srfec_txt:
                                        br.replace_with('\n')
                                    sr_fec = sr_fec_txt.text.strip().split('\n')
                                    sr = sr_fec[0]
                                    if len(sr_fec) >= 2:
                                        fec = sr_fec[1]
                                    else:
                                        fec = ''

                                    # Check for duplicates
                                    channel_key = (sat_name, channel_name, freq_num, freq_pol, video_comp, video_def)
                                    if channel_key in unique_channels:
                                        continue  # Skip duplicate channel
                                    unique_channels.add(channel_key)

                                    print('write broadcast2')
                                    count += 1

                                    writer_broadcast.writerow(
                                        [sat_name, channel_name, beam, freq_num, freq_pol, sr, fec, sys_stand, sys_mod,
                                         video_comp, video_def])

                                    print('write el ba2y.2.')

                                    lang_txt = cols[7]
                                    lang_l = lang_txt.find_all('br')
                                    for br in lang_l:
                                        br.replace_with('\n')
                                    lang_not_clean = lang_txt.text.strip()
                                    lang_p = re.sub(r'\d+', '', lang_not_clean)
                                    for lang_part in re.findall(r'\w+', lang_p):
                                        lang = lang_part.capitalize()
                                        writer_lang.writerow([sat_name, channel_name, lang])

                                    encry = cols[8]
                                    # Split encryption text by <br> tag
                                    encryption_lines = encry.find_all('br')
                                    for br in encryption_lines:
                                        br.replace_with('\n')
                                    encryption = encry.text.strip()
                                    # Split encryption text by newline characters
                                    encryption_types = encryption.split('\n')
                                    for enc_type in encryption_types:
                                        enc_type = re.sub(r'\W+', '', enc_type)
                                        if enc_type:
                                            writer_enc.writerow([sat_name, channel_name, enc_type])
def generate_fake_data(num_users=20, channels_csv='Channels.csv'):
    # Initialize Faker generator
    fake = Faker()

    # Read list of channels from CSV
    with open(channels_csv, 'r', newline='', encoding='utf-8') as channels_file:
        channels_reader = csv.reader(channels_file)
        channels_list = [row[0] for row in channels_reader]

    # Generate fake users
    fake_users = []
    for _ in range(num_users):
        email = fake.email()
        username = fake.user_name()
        gender = fake.random_element(elements=('M', 'F'))
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        region = fake.random_element(elements=('North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania'))
        location = fake.country()


        fake_users.append((email, username, gender, birthdate, region, location))

    # Write fake users to CSV
    with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['email', 'username', 'gender', 'birthdate', 'region', 'location'])
        writer.writerows(fake_users)

    # Generate favorite channels for each user
    with open('favorites.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_email', 'channel_name'])
        for user in fake_users:
            user_email = user[0]
            # Generate favorite channels for each user
            num_favorites = random.randint(1, 10)
            favorite_channels = random.sample(channels_list, num_favorites)

            for channel in favorite_channels:
                writer.writerow([user_email, channel])






if __name__ == "__main__":
    #Start Scrapping
    scrape_satellite()
    scrape_Network()
    scrape_channel_1()
    scrape_channel_2()
    generate_fake_data()
    c = scrape_channel_network()
    scrape_channel_network_2(c)


    # Handeling all the duplicates again because of inconsistencies:
    # Read the CSV file
    df = pd.read_csv('Broadcast_x.csv')

    # Remove duplicates based on specific columns (e.g., 'column_name')
    df_unique = df.drop_duplicates(subset=['Satellite Name', 'Channel Name', 'Beam', 'Freq. Num', 'Freq. Polarisation', 'SR', 'FEC','System Standard', 'System Modulation', 'Video Compression', 'Video Definition'])

    # Write the unique rows to a new CSV file
    df_unique.to_csv('Broadcast.csv', index=False)

    # Read the CSV file
    df = pd.read_csv('Channel_Encryption.csv')

    # Remove duplicates based on specific columns (e.g., 'column_name')
    df_unique = df.drop_duplicates(
        subset=['Satellite Name', 'Channel Name', 'Encryption'])

    # Write the unique rows to a new CSV file
    df_unique.to_csv('Channel_Encryptions.csv', index=False)

    # Read the CSV file
    df = pd.read_csv('Channel_Language.csv')

    # Remove duplicates based on specific columns (e.g., 'column_name')
    df_unique = df.drop_duplicates(
        subset=['Satellite Name', 'Channel Name', 'Language'])

    # Write the unique rows to a new CSV file
    df_unique.to_csv('Channel_Languages.csv', index=False)























