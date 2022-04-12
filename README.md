# MotionPath Converter To Curve Blender Addon
Addon for blender to convert motion path in curve for more comfort worl

This converter can help you solve many type of task like you need to make vizualisation of motion path on render. 

## Plan

1.    [Running](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#running)
2.    [Compramision of boolean modificator](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#comparing-paths-with-differents-settings-of-boolean-on-obj)   
    1.    [With Intersect on boolean](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#1-with-intersect-on-boolean)
    .    
    2.    [Without Intersect on boolean](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#2-without-intersect-on-boolean)
3.  [Working on addon](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#working-on-addon)
4.  [Future plans](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#future-plans)
    1.    [Make diffents version of addon like context menu](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#1-make-diffents-version-of-addon-like-context-menu)
    2.    [Fix error that you can't do curve if you turn more than 1 motion path](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#2-fix-error-that-you-cant-do-curve-if-you-turn-more-than-1-motion-path)
    3.    [Make more flexable](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#3-make-more-flexable)
    4.    [Do automatic creation of path with objects](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#4-do-automatic-creation-of-path-with-objects)





## Running
After installing you need to press F3 and search `Convert Motion Path to Curve` after you will see new object on scene `Curve`.

For correct work you need to keep on scene only 1 motion path and end must equal with end frame of animation.

```mermaid
sequenceDiagram
    autonumber
    Motion Path -) Curve: Addon
    Curve -) OBJ on Curve: OBJ with modificators array, curve and for more beautiful render with boolean(Intersect)
    OBJ on Curve --> Beautiful Path render: some cosmetics work
```


#### All code wasn't completely written by me. I'm just rework source code for more comfortable work with motion paths.

#### [To plan :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#plan)

## Comparing paths with differents settings of boolean on obj
### 1. With Intersect on boolean
![ALT-text](https://im3.ezgif.com/tmp/ezgif-3-0141be9a1d.gif "With Intersect on boolean")

### 2. Without Intersect on boolean
![ALT-text](https://im3.ezgif.com/tmp/ezgif-3-1efe10c9b3.gif "Without Intersect on boolean")

#### [To plan :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#plan)

## Working on addon

```mermaid
journey
    title Searching source code
    section Search in Google
      Search: 4: Me
      Understanding the code: 3: Me
    section Reworking code
      Alpha verison: 5: Me
      Beta version: 4: Me
    section Searching more info about blender addons
        Correcting: 4: Me
        Beta release: 4: Me
    section Publication
        Publicate on github: 5: Me
        Readme layout: 3: Me

```
#### [To plan :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#plan)

## Future Plans

### 1. Make diffents version of addon like context menu
### 2. Fix error that you can't do curve if you turn more than 1 motion path
### 3. Make more flexable
### 4. Do automatic creation of path with objects

#### [To plan :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/README.md#plan)
