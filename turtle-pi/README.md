# python-turtle-pi

[![GNU LGPLv2.1](https://img.shields.io/badge/license-LGPLv2.1-yellowgreen.svg)](LICENSE) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme "RichardLitt/standard-readme")

> Modeling the value of **π** (and **τ**) and visualizing with turtles

## Table of Contents

- [Background](#background)
- [Usage](#usage)

## Background

From [Wikipedia](https://en.wikipedia.org/wiki/Pi):

> The number **π** (/paɪ/) is a mathematical constant. Originally defined as the ratio of a circle's circumference to its diameter, it now has various equivalent definitions and appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159. It has been represented by the Greek letter "π" since the mid-18th century, though it is also sometimes spelled out as "pi". It is also called Archimedes' constant.

We can estimate the value of **π** by inscribing a circle into a square, and picking a large number of random points within the square. Those which also fall inside the circle we designate *hits*, and the ratio of hits to all points picked is equivalent to **¼π**.

### Tau (**τ**)

There is an [argument](https://www.math.utah.edu/~palais/pi.html) that the correct circle constant is not **π**, but **τ**. The [idea](https://en.wikipedia.org/wiki/Turn_(geometry)#Tau_proposals) has been around for [quite a while](https://sites.google.com/site/taubeforeitwascool/), and there is even a [manifesto](https://tauday.com/tau-manifesto/). Because of the mathematical and pedagogical advantages of **τ**, and because it is good for generating discussion or a laugh, `turtle_pi` also calculates **τ**.

## Usage
```
Usage: python[3] turtle-pi/turtle_pi.py [--no-viz] <dots> [radius]
    --no-viz : don't run the visualization (increases speed)
    dots     : number of points to check
    radius   : radius of square/circle
```
