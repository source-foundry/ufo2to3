#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================
# Copyright 2018 Christopher Simpkins
# MIT License
# ====================================================

import os
import sys

import defcon


def main(argv):
    for ufo in argv:
        try:
            font = defcon.Font(ufo)
            font.save(formatVersion=3)
            print("Successfully converted " + ufo)
        except Exception as e:
            sys.stderr.write(
                "[ERROR] There was an error with the conversion attempt: "
                + os.linesep
                + str(e)
            )
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
