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
cntdrun 6 "bash -c ls" 
cntdrun 10 "echo 'Countdown finished!'" --label-font "Times" --label-size 40 --label-x 30 --label-y 10 --label-width 190 --label-height 60 --button-text "Exit" --button-x 90 --button-y 90 --button-width 70 --button-height 40 --button-font "Helvetica" --button-size 12
```
