
# **Finding Lane Lines on the Road** 


**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


---

### Reflection

### 1. Describe your pipeline. 

My pipeline consisted of 5 primary steps:
1. I converted the images to grayscale. I noticed through my trial tests that I was able to best detect white and yellow lanes by splitting up each video frame to separate RGB channels and then applying grayscale on only the R&G channel values. 
2. I then blacked out the regions outside of the quadrilateral shape of a straight lane line-- this removes other edges which might distract my pipeline from identifying a lane line. 
3. Next I applied a Gaussian filter to smooth out the image so that the edge detector can focus on the main edges.
4. Since the image is smoother, now I can apply the Canny Edge detector function to retrieve a list of pixels which are likely candidates to be lane lines.
5. Last I run the pixels detected in the previous step through the opencv houghLinesP function to find find common slopes.
 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function to:
1. Given the (x1,y1) & (x2,y2) coordinates for each line, find the corresponding slope and y-intercepts. 
2. Identify parallel  lines for each side. If these parallel  lines are close to each other, then we keep them all and average the intercepts and slopes. If the lines are far apart, (in this pipeline, we define far as intercepts which are more than +/- 100 px from each other), then only certain slope/intercept pairs are evaluated. For left lanes, we only consider slope/intercept pairs which have a larger intercepts. These pairs would most likely be the line closest to the center of the image and most likely a lane line, as opposed to a parallel highway barrier shadow. For right lanes, we conly consider slope/intercept pairs which have a smaller intercept. Consider the image below: 
 ![](./examples/lane_line_or_barrier_shadow.png)
3. Once we have a set of slope/intercept pairs singled out from the previous step, we attempt to screen out any outliers to prevent them from skewing our final slope/intercept value for the left and right lane. 
     We accomplish this by: 
     * Slopes: Removing each slope/intercept pair if the difference between the selected slope is greater than 20% of the median of the set of slopes.
     Consider:
     `if abs(abs(right_slope_array[i])-abs(right_slope)) > abs(right_slope)*.2:`
          
     * Intercepts: Removing each slope/intercept pair if the difference between the selected intercept is greater than 15 pixels of the median of the set of intercepts.
4. Last we take the average of the final set of slope/intercept pairs for both the left and right side to come to a final value which we use to derive the left and right lane lines. 

### 2. Identify potential shortcomings with your current pipeline


1. One potential shortcoming would be what would happen when the car encounters a stoplight or needs to make a right/left turn. The existing pipeline might become confused with the additional lines or lack of lines in those situations. 

2. The pipeline will most likely not handle videos with dark lighting, such as a video taken while driving at night. Lane lines might become less visible at that point and the pipeline would have to be modified to pick up on the reflective lane line markers.  

3. Perhaps fixed if the pipeline identifies curved lines, the current system does not consider lines that are perpendicular to the frame. Such lines would have a slope of infinity and would break at certain calculations.



### 3. Suggest possible improvements to your pipeline

There are numerous improvements we could make to this pipeline:

 1. As demonstrated in the challenge video, the current pipeline may mistake changes in asphalt cement color for lane edges. To better handle these scenarios, the next iteration of the pipeline should include an algorithm to detect occasional anomalous edges such as the one below and to subsequently ignore them. Perhaps one way of identifying these edges is by keeping track of a global right and left lane slope and intercept parameter, when a frame suddenly switches from a lane edge of one set of parameters to another that is significantly different, the new different parameters would be categorized as an anomaly and ignored. 
 
 ![](./examples/change_in_asphalt_color.png?raw=true)
 2. We could further improve the pipeline such that it could detect curved edges. At the moment, it only detects straight lines. Curved lanes could provide more accurate environmental information to the vehicle. 
 
 3. Many of the parameters (such as the canny threshold or the houghline parameters) input in the pipeline were tuned after a series of sample trials. These parameters could be further trained with additional training videos.
