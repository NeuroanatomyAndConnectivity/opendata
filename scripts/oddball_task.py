#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Januar 22, 2015, at 13:22
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from numpy import *

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'gabor_sound_staircase_german'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'vision_startval': u'', u'audition_startval': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr_vision"
instr_visionClock = core.Clock()
instruction_vision = visual.TextStim(win=win, ori=0, name='instruction_vision',
    text=u'In diesem Teil des Experiments werden Ihnen in schneller Abfolge einzelne graue Kreise pr\xe4sentiert.\nIn seltenen F\xe4llen enthalten diese Kreise jedoch Streifen. Diese sind mehr oder weniger gut erkennbar. \n\nIhre Aufgabe ist es, bei jedem Kreis so schnell und so pr\xe4zise wie m\xf6glich zu entscheiden, ob der Kreis einfach nur grau ist oder ob er Streifen enth\xe4lt.\nWenn Sie der Meinung sind, dass der Kreis KEINE Streifen enth\xe4lt, dann dr\xfccken Sie bitte NICHTS.\nWenn Sie der Meinung sind, dass der gezeigte Kreis Streifen enth\xe4lt, dann dr\xfccken Sie bitte die LEERTASTE.\nBevor ein Kreis erscheint, sehen Sie ein Kreuz. Bitte fixieren Sie dieses.\n\n\n\nDr\xfccken Sie bitte die Leertaste um fortzufahren.\n\n',    font='Arial',
    units='pix', pos=[0, 0], height=25, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr_vision_parttwo"
instr_vision_parttwoClock = core.Clock()
instruction_slider_vision = visual.TextStim(win=win, ori=0, name='instruction_slider_vision',
    text=u'Gelegentlich wird das Experiment au\xdferdem unterbrochen. Hierbei werden Sie dann befragt, woran Sie kurz vor der jeweiligen Unterbrechung gedacht haben. Zur Beantwortung der Fragen steht Ihnen eine Skala zur Verf\xfcgung. Mit Hilfe der Maus k\xf6nnen Sie ein blaues Dreieck auf dieser Skala zu der Stelle bewegen, die am besten auf Ihre Gedanken zutrifft. Sie k\xf6nnen die ganze Skala ausnutzen, wenn Sie wollen.\n\n\nNochmal zur Erinnerung: \n- Fixieren Sie das Kreuz \n- Kreis ohne Streifen = nichts dr\xfccken\n- Kreis mit erkennbaren Streifen = Leertaste\n\nSollten Sie nun noch Fragen haben, wenden Sie sich bitte jetzt an den Versuchsleiter. \n\nAndernfalls dr\xfccken Sie bitte die Leertaste um mit dem Experiment zu beginnen. ',    font='Arial',
    units='pix', pos=[0, 0], height=25, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "get_ready_vision"
get_ready_visionClock = core.Clock()
get_ready_vision_text = visual.TextStim(win=win, ori=0, name='get_ready_vision_text',
    text='In 5 Sekunden geht es los ... ',    font='Arial',
    units='pix', pos=[0, 50], height=25, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
count_five = visual.TextStim(win=win, ori=0, name='count_five',
    text='5',    font='Arial',
    pos=[0, -10], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
count_four = visual.TextStim(win=win, ori=0, name='count_four',
    text='4',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
count_three = visual.TextStim(win=win, ori=0, name='count_three',
    text='3',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
count_two = visual.TextStim(win=win, ori=0, name='count_two',
    text='2',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
count_one = visual.TextStim(win=win, ori=0, name='count_one',
    text='1',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "stand_trial_vision"
stand_trial_visionClock = core.Clock()
stand_fixation_vision = visual.TextStim(win=win, ori=0, name='stand_fixation_vision',
    text=u'+',    font=u'Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None,
    color=[0.00,0.00,0.00], colorSpace='rgb', opacity=1,
    depth=0.0)
stand_grating_vision = visual.GratingStim(win=win, name='stand_grating_vision',
    tex='sin', mask='gauss',
    ori=0, pos=[0, 0], size=[100, 100], sf=0.1, phase=0.0,
    color=[0.00,0.00,0.00], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "dev_trial_vision"
dev_trial_visionClock = core.Clock()
dev_fixiation_vision = visual.TextStim(win=win, ori=0, name='dev_fixiation_vision',
    text=u'+',    font=u'Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None,
    color=[0.00,0.00,0.00], colorSpace='rgb', opacity=1,
    depth=0.0)
dev_grating_vision = visual.GratingStim(win=win, name='dev_grating_vision',units='pix', 
    tex='sin', mask='gauss',
    ori=0, pos=[0, 0], size=[100, 100], sf=0.1, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "MW_questions_vision"
MW_questions_visionClock = core.Clock()
MW_questions_text = visual.TextStim(win=win, ori=0, name='MW_questions_text',
    text='default text',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
probes_rating_vision = visual.RatingScale(win=win, name='probes_rating_vision', marker='triangle', size=1, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='trifft gar nicht zu                                 trifft vollkommen zu', markerStart='0')

# Initialize components for Routine "MW_questions_vision_parttwo"
MW_questions_vision_parttwoClock = core.Clock()
MW_questions_pos_neg_vision = visual.TextStim(win=win, ori=0, name='MW_questions_pos_neg_vision',
    text='Vor der Unterbrechung waren meine Gedanken:',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
probes_ratings_vision_Pos_Neg = visual.RatingScale(win=win, name='probes_ratings_vision_Pos_Neg', marker='triangle', size=1.0, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='negativ                                            positiv', markerStart='0')

# Initialize components for Routine "MW_questions_vision_partThree"
MW_questions_vision_partThreeClock = core.Clock()
MW_questions_vision_spec_vague = visual.TextStim(win=win, ori=0, name='MW_questions_vision_spec_vague',
    text='Vor der Unterbrechung waren meine Gedanken:',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
MW_rating_vision_spec_vague = visual.RatingScale(win=win, name='MW_rating_vision_spec_vague', marker='triangle', size=1.0, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='spezifsch                                          vage', markerStart='0')

# Initialize components for Routine "instr_audition"
instr_auditionClock = core.Clock()
instruction_audition = visual.TextStim(win=win, ori=0, name='instruction_audition',
    text=u'In diesem Teil des Experiments werden Ihnen in schneller Abfolge einzelne T\xf6ne pr\xe4sentiert.\nSetzen Sie dazu bitte jetzt die Kopfh\xf6rer auf.\n\nIn seltenen F\xe4llen klingen diese T\xf6ne nicht ganz normal, sondern scheinen etwas zu schwanken. \n\nIhre Aufgabe ist es, bei jedem Ton so schnell und so pr\xe4zise wie m\xf6glich zu entscheiden, ob der Ton ganz normal ist oder ob er sich ver\xe4ndert anh\xf6rt.\nWenn Sie der Meinung sind, dass der Ton NORMAL ist, dann dr\xfccken Sie bitte NICHTS.\nWenn Sie der Meinung sind, dass der Ton nicht ganz normal ist, dann dr\xfccken Sie bitte die LEERTASTE.\nBevor Sie einen Ton h\xf6ren, sehen Sie ein Kreuz. Bitte fixieren Sie dieses.\n\n\nDr\xfccken Sie bitte die Leertaste um fortzufahren.\n\n',    font='Arial',
    pos=[0, 0], height=25, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "intro_audition_parttwo"
intro_audition_parttwoClock = core.Clock()
instruction_audition_slider = visual.TextStim(win=win, ori=0, name='instruction_audition_slider',
    text=u'Gelegentlich wird das Experiment au\xdferdem unterbrochen. Hierbei werden Sie dann befragt, woran Sie kurz vor der jeweiligen Unterbrechung gedacht haben. Zur Beantwortung der Fragen steht Ihnen eine Skala zur Verf\xfcgung. Mit Hilfe der Maus k\xf6nnen Sie ein blaues Dreieck auf dieser Skala zu der Stelle bewegen, die am besten auf Ihre Gedanken zutrifft. Sie k\xf6nnen die ganze Skala ausnutzen, wenn Sie wollen.\n\n\nNochmal zur Erinnerung: \n- Fixieren Sie das Kreuz \n- ganz normaler Ton = nichts dr\xfccken\n- schwankender Ton = Leertaste\n\nSollten Sie nun noch Fragen haben, wenden Sie sich bitte jetzt an den Versuchsleiter. \n\nAndernfalls dr\xfccken Sie bitte die Leertaste um mit dem Experiment zu beginnen. ',    font='Arial',
    pos=[0, 0], height=25, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "get_ready_audition"
get_ready_auditionClock = core.Clock()
get_ready_audition_test = visual.TextStim(win=win, ori=0, name='get_ready_audition_test',
    text='In 5 Sekunden geht es los ... ',    font='Arial',
    units='pix', pos=[0, 50], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
count_five_audio = visual.TextStim(win=win, ori=0, name='count_five_audio',
    text='5',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
count_four_audio = visual.TextStim(win=win, ori=0, name='count_four_audio',
    text='4',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
count_three_audio = visual.TextStim(win=win, ori=0, name='count_three_audio',
    text='3',    font='Arial',
    pos=[0,-10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
count_two_audio = visual.TextStim(win=win, ori=0, name='count_two_audio',
    text='2',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
count_one_audio = visual.TextStim(win=win, ori=0, name='count_one_audio',
    text='1',    font='Arial',
    pos=[0, -10], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "stand_trial_audition"
stand_trial_auditionClock = core.Clock()
stand_fixation_audition = visual.TextStim(win=win, ori=0, name='stand_fixation_audition',
    text=u'+',    font=u'Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None,
    color=[0.00,0.00,0.00], colorSpace='rgb', opacity=1,
    depth=0.0)

# ##define standard sound ### 
fc = 1000
fm = 25
ac = 0.5
am = 0 #no modulation at all
t = arange(0,0.1,0.1/10000)
carrier = ac * sin(2*pi*fc*t)
signal = am * sin(2*pi*fm*t) + ac
SM = signal*carrier #standard sound


stand_sound_audition = sound.Sound(SM, secs=-1)
stand_sound_audition.setVolume(1)

# Initialize components for Routine "dev_trial_audition"
dev_trial_auditionClock = core.Clock()
dev_sound_fixation = visual.TextStim(win=win, ori=0, name='dev_sound_fixation',
    text=u'+',    font=u'Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None,
    color=[0.00,0.00,0.00], colorSpace='rgb', opacity=1,
    depth=0.0)
    
# #############define deviant sound#######
fc = 1000
fm = 25
ac = 0.5
am = 1
t = arange(0,0.1,0.1/10000)
carrier = ac * sin(2*pi*fc*t)
signal = am * sin(2*pi*fm*t) + ac
AM = signal*carrier


dev_sound_audition = sound.Sound(AM, secs=-1)
dev_sound_audition.setVolume(1)

# Initialize components for Routine "MW_questions_audition"
MW_questions_auditionClock = core.Clock()
MW_question_text = visual.TextStim(win=win, ori=0, name='MW_question_text',
    text='default text',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
probes_rating_audition = visual.RatingScale(win=win, name='probes_rating_audition', marker='triangle', size=1.0, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='trifft gar nicht zu                                 trifft vollkommen zu', markerStart='0')

# Initialize components for Routine "MW_questions_audition_partTwo"
MW_questions_audition_partTwoClock = core.Clock()
MW_questions_pos_neg_audition = visual.TextStim(win=win, ori=0, name='MW_questions_pos_neg_audition',
    text='Vor der Unterbrechung waren meine Gedanken:',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
rating_audition_pos_neg = visual.RatingScale(win=win, name='rating_audition_pos_neg', marker='triangle', size=1.0, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='negativ                                            positiv', markerStart='0')

# Initialize components for Routine "MW_questions_audition_partThree"
MW_questions_audition_partThreeClock = core.Clock()
MW_questions_audition_spec_vague = visual.TextStim(win=win, ori=0, name='MW_questions_audition_spec_vague',
    text='Vor der Unterbrechung waren meine Gedanken:',    font='Arial',
    pos=[0, 250], height=30, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
MW_rating_audition_spec_vague = visual.RatingScale(win=win, name='MW_rating_audition_spec_vague', marker='triangle', size=1.0, textSize = 0.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='spezifsch                                          vage', markerStart='0')

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thankyou = visual.TextStim(win=win, ori=0, name='thankyou',
    text=u'Vielen Dank, dass Sie an diesem Experiment teilgenommen haben.\n\nBitte informieren Sie den Versuchsleiter, dass Sie mit diesem Teil\ndes Experiments fertig sind.',    font=u'Arial',
    pos=[0, 0], height=25, wrapWidth=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
#

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# ######Define startValues for staircases; should be overwritten in round 2#########

sV_vision = float(expInfo['vision_startval']) # default startValue vision (set either to 1 if no pre-run done, or set to the estimated threshold)
sV_audition = float(expInfo['audition_startval']) # default startValue audition (set either to 1 if no pre-run done, or set to the estimated threshold)


# ##### Define Block order (even participant number = vision first, odd participant number = audition first)


subjNum = int(expInfo['participant'])


if subjNum % 2 == 0:
    blockorder = [0,1,0,1] # (0 = vision, 1 = audition) 
else:
    blockorder=[1,0,1,0]
# 

for idx, val in enumerate(blockorder): 
    if val == 0: 

    #------Prepare to start Routine "instr_vision"-------
        t = 0
        instr_visionClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        instruction_vision_keys = event.BuilderKeyResponse()  # create an object of type KeyResponse
        instruction_vision_keys.status = NOT_STARTED
        # keep track of which components have finished
        instr_visionComponents = []
        instr_visionComponents.append(instruction_vision)
        instr_visionComponents.append(instruction_vision_keys)
        for thisComponent in instr_visionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "instr_vision"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = instr_visionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instruction_vision* updates
            if t >= 0.0 and instruction_vision.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_vision.tStart = t  # underestimates by a little under one frame
                instruction_vision.frameNStart = frameN  # exact frame index
                instruction_vision.setAutoDraw(True)
            
            # *instruction_vision_keys* updates
            if t >= 0.0 and instruction_vision_keys.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_vision_keys.tStart = t  # underestimates by a little under one frame
                instruction_vision_keys.frameNStart = frameN  # exact frame index
                instruction_vision_keys.status = STARTED
                # keyboard checking is just starting
                instruction_vision_keys.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if instruction_vision_keys.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    instruction_vision_keys.keys = theseKeys[-1]  # just the last key pressed
                    instruction_vision_keys.rt = instruction_vision_keys.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_visionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "instr_vision"-------
        for thisComponent in instr_visionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if instruction_vision_keys.keys in ['', [], None]:  # No response was made
           instruction_vision_keys.keys=None
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('instruction_vision_keys.keys',instruction_vision_keys.keys)
        if instruction_vision_keys.keys != None:  # we had a response
            thisExp.addData('instruction_vision_keys.rt', instruction_vision_keys.rt)
        thisExp.nextEntry()
        
        #------Prepare to start Routine "instr_vision_parttwo"-------
        t = 0
        instr_vision_parttwoClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        instruction_parttwo_keys = event.BuilderKeyResponse()  # create an object of type KeyResponse
        instruction_parttwo_keys.status = NOT_STARTED
        # keep track of which components have finished
        instr_vision_parttwoComponents = []
        instr_vision_parttwoComponents.append(instruction_slider_vision)
        instr_vision_parttwoComponents.append(instruction_parttwo_keys)
        for thisComponent in instr_vision_parttwoComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "instr_vision_parttwo"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = instr_vision_parttwoClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instruction_slider_vision* updates
            if t >= 0.0 and instruction_slider_vision.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_slider_vision.tStart = t  # underestimates by a little under one frame
                instruction_slider_vision.frameNStart = frameN  # exact frame index
                instruction_slider_vision.setAutoDraw(True)
            
            # *instruction_parttwo_keys* updates
            if t >= 0.0 and instruction_parttwo_keys.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_parttwo_keys.tStart = t  # underestimates by a little under one frame
                instruction_parttwo_keys.frameNStart = frameN  # exact frame index
                instruction_parttwo_keys.status = STARTED
                # keyboard checking is just starting
                instruction_parttwo_keys.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if instruction_parttwo_keys.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    instruction_parttwo_keys.keys = theseKeys[-1]  # just the last key pressed
                    instruction_parttwo_keys.rt = instruction_parttwo_keys.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_vision_parttwoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "instr_vision_parttwo"-------
        for thisComponent in instr_vision_parttwoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if instruction_parttwo_keys.keys in ['', [], None]:  # No response was made
           instruction_parttwo_keys.keys=None
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('instruction_parttwo_keys.keys',instruction_parttwo_keys.keys)
        if instruction_parttwo_keys.keys != None:  # we had a response
            thisExp.addData('instruction_parttwo_keys.rt', instruction_parttwo_keys.rt)
        thisExp.nextEntry()
        
        #------Prepare to start Routine "get_ready_vision"-------
        t = 0
        get_ready_visionClock.reset()  # clock 
        frameN = -1
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        get_ready_visionComponents = []
        get_ready_visionComponents.append(get_ready_vision_text)
        get_ready_visionComponents.append(count_five)
        get_ready_visionComponents.append(count_four)
        get_ready_visionComponents.append(count_three)
        get_ready_visionComponents.append(count_two)
        get_ready_visionComponents.append(count_one)
        for thisComponent in get_ready_visionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "get_ready_vision"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = get_ready_visionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *get_ready_vision_text* updates
            if t >= 0.0 and get_ready_vision_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                get_ready_vision_text.tStart = t  # underestimates by a little under one frame
                get_ready_vision_text.frameNStart = frameN  # exact frame index
                get_ready_vision_text.setAutoDraw(True)
            if get_ready_vision_text.status == STARTED and t >= (0.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                get_ready_vision_text.setAutoDraw(False)
            
            # *count_five* updates
            if t >= 0.0 and count_five.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_five.tStart = t  # underestimates by a little under one frame
                count_five.frameNStart = frameN  # exact frame index
                count_five.setAutoDraw(True)
            if count_five.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_five.setAutoDraw(False)
            
            # *count_four* updates
            if t >= 1.0 and count_four.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_four.tStart = t  # underestimates by a little under one frame
                count_four.frameNStart = frameN  # exact frame index
                count_four.setAutoDraw(True)
            if count_four.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_four.setAutoDraw(False)
            
            # *count_three* updates
            if t >= 2.0 and count_three.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_three.tStart = t  # underestimates by a little under one frame
                count_three.frameNStart = frameN  # exact frame index
                count_three.setAutoDraw(True)
            if count_three.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_three.setAutoDraw(False)
            
            # *count_two* updates
            if t >= 3.0 and count_two.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_two.tStart = t  # underestimates by a little under one frame
                count_two.frameNStart = frameN  # exact frame index
                count_two.setAutoDraw(True)
            if count_two.status == STARTED and t >= (3.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_two.setAutoDraw(False)
            
            # *count_one* updates
            if t >= 4.0 and count_one.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_one.tStart = t  # underestimates by a little under one frame
                count_one.frameNStart = frameN  # exact frame index
                count_one.setAutoDraw(True)
            if count_one.status == STARTED and t >= (4.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_one.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in get_ready_visionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "get_ready_vision"-------
        for thisComponent in get_ready_visionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #--------Prepare to start Staircase "staircase_vision" --------
        
        minNumTrials = 10 # eigentlich 56
        
        
        
        # set up handler to look after next chosen value etc
        staircase_vision = data.StairHandler(startVal=sV_vision, extraInfo=expInfo,
            stepSizes=[3], stepType='db', nReversals=0,
            nTrials=minNumTrials, 
            nUp=1, nDown=2,
            minVal=0, maxVal=1,
            originPath=None, name='staircase_vision')
        thisExp.addLoop(staircase_vision)  # add the loop to the experimentlevel = thisStaircase_vision = 1  # initialise some vals
        
        
        # ###### TrialRandomization/Order
        
        S = [3]*10 + [4]*20 + [5]*62 + [6]*20 + [7]*10 # 56 trains of standards
        shuffle (S)
        g = -1
        
        
        DP = [1]*(minNumTrials-5) + [2]*5 # 56 deviants
        shuffle(DP)
        DP = DP + [1]*(len(S)-len(DP))
        
        
        
        
        
        for thisStaircase_vision in staircase_vision:
            currentLoop = staircase_vision
            level = thisStaircase_vision
            
            # #############
            
            g=g+1
            s=1
            
            while s<=S[g]:
                
            # #############    
            
            #------Prepare to start Routine "stand_trial_vision"-------
                t = 0
                stand_trial_visionClock.reset()  # clock 
                frameN = -1
                routineTimer.add(2.500000)
                # update component parameters for each repeat
                stand_grating_vision.setOpacity(1)
                stand_keyResp_vision = event.BuilderKeyResponse()  # create an object of type KeyResponse
                stand_keyResp_vision.status = NOT_STARTED
                # keep track of which components have finished
                stand_trial_visionComponents = []
                stand_trial_visionComponents.append(stand_fixation_vision)
                stand_trial_visionComponents.append(stand_grating_vision)
                stand_trial_visionComponents.append(stand_keyResp_vision)
                for thisComponent in stand_trial_visionComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "stand_trial_vision"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = stand_trial_visionClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *stand_fixation_vision* updates
                    if t >= 0.0 and stand_fixation_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_fixation_vision.tStart = t  # underestimates by a little under one frame
                        stand_fixation_vision.frameNStart = frameN  # exact frame index
                        stand_fixation_vision.setAutoDraw(True)
                    if stand_fixation_vision.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_fixation_vision.setAutoDraw(False)
                    
                    # *stand_grating_vision* updates
                    if t >= 1.0 and stand_grating_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_grating_vision.tStart = t  # underestimates by a little under one frame
                        stand_grating_vision.frameNStart = frameN  # exact frame index
                        stand_grating_vision.setAutoDraw(True)
                    if stand_grating_vision.status == STARTED and t >= (1.0 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_grating_vision.setAutoDraw(False)
                    
                    # *stand_keyResp_vision* updates
                    if t >= 1.0 and stand_keyResp_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_keyResp_vision.tStart = t  # underestimates by a little under one frame
                        stand_keyResp_vision.frameNStart = frameN  # exact frame index
                        stand_keyResp_vision.status = STARTED
                        # keyboard checking is just starting
                        stand_keyResp_vision.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if stand_keyResp_vision.status == STARTED and t >= (1.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_keyResp_vision.status = STOPPED
                    if stand_keyResp_vision.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            stand_keyResp_vision.keys = theseKeys[-1]  # just the last key pressed
                            stand_keyResp_vision.rt = stand_keyResp_vision.clock.getTime()
                            # was this 'correct'?
                            if (stand_keyResp_vision.keys == str(u'None')) or (stand_keyResp_vision.keys == u'None'):
                                stand_keyResp_vision.corr = 1
                            else:
                                stand_keyResp_vision.corr = 0
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineTimer.reset()  # if we abort early the non-slip timer needs reset
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in stand_trial_visionComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "stand_trial_vision"-------
                for thisComponent in stand_trial_visionComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if stand_keyResp_vision.keys in ['', [], None]:  # No response was made
                   stand_keyResp_vision.keys=None
                   # was no response the correct answer?!
                   if str(u'None').lower() == 'none': stand_keyResp_vision.corr = 1  # correct non-response
                   else: stand_keyResp_vision.corr = 0  # responded incorrectly (false alarm)
                # store data for staircase_vision (StairHandler)
                thisExp.addData('stand_keyResp_vision.corr', stand_keyResp_vision.corr)
                thisExp.addData('stand_keyResp_vision.rt', stand_keyResp_vision.rt)
                thisExp.nextEntry()
                
            # ######### 
                s=s+1
                
            
            if DP[g] == 1:
            
            # ########    
                
                #------Prepare to start Routine "dev_trial_vision"-------
                t = 0
                dev_trial_visionClock.reset()  # clock 
                frameN = -1
                routineTimer.add(2.500000)
                # update component parameters for each repeat
                dev_grating_vision.setContrast(level)
                dev_keyResp_vision = event.BuilderKeyResponse()  # create an object of type KeyResponse
                dev_keyResp_vision.status = NOT_STARTED
                # keep track of which components have finished
                dev_trial_visionComponents = []
                dev_trial_visionComponents.append(dev_fixiation_vision)
                dev_trial_visionComponents.append(dev_grating_vision)
                dev_trial_visionComponents.append(dev_keyResp_vision)
                for thisComponent in dev_trial_visionComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "dev_trial_vision"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = dev_trial_visionClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *dev_fixiation_vision* updates
                    if t >= 0.0 and dev_fixiation_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_fixiation_vision.tStart = t  # underestimates by a little under one frame
                        dev_fixiation_vision.frameNStart = frameN  # exact frame index
                        dev_fixiation_vision.setAutoDraw(True)
                    if dev_fixiation_vision.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_fixiation_vision.setAutoDraw(False)
                    
                    # *dev_grating_vision* updates
                    if t >= 1.0 and dev_grating_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_grating_vision.tStart = t  # underestimates by a little under one frame
                        dev_grating_vision.frameNStart = frameN  # exact frame index
                        dev_grating_vision.setAutoDraw(True)
                    if dev_grating_vision.status == STARTED and t >= (1.0 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_grating_vision.setAutoDraw(False)
                    
                    # *dev_keyResp_vision* updates
                    if t >= 1.0 and dev_keyResp_vision.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_keyResp_vision.tStart = t  # underestimates by a little under one frame
                        dev_keyResp_vision.frameNStart = frameN  # exact frame index
                        dev_keyResp_vision.status = STARTED
                        # keyboard checking is just starting
                        dev_keyResp_vision.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if dev_keyResp_vision.status == STARTED and t >= (1.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_keyResp_vision.status = STOPPED
                    if dev_keyResp_vision.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            dev_keyResp_vision.keys = theseKeys[-1]  # just the last key pressed
                            dev_keyResp_vision.rt = dev_keyResp_vision.clock.getTime()
                            # was this 'correct'?
                            if (dev_keyResp_vision.keys == str(u'space')) or (dev_keyResp_vision.keys == u'space'):
                                dev_keyResp_vision.corr = 1
                            else:
                                dev_keyResp_vision.corr = 0
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineTimer.reset()  # if we abort early the non-slip timer needs reset
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in dev_trial_visionComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "dev_trial_vision"-------
                for thisComponent in dev_trial_visionComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if dev_keyResp_vision.keys in ['', [], None]:  # No response was made
                   dev_keyResp_vision.keys=None
                   # was no response the correct answer?!
                   if str(u'space').lower() == 'none': dev_keyResp_vision.corr = 1  # correct response
                   else: dev_keyResp_vision.corr = 0  # failed to respond (incorrectly)
                # store data for staircase_vision (StairHandler)
                staircase_vision.addResponse(dev_keyResp_vision.corr)
                staircase_vision.addOtherData('dev_keyResp_vision.rt', dev_keyResp_vision.rt)
                
                
                
                
            # ################
            elif DP[g] == 2:
            # #################
            
            
                # set up handler to look after randomisation of conditions etc
                probes_vision_partOne = data.TrialHandler(nReps=1, method='random', 
                    extraInfo=expInfo, originPath=None,
                    trialList=data.importConditions('/SCR/ConnectivityGroup/VisualAuditoryOddballTask/MW_questions_partOne.csv'),
                    seed=None, name='probes_vision_partOne')
                thisExp.addLoop(probes_vision_partOne)  # add the loop to the experiment
                thisProbes_vision_partOne = probes_vision_partOne.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb=thisProbes_vision_partOne.rgb)
                if thisProbes_vision_partOne != None:
                    for paramName in thisProbes_vision_partOne.keys():
                        exec(paramName + '= thisProbes_vision_partOne.' + paramName)
            
            

            
                for thisProbes_vision_partOne in probes_vision_partOne:
                    currentLoop = probes_vision_partOne
                    # abbreviate parameter names if possible (e.g. rgb = thisProbes_vision_partOne.rgb)
                    if thisProbes_vision_partOne != None:
                        for paramName in thisProbes_vision_partOne.keys():
                            exec(paramName + '= thisProbes_vision_partOne.' + paramName)
                    
                    #------Prepare to start Routine "MW_questions_vision"-------
                    t = 0
                    MW_questions_visionClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    MW_questions_text.setText(param_A)
                    probes_rating_vision.reset()
                    # keep track of which components have finished
                    MW_questions_visionComponents = []
                    MW_questions_visionComponents.append(MW_questions_text)
                    MW_questions_visionComponents.append(probes_rating_vision)
                    for thisComponent in MW_questions_visionComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_vision"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_visionClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_questions_text* updates
                        if t >= 0.0 and MW_questions_text.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_questions_text.tStart = t  # underestimates by a little under one frame
                            MW_questions_text.frameNStart = frameN  # exact frame index
                            MW_questions_text.setAutoDraw(True)
                        # *probes_rating_vision* updates
                        if t > 0.0:
                            probes_rating_vision.draw()
                            continueRoutine = probes_rating_vision.noResponse
                            if probes_rating_vision.noResponse == False:
                                probes_rating_vision.response = probes_rating_vision.getRating()
                                probes_rating_vision.rt = probes_rating_vision.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_visionComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_vision"-------
                    for thisComponent in MW_questions_visionComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_vision_partOne (TrialHandler)
                    probes_vision_partOne.addData('probes_rating_vision.response', probes_rating_vision.getRating())
                    probes_vision_partOne.addData('probes_rating_vision.rt', probes_rating_vision.getRT())
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'probes_vision_partOne'
                
                # get names of stimulus parameters
                if probes_vision_partOne.trialList in ([], [None], None):  params = []
                else:  params = probes_vision_partOne.trialList[0].keys()
                # save data for this loop
                probes_vision_partOne.saveAsText(filename + 'probes_vision_partOne.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                
                # set up handler to look after randomisation of conditions etc
                probes_vision_parttwo = data.TrialHandler(nReps=1, method='random', 
                    extraInfo=expInfo, originPath=None,
                    trialList=[None],
                    seed=None, name='probes_vision_parttwo')
                thisExp.addLoop(probes_vision_parttwo)  # add the loop to the experiment
                thisProbes_vision_parttwo = probes_vision_parttwo.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb=thisProbes_vision_parttwo.rgb)
                if thisProbes_vision_parttwo != None:
                    for paramName in thisProbes_vision_parttwo.keys():
                        exec(paramName + '= thisProbes_vision_parttwo.' + paramName)
                
                for thisProbes_vision_parttwo in probes_vision_parttwo:
                    currentLoop = probes_vision_parttwo
                    # abbreviate parameter names if possible (e.g. rgb = thisProbes_vision_parttwo.rgb)
                    if thisProbes_vision_parttwo != None:
                        for paramName in thisProbes_vision_parttwo.keys():
                            exec(paramName + '= thisProbes_vision_parttwo.' + paramName)
                    
                    #------Prepare to start Routine "MW_questions_vision_parttwo"-------
                    t = 0
                    MW_questions_vision_parttwoClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    probes_ratings_vision_Pos_Neg.reset()
                    # keep track of which components have finished
                    MW_questions_vision_parttwoComponents = []
                    MW_questions_vision_parttwoComponents.append(MW_questions_pos_neg_vision)
                    MW_questions_vision_parttwoComponents.append(probes_ratings_vision_Pos_Neg)
                    for thisComponent in MW_questions_vision_parttwoComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_vision_parttwo"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_vision_parttwoClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_questions_pos_neg_vision* updates
                        if t >= 0.0 and MW_questions_pos_neg_vision.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_questions_pos_neg_vision.tStart = t  # underestimates by a little under one frame
                            MW_questions_pos_neg_vision.frameNStart = frameN  # exact frame index
                            MW_questions_pos_neg_vision.setAutoDraw(True)
                        # *probes_ratings_vision_Pos_Neg* updates
                        if t > 0.0:
                            probes_ratings_vision_Pos_Neg.draw()
                            continueRoutine = probes_ratings_vision_Pos_Neg.noResponse
                            if probes_ratings_vision_Pos_Neg.noResponse == False:
                                probes_ratings_vision_Pos_Neg.response = probes_ratings_vision_Pos_Neg.getRating()
                                probes_ratings_vision_Pos_Neg.rt = probes_ratings_vision_Pos_Neg.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_vision_parttwoComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_vision_parttwo"-------
                    for thisComponent in MW_questions_vision_parttwoComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_vision_parttwo (TrialHandler)
                    probes_vision_parttwo.addData('probes_ratings_vision_Pos_Neg.response', probes_ratings_vision_Pos_Neg.getRating())
                    probes_vision_parttwo.addData('probes_ratings_vision_Pos_Neg.rt', probes_ratings_vision_Pos_Neg.getRT())
                    
                    #------Prepare to start Routine "MW_questions_vision_partThree"-------
                    t = 0
                    MW_questions_vision_partThreeClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    MW_rating_vision_spec_vague.reset()
                    # keep track of which components have finished
                    MW_questions_vision_partThreeComponents = []
                    MW_questions_vision_partThreeComponents.append(MW_questions_vision_spec_vague)
                    MW_questions_vision_partThreeComponents.append(MW_rating_vision_spec_vague)
                    for thisComponent in MW_questions_vision_partThreeComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_vision_partThree"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_vision_partThreeClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_questions_vision_spec_vague* updates
                        if t >= 0.0 and MW_questions_vision_spec_vague.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_questions_vision_spec_vague.tStart = t  # underestimates by a little under one frame
                            MW_questions_vision_spec_vague.frameNStart = frameN  # exact frame index
                            MW_questions_vision_spec_vague.setAutoDraw(True)
                        # *MW_rating_vision_spec_vague* updates
                        if t > 0.0:
                            MW_rating_vision_spec_vague.draw()
                            continueRoutine = MW_rating_vision_spec_vague.noResponse
                            if MW_rating_vision_spec_vague.noResponse == False:
                                MW_rating_vision_spec_vague.response = MW_rating_vision_spec_vague.getRating()
                                MW_rating_vision_spec_vague.rt = MW_rating_vision_spec_vague.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_vision_partThreeComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_vision_partThree"-------
                    for thisComponent in MW_questions_vision_partThreeComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_vision_parttwo (TrialHandler)
                    probes_vision_parttwo.addData('MW_rating_vision_spec_vague.response', MW_rating_vision_spec_vague.getRating())
                    probes_vision_parttwo.addData('MW_rating_vision_spec_vague.rt', MW_rating_vision_spec_vague.getRT())
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'probes_vision_parttwo'
                
                # get names of stimulus parameters
                if probes_vision_parttwo.trialList in ([], [None], None):  params = []
                else:  params = probes_vision_parttwo.trialList[0].keys()
                # save data for this loop
                probes_vision_parttwo.saveAsText(filename + 'probes_vision_parttwo.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
            
            
            thisExp.nextEntry() # MUSS DAS HIER, war vorher nicht da! (Hab ich nur eingefügt)
            
        # staircase completed
        
        staircase_vision.saveAsText(filename + 'staircase_vision.csv' + '_' + str(idx+1), delim=',')
        sV_vision = level
        

# #########################AUDITION########################################

    elif val == 1: # #### Blockorder: even participant number == first vision, Odd number == first audition



        #------Prepare to start Routine "instr_audition"-------
        t = 0
        instr_auditionClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        instruction_audtion_keys = event.BuilderKeyResponse()  # create an object of type KeyResponse
        instruction_audtion_keys.status = NOT_STARTED
        # keep track of which components have finished
        instr_auditionComponents = []
        instr_auditionComponents.append(instruction_audition)
        instr_auditionComponents.append(instruction_audtion_keys)
        for thisComponent in instr_auditionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "instr_audition"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = instr_auditionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instruction_audition* updates
            if t >= 0.0 and instruction_audition.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_audition.tStart = t  # underestimates by a little under one frame
                instruction_audition.frameNStart = frameN  # exact frame index
                instruction_audition.setAutoDraw(True)
            
            # *instruction_audtion_keys* updates
            if t >= 0.0 and instruction_audtion_keys.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_audtion_keys.tStart = t  # underestimates by a little under one frame
                instruction_audtion_keys.frameNStart = frameN  # exact frame index
                instruction_audtion_keys.status = STARTED
                # keyboard checking is just starting
                instruction_audtion_keys.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if instruction_audtion_keys.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    instruction_audtion_keys.keys = theseKeys[-1]  # just the last key pressed
                    instruction_audtion_keys.rt = instruction_audtion_keys.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_auditionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "instr_audition"-------
        for thisComponent in instr_auditionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if instruction_audtion_keys.keys in ['', [], None]:  # No response was made
           instruction_audtion_keys.keys=None
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('instruction_audtion_keys.keys',instruction_audtion_keys.keys)
        if instruction_audtion_keys.keys != None:  # we had a response
            thisExp.addData('instruction_audtion_keys.rt', instruction_audtion_keys.rt)
        thisExp.nextEntry()
        
        #------Prepare to start Routine "intro_audition_parttwo"-------
        t = 0
        intro_audition_parttwoClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        intro_audition_slider_keys = event.BuilderKeyResponse()  # create an object of type KeyResponse
        intro_audition_slider_keys.status = NOT_STARTED
        # keep track of which components have finished
        intro_audition_parttwoComponents = []
        intro_audition_parttwoComponents.append(instruction_audition_slider)
        intro_audition_parttwoComponents.append(intro_audition_slider_keys)
        for thisComponent in intro_audition_parttwoComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "intro_audition_parttwo"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = intro_audition_parttwoClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instruction_audition_slider* updates
            if t >= 0.0 and instruction_audition_slider.status == NOT_STARTED:
                # keep track of start time/frame for later
                instruction_audition_slider.tStart = t  # underestimates by a little under one frame
                instruction_audition_slider.frameNStart = frameN  # exact frame index
                instruction_audition_slider.setAutoDraw(True)
            
            # *intro_audition_slider_keys* updates
            if t >= 0.0 and intro_audition_slider_keys.status == NOT_STARTED:
                # keep track of start time/frame for later
                intro_audition_slider_keys.tStart = t  # underestimates by a little under one frame
                intro_audition_slider_keys.frameNStart = frameN  # exact frame index
                intro_audition_slider_keys.status = STARTED
                # keyboard checking is just starting
                intro_audition_slider_keys.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if intro_audition_slider_keys.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    intro_audition_slider_keys.keys = theseKeys[-1]  # just the last key pressed
                    intro_audition_slider_keys.rt = intro_audition_slider_keys.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intro_audition_parttwoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "intro_audition_parttwo"-------
        for thisComponent in intro_audition_parttwoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if intro_audition_slider_keys.keys in ['', [], None]:  # No response was made
           intro_audition_slider_keys.keys=None
        # store data for thisExp (ExperimentHandler)
        thisExp.addData('intro_audition_slider_keys.keys',intro_audition_slider_keys.keys)
        if intro_audition_slider_keys.keys != None:  # we had a response
            thisExp.addData('intro_audition_slider_keys.rt', intro_audition_slider_keys.rt)
        thisExp.nextEntry()
        
        #------Prepare to start Routine "get_ready_audition"-------
        t = 0
        get_ready_auditionClock.reset()  # clock 
        frameN = -1
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        get_ready_auditionComponents = []
        get_ready_auditionComponents.append(get_ready_audition_test)
        get_ready_auditionComponents.append(count_five_audio)
        get_ready_auditionComponents.append(count_four_audio)
        get_ready_auditionComponents.append(count_three_audio)
        get_ready_auditionComponents.append(count_two_audio)
        get_ready_auditionComponents.append(count_one_audio)
        for thisComponent in get_ready_auditionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "get_ready_audition"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = get_ready_auditionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *get_ready_audition_test* updates
            if t >= 0.0 and get_ready_audition_test.status == NOT_STARTED:
                # keep track of start time/frame for later
                get_ready_audition_test.tStart = t  # underestimates by a little under one frame
                get_ready_audition_test.frameNStart = frameN  # exact frame index
                get_ready_audition_test.setAutoDraw(True)
            if get_ready_audition_test.status == STARTED and t >= (0.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                get_ready_audition_test.setAutoDraw(False)
            
            # *count_five_audio* updates
            if t >= 0.0 and count_five_audio.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_five_audio.tStart = t  # underestimates by a little under one frame
                count_five_audio.frameNStart = frameN  # exact frame index
                count_five_audio.setAutoDraw(True)
            if count_five_audio.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_five_audio.setAutoDraw(False)
            
            # *count_four_audio* updates
            if t >= 1.0 and count_four_audio.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_four_audio.tStart = t  # underestimates by a little under one frame
                count_four_audio.frameNStart = frameN  # exact frame index
                count_four_audio.setAutoDraw(True)
            if count_four_audio.status == STARTED and t >= (1.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_four_audio.setAutoDraw(False)
            
            # *count_three_audio* updates
            if t >= 2.0 and count_three_audio.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_three_audio.tStart = t  # underestimates by a little under one frame
                count_three_audio.frameNStart = frameN  # exact frame index
                count_three_audio.setAutoDraw(True)
            if count_three_audio.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_three_audio.setAutoDraw(False)
            
            # *count_two_audio* updates
            if t >= 3.0 and count_two_audio.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_two_audio.tStart = t  # underestimates by a little under one frame
                count_two_audio.frameNStart = frameN  # exact frame index
                count_two_audio.setAutoDraw(True)
            if count_two_audio.status == STARTED and t >= (3.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_two_audio.setAutoDraw(False)
            
            # *count_one_audio* updates
            if t >= 4.0 and count_one_audio.status == NOT_STARTED:
                # keep track of start time/frame for later
                count_one_audio.tStart = t  # underestimates by a little under one frame
                count_one_audio.frameNStart = frameN  # exact frame index
                count_one_audio.setAutoDraw(True)
            if count_one_audio.status == STARTED and t >= (4.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                count_one_audio.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in get_ready_auditionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "get_ready_audition"-------
        for thisComponent in get_ready_auditionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #--------Prepare to start Staircase "staircase_audition" --------
        
        minNumTrials = 10
        
        # set up handler to look after next chosen value etc
        staircase_audition = data.StairHandler(startVal=sV_audition, extraInfo=expInfo,
            stepSizes=[3], stepType='db', nReversals=0,
            nTrials=minNumTrials, 
            nUp=1, nDown=2,
            minVal=0, maxVal=1,
            originPath=None, name='staircase_audition')
        thisExp.addLoop(staircase_audition)  # add the loop to the experimentlevel = thisStaircase_audition = 25  # initialise some vals
        
        
        # ###### TrialRandomization/Order
        
        S = [3]*10 + [4]*20 + [5]*62 + [6]*20 + [7]*10 # 56 trains of standards
        shuffle (S)
        g = -1
        
        
        DP = [1]*(minNumTrials-5) + [2]*5 # 56 deviants
        shuffle(DP)
        DP = DP + [1]*(len(S)-len(DP))
        
        
        
        for thisStaircase_audition in staircase_audition:
            currentLoop = staircase_audition
            level = thisStaircase_audition
            
            # #################
            g=g+1
            s=1
            
            while s<=S[g]:
            
            # #################
            
                #------Prepare to start Routine "stand_trial_audition"-------
                t = 0
                stand_trial_auditionClock.reset()  # clock 
                frameN = -1
                routineTimer.add(2.500000)
                # update component parameters for each repeat
                stand_keyResp_audition = event.BuilderKeyResponse()  # create an object of type KeyResponse
                stand_keyResp_audition.status = NOT_STARTED
                # keep track of which components have finished
                stand_trial_auditionComponents = []
                stand_trial_auditionComponents.append(stand_fixation_audition)
                stand_trial_auditionComponents.append(stand_sound_audition)
                stand_trial_auditionComponents.append(stand_keyResp_audition)
                for thisComponent in stand_trial_auditionComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "stand_trial_audition"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = stand_trial_auditionClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *stand_fixation_audition* updates
                    if t >= 0.0 and stand_fixation_audition.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_fixation_audition.tStart = t  # underestimates by a little under one frame
                        stand_fixation_audition.frameNStart = frameN  # exact frame index
                        stand_fixation_audition.setAutoDraw(True)
                    if stand_fixation_audition.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_fixation_audition.setAutoDraw(False)
                    # start/stop stand_sound_audition
                    if t >= 1.0 and stand_sound_audition.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_sound_audition.tStart = t  # underestimates by a little under one frame
                        stand_sound_audition.frameNStart = frameN  # exact frame index
                        stand_sound_audition.play()  # start the sound (it finishes automatically)
                    if stand_sound_audition.status == STARTED and t >= (1.0 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_sound_audition.stop()  # stop the sound (if longer than duration)
                    
                    # *stand_keyResp_audition* updates
                    if t >= 1.0 and stand_keyResp_audition.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stand_keyResp_audition.tStart = t  # underestimates by a little under one frame
                        stand_keyResp_audition.frameNStart = frameN  # exact frame index
                        stand_keyResp_audition.status = STARTED
                        # keyboard checking is just starting
                        stand_keyResp_audition.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if stand_keyResp_audition.status == STARTED and t >= (1.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                        stand_keyResp_audition.status = STOPPED
                    if stand_keyResp_audition.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            stand_keyResp_audition.keys = theseKeys[-1]  # just the last key pressed
                            stand_keyResp_audition.rt = stand_keyResp_audition.clock.getTime()
                            # was this 'correct'?
                            if (stand_keyResp_audition.keys == str(u'None')) or (stand_keyResp_audition.keys == u'None'):
                                stand_keyResp_audition.corr = 1
                            else:
                                stand_keyResp_audition.corr = 0
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineTimer.reset()  # if we abort early the non-slip timer needs reset
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in stand_trial_auditionComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "stand_trial_audition"-------
                for thisComponent in stand_trial_auditionComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if stand_keyResp_audition.keys in ['', [], None]:  # No response was made
                   stand_keyResp_audition.keys=None
                   # was no response the correct answer?!
                   if str(u'None').lower() == 'none': stand_keyResp_audition.corr = 1  # correct non-response
                   else: stand_keyResp_audition.corr = 0  # respond incorrectly
                # store data for staircase_audition (StairHandler)
                thisExp.addData('stand_keyResp_audition.corr', stand_keyResp_audition.corr)
                thisExp.addData('stand_keyResp_audition.rt', stand_keyResp_audition.rt)
                thisExp.nextEntry()
                
           # ############################## 
                s=s+1
                
            
            if DP[g] == 1:
            # #############################
            
                #------Prepare to start Routine "dev_trial_audition"-------
                t = 0
                dev_trial_auditionClock.reset()  # clock 
                frameN = -1
                routineTimer.add(2.500000)
                # update component parameters for each repeat
                # #################
                fc = 1000
                fm = 25
                ac = 0.5
                am = level
                t = arange(0,0.1,0.1/10000)
                carrier = ac * sin(2*pi*fc*t)
                signal = am * sin(2*pi*fm*t) + ac
                AM = signal*carrier
                dev_sound_audition.setSound(AM)
                # ##################
                dev_keyResp_audition = event.BuilderKeyResponse()  # create an object of type KeyResponse
                dev_keyResp_audition.status = NOT_STARTED
                # keep track of which components have finished
                dev_trial_auditionComponents = []
                dev_trial_auditionComponents.append(dev_sound_fixation)
                dev_trial_auditionComponents.append(dev_sound_audition)
                dev_trial_auditionComponents.append(dev_keyResp_audition)
                for thisComponent in dev_trial_auditionComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "dev_trial_audition"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = dev_trial_auditionClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *dev_sound_fixation* updates
                    if t >= 0.0 and dev_sound_fixation.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_sound_fixation.tStart = t  # underestimates by a little under one frame
                        dev_sound_fixation.frameNStart = frameN  # exact frame index
                        dev_sound_fixation.setAutoDraw(True)
                    if dev_sound_fixation.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_sound_fixation.setAutoDraw(False)
                    # start/stop dev_sound_audition
                    if t >= 1.0 and dev_sound_audition.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_sound_audition.tStart = t  # underestimates by a little under one frame
                        dev_sound_audition.frameNStart = frameN  # exact frame index
                        dev_sound_audition.play()  # start the sound (it finishes automatically)
                    if dev_sound_audition.status == STARTED and t >= (1.0 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_sound_audition.stop()  # stop the sound (if longer than duration)
                    
                    # *dev_keyResp_audition* updates
                    if t >= 1.0 and dev_keyResp_audition.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        dev_keyResp_audition.tStart = t  # underestimates by a little under one frame
                        dev_keyResp_audition.frameNStart = frameN  # exact frame index
                        dev_keyResp_audition.status = STARTED
                        # keyboard checking is just starting
                        dev_keyResp_audition.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if dev_keyResp_audition.status == STARTED and t >= (1.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                        dev_keyResp_audition.status = STOPPED
                    if dev_keyResp_audition.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            dev_keyResp_audition.keys = theseKeys[-1]  # just the last key pressed
                            dev_keyResp_audition.rt = dev_keyResp_audition.clock.getTime()
                            # was this 'correct'?
                            if (dev_keyResp_audition.keys == str(u'space')) or (dev_keyResp_audition.keys == u'space'):
                                dev_keyResp_audition.corr = 1
                            else:
                                dev_keyResp_audition.corr = 0
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineTimer.reset()  # if we abort early the non-slip timer needs reset
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in dev_trial_auditionComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "dev_trial_audition"-------
                for thisComponent in dev_trial_auditionComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if dev_keyResp_audition.keys in ['', [], None]:  # No response was made
                   dev_keyResp_audition.keys=None
                   # was no response the correct answer?!
                   if str(u'space').lower() == 'none': dev_keyResp_audition.corr = 1  # correct response
                   else: dev_keyResp_audition.corr = 0  # failed to respond (incorrectly)
                # store data for staircase_audition (StairHandler)
                staircase_audition.addResponse(dev_keyResp_audition.corr)
                staircase_audition.addOtherData('dev_keyResp_audition.rt', dev_keyResp_audition.rt)
            
            
            
            # ################
            elif DP[g] == 2:
            # #################
            
            
                # set up handler to look after randomisation of conditions etc
                probes_audition_partOne = data.TrialHandler(nReps=1, method='random', 
                    extraInfo=expInfo, originPath=None,
                    trialList=data.importConditions('/SCR/ConnectivityGroup/VisualAuditoryOddballTask/MW_questions_partOne.csv'),
                    seed=None, name='probes_audition_partOne')
                thisExp.addLoop(probes_audition_partOne)  # add the loop to the experiment
                thisProbes_audition_partOne = probes_audition_partOne.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb=thisProbes_audition_partOne.rgb)
                if thisProbes_audition_partOne != None:
                    for paramName in thisProbes_audition_partOne.keys():
                        exec(paramName + '= thisProbes_audition_partOne.' + paramName)
                
                for thisProbes_audition_partOne in probes_audition_partOne:
                    currentLoop = probes_audition_partOne
                    # abbreviate parameter names if possible (e.g. rgb = thisProbes_audition_partOne.rgb)
                    if thisProbes_audition_partOne != None:
                        for paramName in thisProbes_audition_partOne.keys():
                            exec(paramName + '= thisProbes_audition_partOne.' + paramName)
                    
                    #------Prepare to start Routine "MW_questions_audition"-------
                    t = 0
                    MW_questions_auditionClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    MW_question_text.setText(param_A)
                    probes_rating_audition.reset()
                    # keep track of which components have finished
                    MW_questions_auditionComponents = []
                    MW_questions_auditionComponents.append(MW_question_text)
                    MW_questions_auditionComponents.append(probes_rating_audition)
                    for thisComponent in MW_questions_auditionComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_audition"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_auditionClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_question_text* updates
                        if t >= 0.0 and MW_question_text.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_question_text.tStart = t  # underestimates by a little under one frame
                            MW_question_text.frameNStart = frameN  # exact frame index
                            MW_question_text.setAutoDraw(True)
                        # *probes_rating_audition* updates
                        if t > 0.0:
                            probes_rating_audition.draw()
                            continueRoutine = probes_rating_audition.noResponse
                            if probes_rating_audition.noResponse == False:
                                probes_rating_audition.response = probes_rating_audition.getRating()
                                probes_rating_audition.rt = probes_rating_audition.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_auditionComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_audition"-------
                    for thisComponent in MW_questions_auditionComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_audition_partOne (TrialHandler)
                    probes_audition_partOne.addData('probes_rating_audition.response', probes_rating_audition.getRating())
                    probes_audition_partOne.addData('probes_rating_audition.rt', probes_rating_audition.getRT())
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'probes_audition_partOne'
                
                # get names of stimulus parameters
                if probes_audition_partOne.trialList in ([], [None], None):  params = []
                else:  params = probes_audition_partOne.trialList[0].keys()
                # save data for this loop
                probes_audition_partOne.saveAsText(filename + 'probes_audition_partOne.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                
                # set up handler to look after randomisation of conditions etc
                probes_audition_partTwo = data.TrialHandler(nReps=1, method='random', 
                    extraInfo=expInfo, originPath=None,
                    trialList=[None],
                    seed=None, name='probes_audition_partTwo')
                thisExp.addLoop(probes_audition_partTwo)  # add the loop to the experiment
                thisProbes_audition_partTwo = probes_audition_partTwo.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb=thisProbes_audition_partTwo.rgb)
                if thisProbes_audition_partTwo != None:
                    for paramName in thisProbes_audition_partTwo.keys():
                        exec(paramName + '= thisProbes_audition_partTwo.' + paramName)
                
                for thisProbes_audition_partTwo in probes_audition_partTwo:
                    currentLoop = probes_audition_partTwo
                    # abbreviate parameter names if possible (e.g. rgb = thisProbes_audition_partTwo.rgb)
                    if thisProbes_audition_partTwo != None:
                        for paramName in thisProbes_audition_partTwo.keys():
                            exec(paramName + '= thisProbes_audition_partTwo.' + paramName)
                    
                    #------Prepare to start Routine "MW_questions_audition_partTwo"-------
                    t = 0
                    MW_questions_audition_partTwoClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    rating_audition_pos_neg.reset()
                    # keep track of which components have finished
                    MW_questions_audition_partTwoComponents = []
                    MW_questions_audition_partTwoComponents.append(MW_questions_pos_neg_audition)
                    MW_questions_audition_partTwoComponents.append(rating_audition_pos_neg)
                    for thisComponent in MW_questions_audition_partTwoComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_audition_partTwo"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_audition_partTwoClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_questions_pos_neg_audition* updates
                        if t >= 0.0 and MW_questions_pos_neg_audition.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_questions_pos_neg_audition.tStart = t  # underestimates by a little under one frame
                            MW_questions_pos_neg_audition.frameNStart = frameN  # exact frame index
                            MW_questions_pos_neg_audition.setAutoDraw(True)
                        # *rating_audition_pos_neg* updates
                        if t > 0.0:
                            rating_audition_pos_neg.draw()
                            continueRoutine = rating_audition_pos_neg.noResponse
                            if rating_audition_pos_neg.noResponse == False:
                                rating_audition_pos_neg.response = rating_audition_pos_neg.getRating()
                                rating_audition_pos_neg.rt = rating_audition_pos_neg.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_audition_partTwoComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_audition_partTwo"-------
                    for thisComponent in MW_questions_audition_partTwoComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_audition_partTwo (TrialHandler)
                    probes_audition_partTwo.addData('rating_audition_pos_neg.response', rating_audition_pos_neg.getRating())
                    probes_audition_partTwo.addData('rating_audition_pos_neg.rt', rating_audition_pos_neg.getRT())
                    
                    #------Prepare to start Routine "MW_questions_audition_partThree"-------
                    t = 0
                    MW_questions_audition_partThreeClock.reset()  # clock 
                    frameN = -1
                    # update component parameters for each repeat
                    MW_rating_audition_spec_vague.reset()
                    # keep track of which components have finished
                    MW_questions_audition_partThreeComponents = []
                    MW_questions_audition_partThreeComponents.append(MW_questions_audition_spec_vague)
                    MW_questions_audition_partThreeComponents.append(MW_rating_audition_spec_vague)
                    for thisComponent in MW_questions_audition_partThreeComponents:
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    
                    #-------Start Routine "MW_questions_audition_partThree"-------
                    continueRoutine = True
                    while continueRoutine:
                        # get current time
                        t = MW_questions_audition_partThreeClock.getTime()
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *MW_questions_audition_spec_vague* updates
                        if t >= 0.0 and MW_questions_audition_spec_vague.status == NOT_STARTED:
                            # keep track of start time/frame for later
                            MW_questions_audition_spec_vague.tStart = t  # underestimates by a little under one frame
                            MW_questions_audition_spec_vague.frameNStart = frameN  # exact frame index
                            MW_questions_audition_spec_vague.setAutoDraw(True)
                        # *MW_rating_audition_spec_vague* updates
                        if t > 0.0:
                            MW_rating_audition_spec_vague.draw()
                            continueRoutine = MW_rating_audition_spec_vague.noResponse
                            if MW_rating_audition_spec_vague.noResponse == False:
                                MW_rating_audition_spec_vague.response = MW_rating_audition_spec_vague.getRating()
                                MW_rating_audition_spec_vague.rt = MW_rating_audition_spec_vague.getRT()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineTimer.reset()  # if we abort early the non-slip timer needs reset
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in MW_questions_audition_partThreeComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # check for quit (the Esc key)
                        if endExpNow or event.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                        else:  # this Routine was not non-slip safe so reset non-slip timer
                            routineTimer.reset()
                    
                    #-------Ending Routine "MW_questions_audition_partThree"-------
                    for thisComponent in MW_questions_audition_partThreeComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store data for probes_audition_partTwo (TrialHandler)
                    probes_audition_partTwo.addData('MW_rating_audition_spec_vague.response', MW_rating_audition_spec_vague.getRating())
                    probes_audition_partTwo.addData('MW_rating_audition_spec_vague.rt', MW_rating_audition_spec_vague.getRT())
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'probes_audition_partTwo'
                
                # get names of stimulus parameters
                if probes_audition_partTwo.trialList in ([], [None], None):  params = []
                else:  params = probes_audition_partTwo.trialList[0].keys()
                # save data for this loop
                probes_audition_partTwo.saveAsText(filename + 'probes_audition_partTwo.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                thisExp.nextEntry()
            
            thisExp.nextEntry() # SAME QUESTION: MUSS DAT?
            
        # staircase completed
        
        staircase_audition.saveAsText(filename + 'staircase_audition.csv' + '_' + str(idx+1), delim=',')
        sV_audition = level
        
        
#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
keyResp_thanks = event.BuilderKeyResponse()  # create an object of type KeyResponse
keyResp_thanks.status = NOT_STARTED
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(thankyou)
thanksComponents.append(keyResp_thanks)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if t >= 0.0 and thankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankyou.tStart = t  # underestimates by a little under one frame
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.setAutoDraw(True)
    
    # *keyResp_thanks* updates
    if t >= 0.0 and keyResp_thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyResp_thanks.tStart = t  # underestimates by a little under one frame
        keyResp_thanks.frameNStart = frameN  # exact frame index
        keyResp_thanks.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if keyResp_thanks.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ###
#give some output to user in the command line and save data to extra file
print 'reversals:'
print staircase_vision.reversalIntensities
print 'mean of final 6 reversals (vision_oddball) = %.3f' %(average(staircase_vision.reversalIntensities[-6:]))
print 'reversals:'
print staircase_audition.reversalIntensities
print 'mean of final 6 reversals (audition_oddball) = %.3f' %(average(staircase_audition.reversalIntensities[-6:]))


win.close()
core.quit()
