# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

sns.set_style('white')


##############################################################################
#################### Creative Achievement Questionnaire ######################
##############################################################################

def run_CAQ(df, out_dir, public):
    
    cols = ["QACa_QACa1","QACa_QACa2","QACa_QACa3","QACa_QACa4","QACa_QACa5","QACa_QACa6","QACa_QACa7",
           "QACa_QACa8","QACa_QACa9","QACa_QACa10","QACa_QACa11","QACa_QACa12","QACa_QACa13","QACb_QACb1",
           "QACb_QACb2","QACb_QACb3","QACb_QACb4","QACb_QACb5","QACb_QACb6","QACb_QACb7","QACb1","QACc_QACc1",
           "QACc_QACc2","QACc_QACc3","QACc_QACc4","QACc_QACc5","QACc_QACc6","QACc_QACc7","QACc_QACc9","QACc1",
           "QACd_QACd1","QACd_QACd2","QACd_QACd3","QACd_QACd4","QACd_QACd5","QACd_QACd6","QACd_QACd7",
           "QACd_QACd8","QACd1","QACz_QACz1","QACz_QACz2","QACz_QACz3","QACz_QACz4","QACz_QACz5","QACz_QACz6",
           "QACz_QACz7","QACz_QACz8","QACz1","QACe_QACe1","QACe_QACe2","QACe_QACe3","QACe_QACe4","QACe_QACe5",
           "QACe_QACe6","QACe_QACe7","QACe_QACe8","QACe1","QACf_QACf1","QACf_QACf2","QACf_QACf3","QACf_QACf4",
           "QACf_QACf5","QACf_QACf6","QACf_QACf7","QACf_QACf8","QACg_QACg1","QACg_QACg2","QACg_QACg3",
           "QACg_QACg4","QACg_QACg5","QACg_QACg6","QACg_QACg7","QACg1","QACh_QACg8","QACh1","QACi_QACi1",
           "QACi_QACi2","QACi_QACi3","QACi_QACi4","QACi_QACi5","QACi_QACi6","QACi1","QACj_QACj1","QACj1",
           "QACk_QACk1","QACl_QACl1","QACl_QACl2","QACl_QACl3","QACl_QACl4","QACl_QACl5","QACl_QACl6",
           "QACl_QACl7","QACl_QACl8","QACl1","QACm_QACm1","QACm_QACm2","QACm_QACm3","QACm_QACm4","QACm_QACm5",
           "QACm_QACm6","QACm_QACm7","QACm_QACm8","QACm1"]

    cols_export = ['CAQ_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/CAQ.csv' % out_dir, decimal='.', index=False)
        
    else:
    
        df[['ids'] + cols_export].ix[idx].to_csv('%s/CAQ.csv' % out_dir, decimal='.', index=False)    


    
##############################################################################
#################### Metacognition Questionnaire 30 #########################
##############################################################################

def run_MCQ30(df, out_dir, public):
    
    cols = ['MCQ1_MCQ1', 'MCQ1_MCQ2', 'MCQ1_MCQ3', 'MCQ1_MCQ4', 'MCQ1_MCQ5', 
            'MCQ1_MCQ6', 'MCQ1_MCQ7', 'MCQ1_MCQ8', 'MCQ1_MCQ9', 'MCQ1_MCQ10', 
            'MCQ2_MCQ11', 'MCQ2_MCQ12', 'MCQ2_MCQ13', 'MCQ2_MCQ14', 
            'MCQ2_MCQ15', 'MCQ2_MCQ16', 'MCQ2_MCQ17', 'MCQ2_MCQ18', 
            'MCQ2_MCQ19', 'MCQ2_MCQ20', 'MCQ3_MCQ21', 'MCQ3_MCQ22', 
            'MCQ3_MCQ23', 'MCQ3_MCQ24', 'MCQ3_MCQ25', 'MCQ3_MCQ26', 
            'MCQ3_MCQ27', 'MCQ3_MCQ28', 'MCQ3_MCQ29', 'MCQ3_MCQ30']
        
    cols_export = ['MCQ_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/MCQ30.csv' % out_dir, decimal='.', index=False)
        
    else:
                                                                            
        df[['ids'] + cols_export].ix[idx].to_csv('%s/MCQ30.csv' % out_dir, decimal='.', index=False)    
    
 

##############################################################################
#################### Body Consciousness Questionnaire ########################
##############################################################################

def run_BCQ(df, out_dir, public):  
        
    cols = ['BCQ1_BCQ1', 'BCQ1_BCQ2', 'BCQ1_BCQ3', 'BCQ1_BCQ4',
            'BCQ1_BCQ5', 'BCQ1_BCQ6', 'BCQ1_BCQ7', 'BCQ1_BCQ8', 'BCQ1_BCQ9',
            'BCQ1_BCQ10', 'BCQ2_BCQ11', 'BCQ2_BCQ12', 'BCQ2_BCQ13',
            'BCQ2_BCQ14', 'BCQ2_BCQ15']
    
    cols_export = ['BCQ_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/BCQ.csv' % out_dir, decimal='.', index=False)
        
    else:
                                                                            
        df[['ids'] + cols_export].ix[idx].to_csv('%s/BCQ.csv' % out_dir, decimal='.', index=False)  
    
    

##############################################################################
################### Five Facet Mindfulness Questionnaire #####################
##############################################################################
   
def run_FFMQ(df, out_dir, public):
        
    cols = ['FFMQ1_FFMQ1', 'FFMQ1_FFMQ2',
            'FFMQ1_FFMQ3', 'FFMQ1_FFMQ4', 'FFMQ1_FFMQ5', 'FFMQ1_FFMQ6',
            'FFMQ1_FFMQ7', 'FFMQ1_FFMQ8', 'FFMQ1_FFMQ9', 'FFMQ1_FFMQ10',
            'FFMQ2_MMFQ11', 'FFMQ2_MMFQ12', 'FFMQ2_MMFQ13', 'FFMQ2_MMFQ14',
            'FFMQ2_MMFQ15', 'FFMQ2_MMFQ16', 'FFMQ2_MMFQ17', 'FFMQ2_MMFQ18',
            'FFMQ2_MMFQ19', 'FFMQ2_MMFQ20', 'FFMQ3_FFMQ21', 'FFMQ3_FFMQ22',
            'FFMQ3_FFMQ23', 'FFMQ3_FFMQ24', 'FFMQ3_FFMQ25', 'FFMQ3_FFMQ26',
            'FFMQ3_FFMQ27', 'FFMQ3_FFMQ28', 'FFMQ3_FFMQ29', 'FFMQ3_FFMQ30',
            'FFMQ4_FFMQ31', 'FFMQ4_FFMQ32', 'FFMQ4_FFMQ33', 'FFMQ4_FFMQ34',
            'FFMQ4_FFMQ35', 'FFMQ4_FFMQ36', 'FFMQ4_FFMQ37', 'FFMQ4_FFMQ38',
            'FFMQ4_FFMQ39']
                     
    cols_export = ['FFMQ_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/FFMQ.csv' % out_dir, decimal='.', index=False)
        
    else:
                                                               
        df[['ids'] + cols_export].ix[idx].to_csv('%s/FFMQ.csv' % out_dir, decimal='.', index=False) 



##############################################################################
#################### Abbreviated Math Anxiety Scale ##########################
##############################################################################

def run_AMAS(df, out_dir, public):

    cols = ['AMAS[1]',
            'AMAS[2]',
            'AMAS[3]',
            'AMAS[4]',
            'AMAS[5]',
            'AMAS[6]',
            'AMAS[7]',
            'AMAS[8]',
            'AMAS[9]']           
    
    cols_export = ['AMAS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/AMAS.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/AMAS.csv' % out_dir, decimal='.', index=False)        
    


##############################################################################
########################## self control scale ################################
##############################################################################

def run_SelfCtrl(df, out_dir, public):
    
    cols = ['SCSaBASEQ[SCS1]',
            'SCSaBASEQ[SCS2r]',
            'SCSaBASEQ[SCS3r]',
            'SCSaBASEQ[SCS4r]',
            'SCSaBASEQ[SCS5r]',
            'SCSaBASEQ[SCS6r]',
            'SCSbBASEQ[SCS7r]',
            'SCSbBASEQ[SCS8r]',
            'SCSbBASEQ[SCS9r]',
            'SCSbBASEQ[SCS10r]',
            'SCSbBASEQ[SCS11r]',
            'SCSbBASEQ[SCS12]',
            'SCSbBASEQ[SCS13]']                
    
    cols_export = ['SCS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/SCS.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/SCS.csv' % out_dir, decimal='.', index=False)
        
    

##############################################################################                      
################ Internet Addiction test #####################################
##############################################################################

def run_IAT(df, out_dir, public):     
    
    cols = ['IATaBASEQ[IAT1]',
            'IATaBASEQ[IAT2]',
            'IATbBASEQ[IAT3]',
            'IATcBASEQ[IAT4]',
            'IATcBASEQ[IAT5]',
            'IATcBASEQ[IAT6]',
            'IATcBASEQ[IAT7]',
            'IATcBASEQ[IAT8]',
            'IATcBASEQ[IAT9]',
            'IATcBASEQ[IAT10]',
            'IATcBASEQ[IAT11]',
            'IATcBASEQ[IAT12]',
            'IATcBASEQ[IAT13]',
            'IATcBASEQ[IAT14]',
            'IATdBASEQ[IAT15]',
            'IATdBASEQ[IAT16]',
            'IATdBASEQ[IAT17]',
            'IATdBASEQ[IAT18]',
            'IATdBASEQ[IAT19]',
            'IATdBASEQ[IAT20]']          
                     
    cols_export = ['IAT_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/IAT.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/IAT.csv' % out_dir, decimal='.', index=False)



##############################################################################
########################### Arten innerer Sprache ############################
#################### varieties of inner speech (VIS) #########################
##############################################################################

def run_VIS(df, out_dir, public):
        
    cols = ['AISaBASEQ[AIS1]', 'AISaBASEQ[AIS2]', 'AISaBASEQ[AIS3]', 'AISaBASEQ[AIS4]',
            'AISaBASEQ[AIS5]', 'AISaBASEQ[AIS6]', 'AISaBASEQ[AIS7]', 'AISaBASEQ[AIS8]',
            'AISaBASEQ[AIS9]', 'AISaBASEQ[AIS10]', 'AISbBASEQ[AIS11]', 'AISbBASEQ[AIS12]',
            'AISbBASEQ[AIS13]', 'AISbBASEQ[AIS14]', 'AISbBASEQ[AIS15]', 'AISbBASEQ[AIS16]',
            'AISbBASEQ[AIS17]', 'AISbBASEQ[AIS18]']        
                 
    cols_export = ['VIS_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/VISQ.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/VISQ.csv' % out_dir, decimal='.', index=False)



##############################################################################
############# Spontaneous and Deliberate Mind Wandering ######################
##############################################################################

def run_MW_SD(df, out_dir, public):
        
    cols = ["MWBASEQ[MWD1]", "MWBASEQ[MWD2]", "MWBASEQ[MWD3]", "MWBASEQ[MWD4]",
            "MWBASEQ[MWS1]", "MWBASEQ[MWS2]", "MWBASEQ[MWS3]", "MWBASEQ[MWS4]"]
                 
    cols_export = ['S-D-MW_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/S-D-MW.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/S-D-MW.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################# short dark triad  ##############################
##############################################################################

def run_SDT(df, out_dir, public):
    
    cols = ['SDTmBASEQ[SDTM1]', 'SDTmBASEQ[SDTM2]', 'SDTmBASEQ[SDTM3]', 'SDTmBASEQ[SDTM4]',
            'SDTmBASEQ[SDTM5]', 'SDTmBASEQ[SDTM6]', 'SDTmBASEQ[SDTM7]', 'SDTmBASEQ[SDTM8]',
            'SDTmBASEQ[SDTM9]','SDTnBASEQ[SDTN1]', 'SDTnBASEQ[SDTN2r]', 'SDTnBASEQ[SDTN3]',
            'SDTnBASEQ[SDTN4]', 'SDTnBASEQ[SDTN5]', 'SDTnBASEQ[SDTN6r]', 'SDTnBASEQ[SDTN7]',
            'SDTnBASEQ[SDTN8r]', 'SDTnBASEQ[SDTN9]', 'SDTpBASEQ[SDTP1]', 'SDTpBASEQ[SDTP2r]',
            'SDTpBASEQ[SDTP3]', 'SDTpBASEQ[SDTP4]', 'SDTpBASEQ[SDTP5]', 'SDTpBASEQ[SDTP6]',
            'SDTpBASEQ[SDTP7r]', 'SDTpBASEQ[SDTP8]', 'SDTpBASEQ[SDTP9]']
 
    cols_export = ['SD3_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/SD3.csv' % out_dir, decimal='.', index=False)
        
    else:
  
        df[['ids'] + cols_export].ix[idx].to_csv('%s/SD3.csv' % out_dir, decimal='.', index=False)



##############################################################################
################################ SDS #########################################
##############################################################################
# social desirability

def run_SDS(df, out_dir, public):
    
    cols = ['SESaBASEQ[SES1r]',
            'SESaBASEQ[SES2]',
            'SESaBASEQ[SES3]',
            'SESaBASEQ[SES4r]',
            'SESaBASEQ[SES5]',
            'SESaBASEQ[SES6r]',
            'SESaBASEQ[SES7r]',
            'SESaBASEQ[SES8]',
            'SESaBASEQ[SES9]',
            'SESaBASEQ[SES10]',
            'SESbBASEQ[SES11r]',
            'SESbBASEQ[SES12]',
            'SESbBASEQ[SES13]',
            'SESbBASEQ[SES14]',
            'SESbBASEQ[SES15r]',
            'SESbBASEQ[SES16]',
            'SESbBASEQ[SES17r]']  

    cols_export = ['SDS_%s' % (x+1) for x in range(len(cols))]  
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5]) 
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/SDS.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/SDS.csv' % out_dir, decimal='.', index=False)
  


##############################################################################            
##################### UPPSP - impulsivity ####################################
##############################################################################

