"""
Takes four arguments, default=False, and begins the ur_to_sr_mapping code
Also times the whole operation 
"""

from src import sr_creator
import sys
from src import timeme

if __name__ == "__main__":
    start_time = timeme.start()
    # Boolean for All languages versus only the list of desired languages
    try:
        arg = sys.argv[1]
        if arg == "True":
            lang = True
        else:
            lang = False
    except:
        lang = False

    # Boolean for All forces versus only the list of desired forces
    try:
        arg2 = sys.argv[2]
        if arg2 == "True":
            forces = True
        else:
            forces = False
    except:
        forces = False

    # Are we just looking at some test URs?
    try:
        arg3 = sys.argv[3]
        if arg3 == "False":
            test_URs = False
        else:
            test_URs = arg3
    except:
        test_URs = False

    # Did the user put in a outputfilename?
    try:
        arg4 = sys.argv[4]
        if arg4 == "False":
            outputfilename = False
        else:
            outputfilename = arg4
    except:
        outputfilename = "all_all.tsv"
    # Send all to the SR_creator script
    sr_creator.sr_creator(lang, forces, start_time, test_URs, outputfilename)
    timeme.end(start_time)
