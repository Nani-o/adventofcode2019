[![Build Status](https://travis-ci.org/Nani-o/adventofcode2019.svg?branch=master)](https://travis-ci.org/Nani-o/adventofcode2019)

Advent of code 2019
===================

This repo contains my solution for the [Advent of code 2019](https://adventofcode.com/2019/).

Usage
-----

I run aoc.py as a package, which act as a launcher to run the solutions from a file per day with a function per part, the inputs are in a folder named for each day.

```
$ python -m aoc.aoc -h
usage: adventofcode.py [-h] [--day DAY] [--part PART]

optional arguments:
  -h, --help            show this help message and exit
  --day DAY, -d DAY     Day of the puzzle to run
  --part PART, -p PART  Part of the puzzle of the day to run

$ python -m aoc.aoc -d 1 -p 1
Day 1 - part 1
==============

solution : 435
time : 0.5951 ms
```

License
-------

MIT

Author Information
------------------

Sofiane MEDJKOUNE
