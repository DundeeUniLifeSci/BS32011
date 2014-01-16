# Text editors

When you are writing programs, web pages and so on you will be wanting to use a text editor. These can either be graphical (such as Kate, found under the Applications/Accessories menu, or command line such as nano, vi or emacs. 
These editors save your file as plain text. There is no colouring or such like saved in the file though some, if they recognise the type of file will provide *syntax colouring* where different keywords are highlighted.

Always use a text editor, never use a word processor for writing code. 

## Graphical editors

These run under Xwindows so require the use of Xming or a similar Xwindows setup. They respond to mouse movement and support point and click interaction.

### Kate

Kate is found under the Applications/Accessories menu. It provides a file browser and the ability to run code directly from within the editor. 

### xemacs

Start xemacs from a terminal with the command

    xemacs

This is a graphical version of the *emacs* editor. xemacs is straightforward to use with a standard menu system. It supports the emacs keyboard shortcuts (CTRL- etc to launch different commands).

## Command line editors

These run in a terminal from the shell. They do not support point and click.

### nano

nano (and the counterpart *pico*) are very lightweight text editors. They are basic, but fine for short projects and support syntax colouring. 

From a shell prompt type:

    nano
    
or 

    nano filename
    
to edit the file. Save with CTRL-O, exit with CTRL-X. 

Novices should stick with nano unless they are preapred for a steep learning curve.

### emacs

To persuade emacs to do anything you have to remember a bunch of CTRL-key codes. e.g. CTRL-X CTRL-F to open or create  a file. CTRL-X CTRL-W to write a file under a new name, CTRL-X CTRL-S to save. [A guide to emacs](http://www.physics.usyd.edu.au/~robishaw/comp/emacs.crib.html). By convention CTRL-X is referred to as C-x and ALT-X as M-x in emacs speak.

### vi

In many ways vi is the most powerful but also the most frustrating of editors. It has two modes, command mode and edit mode. In command mode different key combinations do different things. In edit mode everything does as expected and what you type goes into the file. Edit mode can be entered using any one of a number of keys (i for insert, a to append, A to append at the end of line, cw to replace everything in the word under the cursor. Edit mode is exited by pressing ESC and many commands can be entered after pressing :. It supports many elements of the command line program *sed* for rapid editing. 

Start vi by typing:

    vi
    
and exit by pressing ESC , then Z twice (or :q! to quit without saving changes)

[A guide to vi](http://www.flamingpenguin.co.uk/vi/vicribsheet.html)