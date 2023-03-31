# smol

## Story time.

Hi cole here I thought I would tell you why I made this board.
I read A LOT of keyboard stuff day to day, one day I was reading about how much some people find the 100x100mm $2 pcbs very important to the hobby.
That made me remember back years ago when I first got into custom ergo boards how thats where I cut my teeth.
So I wanted to give back to this awesome community by making another cheap board.

I also was reading about square matrixes, this all came together into this keyboard.
This keyboard is 1 pcb that flips to make the full single piece board.
It is a symmetric staggered keyboard using 2 square matrixes with pcbs under 100x100mm,
choc spaced with a 3d printed case that comes pre supported,for fdm printing or you can order them from jlc pcb at $1.68.

you only need:

- 1 controller
- 36 choc switches & caps
- 41 diodes
- 2 pcbs
- 2 cases

# Disclaimer

There is no code support for this.
In the firmware section there is kmk code until the pr is finished.
I think you need a custom matrix.c in qmk to use this keyboard.
Depending on your diodes and controller selection this keyboard may not work.
Its tested with normal diodes with Blok controller.
I dont think elite-c's would work being that they are 5V.
I included pin holes but have not tested n!n.
