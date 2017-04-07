# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:18:21 2015

@author: jgolchert
"""

 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

            
##############################################################################            
################################# TMT ########################################
##############################################################################

def run_TMT(df):
    
     cols = ['ids',
             'TMT_1',
             'TMT_2',
             'TMT_3',
             'TMT_4',
             'TMT_5',
             'TMT_6',
             'TMT_7',
             'TMT_8']
     
     #TMT A numbers: seconds
     print 'TMT_A: seconds to complete'
     
     TMT_A_numb_sec = df['TMT_1']
     TMT_A_numb_sec = TMT_A_numb_sec.astype('float64')
     print TMT_A_numb_sec.describe()
     
     TMT_A_numb_sec = list(TMT_A_numb_sec.dropna())
     sns.distplot(TMT_A_numb_sec, kde = True, label = 'TMT_A')
     plt.xlabel('TMT_A_sec', fontsize = 14)
     
     
     #TMT A: brain functions (TMT_2)
     print 'TMT_A: brain functions'
     
     TMT_A_brain = df['TMT_2']
     print TMT_A_brain.describe()
     
     
     #TMT A: errors   
     print '\n' 'TMT_A: errors'
     
     TMT_A_numb_err = df['TMT_3']
     print TMT_A_numb_err.describe()
     
     TMT_A_numb_err = list(TMT_A_numb_err.dropna())
     count = 0
     for err in TMT_A_numb_err:
         if err > 0:
             count = count + 1
     print 'at least one error: N = %s' %count    
     
     
     #TMT A: comments (TMT_4)
     
     
     #TMT_B: seconds
     print '\n', 'TMT_B: seconds to complete'   
     
     TMT_B_sec = df['TMT_5']
     TMT_B_sec = TMT_B_sec.astype('float64')
     print TMT_B_sec.describe()
     
     TMT_B_sec = list(TMT_B_sec.dropna())
     sns.distplot(TMT_B_sec, kde = True, label = 'TMT_B')
     plt.xlabel('sec', fontsize = 14)
     
    
    #TMT B: brain functions (TMT_6)     
     print 'TMT_B: brain functions'
     
     TMT_B_brain = df['TMT_6']
     print TMT_B_brain.describe()
     
     
    #TMT B: errors 
     print '\n' 'TMT_B: errors'
     
     TMT_B_err = df['TMT_7']
     print TMT_B_err.describe()
     
     TMT_B_err = list(TMT_B_err.dropna())
     count = 0
     for err in TMT_B_err:
         if err > 0:
             count = count + 1
     print 'at least one error: N = %s' %count     
     
     
     #TMT B: comments (TMT_8)
     
     
##############################################################################      
########################## Wortschatztest ####################################
############################################################################## 

def run_WST(df):
    
    cols = ['ids',
            'WST_1',
            'WST_2',
            'WST_3',
            'WST_4',
            'WST_5']
    
    print 'Measure of verbal intelligence: Task: find real words; Max = 42'
    print '\n', 'WST raw scores'
    
    WST_RW = df['WST_1']
    print WST_RW.describe()
    
    WST_RW = list(WST_RW.dropna())
    sns.distplot(WST_RW, kde = True)
    
    #WST_2,3,4,5 contain transformed scores: z-scores, IQ, Z-scores, comments (see info file)

##############################################################################     
##################### Leistungsprüfsystem Subtest 3 ########################## 
############################################################################## 
    
def run_LPS(df):
    
    cols = ['ids',
            'LPS_1',
            'LPS_2']
    
    print 'Measure of reasoning: Task: find correct symbol; Max = 40'
    print '\n', 'LPS raw scores'
    
    LPS_RW = df['LPS_1']
    print LPS_RW.describe()
    
    LPS_RW = list(LPS_RW.dropna())
    sns.distplot(LPS_RW, kde = True)
    
    #LPS_2 contains comments
    

##############################################################################     
################ Regensburger Wortflüssigkeitstest ########################### 
############################################################################## 

def run_RWT(df):
    
    cols = ['ids',
            'RWT_1',
            'RWT_2'
            'RWT_3',
            'RWT_4',
            'RWT_5',
            'RWT_6',
            'RWT_7',
            'RWT_8',
            'RWT_9',
            'RWT_10',
            'RWT_11',
            'RWT_12',
            'RWT_13',
            'RWT_14',
            'RWT_15',
            'RWT_16',
            'RWT_17',
            'RWT_18',
            'RWT_19',
            'RWT_20',
            'RWT_21',
            'RWT_22',
            'RWT_23',
            'RWT_24']
    
    print "measures verbal fluency: Task: find as many words as you can from a category (animals) or with a certain letter (s)"
    
    ####s words  (sum across the two minutes)   
    print '\n', "S-words: Raw scores: sum across 2 minutes"
    
    RWT_words_sum = df['RWT_8']

    print RWT_words_sum.describe()
    
    RWT_words_sum = list(RWT_words_sum.dropna())
    sns.distplot(RWT_words_sum, kde = True) 
        
    #Repetitions s-words (sum across the two minutes) 
    print '\n' 'Repetitions S-words across 2 minutes'
     
    RWT_words_rep = df['RWT_10']
     
    print RWT_words_rep.describe()
     
    RWT_words_rep = list(RWT_words_rep.dropna())
    count = 0
    for rep in RWT_words_rep:
        if rep > 0:
            count = count + 1
    print 'at least one rep: N(subjects) = %s' %count 
    
    
    #rule books (rule breaks in total across the two minutes)
    print '\n' 'rule breaks s-words'
    
    RWT_words_rules = df['RWT_11']
     
    print RWT_words_rules.describe()
     
    RWT_words_rules = list(RWT_words_rules.dropna())
    count = 0
    for rules in RWT_words_rules:
        if rules > 0:
            count = count + 1
    print 'at least one rule break: N(subjects) = %s' %count 
 
    
    ###animals### 
    #sum score across the two minutes
    print '\n', "ANIMALS: Raw scores: sum across 2 minutes"
    
    RWT_animals_sum = df['RWT_20']

    print RWT_animals_sum.describe()
    
    RWT_animals_sum = list(RWT_animals_sum.dropna())
    sns.distplot(RWT_animals_sum, kde = True) 
    plt.xlabel('number of words', fontsize = 14)
    
    #Repetitions animal-words  (sum across the two minutes)
    print '\n' 'Repetitions animal-words across 2 minutes'
     
    RWT_animals_rep = df['RWT_22']
     
    print RWT_animals_rep.describe()
     
    RWT_animals_rep = list(RWT_animals_rep.dropna())
    count = 0
    for rep in RWT_animals_rep:
        if rep > 0:
            count = count + 1
    print 'at least one rep: N(subjects) = %s' %count 
    
    
    #rule breaks animals (sum across the two minutes)
    print '\n' 'rule breaks animals-words'
    
    RWT_animals_rules = df['RWT_23']
     
    print RWT_animals_rules.describe()
     
    RWT_animals_rules = list(RWT_animals_rules.dropna())
    count = 0
    for rules in RWT_animals_rules:
        if rules > 0:
            count = count + 1
    print 'at least one rule break: N(subjects) = %s' %count 
    
 

##############################################################################    
#################################### TAP #####################################
############################################################################## 

############################# TAP Alertness ##################################

def run_TAP_A(df):
    
    cols = ['TAP_A_1',
            'TAP_A_2',
            'TAP_A_3',
            'TAP_A_4',
            'TAP_A_5',
            'TAP_A_6',
            'TAP_A_7',
            'TAP_A_8',
            'TAP_A_9',
            'TAP_A_10',
            'TAP_A_11',
            'TAP_A_12',
            'TAP_A_13',
            'TAP_A_14',
            'TAP_A_15',
            'TAP_A_16',
            'TAP_A_17']
    
    print '\n' 'Task: press button when target stim appears on screen; two conditions: with and without prime/signal (tone)'
    print 'two runs for each condition'
    
    print '\n\n' 'ALERT: conditions without signal: mean reaction times'

    Alert_no_sig_Mean = df['TAP_A_5']
    print Alert_no_sig_Mean.describe()
    
    Alert_no_sig_Mean = list(Alert_no_sig_Mean.dropna())
    sns.distplot(Alert_no_sig_Mean, kde = True)    
    
    
    ### condition with signal
    print '\n' 'ALERT: conditions with signal: mean reaction times'
    
    Alert_sig_Mean = df['TAP_A_10']
    print Alert_sig_Mean.describe()
    
    Alert_sig_Mean = list(Alert_sig_Mean.dropna())
    sns.distplot(Alert_sig_Mean, kde = True) 
    plt.xlabel('Mean_RTs', fontsize = 14)
    plt.show()
    
########################## TAP incompat ######################################
def run_TAP_I(df):
    
    cols = ['TAP_I_1',
            'TAP_I_2',
            'TAP_I_3',
            'TAP_I_4',
            'TAP_I_5',
            'TAP_I_6',
            'TAP_I_7',
            'TAP_I_8',
            'TAP_I_9',
            'TAP_I_10',
            'TAP_I_11',
            'TAP_I_12',
            'TAP_I_13',
            'TAP_I_14',
            'TAP_I_15',
            'TAP_I_16',
            'TAP_I_17',
            'TAP_I_18',
            'TAP_I_19',
            'TAP_I_20',
            'TAP_I_21',
            'TAP_I_22',
            'TAP_I_23',
            'TAP_I_24',
            'TAP_I_25',
            'TAP_I_26',
            'TAP_I_27',
            'TAP_I_28']    
            
            
    print '\n' 'Task: button press left/right depending on which side an arrow points (ignore on which side target appears)'
    print 'two runs for each condition - congruent/incongruent'    
    
    #congruent condition
    print '\n\n' 'congruent condition: mean reaction times' 
    
    compat_Mean = df['TAP_I_1']
    print compat_Mean.describe()
    
    compat_Mean = list(compat_Mean.dropna())
    sns.distplot(compat_Mean, kde = True) 
    
    
    # incongruent condition
    print '\n\n' 'incongruent condition: mean reaction times'
    
    incompat_Mean = df['TAP_I_8']
    print incompat_Mean.describe()    
    
    incompat_Mean = list(incompat_Mean.dropna())
    sns.distplot(incompat_Mean, kde = True)     
    plt.xlabel('Mean_RTs', fontsize = 14)
    plt.show()
    
########################## TAP WM ############################################
def run_TAP_WM(df):
    
    cols = ['TAP_WM_1',
            'TAP_WM_2',
            'TAP_WM_3',
            'TAP_WM_4',
            'TAP_WM_5',
            'TAP_WM_6',
            'TAP_WM_7',
            'TAP_WM_8',
            'TAP_WM_9',
            'TAP_WM_10',
            'TAP_WM_11',
            'TAP_WM_12']  
            
            
    print '\n' 'Task: button press if a number is equal to the second last number (numbers 1-9)'
    
    print '\n\n' 'mean reaction times'
    WM_means_ms = df['TAP_WM_1']
    print WM_means_ms.describe()
    
    WM_means_ms = list(WM_means_ms.dropna())
    sns.distplot(WM_means_ms, kde = True)     
    plt.xlabel('Mean_RTs', fontsize = 14)
    plt.show()