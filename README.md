# cntdrun

A program for executing commands with countdown timers.

## Install
```
pip install cntdrun 
pip install --user git+https://github.com/gzj/cntdrun.git
```

## Quick Start
```
cntdrun [count] [command]
cntdrun 3 "bash -c ls" 
cntdrun 3 "echo 'Countdown finished!'" --label-font "Times" --label-size 40 --button-text "Exit" --button-font "Helvetica" --button-size 12 --window-x 100 --window-y 100 --window-width 300 --window-height 200 --command-label "test"
```
