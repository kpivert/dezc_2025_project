# U.S. Physician and Surgeon Dashboard

Final Project for 2025 Cohort of the [DataTalksClub Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main)

## Motivation

## Data

Example API URL (with 2022 UUID)
https://data.cms.gov/data-api/v1/dataset/8889d81e-2ee7-448f-8713-f071038289b5/data

GET /dataset/{uuid}/data



[CMS API Documentation](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider/api-docs)

__Table 1: Available Years__

| Year | UUID                                   |
|---------|----------------------------------------|
| 2022    | 8568be52-dfc9-4fe0-b8d7-95838b3cd0c6  |
| 2021    | 1a3a5f39-09ac-48e2-b9bf-b371ac01c07e  |
| 2020    | 6c0feedd-12a5-401c-bd35-15fabcd6a334  |
| 2019    | 6859b742-ef67-4930-8262-03fb341001e2  |
| 2018    | 1d2877f2-2d19-454b-aee6-b0e657f9ad28  |
| 2017    | 6a4c7840-eb12-400d-ae3f-e33137e4f420  |
| 2016    | 373bec8b-d766-4201-9d8b-8f6577ff5828  |
| 2015    | 686ce936-9324-4241-ac00-fdab3b0b83ea  |
| 2014    | 6a5a5529-9b34-48b7-a576-8dad0b07e87b  |
| 2013    | 20f32dd0-a755-43cd-80bf-091a9200d2d0  |

<br>
__Table 2: Data Schema__

| Column                                    | Type    |
|-------------------------------------------|---------|
| Rndrng_NPI                                | TEXT    |
| Rndrng_Prvdr_Last_Org_Name                | TEXT    |
| Rndrng_Prvdr_First_Name                   | TEXT    |
| Rndrng_Prvdr_MI                           | TEXT    |
| Rndrng_Prvdr_Crdntls                      | TEXT    |
| Rndrng_Prvdr_Gndr                         | TEXT    |
| Rndrng_Prvdr_Ent_Cd                       | TEXT    |
| Rndrng_Prvdr_St1                          | TEXT    |
| Rndrng_Prvdr_St2                          | TEXT    |
| Rndrng_Prvdr_City                         | TEXT    |
| Rndrng_Prvdr_State_Abrvtn                 | TEXT    |
| Rndrng_Prvdr_State_FIPS                   | TEXT    |
| Rndrng_Prvdr_Zip5                         | TEXT    |
| Rndrng_Prvdr_RUCA                         | TEXT    |
| Rndrng_Prvdr_RUCA_Desc                    | TEXT    |
| Rndrng_Prvdr_Cntry                        | TEXT    |
| Rndrng_Prvdr_Type                         | TEXT    |
| Rndrng_Prvdr_Mdcr_Prtcptg_Ind             | TEXT    |
| Tot_HCPCS_Cds                             | TEXT    |
| Tot_Benes                                 | NUMERIC |
| Tot_Srvcs                                 | NUMERIC |
| Tot_Sbmtd_Chrg                            | NUMERIC |
| Tot_Mdcr_Alowd_Amt                        | NUMERIC |
| Tot_Mdcr_Pymt_Amt                         | NUMERIC |
| Tot_Mdcr_Stdzd_Amt                        | NUMERIC |
| Drug_Sprsn_Ind                            | TEXT    |
| Drug_Tot_HCPCS_Cds                        | NUMERIC |
| Drug_Tot_Benes                            | NUMERIC |
| Drug_Tot_Srvcs                            | NUMERIC |
| Drug_Sbmtd_Chrg                           | NUMERIC |
| Drug_Mdcr_Alowd_Amt                       | NUMERIC |
| Drug_Mdcr_Pymt_Amt                        | NUMERIC |
| Drug_Mdcr_Stdzd_Amt                       | NUMERIC |
| Med_Sprsn_Ind                             | TEXT    |
| Med_Tot_HCPCS_Cds                         | NUMERIC |
| Med_Tot_Benes                             | NUMERIC |
| Med_Tot_Srvcs                             | NUMERIC |
| Med_Sbmtd_Chrg                            | NUMERIC |
| Med_Mdcr_Alowd_Amt                        | NUMERIC |
| Med_Mdcr_Pymt_Amt                         | NUMERIC |
| Med_Mdcr_Stdzd_Amt                        | NUMERIC |
| Bene_Avg_Age                              | NUMERIC |
| Bene_Age_LT_65_Cnt                        | NUMERIC |
| Bene_Age_65_74_Cnt                        | NUMERIC |
| Bene_Age_75_84_Cnt                        | NUMERIC |
| Bene_Age_GT_84_Cnt                        | NUMERIC |
| Bene_Feml_Cnt                             | NUMERIC |
| Bene_Male_Cnt                             | NUMERIC |
| Bene_Race_Wht_Cnt                         | NUMERIC |
| Bene_Race_Black_Cnt                       | NUMERIC |
| Bene_Race_API_Cnt                         | NUMERIC |
| Bene_Race_Hspnc_Cnt                       | NUMERIC |
| Bene_Race_NatInd_Cnt                      | NUMERIC |
| Bene_Race_Othr_Cnt                        | NUMERIC |
| Bene_Dual_Cnt                             | NUMERIC |
| Bene_Ndual_Cnt                            | NUMERIC |
| Bene_CC_BH_ADHD_OthCD_V1_Pct              | NUMERIC |
| Bene_CC_BH_Alcohol_Drug_V1_Pct            | NUMERIC |
| Bene_CC_BH_Tobacco_V1_Pct                 | NUMERIC |
| Bene_CC_BH_Alz_NonAlzdem_V2_Pct           | NUMERIC |
| Bene_CC_BH_Anxiety_V1_Pct                 | NUMERIC |
| Bene_CC_BH_Bipolar_V1_Pct                 | NUMERIC |
| Bene_CC_BH_Mood_V2_Pct                    | NUMERIC |
| Bene_CC_BH_Depress_V1_Pct                 | NUMERIC |
| Bene_CC_BH_PD_V1_Pct                      | NUMERIC |
| Bene_CC_BH_PTSD_V1_Pct                    | NUMERIC |
| Bene_CC_BH_Schizo_OthPsy_V1_Pct           | NUMERIC |
| Bene_CC_PH_Asthma_V2_Pct                  | NUMERIC |
| Bene_CC_PH_Afib_V2_Pct                    | NUMERIC |
| Bene_CC_PH_Cancer6_V2_Pct                 | NUMERIC |
| Bene_CC_PH_CKD_V2_Pct                     | NUMERIC |
| Bene_CC_PH_COPD_V2_Pct                    | NUMERIC |
| Bene_CC_PH_Diabetes_V2_Pct                | NUMERIC |
| Bene_CC_PH_HF_NonIHD_V2_Pct               | NUMERIC |
| Bene_CC_PH_Hyperlipidemia_V2_Pct          | NUMERIC |
| Bene_CC_PH_Hypertension_V2_Pct            | NUMERIC |
| Bene_CC_PH_IschemicHeart_V2_Pct           | NUMERIC |
| Bene_CC_PH_Osteoporosis_V2_Pct            | NUMERIC |
| Bene_CC_PH_Parkinson_V2_Pct               | NUMERIC |
| Bene_CC_PH_Arthritis_V2_Pct               | NUMERIC |
| Bene_CC_PH_Stroke_TIA_V2_Pct              | NUMERIC |
| Bene_Avg_Risk_Scre                        | NUMERIC |

[__Data Dictionary__](https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-data-dictionary)

## Tools

## Pipeline
