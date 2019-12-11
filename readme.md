# Schedule Generator for McMaster University 
## Introduction:
This is a program that helps users create timetable when they are in the stage of choosing different sections of different courses before a semester begins. Specifically, this program only works for those organizations having the same course structure as McMaster university's.

   - **Task**: 
      - big view: given courses, return all possible timetables  
   - choice of language: 
      - **Python3**

## Problem Analysis
   - Timetable analysis:
      - Analyze by looking at a real example:
      - ![avatar](md_img/schedule_example.png)
      - Define **class**: class is one inctance in any part of the course. 
      In another word, for a lab, a tutorial, or lecture, they can all be  classes.
      - **Assumption**: there are no classes on weekends.
      - A class usually lasts for 50 minutes and starts from 30 minutes after a certain clock.
      - Note: Some classes in the evening may not apply the pattern.
      - Therefore, the timetable can be viewed as an x-y coordinnate.
      - ![avatar](md_img/coordinate_table.png)
      - Note: n-m means from n:30 to m:20
   - Structure of a course in McMaster Univeristy:
      - Three parts:
         - Lecture
         - Tutorial
         - Lab
      - For each part stated above, there may be more than one sections. 
      - Only one of the sections needs to be scheduled into the timetable.
      - Here is a picture of course structure![avatar](md_img/course_structure.png)
   - things that are unsure:
      - Not sure whether there are conflicts between two sections from two different parts.
---------
## Choice of data structrue
   - class: ADT-Point
   - section: SET
   - part: array of sections
   - course: ADT-Course containing three parts
---------
## Usage
   - use **Python3** to run main.py.
   - in your terminal, execute the following commands:
   ```bash
   > git clone https://github.com/Darin1123/Schedule_Generator
   > cd Schedule_Generator/src
   > python3 main.py
   ```
   - follow the instructions to create your schedules.
   - output:
      - a **.term** file containing the user input
      - some **.csv** files and they are all possible schedules
