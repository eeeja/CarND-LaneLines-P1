{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Finding Lane Lines on the Road** \n",
    "\n",
    "\n",
    "**Finding Lane Lines on the Road**\n",
    "\n",
    "The goals / steps of this project are the following:\n",
    "* Make a pipeline that finds lane lines on the road\n",
    "* Reflect on your work in a written report\n",
    "\n",
    "\n",
    "[//]: # (Image References)\n",
    "\n",
    "[image1]: ./examples/grayscale.jpg \"Grayscale\" \n",
    "[image2]: ./examples/change_in_asphalt_color.png \"Asphalt\" \n",
    "\n",
    "---\n",
    "\n",
    "### Reflection\n",
    "\n",
    "### 1. Describe your pipeline. \n",
    "\n",
    "My pipeline consisted of 5 primary steps:\n",
    "1. First, I converted the images to grayscale. I noticed through my trial tests that I was able to best detect white and yellow lanes by splitting the frame RGB channels and apply grayscale using only the R&G values. \n",
    "2. Second I blacked out the regions outside of the rough quadrilateral shape of a straight lane line-- this removes other edges which might distract my pipeline from identifying a lane line. \n",
    "3. Next I applied a Gaussian filter to smooth out the image so that the edge detector can focus on the main edges.\n",
    "4. Fourth, I apply the Canny Edge detector function so I can retrieve a list of pixels who are likely candidates to be lane lines.\n",
    "5. Fifth, I run the pixels detected in the previous step through a hough transformation so that I can find common slopes-- this helps me identify what the lane line equations are. \n",
    " \n",
    "\n",
    "In order to draw a single line on the left and right lanes, I modified the draw_lines() function to:\n",
    "1. Given the (x1,y1) & (x2,y2) coordinates for each line, find the corresponding slope and y-intercepts. \n",
    "2. Identify parallel  lines for each side. If these parallel  lines are close to each other, then we keep them all and average the intercepts and slopes. If the lines are far apart, (in this pipeline, we define far as more than +/- 20 px from the median of the slope values), then only certain slope/intercept pairs are evaluated. In this situation, for left lanes, we only consider slope/intercept pairs which have a larger intercept. These pairs would most likely be the line closest to the center of the image and most likely a lane line, as opposed to a parallel highway barrier shadow. For right lanes, we conly consider slope/intercept pairs which ahve a smaller intercept. Consider the image below: \n",
    " <img src=\"./examples/lane_line_or_barrier_shadow.png\" alt=\"Parallel lane lines and shadow\" style=\"width:500px;\"\\>\n",
    "3. Once we have a set of slope/intercept pairs singled out from the previous step, we attempt to screen out any outliers to prevent them from skewing our final slope/intercept value for the left and right lane. \n",
    "     We accomplish this by: \n",
    "     * Slopes: Removing each slope/intercept pair if the difference between the selected slope is greater than 20% of the median of the set of slopes.\n",
    "     Consider:\n",
    "     `if abs(abs(right_slope_array[i])-abs(right_slope)) > abs(right_slope)*.2:`\n",
    "          \n",
    "     * Intercepts: Removing each slope/intercept pair if the difference between the selected intercept is greater than 15 pixels of the median of the set of intercepts.\n",
    "4. Last we take the average of the final set of slope/intercept pairs for both the left and right side to come to a final value which we use to derive the left and right lane lines. \n",
    "\n",
    "### 2. Identify potential shortcomings with your current pipeline\n",
    "\n",
    "\n",
    "1. One potential shortcoming would be what would happen when the car encounters a stoplight or needs to make a right/left turn. The existing pipeline might become confused with the additional lines or lack of lines in those situations. \n",
    "\n",
    "2. The pipeline will most likely not handle videos with dark lighting, such as a video taken while driving at night. Lane lines might become less visible at that point and the pipeline would have to be modified to pick up on the reflective lane line markers.  \n",
    "\n",
    "3. Perhaps fixed if the pipeline identifies curved lines, the current system does not consider lines that are perpendicular to the frame. Such lines would have a slope of infinity and would break at certain calculations.\n",
    "\n",
    "\n",
    "\n",
    "### 3. Suggest possible improvements to your pipeline\n",
    "\n",
    "There are numerous improvements we could make to this pipeline:\n",
    "\n",
    " 1. As demonstrated in the challenge video, the current pipeline may mistake changes in asphalt cement color for lane edges. To better handle these scenarios, the next iteration of the pipeline should an algorithm to detect occasional anomalous edges such as the one below and to subsequently ignore them. Perhaps one way of identifying these edges is by keeping track of a global right and left lane slope and intercept parameter, when a frame suddenly switches from a lane edge of one set of parameters to another that is significantly different, the new different parameters would be categorized as an anomaly and ignored. \n",
    " \n",
    " <img src=\"./examples/change_in_asphalt_color.png\" alt=\"Change in asphalt color\" style=\"width:500px;\"\\>\n",
    " \n",
    " 2. We could further improve the pipeline such that it could detect curved edges. At the moment, it only detects straight lines. Curved lanes could provide more accurate environmental information to the vehicle. \n",
    " \n",
    " 3. Many of the parameters (such as the canny threshold or the houghline parameters) input in the pipeline were informally selected after a series of sample trials. These parameters could be better identified if they were systematically identified after training them through a larger dataset. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  },
  "widgets": {
   "state": {},
   "version": "1.1.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
