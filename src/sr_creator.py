from .nodes import nodes
from .parameters import *
from .URs import new_all_URs
from .various import *
from .test_parse import test
from .timeme import *


def sr_creator(start_time, lang_fam, forces, test_URs, outputfoldername):
    now = start_time
    # Beginning of main code, where each input language will be run through
    tree_count = 0
    lang_count = 0
    #outputfilename = tsvcheck(outputfilename)
    # Create pointer here for segmentally printing the all_all.tsv file
    file_add        = "0"
    new_file_add    = "0"
    outputfilename  = outputfoldername+"/"+file_add+".tsv"
    for language in languages(lang_fam):
        if new_file_add != file_add:
            file_add = new_file_add
            outputfilename = outputfoldername+"/"+file_add+".tsv"
            print("Max time elapsed, changed to " +outputfilename)
        lang_count += 1
        print("Lang " + str(lang_count) + ":" + str(language))
        # runs through the list of forces
        for force in force_finder(forces):
            print("Force: " + str(force), end=", ")
            print("Trees:", end=" ")
            starting_tree_count = tree_count
            # returns list of lists, padded to 14 items (i.e. the most lexical items possible)
            all_URs_ = activate_force(force, test_URs)
            # for each UR in this force's list of URs
            for ur in all_URs_:
                # Take the UR, turn it into list of node objects
                node_list = nodes(ur)
                # Run each UR through the parameter settings;
                # Each UR (and its nodes/tree) can produce multiple SR/strings
                # so l_of_l_of_nodes can be max 6 lists of nodes
                # based on optional parameter settings: (null_subXnull_topXprep_stranding) = 6
                PFN = [[]] * 3
                PFN[0] = language
                PFN[1] = force
                PFN[2] = node_list
                assert len(PFN[2]) > 0
                l_of_l_of_nodes = apply_parameters(PFN)
                # assert len(l_of_l_of_nodes)>0
                # Finally make the SOWs/SRs
                for l_of_nodes in l_of_l_of_nodes:
                    tree_count += 1
                    # print(str(tree_count), end=",")
                    # Make an SOW/SR for each node list
                    # i.e. for each possible outcome of parameters & ur
                    if isinstance(l_of_nodes, list):
                        l_of_nodes = get_daughters(l_of_nodes)
                    out(language, force, ur, l_of_nodes, outputfilename, test_URs)
            print(tree_count - starting_tree_count, end="; ")
        print()
        now, new_file_add = check(start_time, now, lang_count)
        # SAVE POINTER
    # If not all the possible parameter settings are being produced, show the set that are
    if lang_fam == False:
        print("\nLanguage families assessed for this run:\n", end="")
        for x in languages(lang_fam):
            print(x)
    #Final output to terminal before returning to parent and running test against licit SRs
    output_final_count(tree_count, outputfoldername)

