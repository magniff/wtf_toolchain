# Ohhhh, brainfuck again, srsly?
## Why?
This is my attempt to build JIT powered bf interpreter using `RPython` toolchain. In order to make it even faster I have build a simple compiler, that generates flat and slightly optimized version of original `*.b` program.

## Hmm..
Toolchain consists of two parts - compiler written in python and JIT powered VM, written in RPython.

### Preparation
First build actual VM, pypy toolchain is required.
```bash
python pypy3-v5.5.0-src/rpython/bin/rpython -Ojit bin/wtf_runner.py 
```
This should produce native `wtf_runner-c` binary - BF VM, yes.

### Run
* First build VM compatible representation:
```bash
$ wtf_compile -i src/mandelbrot.b -o mandelbrot.wtf
```
* Run it with wtf_runner-c
```bash
~/workspace/bf $ time ./wtf_runner-c hanoi.wtf > /dev/null
real	0m0.370s
user	0m0.344s
sys	0m0.024s

~/workspace/bf $ time ./wtf_runner-c mandelbrot.wtf > /dev/null
real	0m3.143s
user	0m3.120s
sys	0m0.020s
```

In comparison to one of the fastest optimizing interpreters (written in pure C, ofc) I have found on the Internet:
```bash
~/workspace/bf $ time ../bff/bff src/hanoi.b > /dev/null 
real	0m0.537s
user	0m0.532s
sys	0m0.004s

~/workspace/bf $ time ../bff/bff src/mandelbrot.b > /dev/null 
real	0m4.777s
user	0m4.776s
sys	0m0.000s
```

See other assets inside `src` folder.
Have fun!
