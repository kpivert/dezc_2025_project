
import pandas as pd

df = pd.read_csv('./01_data/medicare_providers_csv_download_data.csv')
pd.set_option('display.max_colwidth', None)

print(df['downloadURL'])

"https://data.cms.gov/sites/default/files/2024-06/5aed74f7-d04e-48b4-93b3-d396a2e59c87/MUP_PHY_R24_P07_V10_D22_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/bc3a06d3-fdae-4cc0-b3ae-9738f3f0f8dc/MUP_PHY_R24_P07_V10_D21_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b75471cb-ca28-4a7f-93f4-69571b5fb605/MUP_PHY_R24_P07_V10_D20_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/940ed5c1-eee3-4b2a-bb9a-3626670c6cf0/MUP_PHY_R24_P07_V10_D19_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/9925fe87-8675-4fd7-8208-579654edf79f/MUP_PHY_R24_P07_V10_D18_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/14538846-95ce-4bfb-8183-33cdff149408/MUP_PHY_R24_P07_V10_D17_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b5b8f45d-869c-45f2-b2b4-b5d0d843c67e/MUP_PHY_R24_P05_V10_D16_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/403cf35f-148c-45af-9cc0-84abf111f286/MUP_PHY_R24_P05_V10_D15_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/98113a92-3a85-4c65-93fa-d3ede5fc9de9/MUP_PHY_R24_P05_V10_D14_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b42010e8-2029-4adc-b9ef-231d0fecb413/MUP_PHY_R24_P05_V10_D13_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/5aed74f7-d04e-48b4-93b3-d396a2e59c87/MUP_PHY_R24_P07_V10_D22_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/bc3a06d3-fdae-4cc0-b3ae-9738f3f0f8dc/MUP_PHY_R24_P07_V10_D21_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b75471cb-ca28-4a7f-93f4-69571b5fb605/MUP_PHY_R24_P07_V10_D20_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/940ed5c1-eee3-4b2a-bb9a-3626670c6cf0/MUP_PHY_R24_P07_V10_D19_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/9925fe87-8675-4fd7-8208-579654edf79f/MUP_PHY_R24_P07_V10_D18_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/14538846-95ce-4bfb-8183-33cdff149408/MUP_PHY_R24_P07_V10_D17_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b5b8f45d-869c-45f2-b2b4-b5d0d843c67e/MUP_PHY_R24_P05_V10_D16_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/403cf35f-148c-45af-9cc0-84abf111f286/MUP_PHY_R24_P05_V10_D15_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/98113a92-3a85-4c65-93fa-d3ede5fc9de9/MUP_PHY_R24_P05_V10_D14_Prov.csv",
"https://data.cms.gov/sites/default/files/2024-06/b42010e8-2029-4adc-b9ef-231d0fecb413/MUP_PHY_R24_P05_V10_D13_Prov.csv"