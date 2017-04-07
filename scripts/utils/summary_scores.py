# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:35:28 2015

@author: oligschlager
"""


import pandas as pd
import seaborn as sns
import numpy as np

sns.set_style('white')



##############################################################################
#################### Creative Achievement Questionnaire ######################
##############################################################################

def run_CAQ(df, out_dir=None):

    zero = ['CAQ_14','CAQ_22','CAQ_31','CAQ_40','CAQ_49','CAQ_58','CAQ_66','CAQ_76','CAQ_86','CAQ_95']
    one = ['CAQ_15','CAQ_23','CAQ_32','CAQ_41','CAQ_50','CAQ_59','CAQ_67','CAQ_77','CAQ_87','CAQ_96']
    two = ['CAQ_16','CAQ_24','CAQ_33','CAQ_42','CAQ_51','CAQ_60','CAQ_68','CAQ_78','CAQ_88','CAQ_97']
    three = ['CAQ_17','CAQ_25','CAQ_34','CAQ_43','CAQ_52','CAQ_61','CAQ_69','CAQ_79','CAQ_89','CAQ_98']
    four = ['CAQ_18','CAQ_26','CAQ_35','CAQ_44','CAQ_53','CAQ_62','CAQ_70','CAQ_80','CAQ_90','CAQ_99']
    five = ['CAQ_19', 'CAQ_27', 'CAQ_36', 'CAQ_45', 'CAQ_54', 'CAQ_63', 'CAQ_71', 'CAQ_81', 'CAQ_91', 'CAQ_100']
    six = ['CAQ_20', 'CAQ_28', 'CAQ_37', 'CAQ_46', 'CAQ_55', 'CAQ_64', 'CAQ_72', 'CAQ_83', 'CAQ_92', 'CAQ_101']
    seven = ['CAQ_29', 'CAQ_38', 'CAQ_47', 'CAQ_56', 'CAQ_65', 'CAQ_74', 'CAQ_85', 'CAQ_93', 'CAQ_102']

    df[one] = df[one] * 1
    df[two] = df[two] * 2
    df[three] = df[three] * 3
    df[four] = df[four] * 4
    df[five] = df[five] * 5
    df[six] = df[six] * 6
    df[seven] =df[seven] * 7

    #only the questions for patents, scientific achievements and movies have scores and are used!
    for col in ['CAQ_73', 'CAQ_94', 'CAQ_84']:

        for i in df.index:

            try:
                df[col].iloc[i] = int(df[col].iloc[i]) * 7
            except:
                df[col].iloc[i] = 0


    df['seven_sum'] = df[['CAQ_73', 'CAQ_94', 'CAQ_84']].sum(axis=1)

    df['CAQ_score'] = np.log(df[one + two + three + four + five + six + ['seven_sum']].sum(axis=1))

    cols_export = ['ids'] + ['CAQ_score']

    df[cols_export].to_csv('%s/CAQ.csv' % out_dir, decimal='.', index=False)


##############################################################################
#################### Meta Cognition Questionnaire 30 #########################
##############################################################################

def run_MCQ30(df, out_dir):


    df['MCQ_lack_of_cogn_conf_mean'] = df[['MCQ_1', 'MCQ_6', 'MCQ_11',
                                          'MCQ_16', 'MCQ_21', 'MCQ_26']].mean(axis=1)

    df['MCQ_pos_bel_about_worry_mean'] = df[['MCQ_2', 'MCQ_7',  'MCQ_12',
                                             'MCQ_17','MCQ_22','MCQ_27']].mean(axis=1)

    df['MCQ_cogn_self-consc_mean'] = df[['MCQ_3', 'MCQ_8',  'MCQ_13',
                                        'MCQ_18','MCQ_23','MCQ_28']].mean(axis=1)

    df['MCQ_neg_bel_about_uncontr_danger_mean'] = df[['MCQ_4', 'MCQ_9', 'MCQ_14',
                                                     'MCQ_19', 'MCQ_24', 'MCQ_29']].mean(axis=1)

    df['MCQ_need_contr_thoughts_mean'] = df[['MCQ_5','MCQ_10', 'MCQ_15',
                                            'MCQ_20', 'MCQ_25', 'MCQ_30']].mean(axis=1)


    cols_export = ['ids'] + ['MCQ_lack_of_cogn_conf_mean',
                             'MCQ_pos_bel_about_worry_mean',
                             'MCQ_cogn_self-consc_mean',
                             'MCQ_neg_bel_about_uncontr_danger_mean',
                             'MCQ_need_contr_thoughts_mean']

    df[cols_export].to_csv('%s/MCQ30.csv' % out_dir, decimal='.', index=False)



##############################################################################
#################### Body Consciousness Questionnaire ########################
##############################################################################

def run_BCQ(df, out_dir):

    df['BCQ_private_body_mean'] = df[['BCQ_3', 'BCQ_4','BCQ_5',
                                     'BCQ_8', 'BCQ_12',]].mean(axis=1)

    df['BCQ_public_body_mean'] = df[['BCQ_1', 'BCQ_7', 'BCQ_10',
                                    'BCQ_11', 'BCQ_13','BCQ_15']].mean(axis=1)

    df['BCQ_body_competence_mean'] = df[['BCQ_2', 'BCQ_6',
                                        'BCQ_9', 'BCQ_14']].mean(axis=1)


    cols_export = ['ids'] + ['BCQ_private_body_mean',
                             'BCQ_public_body_mean',
                             'BCQ_body_competence_mean']

    df[cols_export].to_csv('%s/BCQ.csv' % out_dir, decimal='.', index=False)



##############################################################################
################### Five Facet Mindfulness Questionnaire #####################
##############################################################################

def run_FFMQ(df, out_dir):

    #items to be recoded
    items_recoded = ['FFMQ_12',
                     'FFMQ_16',
                     'FFMQ_22',
                     'FFMQ_5',
                     'FFMQ_8',
                     'FFMQ_13',
                     'FFMQ_18',
                     'FFMQ_23',
                     'FFMQ_28',
                     'FFMQ_34',
                     'FFMQ_38',
                     'FFMQ_3',
                     'FFMQ_10',
                     'FFMQ_14',
                     'FFMQ_17',
                     'FFMQ_25',
                     'FFMQ_30',
                     'FFMQ_35',
                     'FFMQ_39']

    #recode items
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')


    df['FFMQ_observe_sum'] = df[['FFMQ_1', 'FFMQ_6','FFMQ_11', 'FFMQ_15',
                                 'FFMQ_20','FFMQ_26','FFMQ_31', 'FFMQ_36',]].sum(axis=1)

    df['FFMQ_describe_sum'] = df[['FFMQ_2', 'FFMQ_7', 'FFMQ_12', 'FFMQ_16',
                                  'FFMQ_22', 'FFMQ_27', 'FFMQ_32', 'FFMQ_37']].sum(axis=1)

    df['FFMQ_act_awareness_sum'] = df[['FFMQ_5', 'FFMQ_8','FFMQ_13', 'FFMQ_18',
                                       'FFMQ_23', 'FFMQ_28', 'FFMQ_34', 'FFMQ_38']].sum(axis=1)

    df['FFMQ_nonjudge_sum'] = df[['FFMQ_3', 'FFMQ_10', 'FFMQ_14', 'FFMQ_17',
                                  'FFMQ_25', 'FFMQ_30','FFMQ_35', 'FFMQ_39']].sum(axis=1)

    df['FFMQ_nonreact_sum'] = df[['FFMQ_4',  'FFMQ_9', 'FFMQ_19',  'FFMQ_21',
                                  'FFMQ_24', 'FFMQ_29', 'FFMQ_33']].sum(axis=1)

    cols_export = ['ids'] + ['FFMQ_observe_sum',
                             'FFMQ_describe_sum',
                             'FFMQ_act_awareness_sum',
                             'FFMQ_nonjudge_sum',
                             'FFMQ_nonreact_sum']

    df[cols_export].to_csv('%s/FFMQ.csv' % out_dir, decimal='.', index=False)



##############################################################################
#################### Abbreviated Math Anxiety Scale ##########################
##############################################################################

def run_AMAS(df, out_dir):


    #Calculate total score as the sum of Item 1-9.

    cols = ['AMAS_1',
            'AMAS_2',
            'AMAS_3',
            'AMAS_4',
            'AMAS_5',
            'AMAS_6',
            'AMAS_7',
            'AMAS_8',
            'AMAS_9']

    df['AMAS_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['AMAS_sum']

    df[cols_export].to_csv('%s/AMAS.csv' % out_dir, decimal='.', index=False)



##############################################################################
########################## self control scale ################################
##############################################################################

def run_SelfCtrl(df, out_dir):
    #items to be recoded
    items_recoded = ['SCS_2',
                     'SCS_3',
                     'SCS_4',
                     'SCS_5',
                     'SCS_6',
                     'SCS_7',
                     'SCS_8',
                     'SCS_10',
                     'SCS_11' ]

    #recode items
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-13.

    cols = ['SCS_1',
            'SCS_2',
            'SCS_3',
            'SCS_4',
            'SCS_5',
            'SCS_6',
            'SCS_7',
            'SCS_8',
            'SCS_9',
            'SCS_10',
            'SCS_11',
            'SCS_12',
            'SCS_13']

    df['SCS_SelfCtrl_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['SCS_SelfCtrl_sum']

    df[cols_export].to_csv('%s/SCS.csv' % out_dir, decimal='.', index=False)



##############################################################################
################ Internet Addiction test #####################################
##############################################################################
#note: Item 3 not included due to differerent scale format

def run_IAT(df, out_dir):

    #Calculate total score as the sum of Item 1-19.

    cols = ['IAT_1',
            'IAT_2',
            'IAT_3',
            'IAT_4',
            'IAT_5',
            'IAT_6',
            'IAT_7',
            'IAT_8',
            'IAT_9',
            'IAT_10',
            'IAT_11',
            'IAT_12',
            'IAT_13',
            'IAT_14',
            'IAT_15',
            'IAT_16',
            'IAT_17',
            'IAT_18',
            'IAT_19',
            'IAT_20']

    #recode items
    recoder = {1:1, 2:2, 3:3, 4:4, 5:5, 6:0}
    for i in cols:
        df[i] = df[i].map(recoder).astype('float64')


    df['IAT_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ["IAT_sum"]

    df[cols_export].to_csv('%s/IAT.csv' % out_dir, decimal='.', index=False)



##############################################################################
########################### Arten innerer Sprache ############################
#################### varieties of inner speech (VIS) #########################
##############################################################################

def run_VIS(df, out_dir=None):
    #items to be recoded
    items_recoded = ['VIS_7',
                     'VIS_15']
    #recode items
    recoder = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate subscales (Dialogic, Condensed, Otherpeople, Evaluative/Motivat.) - sumscores
    #dialogic inner speech

    df['VIS_dialog_sum'] = df[['VIS_2',
                               'VIS_6',
                               'VIS_10',
                               'VIS_13']].sum(axis=1)

    #condensed inner speech
    df['VIS_condensed_sum'] = df[['VIS_1',
                                  'VIS_7',
                                  'VIS_8',
                                  'VIS_14',
                                  'VIS_15']].sum(axis=1)

    #other people in inner speech
    df['VIS_other_sum'] = df[['VIS_3',
                              'VIS_4',
                              'VIS_5',
                              'VIS_12',
                              'VIS_16']].sum(axis=1)

    #evaluative/motivational inner speech
    df['VIS_eval_sum'] = df[['VIS_9',
                             'VIS_11',
                             'VIS_17',
                             'VIS_18']].sum(axis=1)

    cols_export = ['ids'] + ['VIS_dialog_sum', 'VIS_condensed_sum', 'VIS_other_sum', 'VIS_eval_sum']
    df[cols_export].to_csv('%s/VISQ.csv' % out_dir, decimal='.', index=False)



##############################################################################
############# Spontaneous and Deliberate Mind Wandering ######################
##############################################################################

def run_MW_SD(df, out_dir):

    df['S-D-MW_delib_mean'] = df[["S-D-MW_1",
                                  "S-D-MW_2",
                                  "S-D-MW_3",
                                  "S-D-MW_4"]].mean(axis=1).round(3)

    df['S-D-MW_spont_mean'] = df[["S-D-MW_5",
                                  "S-D-MW_6",
                                  "S-D-MW_7",
                                  "S-D-MW_8"]].mean(axis=1).round(3)

    cols_export = ['ids']  + ['S-D-MW_delib_mean', 'S-D-MW_spont_mean']

    df[cols_export].to_csv('%s/S-D-MW.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################# short dark triad  ##############################
##############################################################################

def run_SDT(df, out_dir):

    #items to be recoded
    items_recoded = ['SD3_11',
                     'SD3_15',
                     'SD3_17',
                     'SD3_20',
                     'SD3_25']

    #recode items
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-9 for Machiavellism.
    df['SD3_Mach_sum'] = df[['SD3_1',
                             'SD3_2',
                             'SD3_3',
                             'SD3_4',
                             'SD3_5',
                             'SD3_6',
                             'SD3_7',
                             'SD3_8',
                             'SD3_9']].sum(axis=1)

    #Calculate total score as the sum of Item 1-9 for Narcissism.
    df['SD3_Narc_sum'] = df[['SD3_10',
                              'SD3_11',
                              'SD3_12',
                              'SD3_13',
                              'SD3_14',
                              'SD3_15',
                              'SD3_16',
                              'SD3_17',
                              'SD3_18']].sum(axis=1)

    #Calculate total score as the sum of Item 1-9 for Psychopathy.
    df['SD3_Psycho_sum'] = df[['SD3_19',
                               'SD3_20',
                               'SD3_21',
                               'SD3_22',
                               'SD3_23',
                               'SD3_24',
                               'SD3_25',
                               'SD3_26',
                               'SD3_27']].sum(axis=1)

    cols_export = ['ids'] + ['SD3_Mach_sum', 'SD3_Narc_sum', 'SD3_Psycho_sum']

    df[cols_export].to_csv('%s/SD3.csv' % out_dir, decimal='.', index=False)



##############################################################################
################################ SDS #########################################
##############################################################################
# social desirability

def run_SDS(df, out_dir):
    #items to be recoded

    cols = ['SDS_1',
            'SDS_2',
            'SDS_3',
            'SDS_4',
            'SDS_5',
            'SDS_6',
            'SDS_7',
            'SDS_8',
            'SDS_9',
            'SDS_10',
            'SDS_11',
            'SDS_12',
            'SDS_13',
            'SDS_14',
            'SDS_15',
            'SDS_16',
            'SDS_17']

    #recode items
    recoder = {1:1, 2:0}
    for i in cols:
        df[i] = df[i].map(recoder).astype('float64')

    items_reversed = ['SDS_1',
                     'SDS_4',
                     'SDS_6',
                     'SDS_7',
                     'SDS_11',
                     'SDS_15',
                     'SDS_17']

    #recode items
    recoder = {1:0, 0:1}
    for i in items_reversed:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-17.
    df['SDS_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['SDS_sum']

    df[cols_export].to_csv('%s/SDS.csv' % out_dir, decimal='.', index=False)



##############################################################################
##################### UPPSP - impulsivity ####################################
##############################################################################

def run_UPPSP(df, out_dir):

    #items that need to be recoded
    items_recoded = ['UPPS_2','UPPS_3','UPPS_5',
                     'UPPS_7','UPPS_8','UPPS_9',
                     'UPPS_10','UPPS_12','UPPS_13',
                     'UPPS_15','UPPS_17','UPPS_18',
                     'UPPS_20','UPPS_22','UPPS_23',
                     'UPPS_25','UPPS_26','UPPS_29',
                     'UPPS_30','UPPS_31','UPPS_34',
                     'UPPS_35','UPPS_36','UPPS_39',
                     'UPPS_40','UPPS_41','UPPS_44',
                     'UPPS_45','UPPS_46','UPPS_47',
                     'UPPS_49','UPPS_50','UPPS_51',
                     'UPPS_52','UPPS_54','UPPS_56',
                     'UPPS_57','UPPS_58','UPPS_59']
    #recode items
    recoder = {1:4, 2:3, 3:2, 4:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #calculate subscales (averages)
    #Negative Urgency
    df['UPPS_Mean_NegUrg'] = df[['UPPS_2',
                                 'UPPS_7',
                                 'UPPS_12',
                                 'UPPS_17',
                                 'UPPS_22',
                                 'UPPS_29',
                                 'UPPS_34',
                                 'UPPS_39',
                                 'UPPS_44',
                                 'UPPS_50',
                                 'UPPS_53',
                                 'UPPS_58']].mean(axis=1).round(3)

    #lack of premeditation
    df['UPPS_Mean_Premed'] = df[['UPPS_1',
                                 'UPPS_6',
                                 'UPPS_11',
                                 'UPPS_16',
                                 'UPPS_21',
                                 'UPPS_28',
                                 'UPPS_33',
                                 'UPPS_38',
                                 'UPPS_43',
                                 'UPPS_48',
                                 'UPPS_55']].mean(axis=1).round(3)

    #lack of perseverance
    df['UPPS_Mean_Persev'] = df[['UPPS_4',
                                 'UPPS_9',
                                 'UPPS_14',
                                 'UPPS_19',
                                 'UPPS_24',
                                 'UPPS_27',
                                 'UPPS_32',
                                 'UPPS_37',
                                 'UPPS_42',
                                 'UPPS_47']].mean(axis=1).round(3)

    #sensation seeking
    df['UPPS_Mean_SS'] = df[['UPPS_3',
                             'UPPS_8',
                             'UPPS_13',
                             'UPPS_18',
                             'UPPS_23',
                             'UPPS_26',
                             'UPPS_31',
                             'UPPS_36',
                             'UPPS_41',
                             'UPPS_46',
                             'UPPS_51',
                             'UPPS_56']].mean(axis=1).round(3)

    #Positive Urgency
    df['UPPS_Mean_PosUrg'] = df[['UPPS_5',
                                 'UPPS_10',
                                 'UPPS_15',
                                 'UPPS_20',
                                 'UPPS_25',
                                 'UPPS_30',
                                 'UPPS_35',
                                 'UPPS_40',
                                 'UPPS_45',
                                 'UPPS_49',
                                 'UPPS_52',
                                 'UPPS_54',
                                 'UPPS_57',
                                 'UPPS_59']].mean(axis=1).round(3)

    cols_export = ['ids'] + ['UPPS_Mean_NegUrg', 'UPPS_Mean_Premed', 'UPPS_Mean_Persev', 'UPPS_Mean_SS','UPPS_Mean_PosUrg']

    df[cols_export].to_csv('%s/UPPS-P.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################## TPS-D #########################################
################ Tuckmann Procrastination Scale (TPS_D)#######################
##############################################################################

def run_TPS(df, out_dir):

    #items to be recoded
    items_recoded = ['TPS_7',
                     'TPS_12',
                     'TPS_14',
                     'TPS_16']

    #recode items
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-16.
    cols = ['TPS_1',
            'TPS_2',
            'TPS_3',
            'TPS_4',
            'TPS_5',
            'TPS_6',
            'TPS_7',
            'TPS_8',
            'TPS_9',
            'TPS_10',
            'TPS_11',
            'TPS_12',
            'TPS_13',
            'TPS_14',
            'TPS_15',
            'TPS_16']

    df['TPS_D_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['TPS_D_sum']

    df[cols_export].to_csv('%s/TPS.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################ ASR 18-59 #######################################
##############################################################################

def run_ASR(df, out_dir):

    ######################## adaptive functioning #################################

    ##### friends #####
    df['ASR_summary_adaptiveFunctioning_friends_sum' ] = df[['ASR_I_A',
                                                             'ASR_I_B',
                                                             'ASR_I_C',
                                                             'ASR_I_D']].sum(axis=1)

    ##### spouse / partner #####
    recoded = ['ASR_II_B', 'ASR_II_E', 'ASR_II_F', 'ASR_II_H']
    for item in recoded:
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_spouse_sum'] = df[['ASR_II_A',
                                                          'ASR_II_B',
                                                          'ASR_II_C',
                                                          'ASR_II_D',
                                                          'ASR_II_E',
                                                          'ASR_II_F',
                                                          'ASR_II_G',
                                                          'ASR_II_H']].sum(axis=1)
    ##### family #####
    # also in literature: 'ASR_summary_adaptiveFunctioning_family_mean'
    items = ['ASR_III_A', 'ASR_III_B', 'ASR_III_C',
            'ASR_III_D', 'ASR_III_E_1', 'ASR_III_E_2',
            'ASR_III_E_3', 'ASR_III_E_4', 'ASR_III_F']

    df['ASR_summary_adaptiveFunctioning_family_sum'] = pd.Series('NaN', index=df.index)
    for sub in range(len(df)):
        score = 0
        for i in items:
            try:
                if int(df[i].iloc[[sub]]) in [0,1,2,3]:
                    score += 1
            except:
                pass
        df['ASR_summary_adaptiveFunctioning_family_sum'].iloc[[sub]] = float(score)


    ##### job #####
    #satisfied_job = df['ASR_IV_E'] is not scored
    recoded = ['ASR_IV_B', 'ASR_IV_D', 'ASR_IV_F',
               'ASR_IV_G', 'ASR_IV_H', 'ASR_IV_I']
    for item in recoded:
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_job_sum'] = df[['ASR_IV_A',
                                                        'ASR_IV_B',
                                                        'ASR_IV_C',
                                                        'ASR_IV_D',
                                                        'ASR_IV_F',
                                                        'ASR_IV_G',
                                                        'ASR_IV_H',
                                                        'ASR_IV_I']].sum(axis=1)

    ##### education #####
    # careful with older ages
    # though we're using raw total scores, it's important to notice that normed scores only available for ages 18-29
    recoded = ['ASR_V_C', 'ASR_V_E']
    for item in recoded:
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_education_sum'] = df[['ASR_V_A',
                                                              'ASR_V_B',
                                                              'ASR_V_C',
                                                              'ASR_V_D',
                                                              'ASR_V_E']].sum(axis=1)

    scales = ['ASR_summary_adaptiveFunctioning_friends_sum',
              'ASR_summary_adaptiveFunctioning_spouse_sum',
              'ASR_summary_adaptiveFunctioning_family_sum',
              'ASR_summary_adaptiveFunctioning_job_sum',
              'ASR_summary_adaptiveFunctioning_education_sum']



    ######################## substance use #################################

    df['ASR_scale_substanceUse_tabaco_perday'] = df['ASR_124']
    df['ASR_scale_substanceUse_alcohol_daysdrunk'] = df['ASR_125']
    df['ASR_scale_substanceUse_drugs_daysused'] = df['ASR_126']


    ######################### items #############################################
    Q1 = df['ASR_1']
    Q2 = df['ASR_2']
    Q3 = df['ASR_3']
    Q4 = df['ASR_4']
    Q5 = df['ASR_5']
    Q6 = df['ASR_6']
    Q7 = df['ASR_7']
    Q8 = df['ASR_8']
    Q9 = df['ASR_9']
    Q10 = df['ASR_10']
    Q11 = df['ASR_11']
    Q12 = df['ASR_12']
    Q13 = df['ASR_13']
    Q14 = df['ASR_14']
    Q15 = df['ASR_15']
    Q16 = df['ASR_16']
    Q17 = df['ASR_17']
    Q18 = df['ASR_18']
    Q19 = df['ASR_19']
    Q20 = df['ASR_20']
    Q21 = df['ASR_21']
    Q22 = df['ASR_22']
    Q23 = df['ASR_23']
    Q24 = df['ASR_24']
    Q25 = df['ASR_25']
    Q26 = df['ASR_26']
    Q27 = df['ASR_27']
    Q28 = df['ASR_28']
    Q29 = df['ASR_29']
    Q30 = df['ASR_30']
    Q31 = df['ASR_31']
    Q32 = df['ASR_32']
    Q33 = df['ASR_33']
    Q34 = df['ASR_34']
    Q35 = df['ASR_35']
    Q36 = df['ASR_36']
    Q37 = df['ASR_37']
    Q38 = df['ASR_38']
    Q39 = df['ASR_39']
    Q40 = df['ASR_40']
    Q41 = df['ASR_41']
    Q42 = df['ASR_42']
    Q43 = df['ASR_43']
    Q44 = df['ASR_44']
    Q45 = df['ASR_45']
    Q46 = df['ASR_46']
    Q47 = df['ASR_47']
    Q48 = df['ASR_48']
    Q49 = df['ASR_49']
    Q50 = df['ASR_50']
    Q51 = df['ASR_51']
    Q52 = df['ASR_52']
    Q53 = df['ASR_53']
    Q54 = df['ASR_54']
    Q55 = df['ASR_55']
    Q56a = df['ASR_56_a']
    Q56b = df['ASR_56_b']
    Q56c = df['ASR_56_c']
    Q56d = df['ASR_56_d']
    Q56e = df['ASR_56_e']
    Q56f = df['ASR_56_f']
    Q56g = df['ASR_56_g']
    Q57 = df['ASR_57']
    Q58 = df['ASR_58']
    Q59 = df['ASR_59']
    Q60 = df['ASR_60']
    Q61 = df['ASR_61']
    Q62 = df['ASR_62']
    Q63 = df['ASR_63']
    Q64 = df['ASR_64']
    Q65 = df['ASR_65']
    Q66 = df['ASR_66'] # comment?
    Q67 = df['ASR_67']
    Q68 = df['ASR_68']
    Q69 = df['ASR_69']
    Q70 = df['ASR_70']
    Q71 = df['ASR_71']
    Q72 = df['ASR_72']
    Q73 = df['ASR_73']
    Q74 = df['ASR_74']
    Q75 = df['ASR_75']
    Q76 = df['ASR_76']
    Q77 = df['ASR_77']
    Q78 = df['ASR_78']
    Q79 = df['ASR_79']
    Q80 = df['ASR_80']
    Q81 = df['ASR_81']
    Q82 = df['ASR_82']
    Q83 = df['ASR_83']
    Q84 = df['ASR_84']
    Q85 = df['ASR_85']
    Q86 = df['ASR_86']
    Q87 = df['ASR_87']
    Q88 = df['ASR_88']
    Q89 = df['ASR_89']
    Q90 = df['ASR_90']
    Q91 = df['ASR_91']
    Q92 = df['ASR_92']
    Q93 = df['ASR_93']
    Q94 = df['ASR_94']
    Q95 = df['ASR_95']
    Q96 = df['ASR_96']
    Q97 = df['ASR_97']
    Q98 = df['ASR_98']
    Q99 = df['ASR_99']
    Q100 = df['ASR_100']
    Q101 = df['ASR_101']
    Q102 = df['ASR_102']
    Q103 = df['ASR_103']
    Q104 = df['ASR_104']
    Q105 = df['ASR_105']
    Q106 = df['ASR_106']
    Q107 = df['ASR_107']
    Q108 = df['ASR_108']
    Q109 = df['ASR_109']
    Q110 = df['ASR_110']
    Q111 = df['ASR_111']
    Q112 = df['ASR_112']
    Q113 = df['ASR_113']
    Q114 = df['ASR_114']
    Q115 = df['ASR_115']
    Q116 = df['ASR_116']
    Q117 = df['ASR_117']
    Q118 = df['ASR_118']
    Q119 = df['ASR_119']
    Q120 = df['ASR_120']
    Q121 = df['ASR_121']
    Q122 = df['ASR_122']
    Q123 = df['ASR_123']


    ######################## critical items #################################

    df['ASR_summary_criticalItems_sum'] = Q6 + Q8 + Q9 + Q10 + Q14 + Q16 + Q18 + Q21 + Q40 + Q55 + Q57 + Q66 + Q70 + Q84 + Q90 + Q91 + Q92 + Q97 + Q103


    ######################## syndrome profiles #################################

    df['ASR_summary_syndromeProfiles_anxiousdepressed_sum'] = Q12 + Q13 + Q14 + Q22 + Q31 + Q33 + Q34 + Q35 + Q45 + Q47 + Q50 + Q52 + Q71 + Q91 + Q103 + Q107 + Q112 + Q113
    df['ASR_summary_syndromeProfiles_withdrawn_sum'] = Q25 + Q30 + Q42 + Q48 + Q60 + Q65 + Q67 + Q69 + Q111
    df['ASR_summary_syndromeProfiles_somaticComplaints_sum'] = Q51 + Q54 + Q56a + Q56b + Q56c + Q56d + Q56e + Q56f + Q56g + Q100
    df['ASR_summary_syndromeProfiles_thoughtProblems_sum'] = Q9 + Q18 + Q36 + Q40 + Q46 + Q63 + Q66 + Q70 + Q84 + Q85
    df['ASR_summary_syndromeProfiles_attentionProblems_sum'] = Q1 + Q8 + Q11 + Q17 + Q53 + Q59 + Q61 + Q64 + Q78 + Q101 + Q102 + Q105 + Q108 + Q119 + Q121
    df['ASR_summary_syndromeProfiles_aggressiveBehavior_sum'] = Q3 + Q5 + Q16 + Q28 + Q37 + Q55 + Q57 + Q68 + Q81 + Q86 + Q87 + Q95 + Q97 + Q116 + Q118
    df['ASR_summary_syndromeProfiles_rulebreakingBehavior_sum'] = Q6 + Q20 + Q23 + Q26 + Q39 + Q41 + Q43 + Q76 + Q82 + Q90 + Q92 + Q114 + Q117 + Q122
    df['ASR_summary_syndromeProfiles_intrusive_sum'] = Q7 + Q19 + Q74 + Q93 + Q94 + Q104

    df['ASR_summary_syndromeProfiles_internalizing_sum'] = df[['ASR_summary_syndromeProfiles_anxiousdepressed_sum',
                                                               'ASR_summary_syndromeProfiles_withdrawn_sum',
                                                               'ASR_summary_syndromeProfiles_somaticComplaints_sum']].sum(axis=1)

    df['ASR_summary_syndromeProfiles_externalizing_sum'] = df[['ASR_summary_syndromeProfiles_aggressiveBehavior_sum',
                                                               'ASR_summary_syndromeProfiles_rulebreakingBehavior_sum',
                                                               'ASR_summary_syndromeProfiles_intrusive_sum']].sum(axis=1)




    cols_export = ['ids'] + ['ASR_summary_adaptiveFunctioning_friends_sum','ASR_summary_adaptiveFunctioning_spouse_sum',
                            'ASR_summary_adaptiveFunctioning_family_sum',
                            'ASR_summary_adaptiveFunctioning_job_sum', 'ASR_summary_adaptiveFunctioning_education_sum',
                            'ASR_scale_substanceUse_tabaco_perday','ASR_scale_substanceUse_alcohol_daysdrunk',
                            'ASR_scale_substanceUse_drugs_daysused','ASR_summary_criticalItems_sum',
                            'ASR_summary_syndromeProfiles_anxiousdepressed_sum',
                            'ASR_summary_syndromeProfiles_withdrawn_sum',
                            'ASR_summary_syndromeProfiles_somaticComplaints_sum',
                            'ASR_summary_syndromeProfiles_thoughtProblems_sum',
                            'ASR_summary_syndromeProfiles_attentionProblems_sum',
                            'ASR_summary_syndromeProfiles_aggressiveBehavior_sum',
                            'ASR_summary_syndromeProfiles_rulebreakingBehavior_sum',
                            'ASR_summary_syndromeProfiles_intrusive_sum',
                            'ASR_summary_syndromeProfiles_internalizing_sum',
                            'ASR_summary_syndromeProfiles_externalizing_sum']

    df[cols_export].to_csv('%s/ASR.csv' % out_dir, decimal='.', index=False)



##############################################################################
########################## Self-Esteem Scale #################################
##############################################################################

def run_SE(df, out_dir):

    #items to be recoded
    items_recoded = ['SE_5',
                     'SE_6',
                     'SE_7',
                     'SE_8']

    recoder = {1:5, 2:4, 3:3, 4:2, 5:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #scale aggregation
    cols = ['SE_1',
            'SE_2',
            'SE_3',
            'SE_4',
            'SE_5',
            'SE_6',
            'SE_7',
            'SE_8']

    df['SE_Mean_SelfEst'] = df[cols].mean(axis=1).round(3)

    cols_export = ['ids'] + ['SE_Mean_SelfEst']

    df[cols_export].to_csv('%s/SE.csv' % out_dir, decimal='.', index=False)



##############################################################################
####### Involuntary Musical Imagery Scale (Earworm Scale) ####################
##############################################################################

def run_IMIS(df, out_dir):

    #Calculate factors
    df['IMIS_NegVal_sum'] = df[['IMIS_2','IMIS_3','IMIS_4','IMIS_5','IMIS_6','IMIS_7','IMIS_8']].sum(axis=1)
    df['IMIS_Help_sum'] = df[['IMIS_15','IMIS_16']].sum(axis=1)
    df['IMIS_Movement_sum'] = df[['IMIS_9','IMIS_10','IMIS_11']].sum(axis=1)
    df['IMIS_PersRef_sum'] = df[['IMIS_12','IMIS_13','IMIS_14']].sum(axis=1)

    cols_export = ['ids'] + ["IMIS_NegVal_sum", "IMIS_Help_sum", "IMIS_Movement_sum", "IMIS_PersRef_sum"]

    df[cols_export].to_csv('%s/IMIS.csv' % out_dir, decimal='.', index=False)



##############################################################################
####### Goldsmiths Musical Sophistication Index (Gold-MSI) ###################
##############################################################################

def run_GoldMSI(df, out_dir):

    #items to be recoded
    items_recoded = ['GoldMSI_5',
                     'GoldMSI_10',
                     'GoldMSI_11']
    recoder = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1}

    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    df['GoldMSI_Active_sum'] = df[['GoldMSI_5','GoldMSI_1','GoldMSI_4','GoldMSI_6','GoldMSI_7','GoldMSI_2','GoldMSI_3','GoldMSI_8','GoldMSI_9']].sum(axis=1)

    df['GoldMSI_Training_sum'] = df[['GoldMSI_10','GoldMSI_11','GoldMSI_12','GoldMSI_13','GoldMSI_14','GoldMSI_15','GoldMSI_16']].sum(axis=1)

    cols_export = ['ids'] + ["GoldMSI_Active_sum", 'GoldMSI_Training_sum']

    df[cols_export].to_csv('%s/Gold-MSI.csv' % out_dir, decimal='.', index=False)



##############################################################################
####################### Epsworth Sleepiness Scale ############################
##############################################################################

def run_ESS(df, out_dir):

    cols = ['ESS_1', 'ESS_2', 'ESS_3', 'ESS_4',
            'ESS_5', 'ESS_6', 'ESS_7', 'ESS_8']

    df['ESS_summary_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['ESS_summary_sum']

    df[cols_export].to_csv('%s/ESS.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################## BDI ###########################################
##############################################################################

def run_BDI(df, out_dir):

    # recode items
    # each item was initially representd as 4 binary items 
    # e.g. item 1 consists of BDI_1, BDI_2 BDI_3, BDI_4 with 0/1 response code
    # these are here recoded to the approproate scoring for that item raning between 0 and 3 before everything is summed
    
    zero = ['BDI_1', 'BDI_5', 'BDI_9',
            'BDI_13', 'BDI_17', 'BDI_21',
            'BDI_25', 'BDI_29', 'BDI_33',
            'BDI_37', 'BDI_41', 'BDI_45',
            'BDI_49', 'BDI_53', 'BDI_57',
            'BDI_61', 'BDI_65', 'BDI_69',
            'BDI_73', 'BDI_78', 'BDI_82']
    for item in zero:
        df[item].replace(to_replace=1, value=0, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)

    one = ['BDI_2', 'BDI_6', 'BDI_10',
           'BDI_14', 'BDI_18', 'BDI_22',
           'BDI_26', 'BDI_30', 'BDI_34',
           'BDI_38', 'BDI_42', 'BDI_46',
           'BDI_50', 'BDI_54', 'BDI_58',
           'BDI_62', 'BDI_66', 'BDI_70',
           'BDI_74', 'BDI_79', 'BDI_83']
    for item in one:
        df[item].replace(to_replace=1, value=1, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)

    two = ['BDI_3', 'BDI_7', 'BDI_11',
           'BDI_15', 'BDI_19', 'BDI_23',
           'BDI_27', 'BDI_31', 'BDI_35',
           'BDI_39', 'BDI_43', 'BDI_47',
           'BDI_51', 'BDI_55', 'BDI_59',
           'BDI_63', 'BDI_67', 'BDI_71',
           'BDI_75', 'BDI_80', 'BDI_84']
    for item in two:
        df[item].replace(to_replace=1, value=2, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)

    three = ['BDI_4', 'BDI_8', 'BDI_12',
             'BDI_16', 'BDI_20', 'BDI_24',
             'BDI_28', 'BDI_32', 'BDI_36',
             'BDI_40', 'BDI_44', 'BDI_48',
             'BDI_52', 'BDI_56', 'BDI_60',
             'BDI_64', 'BDI_68', 'BDI_72',
             'BDI_76', 'BDI_81', 'BDI_85']
    for item in three:
        df[item].replace(to_replace=1, value=3, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)

    df['BDI_sum_1'] = df[['BDI_1', 'BDI_2', 'BDI_3', 'BDI_4']].sum(axis=1)
    df['BDI_sum_2'] = df[['BDI_5', 'BDI_6', 'BDI_7', 'BDI_8']].sum(axis=1)
    df['BDI_sum_3'] = df[['BDI_9', 'BDI_10', 'BDI_11', 'BDI_12']].sum(axis=1)
    df['BDI_sum_4'] = df[['BDI_13', 'BDI_14', 'BDI_15', 'BDI_16']].sum(axis=1)
    df['BDI_sum_5'] = df[['BDI_17', 'BDI_18', 'BDI_19', 'BDI_20']].sum(axis=1)
    df['BDI_sum_6'] = df[['BDI_21', 'BDI_22', 'BDI_23', 'BDI_24']].sum(axis=1)
    df['BDI_sum_7'] = df[['BDI_25', 'BDI_26', 'BDI_27', 'BDI_28']].sum(axis=1)
    df['BDI_sum_8'] = df[['BDI_29', 'BDI_30', 'BDI_31', 'BDI_32']].sum(axis=1)
    df['BDI_sum_9'] = df[['BDI_33', 'BDI_34', 'BDI_35', 'BDI_36']].sum(axis=1)
    df['BDI_sum_10'] = df[['BDI_37', 'BDI_38', 'BDI_39', 'BDI_40']].sum(axis=1)
    df['BDI_sum_11'] = df[['BDI_41', 'BDI_42', 'BDI_43', 'BDI_44']].sum(axis=1)
    df['BDI_sum_12'] = df[['BDI_45', 'BDI_46', 'BDI_47', 'BDI_48']].sum(axis=1)
    df['BDI_sum_13'] = df[['BDI_49', 'BDI_50', 'BDI_51', 'BDI_52']].sum(axis=1)
    df['BDI_sum_14'] = df[['BDI_53', 'BDI_54', 'BDI_55', 'BDI_56']].sum(axis=1)
    df['BDI_sum_15'] = df[['BDI_57', 'BDI_58', 'BDI_59', 'BDI_60']].sum(axis=1)
    df['BDI_sum_16'] = df[['BDI_61', 'BDI_62', 'BDI_63', 'BDI_64']].sum(axis=1)
    df['BDI_sum_17'] = df[['BDI_65', 'BDI_66', 'BDI_67', 'BDI_68']].sum(axis=1)
    df['BDI_sum_18'] = df[['BDI_69', 'BDI_70', 'BDI_71', 'BDI_72']].sum(axis=1)
    df['BDI_sum_19'] = df[['BDI_73', 'BDI_74', 'BDI_75', 'BDI_76']].sum(axis=1)
    df['BDI_sum_diet'] = df[['BDI_77']]
    df['BDI_sum_20'] = df[['BDI_78', 'BDI_79', 'BDI_80', 'BDI_81']].sum(axis=1)
    df['BDI_sum_21'] = df[['BDI_82', 'BDI_83', 'BDI_84', 'BDI_85']].sum(axis=1)


    cols_sum = ['BDI_sum_%s' % str(x+1) for x in range(21)]

    # output
    df['BDI_summary_sum'] = df[[x for x in cols_sum]].sum(axis=1)

    cols_export = ['ids'] + cols_sum + ['BDI_summary_sum']

    df[cols_export].to_csv('%s/BDI.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################## HADS ##########################################
##############################################################################

def run_HADS(df, out_dir):

    # recoding of items had already happened in conversion.py
    
    df['HADS-A_summary_sum'] = df[['HADS_1', 'HADS_3', 'HADS_5', 'HADS_7',
                                   'HADS_9', 'HADS_11', 'HADS_13']].sum(axis=1)

    df['HADS-D_summary_sum'] = df[['HADS_2', 'HADS_4', 'HADS_6', 'HADS_8',
                                   'HADS_10', 'HADS_12', 'HADS_14']].sum(axis=1)

    cols_export = ['ids'] + ['HADS-A_summary_sum', 'HADS-D_summary_sum']

    df[cols_export].to_csv('%s/HADS.csv' % out_dir, decimal='.', index=False)



##############################################################################
##################### Boredom Proness Scale ##################################
##############################################################################

def run_BPS(df, out_dir):

    #items to be recoded
    items_recoded = ['BPS_1',
                     'BPS_7',
                     'BPS_8',
                     'BPS_11',
                     'BPS_13',
                     'BPS_15',
                     'BPS_18',
                     'BPS_22',
                     'BPS_23',
                     'BPS_24']

    #recode items
    recoder = {1:7 , 2:6, 3:5, 4:4, 5:3, 6:2, 7:1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-28.
    cols = ['BPS_1','BPS_2','BPS_3',
            'BPS_4','BPS_5','BPS_6',
            'BPS_7','BPS_8','BPS_9',
            'BPS_10','BPS_11','BPS_12',
            'BPS_13','BPS_14','BPS_15',
            'BPS_16','BPS_17','BPS_18',
            'BPS_19','BPS_20','BPS_21',
            'BPS_22','BPS_23','BPS_24',
            'BPS_25','BPS_26','BPS_27',
            'BPS_28']

    df['BPS_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['BPS_sum']

    df[cols_export].to_csv('%s/BP.csv' % out_dir, decimal='.', index=False)



##############################################################################
################# Derryberry Attention Control Scale #########################
##############################################################################

def run_ACS(df, out_dir):

    #items to be recoded
    items_recoded = ['ACS_1',
                    'ACS_2',
                    'ACS_3',
                    'ACS_6',
                    'ACS_7',
                    'ACS_8',
                    'ACS_11',
                    'ACS_12',
                    'ACS_15',
                    'ACS_16',
                    'ACS_20']

    #recode items
    recoder = {1:4 , 2:3, 3:2, 4:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-20.
    cols = ['ACS_1','ACS_2','ACS_3',
            'ACS_4','ACS_5','ACS_6',
            'ACS_7','ACS_8','ACS_9',
            'ACS_10','ACS_11','ACS_12',
            'ACS_13','ACS_14','ACS_15',
            'ACS_16','ACS_17','ACS_18',
            'ACS_19','ACS_20']

    df['ACS_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['ACS_sum']

    df[cols_export].to_csv('%s/ACS.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################## NEO-PI-R ######################################
##############################################################################

def run_NEOPIR(df, out_dir):

    #recode reversed items
    items_recoded = ['NEO_61','NEO_1','NEO_121','NEO_181','NEO_36','NEO_96','NEO_156','NEO_11',
                     'NEO_71','NEO_106','NEO_166','NEO_21','NEO_81','NEO_231','NEO_141','NEO_56',
                     'NEO_116','NEO_176','NEO_206','NEO_236','NEO_32','NEO_92','NEO_7','NEO_67',
                     'NEO_127','NEO_187','NEO_42','NEO_102','NEO_162','NEO_222','NEO_17','NEO_77','NEO_137',
                     'NEO_52','NEO_112','NEO_27', 'NEO_87','NEO_147','NEO_207','NEO_33','NEO_93','NEO_153',
                     'NEO_183', 'NEO_213', 'NEO_8','NEO_68','NEO_128','NEO_43','NEO_103','NEO_163','NEO_18',
                     'NEO_78','NEO_138','NEO_198','NEO_228','NEO_53','NEO_113','NEO_173', 'NEO_28',
                     'NEO_88', 'NEO_148', 'NEO_208','NEO_238' ,'NEO_4' ,'NEO_64','NEO_124','NEO_39',
                     'NEO_99','NEO_159','NEO_189','NEO_219', 'NEO_14','NEO_74','NEO_134','NEO_49',
                     'NEO_109','NEO_169','NEO_199','NEO_229','NEO_24','NEO_84','NEO_144','NEO_234',
                     'NEO_59','NEO_119','NEO_35','NEO_95','NEO_155','NEO_10','NEO_70','NEO_130',
                     'NEO_190','NEO_220','NEO_45','NEO_105','NEO_20', 'NEO_80','NEO_140','NEO_55',
                     'NEO_115','NEO_175','NEO_205','NEO_30','NEO_90','NEO_150']



    recoder = {0:4, 1:3, 2:2, 3:1, 4:0}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    # calculate subscales as means for all 30 facets

    #Neuroticism
    df['NEO_N'] = df[['NEO_1','NEO_31', 'NEO_61','NEO_91','NEO_121', 'NEO_151', 'NEO_181','NEO_211','NEO_6',
                      'NEO_36','NEO_66','NEO_96','NEO_126','NEO_156','NEO_186','NEO_216','NEO_11','NEO_41',
                      'NEO_71','NEO_101','NEO_131','NEO_161','NEO_191','NEO_221','NEO_16','NEO_76','NEO_106',
                      'NEO_136','NEO_166','NEO_196','NEO_226','NEO_21','NEO_51','NEO_81','NEO_111','NEO_141',
                      'NEO_171','NEO_201','NEO_231','NEO_26','NEO_56','NEO_86','NEO_116','NEO_146','NEO_176',
                      'NEO_206','NEO_236']].sum(axis=1) # false item 46 excluded

    #N1 anxiety
    df['NEO_N1_anx'] = df[['NEO_1','NEO_31','NEO_61','NEO_91',
                           'NEO_121','NEO_151','NEO_181','NEO_211']].sum(axis=1)
    #N2 angry hostility
    df['NEO_N2_host'] = df[['NEO_6','NEO_36','NEO_66','NEO_96',
                            'NEO_126','NEO_156','NEO_186','NEO_216']].sum(axis=1)
    #N3 Depression
    df['NEO_N3_depr'] = df[['NEO_11','NEO_41','NEO_71','NEO_101',
                            'NEO_131','NEO_161','NEO_191','NEO_221']].sum(axis=1)
    #N4 Self Consciousness
    df['NEO_N4_selfcon'] = df[['NEO_16','NEO_76','NEO_106','NEO_136',
                               'NEO_166','NEO_196','NEO_226']].sum(axis=1) # false item 46 excluded
    #N5 Impulsiveness
    df['NEO_N5_imp'] = df[['NEO_21','NEO_51','NEO_81','NEO_111',
                           'NEO_141','NEO_171','NEO_201','NEO_231']].sum(axis=1)
    #N6 Vulnerability
    df['NEO_N6_vuln'] = df[['NEO_26','NEO_56','NEO_86','NEO_116',
                            'NEO_146','NEO_176','NEO_206','NEO_236']].sum(axis=1)


    #Extraversion
    df['NEO_E'] = df[['NEO_2','NEO_32','NEO_62','NEO_92','NEO_122','NEO_152','NEO_182','NEO_212',
                      'NEO_7','NEO_37','NEO_67','NEO_97','NEO_127','NEO_157','NEO_187','NEO_217',
                      'NEO_12','NEO_42','NEO_72','NEO_102','NEO_132','NEO_162','NEO_192','NEO_222',
                      'NEO_17','NEO_47','NEO_77','NEO_107','NEO_137','NEO_167','NEO_197','NEO_227',
                      'NEO_22','NEO_52','NEO_82','NEO_112','NEO_142','NEO_172','NEO_202','NEO_232',
                      'NEO_27','NEO_57','NEO_87','NEO_117','NEO_147','NEO_177','NEO_207','NEO_237']].sum(axis=1)

    #E1 warmth
    df['NEO_E1_warm'] = df[['NEO_2','NEO_32','NEO_62',
                            'NEO_92','NEO_122','NEO_152','NEO_182','NEO_212']].sum(axis=1)
    #E2 Gregariousness
    df['NEO_E2_greg'] = df[['NEO_7','NEO_37','NEO_67',
                            'NEO_97','NEO_127','NEO_157','NEO_187','NEO_217']].sum(axis=1)
    #N3 Assertiveness
    df['NEO_E3_ass'] = df[['NEO_12','NEO_42','NEO_72',
                           'NEO_102','NEO_132','NEO_162','NEO_192','NEO_222']].sum(axis=1)
    #N4 Activity
    df['NEO_E4_act'] = df[['NEO_17','NEO_47','NEO_77',
                           'NEO_107','NEO_137','NEO_167','NEO_197','NEO_227']].sum(axis=1)
    #N5 Excitement Seeking
    df['NEO_E5_excseek'] = df[['NEO_22','NEO_52','NEO_82',
                               'NEO_112','NEO_142','NEO_172','NEO_202','NEO_232']].sum(axis=1)
    #N6 Positive Emotions
    df['NEO_E6_PosEmo'] = df[['NEO_27','NEO_57','NEO_87',
                              'NEO_117','NEO_147','NEO_177','NEO_207','NEO_237']].sum(axis=1)


    #Openness
    #item 83 missing
    df['NEO_O'] = df[['NEO_3','NEO_33','NEO_63','NEO_93','NEO_123','NEO_153','NEO_183','NEO_213',
                      'NEO_8','NEO_38','NEO_68','NEO_98','NEO_128','NEO_158','NEO_188','NEO_218',
                      'NEO_13','NEO_43','NEO_73','NEO_103','NEO_133','NEO_163','NEO_193','NEO_223',
                      'NEO_18','NEO_48','NEO_78','NEO_108','NEO_138','NEO_168','NEO_198','NEO_228',
                      'NEO_23','NEO_53','NEO_113','NEO_143','NEO_173','NEO_203','NEO_233',
                      'NEO_28','NEO_58','NEO_88','NEO_118','NEO_148','NEO_178','NEO_208','NEO_238']].sum(axis=1)

    #O1 fantasy
    df['NEO_O1_fan'] = df[['NEO_3','NEO_33','NEO_63',
                           'NEO_93','NEO_123','NEO_153','NEO_183','NEO_213']].sum(axis=1)
    #O2 aesthetics
    df['NEO_O2_aest'] = df[['NEO_8','NEO_38','NEO_68',
                            'NEO_98','NEO_128','NEO_158','NEO_188','NEO_218']].sum(axis=1)
    #O3 feelings
    df['NEO_O3_feel'] = df[['NEO_13','NEO_43','NEO_73',
                            'NEO_103','NEO_133','NEO_163','NEO_193','NEO_223']].sum(axis=1)
    #04 actions
    df['NEO_O4_act'] = df[['NEO_18','NEO_48','NEO_78',
                           'NEO_108','NEO_138','NEO_168','NEO_198','NEO_228']].sum(axis=1)
    #05 ideas
    #item 83 missing
    df['NEO_O5_idea'] = df[['NEO_23','NEO_53','NEO_113',
                            'NEO_143','NEO_173','NEO_203','NEO_233']].sum(axis=1)
    #06 values
    df['NEO_O6_value'] = df[['NEO_28','NEO_58','NEO_88',
                             'NEO_118','NEO_148','NEO_178','NEO_208','NEO_238']].sum(axis=1)



    #Agreeableness
    df['NEO_A'] = df[['NEO_4','NEO_34','NEO_64','NEO_94','NEO_124','NEO_154','NEO_184','NEO_214',
                      'NEO_9','NEO_39','NEO_69','NEO_99','NEO_129','NEO_159','NEO_189','NEO_219',
                      'NEO_14','NEO_44','NEO_74','NEO_104','NEO_134','NEO_164','NEO_194','NEO_224',
                      'NEO_19','NEO_49','NEO_79','NEO_109','NEO_139','NEO_169','NEO_199','NEO_229',
                      'NEO_24','NEO_54','NEO_84','NEO_114','NEO_144','NEO_174','NEO_204','NEO_234',
                      'NEO_29','NEO_59','NEO_89','NEO_119','NEO_149','NEO_179','NEO_209','NEO_239']].sum(axis=1)

    #A1 trust
    df['NEO_A1_trust'] = df[['NEO_4','NEO_34','NEO_64',
                             'NEO_94','NEO_124','NEO_154','NEO_184','NEO_214']].sum(axis=1)
    #A2 straightforwardedness
    df['NEO_A2_sf'] = df[['NEO_9','NEO_39','NEO_69',
                          'NEO_99','NEO_129','NEO_159','NEO_189','NEO_219']].sum(axis=1)
    #A3 altruism
    df['NEO_A3_altr'] = df[['NEO_14','NEO_44','NEO_74',
                            'NEO_104','NEO_134','NEO_164','NEO_194','NEO_224']].sum(axis=1)
    #A4 compliance
    df['NEO_A4_compl'] = df[['NEO_19','NEO_49','NEO_79',
                             'NEO_109','NEO_139','NEO_169','NEO_199','NEO_229']].sum(axis=1)
    #A5 modesty
    df['NEO_A5_modes'] = df[['NEO_24','NEO_54','NEO_84',
                             'NEO_114','NEO_144','NEO_174','NEO_204','NEO_234']].sum(axis=1)
    #A6 tender_mindedness
    df['NEO_A6_tenmind'] = df[['NEO_29','NEO_59','NEO_89',
                               'NEO_119','NEO_149','NEO_179','NEO_209','NEO_239']].sum(axis=1)



    #Conscientiousness
    df['NEO_C'] = df[['NEO_5','NEO_35','NEO_65','NEO_95','NEO_125','NEO_155','NEO_185','NEO_215',
                     'NEO_10','NEO_40','NEO_70','NEO_100','NEO_130','NEO_160','NEO_190','NEO_220',
                     'NEO_15','NEO_45','NEO_75','NEO_105','NEO_135','NEO_165','NEO_195','NEO_225',
                     'NEO_20','NEO_50','NEO_80','NEO_110','NEO_140','NEO_170','NEO_200','NEO_230',
                     'NEO_25','NEO_55','NEO_85','NEO_115','NEO_145','NEO_175','NEO_205','NEO_235',
                     'NEO_30','NEO_60','NEO_90','NEO_120','NEO_150','NEO_180','NEO_210','NEO_240']].sum(axis=1)

    #C1 compentence
    df['NEO_C1_comp'] = df[['NEO_5','NEO_35','NEO_65',
                            'NEO_95','NEO_125','NEO_155','NEO_185','NEO_215']].sum(axis=1)
    #C2 order
    df['NEO_C2_order'] = df[['NEO_10','NEO_40','NEO_70',
                             'NEO_100','NEO_130','NEO_160','NEO_190','NEO_220']].sum(axis=1)
    #C3 dutifulness
    df['NEO_C3_dutif'] = df[['NEO_15','NEO_45','NEO_75',
                             'NEO_105','NEO_135','NEO_165','NEO_195','NEO_225']].sum(axis=1)
    #C4 achievement striving
    df['NEO_C4_achstr'] = df[['NEO_20','NEO_50','NEO_80',
                              'NEO_110','NEO_140','NEO_170','NEO_200','NEO_230']].sum(axis=1)
    #C5 self discipline
    df['NEO_C5_selfdis'] = df[['NEO_25','NEO_55','NEO_85',
                               'NEO_115','NEO_145','NEO_175','NEO_205','NEO_235']].sum(axis=1)
    #C6 deliberation
    df['NEO_C6_deli'] = df[['NEO_30','NEO_60','NEO_90',
                            'NEO_120','NEO_150','NEO_180','NEO_210','NEO_240']].sum(axis=1)



    summary_cols = ['NEO_N', 'NEO_N1_anx', 'NEO_N2_host',
                    'NEO_N3_depr', 'NEO_N4_selfcon', 'NEO_N5_imp', 'NEO_N6_vuln',
                    'NEO_E', 'NEO_E1_warm', 'NEO_E2_greg',
                    'NEO_E3_ass', 'NEO_E4_act', 'NEO_E5_excseek', 'NEO_E6_PosEmo',
                    'NEO_O', 'NEO_O1_fan', 'NEO_O2_aest',
                    'NEO_O3_feel', 'NEO_O4_act', 'NEO_O5_idea', 'NEO_O6_value',
                    'NEO_A', 'NEO_A1_trust', 'NEO_A2_sf',
                    'NEO_A3_altr', 'NEO_A4_compl', 'NEO_A5_modes', 'NEO_A6_tenmind',
                    'NEO_C', 'NEO_C1_comp', 'NEO_C2_order',
                    'NEO_C3_dutif', 'NEO_C4_achstr', 'NEO_C5_selfdis', 'NEO_C6_deli']

    df[['ids'] + summary_cols].to_csv('%s/NEO-PI-R.csv' % out_dir, decimal='.', index=False)

##############################################################################
############# PSSI - Persönlichkeitsstil- und Störungsinventar################
##############################################################################

def run_PSSI(df, out_dir):

    cols = ['PSSI_1','PSSI_2','PSSI_3','PSSI_4','PSSI_5','PSSI_6','PSSI_7','PSSI_8','PSSI_9',
             'PSSI_10','PSSI_11','PSSI_12','PSSI_13','PSSI_14','PSSI_15','PSSI_16','PSSI_17',
             'PSSI_18','PSSI_19','PSSI_20','PSSI_21','PSSI_22','PSSI_23','PSSI_24','PSSI_25',
             'PSSI_26','PSSI_27','PSSI_28','PSSI_29','PSSI_30','PSSI_31','PSSI_32','PSSI_33',
             'PSSI_34','PSSI_35','PSSI_36','PSSI_37','PSSI_38','PSSI_39','PSSI_40','PSSI_41',
             'PSSI_42','PSSI_43','PSSI_44','PSSI_45','PSSI_46','PSSI_47','PSSI_48','PSSI_49',
             'PSSI_50','PSSI_51','PSSI_52','PSSI_53','PSSI_54','PSSI_55','PSSI_56','PSSI_57',
             'PSSI_58','PSSI_59','PSSI_60','PSSI_61','PSSI_62','PSSI_63','PSSI_64','PSSI_65',
             'PSSI_66','PSSI_67','PSSI_68','PSSI_69','PSSI_70','PSSI_71','PSSI_72','PSSI_73',
             'PSSI_74','PSSI_75','PSSI_76','PSSI_77','PSSI_78','PSSI_79','PSSI_80','PSSI_81',
             'PSSI_82','PSSI_83','PSSI_84','PSSI_85','PSSI_86','PSSI_87','PSSI_88','PSSI_89',
             'PSSI_90','PSSI_91','PSSI_92','PSSI_93','PSSI_94','PSSI_95','PSSI_96','PSSI_97',
             'PSSI_98','PSSI_99','PSSI_100','PSSI_101','PSSI_102','PSSI_103','PSSI_104','PSSI_105',
             'PSSI_106','PSSI_107','PSSI_108','PSSI_109','PSSI_110','PSSI_111','PSSI_112','PSSI_113',
             'PSSI_114','PSSI_115','PSSI_116','PSSI_117','PSSI_118','PSSI_119','PSSI_120','PSSI_121',
             'PSSI_122','PSSI_123','PSSI_124','PSSI_125','PSSI_126','PSSI_127','PSSI_128','PSSI_129',
             'PSSI_130','PSSI_131','PSSI_132','PSSI_133','PSSI_134','PSSI_135','PSSI_136','PSSI_137',
             'PSSI_138','PSSI_139','PSSI_140']
    #recode all items to original format (limesurvey: 1234, original = 0123)
    recoder = {1:0, 2:1, 3:2, 4:3 }
    for i in cols:
        df[i] = df[i].map(recoder).astype('float64')

    #recode reversed items
    items_recoded = ['PSSI_15',
                     'PSSI_43',
                     'PSSI_71',
                     'PSSI_99',
                     'PSSI_44',
                     'PSSI_72',
                     'PSSI_86',
                     'PSSI_104',
                     'PSSI_49',
                     'PSSI_91',
                     'PSSI_105',
                     'PSSI_39',
                     'PSSI_67',
                     'PSSI_109',
                     'PSSI_137']

    recoder = {0:3, 1:2, 2:1, 3:0}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    # calculate subscales as sumscores

    #PN = eigenwillig_paranoid
    df['PSSI_PN'] = df[['PSSI_1',
                        'PSSI_15',
                        'PSSI_29',
                        'PSSI_43',
                        'PSSI_57',
                        'PSSI_71',
                        'PSSI_85',
                        'PSSI_99',
                        'PSSI_113',
                        'PSSI_127']].sum(axis=1)

    #SZ = zurückhaltend-schizoid
    df['PSSI_SZ'] = df[['PSSI_2',
                        'PSSI_16',
                        'PSSI_30',
                        'PSSI_44',
                        'PSSI_58',
                        'PSSI_72',
                        'PSSI_86',
                        'PSSI_100',
                        'PSSI_114',
                        'PSSI_128']].sum(axis=1)

    #ST = ahnungsvoll-schizotypisch
    df['PSSI_ST'] = df[['PSSI_3',
                        'PSSI_17',
                        'PSSI_31',
                        'PSSI_45',
                        'PSSI_59',
                        'PSSI_73',
                        'PSSI_87',
                        'PSSI_101',
                        'PSSI_115',
                        'PSSI_129']].sum(axis=1)

    #BL = spontan-borderline
    df['PSSI_BL'] = df[['PSSI_4',
                        'PSSI_18',
                        'PSSI_32',
                        'PSSI_46',
                        'PSSI_60',
                        'PSSI_74',
                        'PSSI_88',
                        'PSSI_102',
                        'PSSI_116',
                        'PSSI_130']].sum(axis=1)

    #HI = liebenswürdig-hisrtionisch
    df['PSSI_HI'] = df[['PSSI_5',
                        'PSSI_19',
                        'PSSI_33',
                        'PSSI_47',
                        'PSSI_61',
                        'PSSI_75',
                        'PSSI_89',
                        'PSSI_103',
                        'PSSI_117',
                        'PSSI_131']].sum(axis=1)

    # NA = ehrgeizig_narzisstisch
    df['PSSI_NA'] = df[['PSSI_6',
                        'PSSI_20',
                        'PSSI_34',
                        'PSSI_48',
                        'PSSI_62',
                        'PSSI_76',
                        'PSSI_90',
                        'PSSI_104',
                        'PSSI_118',
                        'PSSI_132']].sum(axis=1)

    #SU = selbstkritisch-selbstunsicher
    df['PSSI_SU'] = df[['PSSI_7',
                        'PSSI_21',
                        'PSSI_35',
                        'PSSI_49',
                        'PSSI_63',
                        'PSSI_77',
                        'PSSI_91',
                        'PSSI_105',
                        'PSSI_119',
                        'PSSI_133']].sum(axis=1)

    # AB = loyal-abhängig
    df['PSSI_AB'] = df[['PSSI_8',
                        'PSSI_22',
                        'PSSI_36',
                        'PSSI_50',
                        'PSSI_64',
                        'PSSI_78',
                        'PSSI_92',
                        'PSSI_106',
                        'PSSI_120',
                        'PSSI_134']].sum(axis=1)

    # ZW = sorgfältig - zwanghaft
    df['PSSI_ZW'] = df[['PSSI_9',
                        'PSSI_23',
                        'PSSI_37',
                        'PSSI_51',
                        'PSSI_65',
                        'PSSI_79',
                        'PSSI_93',
                        'PSSI_107',
                        'PSSI_121',
                        'PSSI_135']].sum(axis=1)

    #NT = kritisch-negativistisch
    df['PSSI_NT'] = df[['PSSI_10',
                        'PSSI_24',
                        'PSSI_38',
                        'PSSI_52',
                        'PSSI_66',
                        'PSSI_80',
                        'PSSI_94',
                        'PSSI_108',
                        'PSSI_122',
                        'PSSI_136']].sum(axis=1)

    # DP = still depressiv
    df['PSSI_DP'] = df[['PSSI_11',
                        'PSSI_25',
                        'PSSI_39',
                        'PSSI_53',
                        'PSSI_67',
                        'PSSI_81',
                        'PSSI_95',
                        'PSSI_109',
                        'PSSI_123',
                        'PSSI_137']].sum(axis=1)

    #SL = hilfsbereit-selbstlos
    df['PSSI_SL'] = df[['PSSI_12',
                        'PSSI_26',
                        'PSSI_40',
                        'PSSI_54',
                        'PSSI_68',
                        'PSSI_82',
                        'PSSI_96',
                        'PSSI_110',
                        'PSSI_124',
                        'PSSI_138']].sum(axis=1)

    #RH = optimistisch-rhapsodisch
    df['PSSI_RH'] = df[['PSSI_13',
                        'PSSI_27',
                        'PSSI_41',
                        'PSSI_55',
                        'PSSI_69',
                        'PSSI_83',
                        'PSSI_97',
                        'PSSI_111',
                        'PSSI_125',
                        'PSSI_139']].sum(axis=1)

    #AS = selbstbehauptend-antisozial
    df['PSSI_AS'] = df[['PSSI_14',
                        'PSSI_28',
                        'PSSI_42',
                        'PSSI_56',
                        'PSSI_70',
                        'PSSI_84',
                        'PSSI_98',
                        'PSSI_112',
                        'PSSI_126',
                        'PSSI_140']].sum(axis=1)

    cols_export = ['ids'] + ["PSSI_PN", 'PSSI_SZ', 'PSSI_ST', 'PSSI_BL',
                            'PSSI_HI', 'PSSI_NA', 'PSSI_SU', 'PSSI_AB',
                            'PSSI_ZW', 'PSSI_NT', 'PSSI_DP', 'PSSI_SL',
                            'PSSI_RH', 'PSSI_AS']

    df[cols_export].to_csv('%s/PSSI.csv' % out_dir, decimal='.', index=False)


##############################################################################
################################## MMI #######################################
##############################################################################

def run_MMI(df, out_dir):

#items to be recoded
    cols= ['MMI_1_4_A' ,'MMI_1_4_B' ,'MMI_1_4_C' ,'MMI_1_4_D' ,'MMI_1_4_E' ,'MMI_1_4_F' ,
           'MMI_1_4_G' ,'MMI_1_4_H' ,'MMI_1_4_I' ,'MMI_1_4_J' ,'MMI_1_4_K' ,'MMI_1_4_L' ,
           'MMI_2_4_A' ,'MMI_2_4_B' ,'MMI_2_4_C' ,'MMI_2_4_D' ,'MMI_2_4_E' ,'MMI_2_4_F' ,
           'MMI_2_4_G' ,'MMI_2_4_H' ,'MMI_2_4_I' ,'MMI_2_4_J' ,'MMI_2_4_K' ,'MMI_2_4_L' ,
           'MMI_3_4_A' ,'MMI_3_4_B' ,'MMI_3_4_C' ,'MMI_3_4_D' ,'MMI_3_4_E' , 'MMI_3_4_F' ,
           'MMI_3_4_G' ,'MMI_3_4_H' ,'MMI_3_4_I' ,'MMI_3_4_J' ,'MMI_3_4_K' ,'MMI_3_4_L' ,
           'MMI_4_4_A' ,'MMI_4_4_B' ,'MMI_4_4_C' ,'MMI_4_4_D' ,'MMI_4_4_E' ,'MMI_4_4_F' ,
           'MMI_4_4_G' ,'MMI_4_4_H' ,'MMI_4_4_I' ,'MMI_4_4_J' ,'MMI_4_4_K' ,'MMI_4_4_L' ,
           'MMI_5_4_A' ,'MMI_5_4_B' ,'MMI_5_4_C' ,'MMI_5_4_D' ,'MMI_5_4_E' ,'MMI_5_4_F' ,
           'MMI_5_4_G' ,'MMI_5_4_H' ,'MMI_5_4_I' ,'MMI_5_4_J' ,'MMI_5_4_K' ,'MMI_5_4_L' ,
           'MMI_6_4_A' ,'MMI_6_4_B' ,'MMI_6_4_C' ,'MMI_6_4_D' ,'MMI_6_4_E' ,'MMI_6_4_F' ,
           'MMI_6_4_G' ,'MMI_6_4_H' ,'MMI_6_4_I' ,'MMI_6_4_J' ,'MMI_6_4_K' ,'MMI_6_4_L' ,
           'MMI_7_4_A' ,'MMI_7_4_B' ,'MMI_7_4_C' ,'MMI_7_4_D' ,'MMI_7_4_E' ,'MMI_7_4_F' ,
           'MMI_7_4_G' ,'MMI_7_4_H' ,'MMI_7_4_I' ,'MMI_7_4_J' ,'MMI_7_4_K' ,'MMI_7_4_L' ,
           'MMI_8_4_A' ,'MMI_8_4_B' ,'MMI_8_4_C' ,'MMI_8_4_D' ,'MMI_8_4_E' ,'MMI_8_4_F' ,
           'MMI_8_4_G' ,'MMI_8_4_H' ,'MMI_8_4_I' ,'MMI_8_4_J' ,'MMI_8_4_K' ,'MMI_8_4_L' ,
           'MMI_9_6_A','MMI_9_6_B' ,'MMI_9_6_C' ,'MMI_9_6_D' ,'MMI_9_6_E' ,'MMI_9_6_F' ,
           'MMI_9_6_G' ,'MMI_9_6_H' ,'MMI_9_6_I' ,'MMI_9_6_J' ,'MMI_9_6_K' ,'MMI_9_6_L' ,
           'MMI_10_4_A' ,'MMI_10_4_B' ,'MMI_10_4_C' ,'MMI_10_4_D' ,'MMI_10_4_E' ,'MMI_10_4_F' ,
           'MMI_10_4_G' ,'MMI_10_4_H' ,'MMI_10_4_I' ,'MMI_10_4_J' ,'MMI_10_4_K' ,'MMI_10_4_L' ,
           'MMI_11_4_A' ,'MMI_11_4_B' ,'MMI_11_4_C' ,'MMI_11_4_D' ,'MMI_11_4_E' ,'MMI_11_4_F' ,
           'MMI_11_4_G' ,'MMI_11_4_H' ,'MMI_11_4_I' ,'MMI_11_4_J' ,'MMI_11_4_K' ,'MMI_11_4_L' ,
           'MMI_12_4_A' ,'MMI_12_4_B' ,'MMI_12_4_C' ,'MMI_12_4_D' ,'MMI_12_4_E' ,'MMI_12_4_F' ,
           'MMI_12_4_G' ,'MMI_12_4_H']

    #recode items
    recoder = {5 :'NaN', 4 :1, 3:0.66, 2:0.33, 1:0}
    for i in cols:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum for media types
    df['MMI1'] = df[['MMI_1_4_A',
                     'MMI_1_4_B',
                     'MMI_1_4_C',
                     'MMI_1_4_D',
                     'MMI_1_4_E',
                     'MMI_1_4_F',
                     'MMI_1_4_G',
                     'MMI_1_4_H',
                     'MMI_1_4_I',
                     'MMI_1_4_J',
                     'MMI_1_4_K',
                     'MMI_1_4_L']].sum(axis=1).astype('float64')

    df['MMI2'] = df[['MMI_2_4_A' ,
                     'MMI_2_4_B' ,
                     'MMI_2_4_C' ,
                     'MMI_2_4_D' ,
                     'MMI_2_4_E' ,
                     'MMI_2_4_F' ,
                     'MMI_2_4_G' ,
                     'MMI_2_4_H' ,
                     'MMI_2_4_I' ,
                     'MMI_2_4_J' ,
                     'MMI_2_4_K' ,
                     'MMI_2_4_L']].sum(axis=1).astype('float64')

    df['MMI3'] = df[['MMI_3_4_A',
                     'MMI_3_4_B',
                     'MMI_3_4_C',
                     'MMI_3_4_D',
                     'MMI_3_4_E',
                     'MMI_3_4_F',
                     'MMI_3_4_G',
                     'MMI_3_4_H',
                     'MMI_3_4_I',
                     'MMI_3_4_J',
                     'MMI_3_4_K',
                     'MMI_3_4_L']].sum(axis=1).astype('float64')

    df['MMI4'] = df[['MMI_4_4_A',
                     'MMI_4_4_B',
                     'MMI_4_4_C',
                     'MMI_4_4_D',
                     'MMI_4_4_E',
                     'MMI_4_4_F',
                     'MMI_4_4_G',
                     'MMI_4_4_H',
                     'MMI_4_4_I',
                     'MMI_4_4_J',
                     'MMI_4_4_K',
                     'MMI_4_4_L']].sum(axis=1).astype('float64')

    df['MMI5'] = df[['MMI_5_4_A',
                     'MMI_5_4_B',
                     'MMI_5_4_C',
                     'MMI_5_4_D',
                     'MMI_5_4_E',
                     'MMI_5_4_F',
                     'MMI_5_4_G',
                     'MMI_5_4_H',
                     'MMI_5_4_I',
                     'MMI_5_4_J',
                     'MMI_5_4_K',
                     'MMI_5_4_L']].sum(axis=1).astype('float64')

    df['MMI6'] = df[['MMI_6_4_A',
                     'MMI_6_4_B',
                     'MMI_6_4_C',
                     'MMI_6_4_D',
                     'MMI_6_4_E',
                     'MMI_6_4_F',
                     'MMI_6_4_G',
                     'MMI_6_4_H',
                     'MMI_6_4_I',
                     'MMI_6_4_J',
                     'MMI_6_4_K',
                     'MMI_6_4_L']].sum(axis=1).astype('float64')

    df['MMI7'] = df[['MMI_7_4_A',
                     'MMI_7_4_B',
                     'MMI_7_4_C',
                     'MMI_7_4_D',
                     'MMI_7_4_E',
                     'MMI_7_4_F',
                     'MMI_7_4_G',
                     'MMI_7_4_H',
                     'MMI_7_4_I',
                     'MMI_7_4_J',
                     'MMI_7_4_K',
                     'MMI_7_4_L']].sum(axis=1).astype('float64')

    df['MMI8'] = df[['MMI_8_4_A',
                     'MMI_8_4_B',
                     'MMI_8_4_C',
                     'MMI_8_4_D',
                     'MMI_8_4_E',
                     'MMI_8_4_F',
                     'MMI_8_4_G',
                     'MMI_8_4_H',
                     'MMI_8_4_I',
                     'MMI_8_4_J',
                     'MMI_8_4_K',
                     'MMI_8_4_L']].sum(axis=1).astype('float64')

    df['MMI9'] = df[['MMI_9_6_A',
                     'MMI_9_6_B',
                     'MMI_9_6_C',
                     'MMI_9_6_D',
                     'MMI_9_6_E',
                     'MMI_9_6_F',
                     'MMI_9_6_G',
                     'MMI_9_6_H',
                     'MMI_9_6_I',
                     'MMI_9_6_J',
                     'MMI_9_6_K',
                     'MMI_9_6_L']].sum(axis=1).astype('float64')

    df['MMI10'] = df[['MMI_10_4_A',
                     'MMI_10_4_B',
                     'MMI_10_4_C',
                     'MMI_10_4_D',
                     'MMI_10_4_E',
                     'MMI_10_4_F',
                     'MMI_10_4_G',
                     'MMI_10_4_H',
                     'MMI_10_4_I',
                     'MMI_10_4_J',
                     'MMI_10_4_K',
                     'MMI_10_4_L']].sum(axis=1).astype('float64')

    df['MMI11'] = df[['MMI_11_4_A',
                     'MMI_11_4_B',
                     'MMI_11_4_C',
                     'MMI_11_4_D',
                     'MMI_11_4_E',
                     'MMI_11_4_F',
                     'MMI_11_4_G',
                     'MMI_11_4_H',
                     'MMI_11_4_I',
                     'MMI_11_4_J',
                     'MMI_11_4_K',
                     'MMI_11_4_L']].sum(axis=1).astype('float64')

    df['MMI12'] = df[['MMI_12_4_A',
                     'MMI_12_4_B',
                     'MMI_12_4_C',
                     'MMI_12_4_D',
                     'MMI_12_4_E',
                     'MMI_12_4_F',
                     'MMI_12_4_G',
                     'MMI_12_4_H',
                     'MMI_12_4_I',
                     'MMI_12_4_J',
                     'MMI_12_4_K',
                     'MMI_12_4_L']].sum(axis=1).astype('float64')

    df['TotalHours'] = df[['MMI_1_1','MMI_2_1', 'MMI_3_1', 'MMI_4_1', 'MMI_5_1', 'MMI_6_1', 'MMI_7_1', 'MMI_8_1',
                           'MMI_9_1', 'MMI_10_1', 'MMI_11_1', 'MMI_12_1']].sum(axis=1).astype('float64')

    #mediatypes weighted by hours of primary medium divided by hours spent with all media

    df['MMI1xhours‎dividedbytotalhours'] = df['MMI1']*df['MMI_1_1'].astype('float64')/df['TotalHours']
    df['MMI2xhours‎dividedbytotalhours'] = df['MMI2']*df['MMI_2_1'].astype('float64')/df['TotalHours']
    df['MMI3xhours‎dividedbytotalhours'] = df['MMI3']*df['MMI_3_1'].astype('float64')/df['TotalHours']
    df['MMI4xhours‎dividedbytotalhours'] = df['MMI4']*df['MMI_4_1'].astype('float64')/df['TotalHours']
    df['MMI5xhours‎dividedbytotalhours'] = df['MMI5']*df['MMI_5_1'].astype('float64')/df['TotalHours']
    df['MMI6xhours‎dividedbytotalhours'] = df['MMI6']*df['MMI_6_1'].astype('float64')/df['TotalHours']
    df['MMI7xhours‎dividedbytotalhours'] = df['MMI7']*df['MMI_7_1'].astype('float64')/df['TotalHours']
    df['MMI8xhours‎dividedbytotalhours'] = df['MMI8']*df['MMI_8_1'].astype('float64')/df['TotalHours']
    df['MMI9xhours‎dividedbytotalhours'] = df['MMI9']*df['MMI_9_1'].astype('float64')/df['TotalHours']
    df['MMI10xhours‎dividedbytotalhours'] = df['MMI10']*df['MMI_10_1'].astype('float64')/df['TotalHours']
    df['MMI11xhours‎dividedbytotalhours'] = df['MMI11']*df['MMI_11_1'].astype('float64')/df['TotalHours']
    df['MMI12xhours‎dividedbytotalhours'] = df['MMI12']*df['MMI_12_1'].astype('float64')/df['TotalHours']


    #Index by summing the weighted scales

    df['MMI_score'] = df[['MMI1xhours‎dividedbytotalhours',
                        'MMI2xhours‎dividedbytotalhours',
                        'MMI3xhours‎dividedbytotalhours',
                        'MMI4xhours‎dividedbytotalhours',
                        'MMI5xhours‎dividedbytotalhours',
                        'MMI6xhours‎dividedbytotalhours',
                        'MMI7xhours‎dividedbytotalhours',
                        'MMI8xhours‎dividedbytotalhours',
                        'MMI9xhours‎dividedbytotalhours',
                        'MMI10xhours‎dividedbytotalhours',
                        'MMI11xhours‎dividedbytotalhours',
                        'MMI12xhours‎dividedbytotalhours']].sum(axis=1)

    cols_export = ['ids'] + ['MMI_score']

    df[cols_export].to_csv('%s/MMI.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################## BIS/BAS #######################################
##############################################################################

def run_BISBAS(df, out_dir):

    #items to be recoded
    items_recoded = ['BISBAS_2',
                     'BISBAS_22']

    #recode items
    recoder = {1:4, 2:3, 3:2, 4:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    #Calculate total score as the sum of Item 1-22.
    df['BISBAS_BIS_sum'] = df[['BISBAS_2', 'BISBAS_8', 'BISBAS_13', 'BISBAS_16',
                       'BISBAS_19', 'BISBAS_22', 'BISBAS_24']].sum(axis=1)


    df['BISBAS_BAS_sum'] = df[['BISBAS_3', 'BISBAS_9', 'BISBAS_12', 'BISBAS_21',
                       'BISBAS_5', 'BISBAS_10', 'BISBAS_15', 'BISBAS_20',
                       'BISBAS_4', 'BISBAS_7', 'BISBAS_14', 'BISBAS_18',
                       'BISBAS_23']].sum(axis=1)

    cols_export = ['ids'] + ['BISBAS_BIS_sum', 'BISBAS_BAS_sum']

    df[cols_export].to_csv('%s/BISBAS.csv' % out_dir, decimal='.', index=False)



##############################################################################
################################# STAI #######################################
##############################################################################

def run_STAI(df, out_dir):

    cols = ['STAI_1','STAI_2','STAI_3','STAI_4','STAI_5','STAI_6','STAI_7','STAI_8',
                 'STAI_9','STAI_10','STAI_11','STAI_12','STAI_13','STAI_14','STAI_15','STAI_16',
                 'STAI_17','STAI_18','STAI_19','STAI_20']

    items_recoded = ['STAI_1', 'STAI_6', 'STAI_7', 'STAI_10',
                     'STAI_13', 'STAI_16', 'STAI_19']

    recoder = {1:4, 2:3, 3:2, 4:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype('float64')

    df['STAI_A-Trait_summary_sum'] = df[cols].sum(axis=1)

    cols_export = ['ids'] + ['STAI_A-Trait_summary_sum']

    df[cols_export].to_csv('%s/STAI-G-X2.csv' % out_dir, decimal='.', index=False)



##############################################################################
############################### STAXI ########################################
##############################################################################

def run_STAXI(df, out_dir):


    cols_trait2 = ['STAXI_11','STAXI_12','STAXI_13','STAXI_14','STAXI_15',
                  'STAXI_16','STAXI_17','STAXI_18','STAXI_19','STAXI_20']
    cols_trait3_inward = ['STAXI_22', 'STAXI_24','STAXI_25', 'STAXI_28',
                          'STAXI_30', 'STAXI_41','STAXI_42', 'STAXI_44']
    cols_trait3_outward = ['STAXI_26','STAXI_27', 'STAXI_31', 'STAXI_35',
                           'STAXI_37','STAXI_38','STAXI_39', 'STAXI_43']
    cols_trait3_control = ['STAXI_21', 'STAXI_23', 'STAXI_29', 'STAXI_32',
                           'STAXI_33','STAXI_34', 'STAXI_36', 'STAXI_40']

    df["STAXI_anger_trait"] = df[cols_trait2].sum(axis=1)
    df["STAXI_anger_inward"] = df[cols_trait3_inward].sum(axis=1)
    df["STAXI_anger_outward"] = df[cols_trait3_outward].sum(axis=1)
    df["STAXI_anger_control"] = df[cols_trait3_control].sum(axis=1)

    cols_export = ['ids'] + ["STAXI_anger_trait", "STAXI_anger_inward", "STAXI_anger_outward", "STAXI_anger_control"]

    df[cols_export].to_csv('%s/STAXI.csv' % out_dir, decimal='.', index=False)
