#!/usr/bin/env python
# ------------------------------------------------------------------------------
# The Learning to Live with Gimp Series
# Adds an X and Y positioning GUI.
# Copyright 2012 Stephen Niedzielski. Licensed under GPLv3.

# For debugging, launch Gimp from the console and collect output. To execute
# standalone:
#  PYTHONPATH+=:/usr/lib/gimp/2.0/python python $0

# Store in ~/.gimp-2.6/plug-ins with chmod +x.

# ------------------------------------------------------------------------------
import os
import sys
from gimpfu import *

# ------------------------------------------------------------------------------
#def main(argv=None):
#  print(main.__name__)

#  if argv is None:
#    argv = sys.argv

# ------------------------------------------------------------------------------
def gimpxy_main(timg, tdrawable, xy):
  print(gimpxy_main.__name__)

# ------------------------------------------------------------------------------
def gimpxy_register():
  print(gimpxy_register.__name__)

  register(proc_name='gimpxy',
           blurb='Position elements by X and Y values',
           help='',
           author='Stephen Niedzielski',
           copyright='Copyright 2012 Stephen Niedzielski. Licensed under GPLv3',
           date='2012',
           label='', #label='<Image>/Layer/_gimpxy...',
           imagetypes='',
           params=[], #params=[ (PF_STRING, "xy", "_x,y:", "x, y") ],
           results=[],
           function=gimpxy_main,
           menu=None,
           domain=None,
           on_query=None,
           on_run=None)

  # TODO: how do I make a persistent GUI?

# ------------------------------------------------------------------------------
#if __name__ == '__main__':
#  sys.exit(main())
#else:
#gimpxy_register()
#main()

# Run from console...
#import sys, os; sys.path.append(os.path.realpath('.gimp-2.6/plug-ins')); from gimpfoo import *

# ------------------------------------------------------------------------------
def img():
  return gimp.image_list()[0]

def lyr():
  return img().active_layer
#  return img().layers[0]

# ------------------------------------------------------------------------------
def to_px(x=0, y=0, metric='px'):
  MM_TO_IN = 0.0393701

  if metric == 'px': return (int(round(x)), int(round(y)))
  if metric ==  '%': return (int(round((lyr().width * x) / 100.0)), int(round((lyr().height * y) / 100.0)))
  if metric == 'mm': return (int(round(img().resolution[0] * x * MM_TO_IN)), int(round(img().resolution[1] * y * MM_TO_IN)))
  if metric == 'cm': return (int(round(img().resolution[0] * x * MM_TO_IN * 10)), int(round(img().resolution[1] * y * MM_TO_IN * 10)))
  if metric == 'm' : return (int(round(img().resolution[0] * x * MM_TO_IN * 1000)), int(round(img().resolution[1] * y * MM_TO_IN * 1000)))
  if metric is 'in': return (int(round(img().resolution[0] * x)), int(round(img().resolution[1] * y)))
  raise Exception('Unhandle metric "%s"' % metric)

# "m" for move (absolute).
def m(x=None, y=None, metric='px'):
  ret = None

  if x is None and y is None:
    ret = lyr().offsets
    ret.append('px')
  else:
    (x,y) = to_px(x, y, metric)
    ret = (x, y, 'px')
    lyr().set_offsets(x, y)

  return ret

# TODO: origin control.
# TODO: self reload? while True: if is_changed(module): module = reload(module)
# TODO: "rm" for relative move.
# TODO: shorthand of xy [blah] ... See IPython, generators, and goto joke.
# TODO: gui
