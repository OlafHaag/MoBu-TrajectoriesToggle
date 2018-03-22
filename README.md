# MotionBuilder: Toggle Trajectories
MotionBuilder Python scripts that deal with trajectories. One to toggles the visibility of trajectories on selected objects, another to diable the trajectories on all scence components

## USAGE:
- Activate the Trajectories button in the top of the viewer window.
- Click the small arrow to its right and disable 'Auto Selection'
- These scripts work best with a keyboard shortcut assigned to each.
It's easiest to do that with Alex Widener's hotkey editor (forked and modified):
https://github.com/OlafHaag/MotionBuilderHotkeyEditor
Documentation: http://www.alexwidener.com/MotionBuilderHotkeyEditor/
  - After executing the hotkey editor script, which opens a window, go to *File->Reset Hotkeys* and choose the one that you typically use for interaction.
  - In the **right pane** set the full path to the *TrajectoriesToggle.py* and *DisableAllTrajectories.py* files, e.g. for entries Script6 and Script7.
  - Then in the **left pane** scroll down until you find the *action.global.script* entries. Assign shortcut commands to the according script entries (e.g. 6 & 7)

You have to restart MotionBuilder after saving the changes.
