#!/usr/bin/env python3

# Last changed: 22/09/2020
# Status: Usable
#
# Module contains following model specific / dependant functions for ESP-r:
#
#  27: def set_corecon(config, cnn_file, old_coreclass, old_corecon, new_coreclass, new_corecon):
#            Switch ...
#  96: def set_htc(config, cnn_file, set_unset):
#            Set / unset? convection coefficients file.
# 156: def set_lam_w6CFC(config, mat_class, mat_entry, lam):
#            Set thermal conductivity for specific material in materials
#            database for model w/ 6 zones featuring CFC(!).
# 210: def set_lam(config, matclass, material, lam):
#            Set thermal conductivity for materials in model w/o CFC
#            constructions(!).
# 261: def set_abs_o(config, matclass, material, abs):
#            Set outside solar absorption for materials in model w/o CFC
#            constructions(!).
    from subprocess import run

"""
Module contains model specific functions using ESP-r project manager
in text mode.
"""

def set_corecon(config, cnn_file, old_coreclass, old_corecon, new_coreclass, new_corecon):
    r"""Function to change construction globally for "movable" rooms.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    cnn_file : str
        Connections file name without extension.
    old_core_class : int
        Old construction category.
    old_corecon : str
        Old construction name.
    new_coreclass : int
        New construction category.
    new_corecon : str
        New construction name.

    """

    print("\n\n\n"
          "-----------------------------------------------\n"
          "           Changing construction ...\n"
          "-----------------------------------------------")

    print("\nchanging construction in " + config + ".cfg globally")
    print("changing slabs w/ internal wood-layer (cores)")
    print("search for " + old_coreclass + " / " + old_corecon)
    print("replace it by " + new_coreclass + " / " + new_corecon)

    # Changing construction
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "c\n"  # composition
                "*\n"  # global tasks
                "f\n"  # search & replace
                "c\n"  # continue
                + old_coreclass + "\n"  # old construction category
                + old_corecon + "\n"  # old construction name
                + new_coreclass + "\n"  # new construction category
                + new_corecon + "\n"  # new construction name
                "*\n"  # search zones (* all zones)
                "-\n"  # exit this menu
                "b\n"  # continue (Schlafen.cfc)
                "Y\n"  # apply construction to Schl_Schrk? [Y/N]
                "Y\n"  # apply construction to Abstell? [Y/N]
                "Y\n"  # apply construction to WC? [Y/N]
                "Y\n"  # apply construction to Ofen? [Y/N]
                "Y\n"  # apply construction to Bad? [Y/N]
                "Y\n"  # apply construction to Bad? [Y/N]
                "b\n"  # continue (Bad.cfc)
                "b\n"  # continue (Essen.cfc)
                "Y\n"  # apply construction to Eingang? [Y/N]
                "b\n"  # continue (Eingang.cfc)
                "b\n"  # continue (Schlafen2.cfc)
                "Y\n"  # apply construction to Schl2_Schrk? [Y/N]
                "Y\n"  # apply construction to Kueche_Schrk? [Y/N]
                "b\n"  # continue (Wohnen.cfc)
                "-\n"  # exit this menu
                "!\n"  # save model
                + config + ".cfg\n"  # Update system configuration file?
                + cnn_file + ".cnn\n"  # Surface connections file name?
                "-\n"  # exit this menu
                "-\n",  # exit Project Manager
                encoding="utf-8")

    f = open(config + "_set_corecon_" + new_corecon + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_htc(config, cnn_file, set_unset):
    r"""Function to set heat transfer coefficients.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    cnn_file : str
        Connections file name without extension.
    set_unset : str
        Zone convection file selection key (must be last part of to-be-switched zone
        convection file name).

    """

    print("\n\n\n"
          "------------------------------------------------------------\n"
          "           Setting heat transfer coefficients ...\n"
          "------------------------------------------------------------")

    print("\nin " + config + ".cfg\n"
          "setting heat transfer coefficients")

    # Setting htc-files
    args = [
        "prj",
        "-file", config + ".cfg",  # executable file
        "-mode", "text",  # opens file in mode text
    ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "c\n"  # composition
                "g\n"  # convection coefficients
                "b\n"  # zone Convection Selection (Schlafen)
                "../zones/Schlafen_" + set_unset + ".htc\n"  # zone conv regime file?
                ">\n"  # save
                "Y\n"  # overwrite this file? [Y/N]                                 
                "-\n"  # exit
                "h\n"  # zone Convection Selection (Essen)
                "../zones/Essen_" + set_unset + ".htc\n"  # zone conv regime file?
                ">\n"  # save
                "Y\n"  # overwrite this file? [Y/N]                                 
                "-\n"  # exit
                "j\n"  # zone Convection Selection (Schlafen2)
                "../zones/Schlafen2_" + set_unset + ".htc\n"  # zone conv regime file?
                ">\n"  # save
                "Y\n"  # overwrite this file? [Y/N]                                 
                "-\n"  # exit
                "m\n"  # zone Convection Selection (Wohnen)
                "../zones/Wohnen_" + set_unset + ".htc\n"  # zone conv regime file?
                ">\n"  # save
                "Y\n"  # overwrite this file? [Y/N]                                 
                "-\n"  # exit
                "-\n"  # exit this menu
                "-\n"  # exit this menu
                "!\n"  # save model
                + config + ".cfg\n"  # update system configuration file?
                + cnn_file + ".cnn\n"  # surface connections file name? 
                "-\n"  # exit this menu
                "-\n-",  # exit Project Manager
                encoding="utf-8")

    f = open(config + "_set_htc.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

def set_lam_w6CFC(config, mat_class, mat_entry, lam):
    r"""Set thermal conductivity for specific material in materials database - for model
    w/ six (6) zones featuring CFC constructions(!).

    Parameters
    ----------
    config : str | Path
        Configuration file name (with relative path!).
    mat_class : str
        Database materials class of interest.
    mat_entry : str
        Database entry letter for material of interest.
    lam : str
        Thermal conductivity value to be used in W/(m K) as string.

    """

    print("   Setting new conductivity in materials database of" + config + ":")
    print("      New value for material class" + mat_class +
          ", material index ", + mat_entry + " is " + lam + " W/(m K).")

    # Setting lam for mat
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("b\n"  # database maintenance
                "c\n"  # materials db
                "a\n"  # browse / edit
                + mat_class + "\n"
                + mat_entry + "\n"
                "c\n"  # conductivity (W/(m K))
                + lam + "\n"
                "-\n"  # exit material details
                "Y\n"  # accept changes
                "!\n"  # save materials file
                "Y\n"  # overwrite file
                "-\n"  # exit material class
                "-\n"  # exit materials classes
                "-\n"  # exit database maintenance
                "Y\n"  # update model NAME LIST
                "Y\n"  # rebuild .con files
                "b\n"  # Schlafen.cfc => continue
                "b\n"  # ...
                "b\n"
                "b\n"
                "b\n"
                "b\n"  # Wohnen.cfc => continue
                "-\n", # exit prj
                encoding="utf-8")

    #<< TODO: make model-independant ... scan for CFC? >>

    f = open(config + "_set_" + mat_class + "_" + mat_entry + "_" + lam + "_con.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

def set_lam(config, matclass, material, lam):
    """Set thermal conductivity for materials in model w/o CFC constructions(!).

    Parameters
    ----------
    config : str | Path
        Configuration file name (with relative path).
    matclass : str
        Material class in materials database.
    material : str
        Material selection letter in materials database.
    lam : str
        Thermal conductivity value in (W/(m K)) as string.

    """

    print("\tSetting new thermal conductivity in materials database of " \
                                                          + config + ".")
    print("\t\tNew value for material class" + matclass + ", material index " \
                                 + material + " is " + lam + " W/(m K).")

    # Get number of .geo files that contain 'CFC2' constructions. This
    # corresponds to the number of CFC file changes to be rejected.
    # cmd='grep -c -w "CFC2" *.geo \
    #          | cut -d ":" -f 2 \
    #          | awk \'{if($1!=0) c+=$1/$1} END{print c+0}\''

    # wd=os.getcwd() # must be <modelpath>/cfg <<check?>>
    # nf = run(cmd, shell=True, cwd=wd, capture_output=True).stdout.strip()
    # nf = nf.decode('utf-8')

    # Setting lam for mat
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    # cmd1 = bytes("b\n"  # database maintenance
    cmd = bytes("b\n"  # database maintenance
                "c\n"  # materials db
                "a\n"  # browse / edit
                + matclass + "\n"
                + material + "\n"
                "c\n"  # Conductivity (W/(m-K))
                + lam + "\n"
                "-\n"  # Exit
                "Y\n"  # accept changes
                "!\n"  # save materials file
                "Y\n"  # overwrite file
                "-\n"  # exit menu
                "-\n"  # exit menu
                "-\n"  # exit menu
                "Y\n"  # Update model to match?
                "Y\n"  # Update zone construction files?
                "-\n", # quite module
                encoding="utf-8")

    # cmd2 = bytes("b\n",  # zone.cfc? => continue
    #              encoding="utf-8")
    #
    # s = ''
    # for i in range(int(nf)):
    #     s += cmd2.decode('utf-8')
    #
    # cmd2 = s.encode('utf-8')

    # cmd3 = bytes("-\n", # exit prj
    #             encoding="utf-8")

    # cmd = cmd1.decode('utf-8')   \
    #       + cmd2.decode('utf-8') \
    #       + cmd3.decode('utf-8') \
    #
    # cmd = cmd.encode('utf-8')

    # Create scratch file.
    f = open(config + "_set_" + matclass + "_" + material + "_" \
                                             + lam + "_lam.scratch", "w")

    # Run prj (args), execute commands (cmd), write scratch file (f)
    run(args, input=cmd, stdout=f)


def set_abs_o(config, matclass, material, abs):
    """Set outside solar absorption for materials in model w/o CFC constructions(!).

    Parameters
    ----------
    config : str | Path
        Configuration file name (with relative path).
    matclass : str
        Material class key in materials database.
    material : str
        Material key in materials database.
    abs : str
        Solar absorption outside value (-) as string.

    """

    print("\tSetting new outside solar absorption in materials database of " \
                                                          + config + ".")
    print("\t\tNew value for material class" + matclass + ", material index " \
                                 + material + " is " + abs + " (-).")

    # Setting lam for mat
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("b\n"  # database maintenance
                "c\n"  # materials db
                "a\n"  # browse / edit
                + matclass + "\n"
                + material + "\n"
                "h\n"  # Absorptivity out (-)
                + abs + "\n"
                "-\n"  # Exit
                "Y\n"  # accept changes
                "!\n"  # save materials file
                "Y\n"  # overwrite file
                "-\n"  # exit menu
                "-\n"  # exit menu
                "-\n"  # exit menu
                "Y\n"  # Update model to match?
                "Y\n"  # Update zone construction files?
                "-\n", # quite module
                encoding="utf-8")

    # Create scratch file.
    f = open(config + "_set_" + matclass + "_" + material + "_" \
                                             + abs + "_abs-o.scratch", "w")

    # Run prj (args), execute commands (cmd), write scratch file (f)
    run(args, input=cmd, stdout=f)

