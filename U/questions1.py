"""I recently appeared for Uber's Backend Engineer role's Online Assesment (OA) and faced following problems. The OA was hosted on code signal and I was given 70 minutes to solve all the 4 questions. I was able to solve 3 of them completly and in the last one I hit TLE. My assessment score came out to be 510. Here are the questions:

Question 1
Start with 1500 rating. You're given a diff array that defines the amount your rating has changed. After performing diff array changes in your initial rating return the max rating so far and your current rating. Example: Input: diff=[10,50,-10,100] Output: [1650,1650]

Question 2
You're given a forest array where 0 means empty space and +ve integer means a stick of size forest[i]. You're also give an index bird which denotes the init place of a bird in forest. Bird will always be at an empty index. The bird wants to build a nest of size 100 using the sticks in forest. In order to do so it follows the following algo:

It flies to right until it finds a stick.

Brings it back to its nest to build it.

Then turns it direction and does the step 2.

The bird keep following above until its nest of size 100 or greater is built. You need to return an array denoting the index of sticks that the bird picked to create the nest sorted in the order it picked them. Example: Input: forest=[10,50,0,100] bird=2 Output: [3]

Question 3
This was directly from the Uber tagged questions: https://leetcode.com/problems/rotating-the-box/description/

 You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

    The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

    It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

    Return an n x m matrix representing the box after the rotation described above.

    Args:
        boxGrid (array): An array of elements

Question 4
You are given a number line of length N. You're given a 2d array query, where query[i][0] is the coordinate which this query colors with query[i][1] color. For each query, you need to tell the number consecutive pairs of same color in the number line. Initially all numbers are not colored and can be assumed to be 0. Example: Input: query=[[2,1],[3,1],[4,3],[5,1],[4,1]] Output: [0,1,1,1,3] Would really appreciate if someone can share the solution for this one or its equivalent LC."""