def run_UPPSP(df, out_dir, public):
    
    cols = ['UPPSaBASEQ[UPP1]', 'UPPSaBASEQ[UPP2r]', 'UPPSaBASEQ[UPP3r]', 'UPPSaBASEQ[UPP4]',
            'UPPSaBASEQ[UPP5r]', 'UPPSaBASEQ[UPP6]', 'UPPSaBASEQ[UPP7r]', 'UPPSaBASEQ[UPP8r]',
            'UPPSaBASEQ[UPP9r]', 'UPPSaBASEQ[UPP10r]', 'UPPSbBASEQ[UPP11]', 'UPPSbBASEQ[UPP12r]',
            'UPPSbBASEQ[UPP13r]', 'UPPSbBASEQ[UPP14]', 'UPPSbBASEQ[UPP15r]', 'UPPSbBASEQ[UPP16]',
            'UPPSbBASEQ[UPP17r]', 'UPPSbBASEQ[UPP18r]', 'UPPSbBASEQ[UPP19]', 'UPPSbBASEQ[UPP20r]',
            'UPPScBASEQ[UPP21]', 'UPPScBASEQ[UPP22r]', 'UPPScBASEQ[UPP23r]', 'UPPScBASEQ[UPP24]',
            'UPPScBASEQ[UPP25r]', 'UPPScBASEQ[UPP26r]', 'UPPScBASEQ[UPP27]', 'UPPScBASEQ[UPP28]',
            'UPPScBASEQ[UPP29r]', 'UPPScBASEQ[UPP30r]', 'UPPSdBASEQ[UPP31r]', 'UPPSdBASEQ[UPP32]',
            'UPPSdBASEQ[UPP33]', 'UPPSdBASEQ[UPP34r]', 'UPPSdBASEQ[UPP35r]', 'UPPSdBASEQ[UPP36r]',
            'UPPSdBASEQ[UPP37]', 'UPPSdBASEQ[UPP38]', 'UPPSdBASEQ[UPP39r]', 'UPPSdBASEQ[UPP40r]',
            'UPPSeBASEQ[UPP41r]', 'UPPSeBASEQ[UPP42]', 'UPPSeBASEQ[UPP43]', 'UPPSeBASEQ[UPP44r]',
            'UPPSeBASEQ[UPP45r]', 'UPPSeBASEQ[UPP46r]', 'UPPSeBASEQ[UPP47r]', 'UPPSeBASEQ[UPP48]',
            'UPPSeBASEQ[UPP49]', 'UPPSeBASEQ[UPP50r]', 'UPPSfBASEQ[UPP51r]', 'UPPSfBASEQ[UPP52r]',
            'UPPSfBASEQ[UPP53r]', 'UPPSfBASEQ[UPP54]', 'UPPSfBASEQ[UPP55r]', 'UPPSfBASEQ[UPP56r]',
            'UPPSfBASEQ[UPP57r]', 'UPPSfBASEQ[UPP58r]','UPPSfBASEQ[UPP59r]']        
     
    cols_export = ['UPPS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/UPPS-P.csv' % out_dir, decimal='.', index=False)
        
    else:
                                                                             
        df[['ids'] + cols_export].ix[idx].to_csv('%s/UPPS-P.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
############################## TPS-D #########################################
################ Tuckmann Procrastination Scale (TPS_D)#######################
##############################################################################

def run_TPS(df, out_dir, public):
    
    cols = ['TPSBASEQ[TPS1]',
            'TPSBASEQ[TPS2]',
            'TPSBASEQ[TPS3]',
            'TPSBASEQ[TPS4]',
            'TPSBASEQ[TPS5]',
            'TPSBASEQ[TPS6]',
            'TPSBASEQ[TPS7]',
            'TPSBASEQ[TPS8]',
            'TPSBASEQ[TPS9]',
            'TPSBASEQ[TPS10]',
            'TPSBASEQ[TPS11]',
            'TPSBASEQ[TPS12]',
            'TPSBASEQ[TPS13]',
            'TPSBASEQ[TPS14]',
            'TPSBASEQ[TPS15]',
            'TPSBASEQ[TPS16]']
        
    cols_export = ['TPS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/TPS.csv' % out_dir, decimal='.', index=False)
        
    else:
 
        df[['ids'] + cols_export].ix[idx].to_csv('%s/TPS.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
############################ ASR 18-59 #######################################
##############################################################################

def run_ASR(df, out_dir, public):
    
    d = {'ASQQ79Freitext': 'ASR_79_comment',
         'ASR100Freitext': 'ASR_100_comment',
         'ASR92Freitext': 'ASR_92_comment',
         'ASRIABASEQ[ASRIA]': 'ASR_I_A',
         'ASRIBBASEQ[ASRIB]': 'ASR_I_B',
         'ASRICBASEQ[ASRIC]': 'ASR_I_C',
         'ASRIDBASEQ[ASRID]': 'ASR_I_D',
         'ASRII1': 'ASR_II_1',
         'ASRII1[comment]': 'ASR_II_1_comment',
         'ASRII2': 'ASR_II_2',
         'ASRII3BASEQ[ASRIIA]': 'ASR_II_A',
         'ASRII3BASEQ[ASRIIBr]': 'ASR_II_B',
         'ASRII3BASEQ[ASRIIC]': 'ASR_II_C',
         'ASRII3BASEQ[ASRIID]': 'ASR_II_D',
         'ASRII3BASEQ[ASRIIEr]': 'ASR_II_E',
         'ASRII3BASEQ[ASRIIFr]': 'ASR_II_F',
         'ASRII3BASEQ[ASRIIG]': 'ASR_II_G',
         'ASRII3BASEQ[ASRIIHr]': 'ASR_II_H',
         'ASRIIIABASEQ[ASRIIIA]': 'ASR_III_A',
         'ASRIIIBBASEQ[ASRIIIB]': 'ASR_III_B',
         'ASRIIICBASEQ[ASRIIIC]': 'ASR_III_C',
         'ASRIIIDBASEQ[ASRIIID]': 'ASR_III_D',
         'ASRIIIEaBASEQ[ASRIIIE]': 'ASR_III_E',
         'ASRIIIEbBASEQ[ASRIIIE1]': 'ASR_III_E_1',
         'ASRIIIEbBASEQ[ASRIIIE2]': 'ASR_III_E_2',
         'ASRIIIEbBASEQ[ASRIIIE3]': 'ASR_III_E_3',
         'ASRIIIEbBASEQ[ASRIIIE4]': 'ASR_III_E_4',
         'ASRIIIFBASEQ[ASRIIIF]': 'ASR_III_F',
         'ASRIVaBASEQ[ASRIV]': 'ASR_IV_1_comment',
         'ASRIVbBASEQ[ASRIVA]': 'ASR_IV_A',
         'ASRIVbBASEQ[ASRIVBr]': 'ASR_IV_B',
         'ASRIVbBASEQ[ASRIVC]': 'ASR_IV_C',
         'ASRIVbBASEQ[ASRIVDr]': 'ASR_IV_D',
         'ASRIVbBASEQ[ASRIVE]': 'ASR_IV_E',
         'ASRIVbBASEQ[ASRIVFr]': 'ASR_IV_F',
         'ASRIVbBASEQ[ASRIVGr]': 'ASR_IV_G',
         'ASRIVbBASEQ[ASRIVHr]': 'ASR_IV_H',
         'ASRIVbBASEQ[ASRIVIr]': 'ASR_IV_I',
         'ASRQ101BASEQ[ASRQ101]': 'ASR_101',
         'ASRQ101BASEQ[ASRQ102]': 'ASR_102',
         'ASRQ101BASEQ[ASRQ103]': 'ASR_103',
         'ASRQ101BASEQ[ASRQ104]': 'ASR_104',
         'ASRQ101BASEQ[ASRQ105]': 'ASR_105',
         'ASRQ101BASEQ[ASRQ106]': 'ASR_106',
         'ASRQ101BASEQ[ASRQ107]': 'ASR_107',
         'ASRQ101BASEQ[ASRQ108]': 'ASR_108',
         'ASRQ101BASEQ[ASRQ109]': 'ASR_109',
         'ASRQ101BASEQ[ASRQ110]': 'ASR_110',
         'ASRQ10BASEQ[ASRQ10]': 'ASR_10',
         'ASRQ10BASEQ[ASRQ11]': 'ASR_11',
         'ASRQ10BASEQ[ASRQ12]': 'ASR_12',
         'ASRQ10BASEQ[ASRQ13]': 'ASR_13',
         'ASRQ10BASEQ[ASRQ14]': 'ASR_14',
         'ASRQ10BASEQ[ASRQ15]': 'ASR_15',
         'ASRQ10BASEQ[ASRQ16]': 'ASR_16',
         'ASRQ10BASEQ[ASRQ17]': 'ASR_17',
         'ASRQ10BASEQ[ASRQ18]': 'ASR_18',
         'ASRQ10BASEQ[ASRQ19]': 'ASR_19',
         'ASRQ10BASEQ[ASRQ20]': 'ASR_20',
         'ASRQ111BASEQ[ASRQ111]': 'ASR_111',
         'ASRQ111BASEQ[ASRQ112]': 'ASR_112',
         'ASRQ111BASEQ[ASRQ113]': 'ASR_113',
         'ASRQ111BASEQ[ASRQ114]': 'ASR_114',
         'ASRQ111BASEQ[ASRQ115]': 'ASR_115',
         'ASRQ111BASEQ[ASRQ116]': 'ASR_116',
         'ASRQ111BASEQ[ASRQ117]': 'ASR_117',
         'ASRQ111BASEQ[ASRQ118]': 'ASR_118',
         'ASRQ111BASEQ[ASRQ119]': 'ASR_119',
         'ASRQ111BASEQ[ASRQ120]': 'ASR_120',
         'ASRQ121BASEQ[ASRQ121]': 'ASR_121',
         'ASRQ121BASEQ[ASRQ122]': 'ASR_122',
         'ASRQ121BASEQ[ASRQ123]': 'ASR_123',
         'ASRQ124': 'ASR_124',
         'ASRQ125': 'ASR_125',
         'ASRQ126': 'ASR_126',
         'ASRQ1BASEQ[ASRQ1]': 'ASR_1',
         'ASRQ1BASEQ[ASRQ2]': 'ASR_2',
         'ASRQ1BASEQ[ASRQ3]': 'ASR_3',
         'ASRQ1BASEQ[ASRQ4]': 'ASR_4',
         'ASRQ1BASEQ[ASRQ5]': 'ASR_5',
         'ASRQ1BASEQ[ASRQ6]': 'ASR_6',
         'ASRQ21BASEQ[ASRQ21]': 'ASR_21',
         'ASRQ21BASEQ[ASRQ22]': 'ASR_22',
         'ASRQ21BASEQ[ASRQ23]': 'ASR_23',
         'ASRQ21BASEQ[ASRQ24]': 'ASR_24',
         'ASRQ21BASEQ[ASRQ25]': 'ASR_25',
         'ASRQ21BASEQ[ASRQ26]': 'ASR_26',
         'ASRQ21BASEQ[ASRQ27]': 'ASR_27',
         'ASRQ21BASEQ[ASRQ28]': 'ASR_28',
         'ASRQ21BASEQ[ASRQ29]': 'ASR_29',
         'ASRQ29Freitext': 'ASR_29_comment',
         'ASRQ30BASEQ[ASRQ30]': 'ASR_30',
         'ASRQ30BASEQ[ASRQ31]': 'ASR_31',
         'ASRQ30BASEQ[ASRQ32]': 'ASR_32',
         'ASRQ30BASEQ[ASRQ33]': 'ASR_33',
         'ASRQ30BASEQ[ASRQ34]': 'ASR_34',
         'ASRQ30BASEQ[ASRQ35]': 'ASR_35',
         'ASRQ30BASEQ[ASRQ36]': 'ASR_36',
         'ASRQ30BASEQ[ASRQ37]': 'ASR_37',
         'ASRQ30BASEQ[ASRQ38]': 'ASR_38',
         'ASRQ30BASEQ[ASRQ39]': 'ASR_39',
         'ASRQ30BASEQ[ASRQ40]': 'ASR_40',
         'ASRQ40Freitext': 'ASR_40_comment',
         'ASRQ41BASEQ[ASRQ41]': 'ASR_41',
         'ASRQ41BASEQ[ASRQ42]': 'ASR_42',
         'ASRQ41BASEQ[ASRQ43]': 'ASR_43',
         'ASRQ41BASEQ[ASRQ44]': 'ASR_44',
         'ASRQ41BASEQ[ASRQ45]': 'ASR_45',
         'ASRQ41BASEQ[ASRQ46]': 'ASR_46',
         'ASRQ41BASEQ[ASRQ47]': 'ASR_47',
         'ASRQ41BASEQ[ASRQ48]': 'ASR_48',
         'ASRQ41BASEQ[ASRQ49]': 'ASR_49',
         'ASRQ41BASEQ[ASRQ50]': 'ASR_50',
         'ASRQ46Freitext': 'ASR_46_comment',
         'ASRQ51BASEQ[ASRQ51]': 'ASR_51',
         'ASRQ51BASEQ[ASRQ52]': 'ASR_52',
         'ASRQ51BASEQ[ASRQ53]': 'ASR_53',
         'ASRQ51BASEQ[ASRQ54]': 'ASR_54',
         'ASRQ51BASEQ[ASRQ55]': 'ASR_55',
         'ASRQ56BASEQ[ASRVIII561]': 'ASR_56_a',
         'ASRQ56BASEQ[ASRVIII562]': 'ASR_56_b',
         'ASRQ56BASEQ[ASRVIII563]': 'ASR_56_c',
         'ASRQ56BASEQ[ASRVIII564]': 'ASR_56_d',
         'ASRQ56BASEQ[ASRVIII565]': 'ASR_56_e',
         'ASRQ56BASEQ[ASRVIII566]': 'ASR_56_f',
         'ASRQ56BASEQ[ASRVIII567]': 'ASR_56_g',
         'ASRQ56Freitext': 'ASR_56_d_comment',
         'ASRQ57BASEQ[ASRQ57]': 'ASR_57',
         'ASRQ57BASEQ[ASRQ58]': 'ASR_58',
         'ASRQ57BASEQ[ASRQ59]': 'ASR_59',
         'ASRQ57BASEQ[ASRQ60]': 'ASR_60',
         'ASRQ58Freitext': 'ASR_58_comment',
         'ASRQ61BASEQ[ASRQ61]': 'ASR_61',
         'ASRQ61BASEQ[ASRQ62]': 'ASR_62',
         'ASRQ61BASEQ[ASRQ63]': 'ASR_63',
         'ASRQ61BASEQ[ASRQ64]': 'ASR_64',
         'ASRQ61BASEQ[ASRQ65]': 'ASR_65',
         'ASRQ61BASEQ[ASRQ66]': 'ASR_66',
         'ASRQ61BASEQ[ASRQ67]': 'ASR_67',
         'ASRQ61BASEQ[ASRQ68]': 'ASR_68',
         'ASRQ61BASEQ[ASRQ69]': 'ASR_69',
         'ASRQ61BASEQ[ASRQ70]': 'ASR_70',
         'ASRQ66': 'ASR_66_comment',
         'ASRQ6Freitext': 'ASR_6_comment',
         'ASRQ70': 'ASR_70_comment',
         'ASRQ71BASEQ[ASRQ71]': 'ASR_71',
         'ASRQ71BASEQ[ASRQ72]': 'ASR_72',
         'ASRQ71BASEQ[ASRQ73]': 'ASR_73',
         'ASRQ71BASEQ[ASRQ74]': 'ASR_74',
         'ASRQ71BASEQ[ASRQ75]': 'ASR_75',
         'ASRQ71BASEQ[ASRQ76]': 'ASR_76',
         'ASRQ71BASEQ[ASRQ77]': 'ASR_77',
         'ASRQ71BASEQ[ASRQ78]': 'ASR_78',
         'ASRQ71BASEQ[ASRQ79]': 'ASR_79',
         'ASRQ71BASEQ[ASRQ80]': 'ASR_80',
         'ASRQ77Freitext': 'ASR_77_comment',
         'ASRQ7BASEQ[ASRQ7]': 'ASR_7',
         'ASRQ7BASEQ[ASRQ8]': 'ASR_8',
         'ASRQ7BASEQ[ASRQ9]': 'ASR_9',
         'ASRQ81BASEQ[ASRQ81]': 'ASR_81',
         'ASRQ81BASEQ[ASRQ82]': 'ASR_82',
         'ASRQ81BASEQ[ASRQ83]': 'ASR_83',
         'ASRQ81BASEQ[ASRQ84]': 'ASR_84',
         'ASRQ81BASEQ[ASRQ85]': 'ASR_85',
         'ASRQ81BASEQ[ASRQ86]': 'ASR_86',
         'ASRQ81BASEQ[ASRQ87]': 'ASR_87',
         'ASRQ81BASEQ[ASRQ88]': 'ASR_88',
         'ASRQ81BASEQ[ASRQ89]': 'ASR_89',
         'ASRQ81BASEQ[ASRQ90]': 'ASR_90',
         'ASRQ84Freitext': 'ASR_84_comment',
         'ASRQ85Freitext': 'ASR_85_comment',
         'ASRQ91BASEQ[ASRQ100]': 'ASR_100',
         'ASRQ91BASEQ[ASRQ91]': 'ASR_91',
         'ASRQ91BASEQ[ASRQ92]': 'ASR_92',
         'ASRQ91BASEQ[ASRQ93]': 'ASR_93',
         'ASRQ91BASEQ[ASRQ94]': 'ASR_94',
         'ASRQ91BASEQ[ASRQ95]': 'ASR_95',
         'ASRQ91BASEQ[ASRQ96]': 'ASR_96',
         'ASRQ91BASEQ[ASRQ97]': 'ASR_97',
         'ASRQ91BASEQ[ASRQ98]': 'ASR_98',
         'ASRQ91BASEQ[ASRQ99]': 'ASR_99',
         'ASRQ9Freitext': 'ASR_9_comment',
         'ASRVI': 'ASR_VI',
         'ASRVII': 'ASR_VII',
         'ASRVIII': 'ASR_VIII',
         'ASRVII[comment]': 'ASR_VII_comment',
         'ASRVI[comment]': 'ASR_VI_comment',
         'ASRVa': 'ASR_V_1',
         'ASRVa[comment]': 'ASR_V_1_comment',
         'ASRVbBASEQ[ASRV1]': 'ASR_V_2',
         'ASRVbBASEQ[ASRV1comment]': 'ASR_V_2_comment',
         'ASRVbBASEQ[ASRV3]': 'ASR_V_3',
         'ASRVbBASEQ[ASRV3comment]': 'ASR_V_3_comment',
         'ASRVbBASEQ[ASRV4]': 'ASR_V_4',
         'ASRVbBASEQ[ASRV4comment]': 'ASR_V_4_comment',
         'ASRVcBASEQ[ASRVA]': 'ASR_V_A',
         'ASRVcBASEQ[ASRVB]': 'ASR_V_B',
         'ASRVcBASEQ[ASRVCr]': 'ASR_V_C',
         'ASRVcBASEQ[ASRVD]': 'ASR_V_D',
         'ASRVcBASEQ[ASRVEr]': 'ASR_V_E'}
    
    item_order = ['ASR_I_A',
                  'ASR_I_B',
                  'ASR_I_C',
                  'ASR_I_D',
                  'ASR_II_1',
                  'ASR_II_1_comment',
                  'ASR_II_2',
                  'ASR_II_A',
                  'ASR_II_B',
                  'ASR_II_C',
                  'ASR_II_D',
                  'ASR_II_E',
                  'ASR_II_F',
                  'ASR_II_G',
                  'ASR_II_H',
                  'ASR_III_A',
                  'ASR_III_B',
                  'ASR_III_C',
                  'ASR_III_D',
                  'ASR_III_E',
                  'ASR_III_E_1',
                  'ASR_III_E_2',
                  'ASR_III_E_3',
                  'ASR_III_E_4',
                  'ASR_III_F',
                  'ASR_IV_1_comment',
                  'ASR_IV_A',
                  'ASR_IV_B',
                  'ASR_IV_C',
                  'ASR_IV_D',
                  'ASR_IV_E',
                  'ASR_IV_F',
                  'ASR_IV_G',
                  'ASR_IV_H',
                  'ASR_IV_I',
                  'ASR_V_1',
                  'ASR_V_1_comment',
                  'ASR_V_2',
                  'ASR_V_2_comment',
                  'ASR_V_3',
                  'ASR_V_3_comment',
                  'ASR_V_4',
                  'ASR_V_4_comment',
                  'ASR_V_A',
                  'ASR_V_B',
                  'ASR_V_C',
                  'ASR_V_D',
                  'ASR_V_E',
                  'ASR_VI',
                  'ASR_VI_comment',
                  'ASR_VII',
                  'ASR_VII_comment',
                  'ASR_VIII',
                  'ASR_1',
                  'ASR_2',
                  'ASR_3',
                  'ASR_4',
                  'ASR_5',
                  'ASR_6',
                  'ASR_6_comment',
                  'ASR_7',
                  'ASR_8',
                  'ASR_9',
                  'ASR_9_comment',
                  'ASR_10',
                  'ASR_11',
                  'ASR_12',
                  'ASR_13',
                  'ASR_14',
                  'ASR_15',
                  'ASR_16',
                  'ASR_17',
                  'ASR_18',
                  'ASR_19',
                  'ASR_20',
                  'ASR_21',
                  'ASR_22',
                  'ASR_23',
                  'ASR_24',
                  'ASR_25',
                  'ASR_26',
                  'ASR_27',
                  'ASR_28',
                  'ASR_29',
                  'ASR_29_comment',
                  'ASR_30',
                  'ASR_31',
                  'ASR_32',
                  'ASR_33',
                  'ASR_34',
                  'ASR_35',
                  'ASR_36',
                  'ASR_37',
                  'ASR_38',
                  'ASR_39',
                  'ASR_40',
                  'ASR_40_comment',
                  'ASR_41',
                  'ASR_42',
                  'ASR_43',
                  'ASR_44',
                  'ASR_45',
                  'ASR_46',
                  'ASR_47',
                  'ASR_48',
                  'ASR_49',
                  'ASR_50',
                  'ASR_46_comment',
                  'ASR_51',
                  'ASR_52',
                  'ASR_53',
                  'ASR_54',
                  'ASR_55',
                  'ASR_56_a',
                  'ASR_56_b',
                  'ASR_56_c',
                  'ASR_56_d',
                  'ASR_56_e',
                  'ASR_56_f',
                  'ASR_56_g',
                  'ASR_56_d_comment',
                  'ASR_57',
                  'ASR_58',
                  'ASR_59',
                  'ASR_60',
                  'ASR_58_comment',
                  'ASR_61',
                  'ASR_62',
                  'ASR_63',
                  'ASR_64',
                  'ASR_65',
                  'ASR_66',
                  'ASR_67',
                  'ASR_68',
                  'ASR_69',
                  'ASR_70',
                  'ASR_66_comment',
                  'ASR_70_comment',
                  'ASR_71',
                  'ASR_72',
                  'ASR_73',
                  'ASR_74',
                  'ASR_75',
                  'ASR_76',
                  'ASR_77',
                  'ASR_78',
                  'ASR_79',
                  'ASR_80',
                  'ASR_77_comment',
                  'ASR_79_comment',
                  'ASR_81',
                  'ASR_82',
                  'ASR_83',
                  'ASR_84',
                  'ASR_85',
                  'ASR_86',
                  'ASR_87',
                  'ASR_88',
                  'ASR_89',
                  'ASR_90',
                  'ASR_84_comment',
                  'ASR_85_comment',
                  'ASR_91',
                  'ASR_92',
                  'ASR_93',
                  'ASR_94',
                  'ASR_95',
                  'ASR_96',
                  'ASR_97',
                  'ASR_98',
                  'ASR_99',
                  'ASR_100',
                  'ASR_92_comment',
                  'ASR_100_comment',
                  'ASR_101',
                  'ASR_102',
                  'ASR_103',
                  'ASR_104',
                  'ASR_105',
                  'ASR_106',
                  'ASR_107',
                  'ASR_108',
                  'ASR_109',
                  'ASR_110',
                  'ASR_111',
                  'ASR_112',
                  'ASR_113',
                  'ASR_114',
                  'ASR_115',
                  'ASR_116',
                  'ASR_117',
                  'ASR_118',
                  'ASR_119',
                  'ASR_120',
                  'ASR_121',
                  'ASR_122',
                  'ASR_123',
                  'ASR_124',
                  'ASR_125',
                  'ASR_126']
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
    df.rename(columns=d, inplace=True)
    
    if public:
        # excluding pp comments
        # ASR_IV_1_comment is coded as binary variable and can stay
        remove = ['ASR_II_1_comment', 'ASR_V_1_comment', 'ASR_V_2_comment', 'ASR_V_3_comment',
                  'ASR_V_4_comment', 'ASR_VI_comment', 'ASR_VII_comment', 'ASR_VIII', 'ASR_6_comment',
                  'ASR_9_comment', 'ASR_29_comment', 'ASR_40_comment', 'ASR_46_comment', 'ASR_56_d_comment',
                  'ASR_58_comment', 'ASR_66_comment', 'ASR_70_comment', 'ASR_77_comment', 'ASR_79_comment',
                  'ASR_84_comment', 'ASR_85_comment', 'ASR_92_comment', 'ASR_100_comment']

        cols_export = [item for item in item_order if item not in remove]
        
        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/ASR.csv' % out_dir, decimal='.', index=False)
        
    else:
        
        # including pp comments
        cols_export = item_order
        
        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
    
        df[['ids'] + cols_export].ix[idx].to_csv('%s/ASR.csv' % out_dir, decimal='.', index=False)


        
##############################################################################
########################## Self-Esteem Scale ################################# 
##############################################################################

def run_SE(df, out_dir, public):
    
    cols = ['SEBASEQ[SE1]',
            'SEBASEQ[SE2]',
            'SEBASEQ[SE3]',
            'SEBASEQ[SE4]',
            'SEBASEQ[SE5r]', 
            'SEBASEQ[SE6r]',
            'SEBASEQ[SE7r]',
            'SEBASEQ[SE8r]']
        
    cols_export = ['SE_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/SE.csv' % out_dir, decimal='.', index=False)
        
    else:
         
        df[['ids'] + cols_export].ix[idx].to_csv('%s/SE.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
####### Involuntary Musical Imagery Scale (Earworm Scale) ####################
##############################################################################

def run_IMIS(df, out_dir, public):

    cols = ['EWSaBASEQ[AQ_1]','EWSbBASEQ[NV1]','EWSbBASEQ[NV2]','EWSbBASEQ[NV3]','EWSbBASEQ[NV4]','EWSbBASEQ[NV5]',
            'EWSbBASEQ[NV6]','EWSbBASEQ[NV7]','EWScBASEQ[M1]','EWScBASEQ[M2]','EWScBASEQ[M3]','EWScBASEQ[PR1]',
            'EWScBASEQ[PR2]','EWScBASEQ[PR3]','EWScBASEQ[H1]','EWScBASEQ[H2]','EWSdBASEQ[AQ2]','EWSeBASEQ[AQ3]']
            
    cols_export = ['IMIS_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/IMIS.csv' % out_dir, decimal='.', index=False)
        
    else:
    
        df[['ids'] + cols_export].ix[idx].to_csv('%s/IMIS.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
####### Goldsmiths Musical Sophistication Index (Gold-MSI) ###################
##############################################################################

def run_GoldMSI(df, out_dir, public):
    
    cols = ['MUSaBASEQ[MUS_1]','MUSaBASEQ[MUS_3]','MUSaBASEQ[MUS_8]','MUSaBASEQ[MUS_15]','MUSaBASEQ[MUS_21]','MUSaBASEQ[MUS_24]',
            'MUSaBASEQ[MUS_28]','MUSbBASEQ[MUS_34]','MUScBASEQ[MUS_38]','MUSdBASEQ[MUS_14]','MUSdBASEQ[MUS_27]','MUSeBASEQ[MUS_32]',
            'MUSfBASEQ[MUS_33]','MUSgBASEQ[MUS_35]','MUShBASEQ[MUS_36]','MUSiBASEQ[MUS_37]']

    cols_export = ['GoldMSI_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/Gold-MSI.csv' % out_dir, decimal='.', index=False)
        
    else:
        
        df[['ids'] + cols_export].ix[idx].to_csv('%s/Gold-MSI.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
####################### Epsworth Sleepiness Scale ############################
##############################################################################

def run_ESS(df, out_dir, public):
    
    cols = ['ESSBASEQ[ESS1]', 'ESSBASEQ[ESS2]', 'ESSBASEQ[ESS3]', 'ESSBASEQ[ESS4]',
            'ESSBASEQ[ESS5]', 'ESSBASEQ[ESS6]', 'ESSBASEQ[ESS7]', 'ESSBASEQ[ESS8]']    
       
    cols_export = ['ESS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/ESS.csv' % out_dir, decimal='.', index=False)
        
    else:
  
        df[['ids'] + cols_export].ix[idx].to_csv('%s/ESS.csv' % out_dir, decimal='.', index=False)
  
    

##############################################################################
############################## BDI ###########################################
##############################################################################

def run_BDI(df, out_dir, public):

    cols_raw = ['BDIABASEQ[BDIA0]', 'BDIABASEQ[BDIA1]', 'BDIABASEQ[BDIA2]', 'BDIABASEQ[BDIA3]',
               'BDIBBASEQ[BDIB0]', 'BDIBBASEQ[BDIB1]', 'BDIBBASEQ[BDIB2]',
               'BDIBBASEQ[BDIB3]', 'BDICBASEQ[BDIC0]', 'BDICBASEQ[BDIC1]',
               'BDICBASEQ[BDIC2]', 'BDICBASEQ[BDIC3]', 'BDIDBASEQ[BDID0]',
               'BDIDBASEQ[BDID1]', 'BDIDBASEQ[BDID2]', 'BDIDBASEQ[BDID3]',
               'BDIEBASEQ[BDIE0]', 'BDIEBASEQ[BDIE1]', 'BDIEBASEQ[BDIE2]',
               'BDIEBASEQ[BDIE3]', 'BDIFBASEQ[BDIF0]', 'BDIFBASEQ[BDIF1]',
               'BDIFBASEQ[BDIF2]', 'BDIFBASEQ[BDIF3]', 'BDIGBASEQ[BDIG0]',
               'BDIGBASEQ[BDIG1]', 'BDIGBASEQ[BDIG2]', 'BDIGBASEQ[BDIG3]',
               'BDIHBASEQ[BDIH0]', 'BDIHBASEQ[BDIH1]', 'BDIHBASEQ[BDIH2]',
               'BDIHBASEQ[BDIH3]', 'BDIIBASEQ[BDII0]', 'BDIIBASEQ[BDII1]',
               'BDIIBASEQ[BDII2]', 'BDIIBASEQ[BDII3]', 'BDIJBASEQ[BDIJ0]',
               'BDIJBASEQ[BDIJ1]', 'BDIJBASEQ[BDIJ2]', 'BDIJBASEQ[BDIJ3]',
               'BDIKBASEQ[BDIK0]', 'BDIKBASEQ[BDIK1]', 'BDIKBASEQ[BDIK2]',
               'BDIKBASEQ[BDIK3]', 'BDILBASEQ[BDIL0]', 'BDILBASEQ[BDIL1]',
               'BDILBASEQ[BDIL2]', 'BDILBASEQ[BDIL3]', 'BDIMBASEQ[BDIM0]',
               'BDIMBASEQ[BDIM1]', 'BDIMBASEQ[BDIM2]', 'BDIMBASEQ[BDIM3]',
               'BDINBASEQ[BDIN0]', 'BDINBASEQ[BDIN1]', 'BDINBASEQ[BDIN2]',
               'BDINBASEQ[BDIN3]', 'BDIOBASEQ[BDIO0]', 'BDIOBASEQ[BDIO1]',
               'BDIOBASEQ[BDIO2]', 'BDIOBASEQ[BDIO3]', 'BDIPBASEQ[BDIP0]',
               'BDIPBASEQ[BDIP1]', 'BDIPBASEQ[BDIP2]', 'BDIPBASEQ[BDIP3]',
               'BDIQBASEQ[BDIQ0]', 'BDIQBASEQ[BDIQ1]', 'BDIQBASEQ[BDIQ2]',
               'BDIQBASEQ[BDIQ3]', 'BDIRBASEQ[BDIR0]', 'BDIRBASEQ[BDIR1]',
               'BDIRBASEQ[BDIR2]', 'BDIRBASEQ[BDIR3]', 'BDISBASEQ[BDIS0]',
               'BDISBASEQ[BDIS1]', 'BDISBASEQ[BDIS2]', 'BDISBASEQ[BDIS3]', 'BDIS4',
               'BDITBASEQ[BDIT0]', 'BDITBASEQ[BDIT1]', 'BDITBASEQ[BDIT2]',
               'BDITBASEQ[BDIT3]', 'BDIUBASEQ[BDIU0]', 'BDIUBASEQ[BDIU1]',
               'BDIUBASEQ[BDIU2]', 'BDIUBASEQ[BDIU3]']
    
    cols_export = ['BDI_%s' % (x+1) for x in range(len(cols_raw))]
    df.rename(columns=dict(zip(cols_raw, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/BDI.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/BDI.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
############################## HADS ##########################################
##############################################################################

def run_HADS(df, out_dir, public):
    
    # anxiety / HADS-A
    df['tense'] = df['HADS1BASEQ[HADS1]'].subtract(1).multiply(-1).add(3)
    df['frightened'] = df['HADS3BASEQ[HADS3]'].subtract(1).multiply(-1).add(3)
    df['worry'] = df['HADS5BASEQ[HADS5]'].subtract(1).multiply(-1).add(3)
    df['relaxed'] = df['HADS7BASEQ[HADS7]'].subtract(1)
    df['butterflies'] = df['HADS9BASEQ[HADS9]'].subtract(1)
    df['restless'] = df['HADS11BASEQ[HADS11]'].subtract(1).multiply(-1).add(3)
    df['panic'] = df['HADS13BASEQ[HADS13]'].subtract(1).multiply(-1).add(3)
    
    # depression / HADS-D
    df['enjoy'] = df['HADS2BASEQ[HADS2]'].subtract(1)
    df['laugh'] = df['HADS4BASEQ[HADS4]'].subtract(1)
    df['cheerful'] = df['HADS6BASEQ[HADS6]'].subtract(1).multiply(-1).add(3)
    df['slowed'] = df['HADS8BASEQ[HADS8]'].subtract(1).multiply(-1).add(3)
    df['appearance'] = df['HADS10BASEQ[HADS10]'].subtract(1).multiply(-1).add(3)
    df['lookforward'] = df['HADS12BASEQ[HADS12]'].subtract(1)
    df['entertain'] = df['HADS14BASEQ[HADS14]'].subtract(1)

    cols = ['tense','enjoy','frightened','laugh','worry','cheerful','relaxed','slowed',
            'butterflies','appearance','restless','lookforward','panic','entertain']
    
    cols_export = ['HADS_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/HADS.csv' % out_dir, decimal='.', index=False)
        
    else:
           
        df[['ids'] + cols_export].ix[idx].to_csv('%s/HADS.csv' % out_dir, decimal='.', index=False)



##############################################################################
##################### Boredom Proness Scale ##################################
##############################################################################

def run_BPS(df, out_dir, public):

    cols = ['BPSaBASEQ[BPS1]','BPSaBASEQ[BPS2]','BPSaBASEQ[BPS3]',
            'BPSaBASEQ[BPS4]','BPSaBASEQ[BPS5]','BPSaBASEQ[BPS6]',
            'BPSaBASEQ[BPS7]','BPSaBASEQ[BPS8]','BPSaBASEQ[BPS9]',
            'BPSaBASEQ[BPS10]','BPSbBASEQ[BPS11]','BPSbBASEQ[BPS12]',
            'BPSbBASEQ[BPS13]','BPSbBASEQ[BPS14]','BPSbBASEQ[BPS15]',
            'BPSbBASEQ[BPS16]','BPSbBASEQ[BPS17]','BPSbBASEQ[BPS18]',
            'BPSbBASEQ[BPS19]','BPSbBASEQ[BPS20]','BPSbBASEQ[BPS21]',
            'BPScBASEQ[BPS22]','BPScBASEQ[BPS23]','BPScBASEQ[BPS24]',
            'BPScBASEQ[BPS25]','BPScBASEQ[BPS26]','BPScBASEQ[BPS27]',
            'BPScBASEQ[BPS28]']
        
    cols_export = ['BPS_%s' % (x+1) for x in range(len(cols))]  
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/BP.csv' % out_dir, decimal='.', index=False)
        
    else:
               
        df[['ids'] + cols_export].ix[idx].to_csv('%s/BP.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
################# Derryberry Attention Control Scale #########################
##############################################################################

def run_ACS(df, out_dir, public):
    
    cols = ['DACaBASEQ[DAC1]','DACaBASEQ[DAC2]','DACaBASEQ[DAC3]',
            'DACaBASEQ[DAC4]','DACaBASEQ[DAC5]','DACaBASEQ[DAC6]',
            'DACaBASEQ[DAC7]','DACbBASEQ[DAC8]','DACbBASEQ[DAC9]',
            'DACbBASEQ[DAC10]','DACbBASEQ[DAC11]','DACbBASEQ[DAC12]',
            'DACbBASEQ[DAC13]','DACbBASEQ[DAC14]','DACbBASEQ[DAC15]',
            'DACcBASEQ[DAC16]','DACcBASEQ[DAC17]','DACcBASEQ[DAC18]',
            'DACcBASEQ[DAC19]','DACcBASEQ[DAC20]']     
        
    cols_export = ['ACS_%s' % (x+1) for x in range(len(cols))]  
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/ACS.csv' % out_dir, decimal='.', index=False)
        
    else:
         
        df[['ids'] + cols_export].ix[idx].to_csv('%s/ACS.csv' % out_dir, decimal='.', index=False)
  
  

##############################################################################
############################## NEO-PI-R ######################################
##############################################################################

def run_NEOPIR(pir_f, ffi_lsd_f, out_dir, public):
    
#####  create combined dataframe from FFI (lemon, lsd) and PIR items ####    

    cols_neo_pir = ['ID', 'NEOaBASEQ[NEO2]','NEOaBASEQ[NEO3]','NEOaBASEQ[NEO5]','NEOaBASEQ[NEO7r]','NEOaBASEQ[NEO8r]','NEOaBASEQ[NEO9]','NEOaBASEQ[NEO10r]','NEOaBASEQ[NEO12]',
                'NEOaBASEQ[NEO13]','NEOaBASEQ[NEO16]','NEObBASEQ[NEO17r]','NEObBASEQ[NEO18r]','NEObBASEQ[NEO20r]','NEObBASEQ[NEO21r]','NEObBASEQ[NEO22]','NEObBASEQ[NEO24r]',
                'NEObBASEQ[NEO27r]','NEObBASEQ[NEO29]','NEObBASEQ[NEO30r]','NEObBASEQ[NEO31]','NEOcBASEQ[NEO32r]','NEOcBASEQ[NEO33r]','NEOcBASEQ[NEO34]','NEOcBASEQ[NEO35r]',
                'NEOcBASEQ[NEO36r]','NEOcBASEQ[NEO38]','NEOcBASEQ[NEO42r]','NEOcBASEQ[NEO43r]','NEOcBASEQ[NEO47]','NEOcBASEQ[NEO48]','NEOdBASEQ[NEO49r]','NEOdBASEQ[NEO51]',
                'NEOdBASEQ[NEO52r]','NEOdBASEQ[NEO54]','NEOdBASEQ[NEO56r]','NEOdBASEQ[NEO57]','NEOdBASEQ[NEO58]','NEOdBASEQ[NEO60]','NEOdBASEQ[NEO62]','NEOdBASEQ[NEO63]',
                'NEOeBASEQ[NEO65]','NEOeBASEQ[NEO66]','NEOeBASEQ[NEO68r]','NEOeBASEQ[NEO69]','NEOeBASEQ[NEO70r]','NEOeBASEQ[NEO71r]','NEOeBASEQ[NEO72]','NEOeBASEQ[NEO73]',
                'NEOeBASEQ[NEO75]','NEOeBASEQ[NEO77r]','NEOfBASEQ[NEO78r]','NEOfBASEQ[NEO79]','NEOfBASEQ[NEO80r]','NEOfBASEQ[NEO81r]','NEOfBASEQ[NEO82]','NEOfBASEQ[NEO84r]',
                'NEOfBASEQ[NEO89]','NEOfBASEQ[NEO90r]','NEOfBASEQ[NEO92r]','NEOfBASEQ[NEO94]','NEOgBASEQ[NEO95r]','NEOgBASEQ[NEO96r]','NEOgBASEQ[NEO97]','NEOgBASEQ[NEO99r]',
                'NEOgBASEQ[NEO100]','NEOgBASEQ[NEO101]','NEOgBASEQ[NEO102r]','NEOgBASEQ[NEO103r]','NEOgBASEQ[NEO105r]','NEOgBASEQ[NEO106r]','NEOhBASEQ[NEO111]','NEOhBASEQ[NEO112r]',
                'NEOhBASEQ[NEO113r]','NEOhBASEQ[NEO114]','NEOhBASEQ[NEO115r]','NEOhBASEQ[NEO116r]','NEOhBASEQ[NEO117]','NEOhBASEQ[NEO118]','NEOhBASEQ[NEO119r]','NEOhBASEQ[NEO120]',
                'NEOiBASEQ[NEO121r]','NEOiBASEQ[NEO123]','NEOiBASEQ[NEO124r]','NEOiBASEQ[NEO125]','NEOiBASEQ[NEO126]','NEOiBASEQ[NEO127r]','NEOiBASEQ[NEO129]','NEOiBASEQ[NEO131]',
                'NEOiBASEQ[NEO132]','NEOiBASEQ[NEO133]','NEOjBASEQ[NEO134r]','NEOjBASEQ[NEO137r]','NEOjBASEQ[NEO138r]','NEOjBASEQ[NEO139]','NEOjBASEQ[NEO140r]','NEOjBASEQ[NEO141r]',
                'NEOjBASEQ[NEO143]','NEOjBASEQ[NEO144r]','NEOjBASEQ[NEO145]','NEOjBASEQ[NEO146]','NEOkBASEQ[NEO148r]','NEOkBASEQ[NEO149]','NEOkBASEQ[NEO150r]','NEOkBASEQ[NEO151]',
                'NEOkBASEQ[NEO152]','NEOkBASEQ[NEO153r]','NEOkBASEQ[NEO154]','NEOkBASEQ[NEO155r]','NEOkBASEQ[NEO156r]','NEOkBASEQ[NEO157]','NEOlBASEQ[NEO158]','NEOlBASEQ[NEO159r]',
                'NEOlBASEQ[NEO160]','NEOlBASEQ[NEO161]','NEOlBASEQ[NEO165]','NEOlBASEQ[NEO166r]','NEOlBASEQ[NEO167]','NEOlBASEQ[NEO168]','NEOlBASEQ[NEO169r]','NEOlBASEQ[NEO170]',
                'NEOmBASEQ[NEO171]','NEOmBASEQ[NEO172]','NEOmBASEQ[NEO174]','NEOmBASEQ[NEO175r]','NEOmBASEQ[NEO176r]','NEOmBASEQ[NEO178]','NEOmBASEQ[NEO179]','NEOmBASEQ[NEO180]',
                'NEOmBASEQ[NEO181r]','NEOmBASEQ[NEO182]','NEOnBASEQ[NEO183r]','NEOnBASEQ[NEO184]','NEOnBASEQ[NEO185]','NEOnBASEQ[NEO186]','NEOnBASEQ[NEO187r]','NEOnBASEQ[NEO189r]',
                'NEOnBASEQ[NEO190r]','NEOnBASEQ[NEO191]','NEOnBASEQ[NEO192]','NEOnBASEQ[NEO193]','NEOoBASEQ[NEO194]','NEOoBASEQ[NEO195]','NEOoBASEQ[NEO196]','NEOoBASEQ[NEO198r]',
                'NEOoBASEQ[NEO199r]','NEOoBASEQ[NEO201]','NEOoBASEQ[NEO202]','NEOoBASEQ[NEO204]','NEOoBASEQ[NEO205r]','NEOoBASEQ[NEO206r]','NEOpBASEQ[NEO207r]','NEOpBASEQ[NEO208r]',
                'NEOpBASEQ[NEO209]','NEOpBASEQ[NEO210]','NEOpBASEQ[NEO211]','NEOpBASEQ[NEO212]','NEOpBASEQ[NEO213r]','NEOpBASEQ[NEO214]','NEOpBASEQ[NEO215]','NEOpBASEQ[NEO216]',
                'NEOqBASEQ[NEO217]','NEOqBASEQ[NEO218]','NEOqBASEQ[NEO219r]','NEOqBASEQ[NEO220r]','NEOqBASEQ[NEO222r]','NEOqBASEQ[NEO223]','NEOqBASEQ[NEO224]','NEOqBASEQ[NEO225]',
                'NEOqBASEQ[NEO226]','NEOqBASEQ[NEO228r]','NEOrBASEQ[NEO230]','NEOrBASEQ[NEO231r]','NEOrBASEQ[NEO232]','NEOrBASEQ[NEO233]','NEOrBASEQ[NEO234r]','NEOrBASEQ[NEO235]',
                'NEOrBASEQ[NEO236r]','NEOrBASEQ[NEO238r]','NEOrBASEQ[NEO239]','NEOrBASEQ[NEO240]','NEOrBASEQ[NEO241]']
    
    cols_NEOFFI = ['ID', 'NEOFFI01[NEOFFI01]','NEOFFI01[NEOFFI02]','NEOFFI01[NEOFFI03]','NEOFFI01[NEOFFI04]','NEOFFI01[NEOFFI05]','NEOFFI01[NEOFFI06]','NEOFFI01[NEOFFI07]',
                   'NEOFFI01[NEOFFI08]','NEOFFI01[NEOFFI09]','NEOFFI01[NEOFFI10]','NEOFFI01[NEOFFI11]','NEOFFI01[NEOFFI12]','NEOFFI13[NEOFFI13]','NEOFFI13[NEOFFI14]',
                   'NEOFFI13[NEOFFI15]','NEOFFI13[NEOFFI16]','NEOFFI13[NEOFFI17]','NEOFFI13[NEOFFI18]','NEOFFI13[NEOFFI19]','NEOFFI13[NEOFFI20]','NEOFFI13[NEOFFI21]',
                   'NEOFFI13[NEOFFI22]','NEOFFI13[NEOFFI23]','NEOFFI13[NEOFFI24]','NEOFFI25[NEOFFI25]','NEOFFI25[NEOFFI26]','NEOFFI25[NEOFFI27]','NEOFFI25[NEOFFI28]',
                   'NEOFFI25[NEOFFI29]','NEOFFI25[NEOFFI30]','NEOFFI25[NEOFFI31]','NEOFFI25[NEOFFI32]','NEOFFI25[NEOFFI33]','NEOFFI25[NEOFFI34]','NEOFFI25[NEOFFI35]',
                   'NEOFFI25[NEOFFI36]','NEOFFI37[NEOFFI37]','NEOFFI37[NEOFFI38]','NEOFFI37[NEOFFI39]','NEOFFI37[NEOFFI40]','NEOFFI37[NEOFFI41]','NEOFFI37[NEOFFI42]',
                   'NEOFFI37[NEOFFI43]','NEOFFI37[NEOFFI44]','NEOFFI37[NEOFFI45]','NEOFFI37[NEOFFI46]','NEOFFI37[NEOFFI47]','NEOFFI37[NEOFFI48]','NEOFFI49[NEOFFI49]',
                   'NEOFFI49[NEOFFI50]','NEOFFI49[NEOFFI51]','NEOFFI49[NEOFFI52]','NEOFFI49[NEOFFI53]','NEOFFI49[NEOFFI54]','NEOFFI49[NEOFFI55]','NEOFFI49[NEOFFI56]',
                   'NEOFFI49[NEOFFI57]','NEOFFI49[NEOFFI58]','NEOFFI49[NEOFFI59]','NEOFFI49[NEOFFI60]']
     
    
    ##### Neo PI R lemon & lsd #### 
    
    df_pir = pd.read_csv(pir_f, sep = ",")[cols_neo_pir]
    # prep df
    df_pir['ID'].replace('LSD2', '25729', inplace = True)
    df_pir['ID'] = df_pir['ID'].map(lambda x: str(x)[0:5])
    
    # drop subject that was tested twice
    #idx_drop = df_pir[df_pir.ID == '26642'].index[0]
    #df_pir.drop(idx_drop, axis=0, inplace=True)
    #df_pir.set_index([range(len(df_pir.index))], inplace=True)
    
    # recode item names from complicated to item numbers
    new_items = []
    for item in df_pir.columns.values[1:]:
        item = item[13:]
        item = item[:-1]
        if item[-1] == 'r':
            item = item[:-1]
        new_items.append(item)
    dictionary1 = dict(zip(df_pir.columns.values[1:], new_items))
    df_pir.rename(columns=dictionary1, inplace=True)
    df_pir.dropna(inplace=True)
    
    
    
    ##### NEO FFI lsd #####
    
    df_ffi_lsd = pd.read_csv(ffi_lsd_f, sep = ",", converters={'ID':str})[cols_NEOFFI]
    
    # drop subject that was tested twice
    idx_drop = df_ffi_lsd[df_ffi_lsd.ID == '26642'].index[0]
    df_ffi_lsd.drop(idx_drop, axis=0, inplace=True)
    df_ffi_lsd.set_index([range(len(df_ffi_lsd.index))], inplace=True)
    
    # recode item names from complicated to 1-60
    new_items = []
    for item in df_ffi_lsd.columns.values[1:]:
        item = item[15:]
        item = item[:-1]
        item = int(item)
        item = str(item)
        new_items.append(item)
    dictionary2 = dict(zip(df_ffi_lsd.columns.values[1:], new_items))
    df_ffi_lsd.rename(columns=dictionary2, inplace=True)
    
    # recode ffi item numbers into pir item numbers
    ffi2pir = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Raw/Questionnaires/NEO/NEO KEY.xlsx', converters={0:str, 1:str})
    dictionary3 = dict(zip(ffi2pir['Neo FFI'],ffi2pir['NEO PI R']))
    df_ffi_lsd.rename(columns=dictionary3, inplace=True)
    df_ffi_lsd.dropna(inplace=True)
    df_ffi_lsd['project'] = 'lsd'
    
    
    
    ##### NEO FFI lemon #####
    
    # read in lemon ffi
    #df_ffi_lemon = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Raw/Questionnaires/NEO/NEO-FFI_60.csv').ix[:, 0:61]
    lemon_dir = '/nobackup/adenauer2/XNAT/Emotion Battery LEMON001-229_ 1-4 Rounds_CSV files'
    df_ffi_lemon = pd.read_csv('%s/NEO-FFI/NEO-FFI_60_dbid.csv' % lemon_dir,
                               converters={'ids':str})
    
    # adapt column names
    temp = ['ID'] + [str(int(x.replace('NEO-FFI_', ''))) for x in df_ffi_lemon.columns.values[1:]]
    df_ffi_lemon.rename(columns=dict(zip(df_ffi_lemon.columns.values, temp)), inplace=True)
    df_ffi_lemon['project'] = 'lemon'
    
    # recode ffi item numbers into pir item numbers
    df_ffi_lemon.rename(columns=dictionary3, inplace=True)
    
    
    
    ##### merge everything #####
    
    # combine FFI of lemon and lsd
    df_ffi = pd.concat([df_ffi_lemon, df_ffi_lsd])
    # merge FFI with PI R
    df_neo = pd.merge(df_pir, df_ffi, on='ID', how='inner')
    df_neo.rename(columns={'70_x':'70_pir', '70_y':'70'}, inplace=True)
    col_ordered = ['ID']+[str(x+1) for x in range(241) if x != 82]+['project']
    df =  df_neo[col_ordered].copy()
   

    # export
   
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    cols = [str(x+1) for x in range(241) if x != 82] # item 83 missing
    df.rename(columns=dict(zip(cols, ['NEO_%s' % x for x in cols])), inplace=True) 

    df.drop(['project', 'NEO_46', 'NEO_241'], axis=1, inplace = True) # removed because: item 46 was wrong and
                                                                      # item 241 not included in original neo
    df.drop('ID', axis=1, inplace = True)
    
    cols_export = list(df.columns.values[:len(df.columns.values)-1])
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/NEO-PI-R.csv' % out_dir, decimal='.', index=False)
        
    else:
        
        df[['ids'] + cols_export].ix[idx].to_csv('%s/NEO-PI-R.csv' % out_dir, decimal='.', index=False)   
    
    
  

##############################################################################
############# PSSI - Persönlichkeitsstil- und Störungsinventar################
##############################################################################

def run_PSSI(df, out_dir, public):
    
    cols = ['PSSaBASEQ[PSS1]','PSSaBASEQ[PSS2]','PSSaBASEQ[PSS3]','PSSaBASEQ[PSS4]','PSSaBASEQ[PSS5]','PSSaBASEQ[PSS6]','PSSaBASEQ[PSS7]','PSSaBASEQ[PSS8]','PSSaBASEQ[PSS9]',
             'PSSaBASEQ[PSS10]','PSSbBASEQ[PSS11]','PSSbBASEQ[PSS12]','PSSbBASEQ[PSS13]','PSSbBASEQ[PSS14]','PSSbBASEQ[PSS15r]','PSSbBASEQ[PSS16]','PSSbBASEQ[PSS17]',
             'PSSbBASEQ[PSS18]','PSSbBASEQ[PSS19]','PSSbBASEQ[PSS20]','PSScBASEQ[PSS21]','PSScBASEQ[PSS22]','PSScBASEQ[PSS23]','PSScBASEQ[PSS24]','PSScBASEQ[PSS25]',
             'PSScBASEQ[PSS26]','PSScBASEQ[PSS27]','PSScBASEQ[PSS28]','PSScBASEQ[PSS29]','PSScBASEQ[PSS30]','PSSdBASEQ[PSS31]','PSSdBASEQ[PSS32]','PSSdBASEQ[PSS33]',
             'PSSdBASEQ[PSS34]','PSSdBASEQ[PSS35]','PSSdBASEQ[PSS36]','PSSdBASEQ[PSS37]','PSSdBASEQ[PSS38]','PSSdBASEQ[PSS39r]','PSSdBASEQ[PSS40]','PSSeBASEQ[PSS41]',
             'PSSeBASEQ[PSS42]','PSSeBASEQ[PSS43r]','PSSeBASEQ[PSS44r]','PSSeBASEQ[PSS45]','PSSeBASEQ[PSS46]','PSSeBASEQ[PSS47]','PSSeBASEQ[PSS48]','PSSeBASEQ[PSS49r]',
             'PSSeBASEQ[PSS50]','PSSfBASEQ[PSS51]','PSSfBASEQ[PSS52]','PSSfBASEQ[PSS53]','PSSfBASEQ[PSS54]','PSSfBASEQ[PSS55]','PSSfBASEQ[PSS56]','PSSfBASEQ[PSS57]',
             'PSSfBASEQ[PSS58]','PSSfBASEQ[PSS59]','PSSfBASEQ[PSS60]','PSSgBASEQ[PSS61]','PSSgBASEQ[PSS62]','PSSgBASEQ[PSS63]','PSSgBASEQ[PSS64]','PSSgBASEQ[PSS65]',
             'PSSgBASEQ[PSS66]','PSSgBASEQ[PSS67r]','PSSgBASEQ[PSS68]','PSSgBASEQ[PSS69]','PSSgBASEQ[PSS70]','PSShBASEQ[PSS71r]','PSShBASEQ[PSS72r]','PSShBASEQ[PSS73]',
             'PSShBASEQ[PSS74]','PSShBASEQ[PSS75]','PSShBASEQ[PSS76]','PSShBASEQ[PSS77]','PSShBASEQ[PSS78]','PSShBASEQ[PSS79]','PSShBASEQ[PSS80]','PSSiBASEQ[PSS81]',
             'PSSiBASEQ[PSS82]','PSSiBASEQ[PSS83]','PSSiBASEQ[PSS84]','PSSiBASEQ[PSS85]','PSSiBASEQ[PSS86r]','PSSiBASEQ[PSS87]','PSSiBASEQ[PSS88]','PSSiBASEQ[PSS89]',
             'PSSiBASEQ[PSS90]','PSSjBASEQ[PSS91r]','PSSjBASEQ[PSS92]','PSSjBASEQ[PSS93]','PSSjBASEQ[PSS94]','PSSjBASEQ[PSS95]','PSSjBASEQ[PSS96]','PSSjBASEQ[PSS97]',
             'PSSjBASEQ[PSS98]','PSSjBASEQ[PSS99r]','PSSjBASEQ[PSS100]','PSSkBASEQ[PSS101]','PSSkBASEQ[PSS102]','PSSkBASEQ[PSS103]','PSSkBASEQ[PSS104r]','PSSkBASEQ[PSS105r]',
             'PSSkBASEQ[PSS106]','PSSkBASEQ[PSS107]','PSSkBASEQ[PSS108]','PSSkBASEQ[PSS109r]','PSSkBASEQ[PSS110]','PSSlBASEQ[PSS111]','PSSlBASEQ[PSS112]','PSSlBASEQ[PSS113]',
             'PSSlBASEQ[PSS114]','PSSlBASEQ[PSS115]','PSSlBASEQ[PSS116]','PSSlBASEQ[PSS117]','PSSlBASEQ[PSS118]','PSSlBASEQ[PSS119]','PSSlBASEQ[PSS120]','PSSmBASEQ[PSS121]',
             'PSSmBASEQ[PSS122]','PSSmBASEQ[PSS123]','PSSmBASEQ[PSS124]','PSSmBASEQ[PSS125]','PSSmBASEQ[PSS126]','PSSmBASEQ[PSS127]','PSSmBASEQ[PSS128]','PSSmBASEQ[PSS129]',
             'PSSmBASEQ[PSS130]','PSSnBASEQ[PSS131]','PSSnBASEQ[PSS132]','PSSnBASEQ[PSS133]','PSSnBASEQ[PSS134]','PSSnBASEQ[PSS135]','PSSnBASEQ[PSS136]','PSSnBASEQ[PSS137r]',
             'PSSnBASEQ[PSS138]','PSSnBASEQ[PSS139]','PSSnBASEQ[PSS140]']
        
    cols_export = ['PSSI_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/PSSI.csv' % out_dir, decimal='.', index=False)
        
    else:
                                                                
        df[['ids'] + cols_export].ix[idx].to_csv('%s/PSSI.csv' % out_dir, decimal='.', index=False)
  

##############################################################################
################################## MMI #######################################
##############################################################################

def run_MMI(df, out_dir, public):
    
    d = {'MMIaa': 'MMI_1_1',
         'MMIab': 'MMI_1_2',
         'MMIacBASEQ[MMI31]': 'MMI_1_3_A',
         'MMIacBASEQ[MMI32]': 'MMI_1_3_B',
         'MMIacBASEQ[MMI33]': 'MMI_1_3_C',
         'MMIacBASEQ[MMI34]': 'MMI_1_3_D',
         'MMIacBASEQ[MMI35]': 'MMI_1_3_E',
         'MMIadBASEQ[MMI410]': 'MMI_1_4_J',
         'MMIadBASEQ[MMI411]': 'MMI_1_4_K',
         'MMIadBASEQ[MMI412]': 'MMI_1_4_L',
         'MMIadBASEQ[MMI41]': 'MMI_1_4_A',
         'MMIadBASEQ[MMI42]': 'MMI_1_4_B',
         'MMIadBASEQ[MMI43]': 'MMI_1_4_C',
         'MMIadBASEQ[MMI44]': 'MMI_1_4_D',
         'MMIadBASEQ[MMI45]': 'MMI_1_4_E',
         'MMIadBASEQ[MMI46]': 'MMI_1_4_F',
         'MMIadBASEQ[MMI47]': 'MMI_1_4_G',
         'MMIadBASEQ[MMI48]': 'MMI_1_4_H',
         'MMIadBASEQ[MMI49]': 'MMI_1_4_I',
         'MMIae': 'MMI_2_1',
         'MMIaf': 'MMI_2_2',
         'MMIagBASEQ[MMI71]': 'MMI_2_3_A',
         'MMIagBASEQ[MMI72]': 'MMI_2_3_B',
         'MMIagBASEQ[MMI73]': 'MMI_2_3_C',
         'MMIagBASEQ[MMI74]': 'MMI_2_3_D',
         'MMIagBASEQ[MMI75]': 'MMI_2_3_E',
         'MMIahBASEQ[MMI810]': 'MMI_2_4_J',
         'MMIahBASEQ[MMI811]': 'MMI_2_4_K',
         'MMIahBASEQ[MMI812]': 'MMI_2_4_L',
         'MMIahBASEQ[MMI81]': 'MMI_2_4_A',
         'MMIahBASEQ[MMI82]': 'MMI_2_4_B',
         'MMIahBASEQ[MMI83]': 'MMI_2_4_C',
         'MMIahBASEQ[MMI84]': 'MMI_2_4_D',
         'MMIahBASEQ[MMI85]': 'MMI_2_4_E',
         'MMIahBASEQ[MMI86]': 'MMI_2_4_F',
         'MMIahBASEQ[MMI87]': 'MMI_2_4_G',
         'MMIahBASEQ[MMI88]': 'MMI_2_4_H',
         'MMIahBASEQ[MMI89]': 'MMI_2_4_I',
         'MMIai': 'MMI_3_1',
         'MMIaj': 'MMI_3_2',
         'MMIakBASEQ[MMI111]': 'MMI_3_3_A',
         'MMIakBASEQ[MMI112]': 'MMI_3_3_B',
         'MMIakBASEQ[MMI113]': 'MMI_3_3_C',
         'MMIakBASEQ[MMI114]': 'MMI_3_3_D',
         'MMIakBASEQ[MMI115]': 'MMI_3_3_E',
         'MMIalBASEQ[MMI1210]': 'MMI_3_4_J',
         'MMIalBASEQ[MMI1211]': 'MMI_3_4_K',
         'MMIalBASEQ[MMI1212]': 'MMI_3_4_L',
         'MMIalBASEQ[MMI121]': 'MMI_3_4_A',
         'MMIalBASEQ[MMI122]': 'MMI_3_4_B',
         'MMIalBASEQ[MMI123]': 'MMI_3_4_C',
         'MMIalBASEQ[MMI124]': 'MMI_3_4_D',
         'MMIalBASEQ[MMI125]': 'MMI_3_4_E',
         'MMIalBASEQ[MMI126]': 'MMI_3_4_F',
         'MMIalBASEQ[MMI127]': 'MMI_3_4_G',
         'MMIalBASEQ[MMI128]': 'MMI_3_4_H',
         'MMIalBASEQ[MMI129]': 'MMI_3_4_I',
         'MMIam': 'MMI_4_1',
         'MMIan': 'MMI_4_2',
         'MMIaoBASEQ[MMI151]': 'MMI_4_3_A',
         'MMIaoBASEQ[MMI152]': 'MMI_4_3_B',
         'MMIaoBASEQ[MMI153]': 'MMI_4_3_C',
         'MMIaoBASEQ[MMI154]': 'MMI_4_3_D',
         'MMIaoBASEQ[MMI155]': 'MMI_4_3_E',
         'MMIapBASEQ[MMI1610]': 'MMI_4_4_J',
         'MMIapBASEQ[MMI1611]': 'MMI_4_4_K',
         'MMIapBASEQ[MMI1612]': 'MMI_4_4_L',
         'MMIapBASEQ[MMI161]': 'MMI_4_4_A',
         'MMIapBASEQ[MMI162]': 'MMI_4_4_B',
         'MMIapBASEQ[MMI163]': 'MMI_4_4_C',
         'MMIapBASEQ[MMI164]': 'MMI_4_4_D',
         'MMIapBASEQ[MMI165]': 'MMI_4_4_E',
         'MMIapBASEQ[MMI166]': 'MMI_4_4_F',
         'MMIapBASEQ[MMI167]': 'MMI_4_4_G',
         'MMIapBASEQ[MMI168]': 'MMI_4_4_H',
         'MMIapBASEQ[MMI169]': 'MMI_4_4_I',
         'MMIaq': 'MMI_5_1',
         'MMIar': 'MMI_5_2',
         'MMIasBASEQ[MMI191]': 'MMI_5_3_A',
         'MMIasBASEQ[MMI192]': 'MMI_5_3_B',
         'MMIasBASEQ[MMI193]': 'MMI_5_3_C',
         'MMIasBASEQ[MMI194]': 'MMI_5_3_D',
         'MMIasBASEQ[MMI195]': 'MMI_5_3_E',
         'MMIatBASEQ[MMI2010]': 'MMI_5_4_J',
         'MMIatBASEQ[MMI2011]': 'MMI_5_4_K',
         'MMIatBASEQ[MMI2012]': 'MMI_5_4_L',
         'MMIatBASEQ[MMI201]': 'MMI_5_4_A',
         'MMIatBASEQ[MMI202]': 'MMI_5_4_B',
         'MMIatBASEQ[MMI203]': 'MMI_5_4_C',
         'MMIatBASEQ[MMI204]': 'MMI_5_4_D',
         'MMIatBASEQ[MMI205]': 'MMI_5_4_E',
         'MMIatBASEQ[MMI206]': 'MMI_5_4_F',
         'MMIatBASEQ[MMI207]': 'MMI_5_4_G',
         'MMIatBASEQ[MMI208]': 'MMI_5_4_H',
         'MMIatBASEQ[MMI209]': 'MMI_5_4_I',
         'MMIau': 'MMI_6_1',
         'MMIav': 'MMI_6_2',
         'MMIawBASEQ[MMI232]': 'MMI_6_3_B',
         'MMIawBASEQ[MMI233]': 'MMI_6_3_C',
         'MMIawBASEQ[MMI234]': 'MMI_6_3_D',
         'MMIawBASEQ[MMI235]': 'MMI_6_3_E',
         'MMIawBASEQ[MMI23]': 'MMI_6_3_A',
         'MMIaxBASEQ[MMI2410]': 'MMI_6_4_J',
         'MMIaxBASEQ[MMI2411]': 'MMI_6_4_K',
         'MMIaxBASEQ[MMI2412]': 'MMI_6_4_L',
         'MMIaxBASEQ[MMI241]': 'MMI_6_4_A',
         'MMIaxBASEQ[MMI242]': 'MMI_6_4_B',
         'MMIaxBASEQ[MMI243]': 'MMI_6_4_C',
         'MMIaxBASEQ[MMI244]': 'MMI_6_4_D',
         'MMIaxBASEQ[MMI245]': 'MMI_6_4_E',
         'MMIaxBASEQ[MMI246]': 'MMI_6_4_F',
         'MMIaxBASEQ[MMI247]': 'MMI_6_4_G',
         'MMIaxBASEQ[MMI248]': 'MMI_6_4_H',
         'MMIaxBASEQ[MMI249]': 'MMI_6_4_I',
         'MMIay': 'MMI_7_1',
         'MMIaz': 'MMI_7_2',
         'MMIbaBASEQ[MMI271]': 'MMI_7_3_A',
         'MMIbaBASEQ[MMI272]': 'MMI_7_3_B',
         'MMIbaBASEQ[MMI273]': 'MMI_7_3_C',
         'MMIbaBASEQ[MMI274]': 'MMI_7_3_D',
         'MMIbaBASEQ[MMI275]': 'MMI_7_3_E',
         'MMIbbBASEQ[MMI2810]': 'MMI_7_4_J',
         'MMIbbBASEQ[MMI2811]': 'MMI_7_4_K',
         'MMIbbBASEQ[MMI2812]': 'MMI_7_4_L',
         'MMIbbBASEQ[MMI281]': 'MMI_7_4_A',
         'MMIbbBASEQ[MMI282]': 'MMI_7_4_B',
         'MMIbbBASEQ[MMI283]': 'MMI_7_4_C',
         'MMIbbBASEQ[MMI284]': 'MMI_7_4_D',
         'MMIbbBASEQ[MMI285]': 'MMI_7_4_E',
         'MMIbbBASEQ[MMI286]': 'MMI_7_4_F',
         'MMIbbBASEQ[MMI287]': 'MMI_7_4_G',
         'MMIbbBASEQ[MMI288]': 'MMI_7_4_H',
         'MMIbbBASEQ[MMI289]': 'MMI_7_4_I',
         'MMIbc': 'MMI_8_1',
         'MMIbd': 'MMI_8_2',
         'MMIbeBASEQ[MMI311]': 'MMI_8_3_A',
         'MMIbeBASEQ[MMI312]': 'MMI_8_3_B',
         'MMIbeBASEQ[MMI313]': 'MMI_8_3_C',
         'MMIbeBASEQ[MMI314]': 'MMI_8_3_D',
         'MMIbeBASEQ[MMI315]': 'MMI_8_3_E',
         'MMIbfBASEQ[MMI3210]': 'MMI_8_4_J',
         'MMIbfBASEQ[MMI3211]': 'MMI_8_4_K',
         'MMIbfBASEQ[MMI3212]': 'MMI_8_4_L',
         'MMIbfBASEQ[MMI321]': 'MMI_8_4_A',
         'MMIbfBASEQ[MMI322]': 'MMI_8_4_B',
         'MMIbfBASEQ[MMI323]': 'MMI_8_4_C',
         'MMIbfBASEQ[MMI324]': 'MMI_8_4_D',
         'MMIbfBASEQ[MMI325]': 'MMI_8_4_E',
         'MMIbfBASEQ[MMI326]': 'MMI_8_4_F',
         'MMIbfBASEQ[MMI327]': 'MMI_8_4_G',
         'MMIbfBASEQ[MMI328]': 'MMI_8_4_H',
         'MMIbfBASEQ[MMI329]': 'MMI_8_4_I',
         'MMIbg': 'MMI_9_1',
         'MMIbh': 'MMI_9_2',
         'MMIbh[comment]': 'MMI_9_3',
         'MMIbi': 'MMI_9_4',
         'MMIbjBASEQ[MMI361]': 'MMI_9_5_A',
         'MMIbjBASEQ[MMI362]': 'MMI_9_5_B',
         'MMIbjBASEQ[MMI363]': 'MMI_9_5_C',
         'MMIbjBASEQ[MMI364]': 'MMI_9_5_D',
         'MMIbjBASEQ[MMI365]': 'MMI_9_5_E',
         'MMIbkBASEQ[MMI3710]': 'MMI_9_6_J',
         'MMIbkBASEQ[MMI3711]': 'MMI_9_6_K',
         'MMIbkBASEQ[MMI3712]': 'MMI_9_6_L',
         'MMIbkBASEQ[MMI371]': 'MMI_9_6_A',
         'MMIbkBASEQ[MMI372]': 'MMI_9_6_B',
         'MMIbkBASEQ[MMI373]': 'MMI_9_6_C',
         'MMIbkBASEQ[MMI374]': 'MMI_9_6_D',
         'MMIbkBASEQ[MMI375]': 'MMI_9_6_E',
         'MMIbkBASEQ[MMI376]': 'MMI_9_6_F',
         'MMIbkBASEQ[MMI377]': 'MMI_9_6_G',
         'MMIbkBASEQ[MMI378]': 'MMI_9_6_H',
         'MMIbkBASEQ[MMI379]': 'MMI_9_6_I',
         'MMIbl': 'MMI_10_1',
         'MMIbm': 'MMI_10_2',
         'MMIbnBASEQ[MMI402]': 'MMI_10_3_B',
         'MMIbnBASEQ[MMI403]': 'MMI_10_3_C',
         'MMIbnBASEQ[MMI404]': 'MMI_10_3_D',
         'MMIbnBASEQ[MMI405]': 'MMI_10_3_E',
         'MMIbnBASEQ[MMI40]': 'MMI_10_3_A',
         'MMIboBASEQ[MMI4110]': 'MMI_10_4_J',
         'MMIboBASEQ[MMI4111]': 'MMI_10_4_K',
         'MMIboBASEQ[MMI4112]': 'MMI_10_4_L',
         'MMIboBASEQ[MMI411]': 'MMI_10_4_A',
         'MMIboBASEQ[MMI412]': 'MMI_10_4_B',
         'MMIboBASEQ[MMI413]': 'MMI_10_4_C',
         'MMIboBASEQ[MMI414]': 'MMI_10_4_D',
         'MMIboBASEQ[MMI415]': 'MMI_10_4_E',
         'MMIboBASEQ[MMI416]': 'MMI_10_4_F',
         'MMIboBASEQ[MMI417]': 'MMI_10_4_G',
         'MMIboBASEQ[MMI418]': 'MMI_10_4_H',
         'MMIboBASEQ[MMI419]': 'MMI_10_4_I',
         'MMIbp': 'MMI_11_1',
         'MMIbq': 'MMI_11_2',
         'MMIbrBASEQ[MMI441]': 'MMI_11_3_A',
         'MMIbrBASEQ[MMI442]': 'MMI_11_3_B',
         'MMIbrBASEQ[MMI443]': 'MMI_11_3_C',
         'MMIbrBASEQ[MMI444]': 'MMI_11_3_D',
         'MMIbrBASEQ[MMI445]': 'MMI_11_3_E',
         'MMIbsBASEQ[MMI4510]': 'MMI_11_4_J',
         'MMIbsBASEQ[MMI4511]': 'MMI_11_4_K',
         'MMIbsBASEQ[MMI4512]': 'MMI_11_4_L',
         'MMIbsBASEQ[MMI451]': 'MMI_11_4_A',
         'MMIbsBASEQ[MMI452]': 'MMI_11_4_B',
         'MMIbsBASEQ[MMI453]': 'MMI_11_4_C',
         'MMIbsBASEQ[MMI454]': 'MMI_11_4_D',
         'MMIbsBASEQ[MMI455]': 'MMI_11_4_E',
         'MMIbsBASEQ[MMI456]': 'MMI_11_4_F',
         'MMIbsBASEQ[MMI457]': 'MMI_11_4_G',
         'MMIbsBASEQ[MMI458]': 'MMI_11_4_H',
         'MMIbsBASEQ[MMI459]': 'MMI_11_4_I',
         'MMIbt': 'MMI_12_1',
         'MMIbu': 'MMI_12_2',
         'MMIbvBASEQ[MMI481]': 'MMI_12_3_A',
         'MMIbvBASEQ[MMI482]': 'MMI_12_3_B',
         'MMIbvBASEQ[MMI483]': 'MMI_12_3_C',
         'MMIbvBASEQ[MMI484]': 'MMI_12_3_D',
         'MMIbvBASEQ[MMI485]': 'MMI_12_3_E',
         'MMIbwBASEQ[MMI4910]': 'MMI_12_4_J',
         'MMIbwBASEQ[MMI4911]': 'MMI_12_4_K',
         'MMIbwBASEQ[MMI4912]': 'MMI_12_4_L',
         'MMIbwBASEQ[MMI491]': 'MMI_12_4_A',
         'MMIbwBASEQ[MMI492]': 'MMI_12_4_B',
         'MMIbwBASEQ[MMI493]': 'MMI_12_4_C',
         'MMIbwBASEQ[MMI494]': 'MMI_12_4_D',
         'MMIbwBASEQ[MMI495]': 'MMI_12_4_E',
         'MMIbwBASEQ[MMI496]': 'MMI_12_4_F',
         'MMIbwBASEQ[MMI497]': 'MMI_12_4_G',
         'MMIbwBASEQ[MMI498]': 'MMI_12_4_H',
         'MMIbwBASEQ[MMI499]': 'MMI_12_4_I'}


    item_order = ['MMI_1_1',
                 'MMI_1_2',
                 'MMI_1_3_A',
                 'MMI_1_3_B',
                 'MMI_1_3_C',
                 'MMI_1_3_D',
                 'MMI_1_3_E',
                 'MMI_1_4_J',
                 'MMI_1_4_K',
                 'MMI_1_4_L',
                 'MMI_1_4_A',
                 'MMI_1_4_B',
                 'MMI_1_4_C',
                 'MMI_1_4_D',
                 'MMI_1_4_E',
                 'MMI_1_4_F',
                 'MMI_1_4_G',
                 'MMI_1_4_H',
                 'MMI_1_4_I',
                 'MMI_2_1',
                 'MMI_2_2',
                 'MMI_2_3_A',
                 'MMI_2_3_B',
                 'MMI_2_3_C',
                 'MMI_2_3_D',
                 'MMI_2_3_E',
                 'MMI_2_4_J',
                 'MMI_2_4_K',
                 'MMI_2_4_L',
                 'MMI_2_4_A',
                 'MMI_2_4_B',
                 'MMI_2_4_C',
                 'MMI_2_4_D',
                 'MMI_2_4_E',
                 'MMI_2_4_F',
                 'MMI_2_4_G',
                 'MMI_2_4_H',
                 'MMI_2_4_I',
                 'MMI_3_1',
                 'MMI_3_2',
                 'MMI_3_3_A',
                 'MMI_3_3_B',
                 'MMI_3_3_C',
                 'MMI_3_3_D',
                 'MMI_3_3_E',
                 'MMI_3_4_J',
                 'MMI_3_4_K',
                 'MMI_3_4_L',
                 'MMI_3_4_A',
                 'MMI_3_4_B',
                 'MMI_3_4_C',
                 'MMI_3_4_D',
                 'MMI_3_4_E',
                 'MMI_3_4_F',
                 'MMI_3_4_G',
                 'MMI_3_4_H',
                 'MMI_3_4_I',
                 'MMI_4_1',
                 'MMI_4_2',
                 'MMI_4_3_A',
                 'MMI_4_3_B',
                 'MMI_4_3_C',
                 'MMI_4_3_D',
                 'MMI_4_3_E',
                 'MMI_4_4_J',
                 'MMI_4_4_K',
                 'MMI_4_4_L',
                 'MMI_4_4_A',
                 'MMI_4_4_B',
                 'MMI_4_4_C',
                 'MMI_4_4_D',
                 'MMI_4_4_E',
                 'MMI_4_4_F',
                 'MMI_4_4_G',
                 'MMI_4_4_H',
                 'MMI_4_4_I',
                 'MMI_5_1',
                 'MMI_5_2',
                 'MMI_5_3_A',
                 'MMI_5_3_B',
                 'MMI_5_3_C',
                 'MMI_5_3_D',
                 'MMI_5_3_E',
                 'MMI_5_4_J',
                 'MMI_5_4_K',
                 'MMI_5_4_L',
                 'MMI_5_4_A',
                 'MMI_5_4_B',
                 'MMI_5_4_C',
                 'MMI_5_4_D',
                 'MMI_5_4_E',
                 'MMI_5_4_F',
                 'MMI_5_4_G',
                 'MMI_5_4_H',
                 'MMI_5_4_I',
                 'MMI_6_1',
                 'MMI_6_2',
                 'MMI_6_3_B',
                 'MMI_6_3_C',
                 'MMI_6_3_D',
                 'MMI_6_3_E',
                 'MMI_6_3_A',
                 'MMI_6_4_J',
                 'MMI_6_4_K',
                 'MMI_6_4_L',
                 'MMI_6_4_A',
                 'MMI_6_4_B',
                 'MMI_6_4_C',
                 'MMI_6_4_D',
                 'MMI_6_4_E',
                 'MMI_6_4_F',
                 'MMI_6_4_G',
                 'MMI_6_4_H',
                 'MMI_6_4_I',
                 'MMI_7_1',
                 'MMI_7_2',
                 'MMI_7_3_A',
                 'MMI_7_3_B',
                 'MMI_7_3_C',
                 'MMI_7_3_D',
                 'MMI_7_3_E',
                 'MMI_7_4_J',
                 'MMI_7_4_K',
                 'MMI_7_4_L',
                 'MMI_7_4_A',
                 'MMI_7_4_B',
                 'MMI_7_4_C',
                 'MMI_7_4_D',
                 'MMI_7_4_E',
                 'MMI_7_4_F',
                 'MMI_7_4_G',
                 'MMI_7_4_H',
                 'MMI_7_4_I',
                 'MMI_8_1',
                 'MMI_8_2',
                 'MMI_8_3_A',
                 'MMI_8_3_B',
                 'MMI_8_3_C',
                 'MMI_8_3_D',
                 'MMI_8_3_E',
                 'MMI_8_4_J',
                 'MMI_8_4_K',
                 'MMI_8_4_L',
                 'MMI_8_4_A',
                 'MMI_8_4_B',
                 'MMI_8_4_C',
                 'MMI_8_4_D',
                 'MMI_8_4_E',
                 'MMI_8_4_F',
                 'MMI_8_4_G',
                 'MMI_8_4_H',
                 'MMI_8_4_I',
                 'MMI_9_1',
                 'MMI_9_2',
                 'MMI_9_3',
                 'MMI_9_4',
                 'MMI_9_5_A',
                 'MMI_9_5_B',
                 'MMI_9_5_C',
                 'MMI_9_5_D',
                 'MMI_9_5_E',
                 'MMI_9_6_J',
                 'MMI_9_6_K',
                 'MMI_9_6_L',
                 'MMI_9_6_A',
                 'MMI_9_6_B',
                 'MMI_9_6_C',
                 'MMI_9_6_D',
                 'MMI_9_6_E',
                 'MMI_9_6_F',
                 'MMI_9_6_G',
                 'MMI_9_6_H',
                 'MMI_9_6_I',
                 'MMI_10_1',
                 'MMI_10_2',
                 'MMI_10_3_B',
                 'MMI_10_3_C',
                 'MMI_10_3_D',
                 'MMI_10_3_E',
                 'MMI_10_3_A',
                 'MMI_10_4_J',
                 'MMI_10_4_K',
                 'MMI_10_4_L',
                 'MMI_10_4_A',
                 'MMI_10_4_B',
                 'MMI_10_4_C',
                 'MMI_10_4_D',
                 'MMI_10_4_E',
                 'MMI_10_4_F',
                 'MMI_10_4_G',
                 'MMI_10_4_H',
                 'MMI_10_4_I',
                 'MMI_11_1',
                 'MMI_11_2',
                 'MMI_11_3_A',
                 'MMI_11_3_B',
                 'MMI_11_3_C',
                 'MMI_11_3_D',
                 'MMI_11_3_E',
                 'MMI_11_4_J',
                 'MMI_11_4_K',
                 'MMI_11_4_L',
                 'MMI_11_4_A',
                 'MMI_11_4_B',
                 'MMI_11_4_C',
                 'MMI_11_4_D',
                 'MMI_11_4_E',
                 'MMI_11_4_F',
                 'MMI_11_4_G',
                 'MMI_11_4_H',
                 'MMI_11_4_I',
                 'MMI_12_1',
                 'MMI_12_2',
                 'MMI_12_3_A',
                 'MMI_12_3_B',
                 'MMI_12_3_C',
                 'MMI_12_3_D',
                 'MMI_12_3_E',
                 'MMI_12_4_J',
                 'MMI_12_4_K',
                 'MMI_12_4_L',
                 'MMI_12_4_A',
                 'MMI_12_4_B',
                 'MMI_12_4_C',
                 'MMI_12_4_D',
                 'MMI_12_4_E',
                 'MMI_12_4_F',
                 'MMI_12_4_G',
                 'MMI_12_4_H',
                 'MMI_12_4_I']
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
    df.rename(columns=d, inplace=True)
    
    if public:
        
        # excluding pp comments
        remove = ['MMI_9_3']

        cols_export = [item for item in item_order if item not in remove]
        
        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/MMI.csv' % out_dir, decimal='.', index=False)
        
    else:
        
        # including pp comments
        cols_export = item_order
        
        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
        
        df[['ids'] + cols_export].ix[idx].to_csv('%s/MMI.csv' % out_dir, decimal='.', index=False)
  
  

##############################################################################
############################## BIS/BAS #######################################
##############################################################################

def run_BISBAS(df, out_dir, public):

    cols = ['BISBAS01[SQ001]','BISBAS02[SQ001]','BISBAS03[SQ001]','BISBAS04[SQ001]','BISBAS05[SQ001]','BISBAS06[SQ001]','BISBAS07[SQ001]','BISBAS08[SQ001]',
           'BISBAS09[SQ001]','BISBAS10[SQ001]','BISBAS11[SQ001]','BISBAS12[SQ001]','BISBAS13[SQ001]','BISBAS14[SQ001]','BISBAS15[SQ001]','BISBAS16[SQ001]',
           'BISBAS17[SQ001]','BISBAS18[SQ001]','BISBAS19[SQ001]','BISBAS20[SQ001]','BISBAS21[SQ001]','BISBAS22[SQ001]','BISBAS23[SQ001]','BISBAS24[SQ001]']
 
   
    cols_export = ['BISBAS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        
        # subject that was tested both in lemon and lsd, so remove from lsd
        idx.remove(df[df.ids == '26642'].index[0])
        
        # keep subjects with complete data 
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/BISBAS.csv' % out_dir, decimal='.', index=False)
        
    else:
                
        df[['ids'] + cols_export].ix[idx].to_csv('%s/BISBAS.csv' % out_dir, decimal='.', index=False)
  

      
##############################################################################
################################# STAI #######################################
##############################################################################

def run_STAI(df, out_dir, public):

    cols = ['STAI01[STAI01]','STAI01[STAI02]','STAI01[STAI03]','STAI01[STAI04]','STAI01[STAI05]','STAI01[STAI06]','STAI01[STAI07]','STAI01[STAI08]',
             'STAI01[STAI09]','STAI01[STAI10]','STAI11[STAI11]','STAI11[STAI12]','STAI11[STAI13]','STAI11[STAI14]','STAI11[STAI15]','STAI11[STAI16]',
             'STAI11[STAI17]','STAI11[STAI18]','STAI11[STAI19]','STAI11[STAI20]']


    cols_export = ['STAI_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        
        # subject that was tested both in lemon and lsd, so remove from lsd
        idx.remove(df[df.ids == '26642'].index[0])
        
        # keep subjects with complete data 
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/STAI-G-X2.csv' % out_dir, decimal='.', index=False)
        
    else:
               
        df[['ids'] + cols_export].ix[idx].to_csv('%s/STAI-G-X2.csv' % out_dir, decimal='.', index=False)
  


##############################################################################    
############################### STAXI ########################################
##############################################################################

def run_STAXI(df, out_dir, public):
        
    cols = ['STAXI01[STAXI01]','STAXI01[STAXI02]','STAXI01[STAXI03]','STAXI01[STAXI04]','STAXI01[STAXI05]','STAXI01[STAXI06]','STAXI01[STAXI07]',
          'STAXI01[STAXI08]','STAXI01[STAXI09]','STAXI01[STAXI10]','STAXI11[STAXI11]','STAXI11[STAXI12]','STAXI11[STAXI13]','STAXI11[STAXI14]','STAXI11[STAXI15]',
          'STAXI11[STAXI16]','STAXI11[STAXI17]','STAXI11[STAXI18]','STAXI11[STAXI19]','STAXI11[STAXI20]','STAXI21[STAXI21]','STAXI21[STAXI22]','STAXI21[STAXI23]',
          'STAXI21[STAXI24]','STAXI21[STAXI25]','STAXI21[STAXI26]','STAXI21[STAXI27]','STAXI21[STAXI28]','STAXI21[STAXI29]','STAXI21[STAXI30]','STAXI21[STAXI31]',
          'STAXI21[STAXI32]','STAXI21[STAXI33]','STAXI34[STAXI34]','STAXI34[STAXI35]','STAXI34[STAXI36]','STAXI34[STAXI37]','STAXI34[STAXI38]','STAXI34[STAXI39]',
          'STAXI34[STAXI40]','STAXI34[STAXI41]','STAXI34[STAXI42]','STAXI34[STAXI43]','STAXI34[STAXI44]']
    
    cols_export = ['STAXI_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        
        # subject that was tested both in lemon and lsd, so remove from lsd
        idx.remove(df[df.ids == '26642'].index[0])
        
        # keep subjects with complete data 
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/STAXI.csv' % out_dir, decimal='.', index=False)
        
    else:
            
        df[['ids'] + cols_export].ix[idx].to_csv('%s/STAXI.csv' % out_dir, decimal='.', index=False)
  


##############################################################################
#################### Gender Identitiy Questionnaire ##########################
##############################################################################

def run_MGIQ(df, out_dir, public):
    
    import numpy as np
    
    d = {'MGQ11BASEQ[MGQ11]': 'MGIQ_11',
         'MGQ11BASEQ[MGQ12]': 'MGIQ_12',
         'MGQ11BASEQ[MGQ13]': 'MGIQ_13',
         'MGQ11BASEQ[MGQ14]': 'MGIQ_14',
         'MGQ11BASEQ[MGQ15]': 'MGIQ_15',
         'MGQ11BASEQ[MGQ16]': 'MGIQ_16',
         'MGQ11BASEQ[MGQ17]': 'MGIQ_17',
         'MGQ11BASEQ[MGQ18]': 'MGIQ_18',
         'MGQ11BASEQ[MGQ19]': 'MGIQ_19',
         'MGQ1BASEQ[MGQ1]': 'MGIQ_1',
         'MGQ1BASEQ[MGQ2]': 'MGIQ_2',
         'MGQ20BASEQ[MGQ20]': 'MGIQ_20',
         'MGQ21BASEQ[MGQ21]': 'MGIQ_21',
         'MGQ22BASEQ[MGQ22]': 'MGIQ_22',
         'MGQ22BASEQ[MGQ23]': 'MGIQ_23',
         'MGQ24BASEQ[MGQ24]': 'MGIQ_24',
         'MGQ25BASEQ[MGQ25]': 'MGIQ_25',
         'MGQ25BASEQ[MGQ26]': 'MGIQ_26',
         'MGQ27BASEQ[MGQ27]': 'MGIQ_27',
         'MGQ27BASEQ[MGQ28]': 'MGIQ_28',
         'MGQ29BASEQ[MGQ29]': 'MGIQ_29',
         'MGQ29BASEQ[MGQ30]': 'MGIQ_30',
         'MGQ31BASEQ[MGQ31]': 'MGIQ_31',
         'MGQ31BASEQ[MGQ32]': 'MGIQ_32',
         'MGQ33': 'MGIQ_33',
         'MGQ33[other]': 'MGIQ_33_B',
         'MGQ34': 'MGIQ_34',
         'MGQ34[comment]': 'MGIQ_34_B',
         'MGQ35': 'MGIQ_34_C',
         'MGQ36': 'MGIQ_34_D',
         'MGQ37': 'MGIQ_35',
         'MGQ37[comment]': 'MGIQ_35_B',
         'MGQ38': 'MGIQ_36',
         'MGQ39': 'MGIQ_37',
         'MGQ3BASEQ[MGQ10]': 'MGIQ_10',
         'MGQ3BASEQ[MGQ3]': 'MGIQ_3',
         'MGQ3BASEQ[MGQ4]': 'MGIQ_4',
         'MGQ3BASEQ[MGQ5]': 'MGIQ_5',
         'MGQ3BASEQ[MGQ6]': 'MGIQ_6',
         'MGQ3BASEQ[MGQ7]': 'MGIQ_7',
         'MGQ3BASEQ[MGQ8]': 'MGIQ_8',
         'MGQ3BASEQ[MGQ9]': 'MGIQ_9',
         'MGQ40': 'MGIQ_38',
         'MGQ41': 'MGIQ_39',
         'MGQ42': 'MGIQ_40',
         'MGQ43BASEQ[MGQ431]': 'MGIQ_41_A',
         'MGQ43BASEQ[MGQ432]': 'MGIQ_41_B',
         'MGQ43BASEQ[MGQ433]': 'MGIQ_41_C',
         'MGQ43BASEQ[MGQ434]': 'MGIQ_41_D',
         'MGQ43BASEQ[MGQ435]': 'MGIQ_41_E',
         'MGQ43BASEQ[MGQ436]': 'MGIQ_41_F',
         'MGQ43BASEQ[MGQ437]': 'MGIQ_41_G',
         'MGQ43BASEQ[MGQ438]': 'MGIQ_41_H',
         'MGQ43BASEQ[MGQ439]': 'MGIQ_41_I',
         'MGQ43BASEQ[other]': 'MGIQ_41_J',
         'MGQ44BASEQ[MGQ44]': 'MGIQ_42',
         'MGQ44BASEQ[MGQ45]': 'MGIQ_43',
         'MGQ46': 'MGIQ_44',
         'MGQ46[other]': 'MGIQ_44_B',
         'MGQ47': 'MGIQ_45',
         'MGQ48': 'MGIQ_46',
         'MGQ48[other]': 'MGIQ_46_B',
         'MGQ49BASEQ[MGQ49a]': 'MGIQ_47_A',
         'MGQ49BASEQ[MGQ49b]': 'MGIQ_47_B',
         'MGQ49BASEQ[MGQ49c]': 'MGIQ_47_C',
         'MGQ49BASEQ[MGQ49d]': 'MGIQ_47_D',
         'MGQ49BASEQ[MGQ49e]': 'MGIQ_47_E',
         'MGQ49BASEQ[MGQ49f]': 'MGIQ_47_F',
         'MGQ49BASEQ[MGQ49g]': 'MGIQ_47_G',
         'MGQ49BASEQ[MGQ49h]': 'MGIQ_47_H',
         'MGQ49BASEQ[MGQ49i]': 'MGIQ_47_I',
         'MGQ49BASEQ[MGQ49j]': 'MGIQ_47_J',
         'MGQ49BASEQ[MGQ49k]': 'MGIQ_47_K',
         'MGQ49BASEQ[MGQ49l]': 'MGIQ_47_L',
         'MGQ49BASEQ[other]': 'MGIQ_47_M',
         'MGQ50BASEQ[MGQ50]': 'MGIQ_48',
         'MGQ50BASEQ[MGQ51]': 'MGIQ_49',
         'MGQ52BASEQ[MGQ52]': 'MGIQ_50',
         'MGQ52BASEQ[MGQ53]': 'MGIQ_51',
         'MGQ52BASEQ[MGQ54]': 'MGIQ_52',
         'MGQ52BASEQ[MGQ55]': 'MGIQ_53',
         'MGQ52BASEQ[MGQ56]': 'MGIQ_54',
         'MGQ52BASEQ[MGQ57]': 'MGIQ_55',
         'MGQ52BASEQ[MGQ58]': 'MGIQ_56',
         'MGQ52BASEQ[MGQ59]': 'MGIQ_57',
         'MGQ52BASEQ[MGQ60]': 'MGIQ_58',
         'MGQ52BASEQ[MGQ61]': 'MGIQ_59',
         'MGQ62BASEQ[MGQ62]': 'MGIQ_60',
         'MGQ62BASEQ[MGQ63]': 'MGIQ_61',
         'MGQ62BASEQ[MGQ64]': 'MGIQ_62',
         'MGQ62BASEQ[MGQ65]': 'MGIQ_63',
         'MGQ62BASEQ[MGQ66]': 'MGIQ_64',
         'MGQ62BASEQ[MGQ67]': 'MGIQ_65',
         'MGQ62BASEQ[MGQ68]': 'MGIQ_66',
         'MGQ62BASEQ[MGQ69]': 'MGIQ_67',
         'MGQ62BASEQ[MGQ70]': 'MGIQ_68',
         'MGQ62BASEQ[MGQ71]': 'MGIQ_69',
         'MGQ62BASEQ[MGQ72]': 'MGIQ_70',
         'MGQ73BASEQ[MGQ73]': 'MGIQ_71',
         'MGQ73BASEQ[MGQ74]': 'MGIQ_72',
         'MGQ73BASEQ[MGQ75]': 'MGIQ_73',
         'MGQ73BASEQ[MGQ76]': 'MGIQ_74',
         'MGQ73BASEQ[MGQ77]': 'MGIQ_75',
         'MGQ73BASEQ[MGQ78]': 'MGIQ_76',
         'MGQ73BASEQ[MGQ79]': 'MGIQ_77',
         'MGQ73BASEQ[MGQ80]': 'MGIQ_78',
         'MGQ73BASEQ[MGQ81]': 'MGIQ_79',
         'MGQ73BASEQ[MGQ82]': 'MGIQ_80',
         'MGQ73BASEQ[MGQ83]': 'MGIQ_81',
         'MGQ84BASEQ[MGQ84]': 'MGIQ_82',
         'MGQ85BASEQ[MGQ85]': 'MGIQ_83',
         'MGQ85BASEQ[MGQ86]': 'MGIQ_84',
         'MGQ85BASEQ[MGQ87]': 'MGIQ_85',
         'MGQ88BASEQ[MGQ88]': 'MGIQ_86',
         'MGQ89BASEQ[MGQ89]': 'MGIQ_87',
         'MGQ89BASEQ[MGQ90]': 'MGIQ_88',
         'MGQ89BASEQ[MGQ91]': 'MGIQ_89',
         'MGQ89BASEQ[MGQ92]': 'MGIQ_90',
         'MGQ89BASEQ[MGQ93]': 'MGIQ_91',
         'MGQ89BASEQ[MGQ94]': 'MGIQ_92',
         'MGQ89BASEQ[MGQ95]': 'MGIQ_93',
         'MGQ96BASEQ[MGQ100]': 'MGIQ_98',
         'MGQ96BASEQ[MGQ101]': 'MGIQ_99',
         'MGQ96BASEQ[MGQ102]': 'MGIQ_100',
         'MGQ96BASEQ[MGQ96]': 'MGIQ_94',
         'MGQ96BASEQ[MGQ97]': 'MGIQ_95',
         'MGQ96BASEQ[MGQ98]': 'MGIQ_96',
         'MGQ96BASEQ[MGQ99]': 'MGIQ_97'}
         
    item_order = ['MGIQ_1',
                  'MGIQ_2',
                  'MGIQ_3',
                  'MGIQ_4',
                  'MGIQ_5',
                  'MGIQ_6',
                  'MGIQ_7',
                  'MGIQ_8',
                  'MGIQ_9',
                  'MGIQ_10',
                  'MGIQ_11',
                  'MGIQ_12',
                  'MGIQ_13',
                  'MGIQ_14',
                  'MGIQ_15',
                  'MGIQ_16',
                  'MGIQ_17',
                  'MGIQ_18',
                  'MGIQ_19',
                  'MGIQ_20',
                  'MGIQ_21',
                  'MGIQ_22',
                  'MGIQ_23',
                  'MGIQ_24',
                  'MGIQ_25',
                  'MGIQ_26',
                  'MGIQ_27',
                  'MGIQ_28',
                  'MGIQ_29',
                  'MGIQ_30',
                  'MGIQ_31',
                  'MGIQ_32',
                  'MGIQ_33',
                  'MGIQ_33_B',
                  'MGIQ_34',
                  'MGIQ_34_B',
                  'MGIQ_34_C',
                  'MGIQ_34_D',
                  'MGIQ_35',
                  'MGIQ_35_B',
                  'MGIQ_36',
                  'MGIQ_37',
                  'MGIQ_38',
                  'MGIQ_39',
                  'MGIQ_40',
                  'MGIQ_41_A',
                  'MGIQ_41_B',
                  'MGIQ_41_C',
                  'MGIQ_41_D',
                  'MGIQ_41_E',
                  'MGIQ_41_F',
                  'MGIQ_41_G',
                  'MGIQ_41_H',
                  'MGIQ_41_I',
                  'MGIQ_41_J',
                  'MGIQ_42',
                  'MGIQ_43',
                  'MGIQ_44',
                  'MGIQ_44_B',
                  'MGIQ_45',
                  'MGIQ_46',
                  'MGIQ_46_B',
                  'MGIQ_47_A',
                  'MGIQ_47_B',
                  'MGIQ_47_C',
                  'MGIQ_47_D',
                  'MGIQ_47_E',
                  'MGIQ_47_F',
                  'MGIQ_47_G',
                  'MGIQ_47_H',
                  'MGIQ_47_I',
                  'MGIQ_47_J',
                  'MGIQ_47_K',
                  'MGIQ_47_L',
                  'MGIQ_47_M',
                  'MGIQ_48',
                  'MGIQ_49',
                  'MGIQ_50',
                  'MGIQ_51',
                  'MGIQ_52',
                  'MGIQ_53',
                  'MGIQ_54',
                  'MGIQ_55',
                  'MGIQ_56',
                  'MGIQ_57',
                  'MGIQ_58',
                  'MGIQ_59',
                  'MGIQ_60',
                  'MGIQ_61',
                  'MGIQ_62',
                  'MGIQ_63',
                  'MGIQ_64',
                  'MGIQ_65',
                  'MGIQ_66',
                  'MGIQ_67',
                  'MGIQ_68',
                  'MGIQ_69',
                  'MGIQ_70',
                  'MGIQ_71',
                  'MGIQ_72',
                  'MGIQ_73',
                  'MGIQ_74',
                  'MGIQ_75',
                  'MGIQ_76',
                  'MGIQ_77',
                  'MGIQ_78',
                  'MGIQ_79',
                  'MGIQ_80',
                  'MGIQ_81',
                  'MGIQ_82',
                  'MGIQ_83',
                  'MGIQ_84',
                  'MGIQ_85',
                  'MGIQ_86',
                  'MGIQ_87',
                  'MGIQ_88',
                  'MGIQ_89',
                  'MGIQ_90',
                  'MGIQ_91',
                  'MGIQ_92',
                  'MGIQ_93',
                  'MGIQ_94',
                  'MGIQ_95',
                  'MGIQ_96',
                  'MGIQ_97',
                  'MGIQ_98',
                  'MGIQ_99',
                  'MGIQ_100']   

    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
    df.rename(columns=d, inplace=True)
       
    if public:
        # excluding pp comments
        remove = ['MGIQ_33_B', 'MGIQ_34_B', 'MGIQ_35_B', 'MGIQ_40',
                  'MGIQ_41_J', 'MGIQ_44_B', 'MGIQ_46_B', 'MGIQ_47_M']

        cols_export = [item for item in item_order if item not in remove]
        
        # subjects with at least one data entry
        df = df.replace(r'\s+', np.nan, regex=True) # removing white spaces
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/MGIQ.csv' % out_dir, decimal='.', index=False)     
        
    else:
        # including pp comments
        cols_export = item_order
        
        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index
        
        df[['ids'] + cols_export].ix[idx].to_csv('%s/MGIQ.csv' % out_dir, decimal='.', index=False) 



##############################################################################
#################### childhood trauma questionnaire ##########################
##############################################################################

def run_CTQ(df, out_dir, public):
    
    cols = ['ChildTraum1BASE[1]', 'ChildTraum1BASE[2]', 'ChildTraum1BASE[3]',
           'ChildTraum1BASE[4]', 'ChildTraum1BASE[5]', 'ChildTraum1BASE[6]',
           'ChildTraum1BASE[7]', 'ChildTraum1BASE[8]', 'ChildTraum1BASE[9]',
           'ChildTraum2BASE[10]', 'ChildTraum2BASE[11]', 'ChildTraum2BASE[12]',
           'ChildTraum2BASE[13]', 'ChildTraum2BASE[14]', 'ChildTraum2BASE[15]',
           'ChildTraum2BASE[16]', 'ChildTraum2BASE[17]', 'ChildTraum2BASE[18]',
           'ChildTraum3BASE[19]', 'ChildTraum3BASE[20]', 'ChildTraum3BASE[21]',
           'ChildTraum3BASE[22]', 'ChildTraum3BASE[23]', 'ChildTraum3BASE[24]',
           'ChildTraum3BASE[25]', 'ChildTraum3BASE[26]', 'ChildTraum3BASE[27]',
           'ChildTraum3BASE[28]']
        
    cols_export = ['CTQ_%s' % (x+1) for x in range(len(cols))] 
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/CTQ.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/CTQ.csv' % out_dir, decimal='.', index=False)
        
        
##############################################################################
########################### short NYC-Q pre-scan #############################
############################################################################## 

def run_NYCQ_prescan(df, out_dir, public):
        
    cols = ['1', '2', '3', '4', '5', '6', 
            '7', '8', '9','10', '11', '12']
    
    for col in cols:
        df[col] = 100 * df[col] / 15.2

        
    cols_export = ['NYCQ_prescan_%s' % x for x in cols]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/Short-NYC-Q_prescan.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/Short-NYC-Q_prescan.csv' % out_dir, decimal='.', index=False)
    
        

###############################################################################
####################### short NYC-Q during scanning ###########################
###############################################################################

def run_NYCQ_inscan(df, scan, out_dir, public):

    df = df[df.scan == scan]
    
    cols = ['positive', 'negative', 'future', 'past', 'myself', 'people', 'surrpundings', 
            'vigilance', 'images', 'words', 'specific_vague', 'intrusive']

    cols_export = ['NYCQ_inscan%s_%s' % (scan,x) for x in cols]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ids'].map(lambda x: str(x)[0:5])
    
    if public:
    
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                               header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)

        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)

        df[['ids'] + cols_export].to_csv('%s/Short-NYC-Q_inscan%s.csv' % (out_dir,scan), 
                                                           decimal='.', index=False)

    else:

         df[['ids'] + cols_export].ix[idx].to_csv('%s/Short-NYC-Q_inscan%s.csv' % (out_dir,scan), 
                                                                         decimal='.', index=False)



##############################################################################
######################## LIMIT - NYC-Q post scan #############################
##############################################################################
        
def run_NYCQ_postscan(df, out_dir, public):
    
    cols = ['Q01', 'Q02', 'Q03', 'Q04', 'Q05', 'Q06', 'Q07', 'Q08', 
            'Q09', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16',
            'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 
            'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31']
            
    cols_export = ['NYCQ_postscan_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/NYC-Q_postscan.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/NYC-Q_postscan.csv' % out_dir, decimal='.', index=False)
        
        

##############################################################################
##################### short NYC-Q post emotional task switching ##############
##############################################################################                
    
def run_NYCQ_postETS(df, out_dir, public):
    
    cols = ['1', '2', '3', '4','5', '6', '7', '8', '9', '10', '11', '12']
    
    for col in cols:
        df[col] = 100 * df[col] / 15.2
    
    cols_export = ['NYCQ_postETS_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/Short-NYC-Q_postETS.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/Short-NYC-Q_postETS.csv' % out_dir, decimal='.', index=False)

        

##############################################################################
############################## Facebook Intensity ############################
##############################################################################

def run_FIS(df, out_dir, public):
    
    
    
    cols = ["FACE0BASEQ","FACE1aBASEQ","FACE1bBASEQ","FACE2aBASEQ",
            "FACE2bBASEQ","FACE3BASEQ","FACE4BASEQ[FACE4]","FACE4BASEQ[FACE5]",
            "FACE4BASEQ[FACE6]","FACE4BASEQ[FACE7]","FACE4BASEQ[FACE8]",
            "FACE4BASEQ[FACE9]"]
        
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
    df.rename(columns=dict(zip(cols, ['FBI_%s' % (x+1) for x in range(len(cols))])), inplace=True)
    
    # change date entry to number of years
    df['datestamp'] = pd.to_datetime(df['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df['FBI_2'] = pd.to_datetime(df['FBI_2'], format='%Y-%m-%d %H:%M:%S')
    df['FBI_2'] = pd.Series(df['datestamp'] - df['FBI_2']).dt.days / 365
    
    cols_export = ['FBI_%s' % (x+1) for x in range(len(cols))]
    
    if public:
        
        # remove subjects with missing indication of FB membership and unplausible date
        df.set_index([range(len(df.index))], inplace=True)
        remove = df.index[(df["FBI_1"].isnull()) & ((df["FBI_2"].isnull()) | (df["FBI_2"] < 0))]
        df.drop(df.index[remove], inplace=True)
    
        # bin years of membership
        age_bins = [0, 4, 8, 12]
        age_labels = ['0-4', '4-8', '8-12']
        df['FBI_2'] = pd.cut(df['FBI_2'], age_bins, labels=age_labels)

        # bin number of friends
        friends_bins = [0, 200, 400, 600, 800, 1000]
        friends_labels = ['0-199', '200-399', '400-599', '600-799', '800-1000']
        df['FBI_4'] = pd.cut(df['FBI_4'], friends_bins, labels=friends_labels)

        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index

        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/FBI.csv' % out_dir, decimal='.', index=False) 
        
    else:
        
        cols_export = ['FBI_%s' % (x+1) for x in range(len(cols))]

        # subjects with at least one data entry
        df.set_index([range(len(df.index))], inplace=True)
        idx = df[cols_export].dropna(how='all').index

        df[['ids'] + cols_export].ix[idx].to_csv('%s/FBI.csv' % out_dir, decimal='.', index=False)        



##############################################################################
############################ mobile phone usage ###############################
##############################################################################

def run_mobile(df, out_dir, public):
    
    cols = ['HND1', 'HND2', 'HND3', 'HND4', 'HND5', 'HND6', 'HND7', 'HND8', 
            'HND9', 'HND10', 'HND11', 'HND12', 'HND13', 'HND14', 'HND15', 
            'HND16', 'HND17', 'HND18', 'HND19']        
        
    cols_export = ['MPU_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/MPU.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/MPU.csv' % out_dir, decimal='.', index=False)
        
        
        
##############################################################################
######################## LIMIT - NYC-Q  in Survey C ##########################
##############################################################################
      
def run_NYCQ_posttasks(df, out_dir, public):
    
    cols = ['LMTaBASEQ[LMT1]', 'LMTaBASEQ[LMT2]', 'LMTaBASEQ[LMT3]',
           'LMTaBASEQ[LMT4]', 'LMTaBASEQ[LMT5]', 'LMTaBASEQ[LMT6]',
           'LMTaBASEQ[LMT7]', 'LMTaBASEQ[LMT8]', 'LMTaBASEQ[LMT9]',
           'LMTaBASEQ[LMT10]', 'LMTbBASEQ[LMT11]', 'LMTbBASEQ[LMT12]',
           'LMTbBASEQ[LMT13]', 'LMTbBASEQ[LMT14]', 'LMTbBASEQ[LMT15]',
           'LMTbBASEQ[LMT16]', 'LMTbBASEQ[LMT17]', 'LMTbBASEQ[LMT18]',
           'LMTcBASEQ[LMT19]', 'LMTcBASEQ[LMT20]', 'LMTcBASEQ[LMT21]',
           'LMTcBASEQ[LMT22]', 'LMTcBASEQ[LMT23]']
        
    cols_export = ['NYCQ_posttasks_%s' % (x+1) for x in range(len(cols))]
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
    
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/NYC-Q_posttasks.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/NYC-Q_posttasks.csv' % out_dir, decimal='.', index=False) 
        
        
        
##############################################################################
###################### Synesthesia color picker test #########################
##############################################################################        
      
def run_syn(df, out_dir, public):
    
    df['consistency'] = df['consistency'].astype('float')
    df = df[~ pd.isnull(df.consistency)]
 
    cols = ['consistency', 'notes']
    cols_export = ['SYN_consistency', 'SYN_notes']
    df.rename(columns=dict(zip(cols, cols_export)), inplace=True)
    
    # subjects with at least one data entry
    df.set_index([range(len(df.index))], inplace=True)
    idx = df[cols_export].dropna(how='all').index
     
    df['ids'] = df['ID'].map(lambda x: str(x)[0:5])
    
    if public:
        
        # subjects with MRI data
        subjects_mri = pd.read_csv('/nobackup/adenauer2/LSD/Originals/Documentation/subjects_mri', 
                                   header=None, dtype=str)[0]
        idx_mri = df.index[df.ids.isin(subjects_mri)]

        # subjects with both data for questionnaire and MRI
        idx = list(set(idx).intersection(idx_mri))
        df = df.iloc[idx]
        df.set_index([range(len(df.index))], inplace=True)
        
        # anonymize IDs
        converter = pd.read_excel('/nobackup/adenauer2/LSD/Originals/Documentation/lookup_table.xlsx',
                                  converters={'ids_probanden_db' : str, 'ids_xnat_publicp' : str})
        converter_dict = dict(zip(converter['ids_probanden_db'], converter['ids_xnat_publicp']))

        df.replace({'ids': converter_dict}, inplace=True)
        
        df[['ids'] + cols_export].to_csv('%s/SYN.csv' % out_dir, decimal='.', index=False)
        
    else:

        df[['ids'] + cols_export].ix[idx].to_csv('%s/SYN.csv' % out_dir, decimal='.', index=False)    