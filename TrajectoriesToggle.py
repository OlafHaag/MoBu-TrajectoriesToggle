#    MIT License
#    
#    Copyright (c) 2018 Olaf Haag
#    
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

# What it does:
# It toggles the visibility of trajectories on selected objects.
#    
# USAGE:
# - Activate the Trajectories button in the top of the viewer window.
# - Click the small arrow to its right and disable 'Auto Selection'
# - This script works best with a keyboard shortcut assigned to it.
#   > It's easiest to do that with Alex Widener's hotkey editor (forked and modified):
#   > https://github.com/OlafHaag/MotionBuilderHotkeyEditor
#   > Documentation: http://www.alexwidener.com/MotionBuilderHotkeyEditor/

from pyfbsdk import *


def main():
    objects = FBModelList()
    FBGetSelectedModels(objects)
    for obj in objects:
        try:
            obj.PropertyList.Find('ShowTrajectories').Data = not obj.PropertyList.Find('ShowTrajectories').Data
        except AttributeError:
            continue
    
if __name__ in ('__main__', '__builtin__'):
    main()

