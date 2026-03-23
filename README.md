
![Project Overview](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/1.jpeg)

## Project Directory

| Folder | Filename | Description |
|------|-------------|-------|
| marshmallow_feeder_cad_file | cam_case.stl<br/>cam_case.stp | Case for the webcam |
| |marshmallow_feeder.stl<br/>marshmallow_feeder.stp | Complete 3D model file for the marshmallow feeder |
| |marshmallow_feeder_arm.stl<br/>marshmallow_feeder_arm.stp | 3D model file for the arm of the marshmallow feeder |
| |marshmallow_feeder_base.stl<br/>marshmallow_feeder_base.stp | 3D model file for the base of the marshmallow feeder |
| |marshmallow_feeder_head.stl<br/>marshmallow_feeder_head.stp | 3D model file for the head (launch mechanism) of the marshmallow feeder |
| marshmallow_feeder_code | arduino_code/aiming_servos | Arduino sketch that controls two aiming servos based on incoming messages. |
| | arduino_code/feeding_servo_and_motors | An Arduino sketch that controls two DC motors for launching and one servo for loading, based on incoming messages. |
| | python_code/cam_to_weki.py | Python code which reads facial x and y coordinates from a camera and sends them via OSC messages. |
| | python_code/mouth_detect.py | Python code that reads the mouth open/close state and sends the information directly to Arduino. |
| | python_code/weki_to_arduino.py | Python code that listens for OSC messages from Wekinator and converts them into serial messages for Arduino. |
| wekinator_file/face_track/WekinatorProject | WekinatorProject.wekproj | A trained Wekinator model that outputs aiming servo angles based on facial coordinates. |

## Overall Concept

The aim was to build a gamified marshmallow launcher that:
1) Tracks a mouth opening/closing
2) Tracks a person's x and y position using 2 servos and an ML algorithm
3) Reloads marshmallows using 1 servo
4) Launches a single marshmallow into the general area of the mouth using 2 DC motors

The project can be viewed as a human snack dispenser that trains humans to catch marshmallows with their mouths.

**Aesthetics**

We wanted the final product to look simplistic, robotic and elegant. Inspired by brutalist architecture, we used white PLA to mimic the minimalist style which focuses on bare materials and structural elements over decorative design. We reinforced the robotic design by separating the machine into distinct parts that each serve their function, with each part exposed so the user can see and understand the mechanical structure whilst using the machine. We used PLA because we could rapidly prototype complex geometries in order to refine the mechanism of the design and iterate on small adjustments and tolerances. It is also a lightweight material, allowing us to keep the movement of the mechanism responsive and smooth.

We made a wooden box to attach the camera and the feeding machine together into one cohesive object. We decided to use 12mm plywood as it provides a good balance between strength, durability and ease of cutting, while keeping the overall weight manageable. The box housed the circuitry and the majority of the wiring to ensure a clean aesthetic. Heat-shrink and crimped connections allowed us to make the wires and connections neater and stronger, whilst ensuring repeatable connection and disconnection during debugging and ML training.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/2.jpeg)

**The final design after heat-shrink and cable management:**

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/3.jpeg)
![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/4.jpeg)


## Mechanical Design

Using the mechanism of controlling 4 servos to make a robotic arm move, we simplified the robotic arm into a structure that moves in the x and y directions using 2 servos. The rest of the marshmallow launcher's mechanism was inspired by baseball pitching machines, working by constantly rotating two motors in opposite directions in order to accelerate the marshmallow. Once a 'mouth open' event is detected by the camera tracking, a pinion gear controlled by a servo drives a rack gear forwards, pushing a marshmallow into the gap between the two motors for propulsion out of the device. In parallel, the x and y servos track the person's face position, delivering the marshmallow into the person's general mouth area. This exceeds the performance of the original robot arm by serving the purpose of aiming and launching, which the original arm is not capable of performing.

**Catapult system**

We experimented with a catapult launching mechanism, prior to the baseball pitching mechanism we have implemented into our design. We decided not to continue with the catapult, as it would take up more space and did not provide adequate acceleration and accuracy. The mechanism worked by stretching 2 springs and placing a backboard behind two servos, once a button is pressed, the two servos turn and the backboard is released forward as the 2 springs tighten and move towards the slit in the design.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/5.jpeg)

**Baseball pitching mechanism (2 power supplies)**

With the baseball pitching mechanism, we first made it work with the use of 2 power supplies - one for each switch. We shortly realised that we do not need to power the 2 motors separately and so we altered the circuit so that both motors can be powered by the same power supply. 

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/6.jpeg)

**Baseball pitching mechanism (1 power supply) with adjustable distance**

We built a wooden structure to support the DC motors where the relative distance between the motors could be adjusted, allowing us to determine the ideal distance between the acceleration wheels. 

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/7%202%20Large.jpeg)

**Feeding system with acrylic pipe, rack and pinion marshmallow engagement mechanism**

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/8.jpeg)

The body of the device was developed from the ground up in Rhino, taking into account the dimensions of the servos, motors, feeder tube, etc. Based on our wooden prototypes, we incorporated the elements we had tested, such as the propulsion wheels, feeding system and feeding tube.

One clear tube (ID 11mm, OD 13mm, acrylic tubing) was added to aid the reloading mechanism. Marshmallows fit snugly into the tube and enter a slot in which the rack gear can push the marshmallow through the two rotating motors.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/9.jpeg)

We then 3D printed the baseball pitching mechanism in alignment with our aim for a robotic design. PLA is less dense than wood and we wanted the prototype to be as light as possible so the servos can move it more easily according to the power output of the servos. 

First 3D printed prototype (green PLA, with 2 slits to slide in the 2 motors with gears attached)

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/10%202%20Large.jpeg)

**Laser pointer (later eliminated)**


We also considered adding a laser pointer to help aim at the mouth during the ML training process but eliminated it due to health and safety concerns.

<img width="538" height="796" alt="Screenshot 2025-11-04 at 19 14 37" src="https://github.com/user-attachments/assets/e40b7ad7-427c-47a6-9644-b403d0277ef3" />![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/11%202%20Large.jpeg)
**Problems with the design**

Launching mechanism weight and friction - the head of the device was too heavy for the servo to move freely. To address this, we cut out sections of the feeder mechanism housing and decreased the surface area of the bearing surfaces in the pivots. This allowed for more efficient power transfer and responsive turning and tilting movements.

**Launching jams and double feeding**

This was addressed by testing various elements. Adjusting the height of the feeding tube in relation to the track the marshmallow was pushed along by the rack gear helped avoid double launches where two marshmallows fell into the feeder chamber. Changing the height and shape of the rack allowed us to block the feeder tube during the launching sequence whilst more reliably presenting the marshmallow to the acceleration wheels. Testing the surface textures of the acceleration wheels helps to increase friction on the marshmallows during launch, allowing the system to reliably grip the marshmallow and also self-clear jams. The top photo shows the wheel with the least friction, as it is smooth, progressing to the wheel with the most friction and grip (bottom photo), which is the one we used in our final project. The middle photo shows the wheel we used; it was better than the top one but it still did not have enough grip for the marshmallows.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/12.jpeg)


## Software design

**Python Script 1 - mouth_detect.py**

This code uses Media Pipe tracking to analyse if a person’s mouth is open or closed based on a video input. It sends values to a local port according to which state is detected.

**Python Script 2 – cam_to_weki.py** 

This code uses Media Pipe to track the xy position of a person’s face based on a video input and sends two values via OSC message that can be processed by Wekinator.

**Python Script 3 – weki_to_arduino.py**

This code converts OSC messages to Serial messages that can be interpreted by Arduino.

**Arduino Sketch 1 – feeding_servo_and_motors**

This sketch controls the DC motors through a dual-H-bridge module and 1 servo that actuates the rack and pinion gears. It receives one input from Python script 1 and runs a launching sequence when it receives a ‘mouth open’ event.

**Arduino Sketch 2 – aiming_servos**

This code controls two servos for the tilting and panning mechanism. It receives a serial code from Wekinator and controls the servos according to the value it receives.

## Hardware design

2 DC motors (3V each)

3 servos (180º)

2 Arduino nanos

4k Logitech webcam + USB-C cable

1 H-bridge

1 5V power board

6 2-pin Molex connectors (male)

9 3-pin Molex connectors (male)

6 2-pin Molex connectors (female)

9 3-pin Molex connectors (female)

12 single core 1mm wires ca. 1m each

1 power bank + USB-A to USB-Micro cable

Acrylic tubing ID 11mm, OD 13mm, 150mm


**Circuit diagram**

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/13.jpeg)

To make the circuits in a manner robust enough to withstand the designed movements of the system, the servos and motor wiring were connected to a small junction board mounted to the box via Molex connectors. Molex-terminated cables, heat-shrunk together, connected the junction board to the main circuitry. All remaining components were soldered to a Veroboard, which is housed inside the wooden base.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/14.jpeg)

This is a diagram displaying the circuit on the Veroboard:

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/15.jpeg)

To make the connections neater, we also added this Veroboard, which have labels S1, S2, S3, M1 and M2, which stand for servos 1,2,3 and motors 1 and 2, respectively. This is also so we can clearly see how each motor/servo is connected when we rebuild the setup and ensure consistent DC motor polarity.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/16.jpeg)

## Justification for Using MediaPipe Face Mesh

We are using Python instead of Processing, specifically the MediaPipe Face Mesh package, to monitor the movement of the mouth. MediaPipe Face Mesh uses a CNN-based model. The Convolutional Neural Networks (CNN) are trained to predict 3D face landmarks (468 key points) from a single RGB image. In this case, we used CNN as neural networks are computational models inspired by the human brain. CNN was designed to recognise patterns and make predictions by processing data through interconnected layers of neurons. In a neural network, each neuron receives inputs, applies weights (trains) and produces an output through an activation function, which is a mathematical function applied to the output of a neuron after the weighted sum of its inputs. The CNN method was initially used in image processing, as CNNs are powerful for feature extraction in structured data, which is why it is very powerful for facial recognition in this project. CNNs also use convolutional layers to detect spatial hierarchies, reducing dimensionality and highlighting important features in data, this helps, as all we have to detect is the mouth opening and nothing else.

Other models mentioned in the lecture are not used as KNN (k-Nearest Neighbours) is too slow and not used for image regression and RF (Random Forest) is not suitable for dense landmark prediction. Another commonly used model, GRU (Gated Recurrent Unit), is a recurrent model, so it is not used since Face Mesh processes single frames independently.

## Machine Learning

We evaluated the performance of the trained Wekinator model by testing the dual-servo base's ability to track faces not used during training. The model was trained using face position data (x, y coordinates) recorded from a webcam, with corresponding servo motor positions as output targets. During evaluation, the arm successfully tracked and aimed at new faces in real time, maintaining smooth motion across the frame. Minor deviations (typically within 5–10% of the target position) occurred when faces moved rapidly or when lighting conditions changed significantly. Performance did not depend on the specific person used during training, confirming that the model learned a general mapping for human face positions rather than overfitting to individual features.

The deviation was calculated using the difference between the desired servo position (corresponding to the face’s location) and the actual servo position commanded by the model. The equation used to calculate this was:

Error = (|Predicted Position - Target Position|/Full Range of Servo Motion ) x 100%

The percentage error was computed separately for both the x and y servo axes. Results showed that the errors in both directions followed the same overall trend, with no significant difference between them. This indicates that the model learned a balanced mapping for horizontal and vertical movement, maintaining consistent accuracy across both axes.

## The Future

**Future accomplishment**

The marshmallow can be directly shot in the mouth without the human trying to catch it.

**Further data collection**

The main source of error seemed to be that the face-tracking was distance-dependent. The maximum reliable operating distance was ca. 1.5m. This could be addressed in the future by exploring different models capable of tracking fewer pixels for smaller data points when a person is further away, as well as testing cameras with a longer focal length. Additionally, depth sensors such as ultrasonic or LIDAR sensors could help determine distance to the person in frame and make the training of the launching trajectory more accurate. 

**Potential gain**

A more accurate measurement of how far away the target is can enhance the aim to make launching directly in the mouth more probable.

**Improvement of ML performance**

If we train using Face Mesh and a distance sensor, the system can have metric 3D positions rather than pixel-only estimates. We can also train a motion predictor to aim slightly ahead of the current mouth position.

**Limitations**

Because marshmallows are quite small and the shape is not quite streamlined, aiming it would be harder than other sweets, but due to safety concerns, we are limited to using marshmallows. Although accuracy and aim can be improved immensely with the use of another sensor, it would still not shoot in the mouth exactly all the time. 
Mouth aperture, head micro-movements, breathing, talking, blinking and reflexive movements are highly variable and sometimes unpredictable. Prediction can reduce but not eliminate this source of error.

## Limitations

**Physics**

Reynolds number (Re)
Re = (characteristic speed × characteristic length) / kinematic viscosity
Re = vL/ν
v = speed of the object through the fluid (m/s)
L = characteristic length (m) — for a marshmallow use diameter 
ν = kinematic viscosity of air (m²/s)
Because the Re for marshmallows is so large, it is in the regime where inertial forces dominate and drag behaviour is not linear with speed. Contrary to projectiles, we cannot safely assume a simple parabolic trajectory with constant horizontal speed. Marshmallows vary in shape, mass, elasticity and surface friction. They deform and can tumble unpredictably in flight - this increases aerodynamic uncertainty compared to rigid projectiles. This makes it very hard to predict its flight trajectory, making aiming it even harder. 

If we could also simulate the design, precise values of the metrics can be mathematically calculated so the velocity of the motors can be adjusted based on eg the different masses of the marshmallows during launching. Motors that change speed according to the mass of the marshmallow can also enhance the aim to make launching directly in the mouth more probable. 

**Marshmallows**

We bought two bags of Waitrose & Partners Cooks Ingredients Mini Pink & White Marshmallows (150g) (https://www.waitrose.com/ecom/products/cooks-ingredients-mini-pink-white-marshmallows/479274-816966-816967?srsltid=AfmBOopxX4-NcZ0MfgPjvwgXtyKXMwVh3HlS8yC_JedqS964UFjpT6UL). 
We soon realised that the pink marshmallows are slightly larger than the white ones and within the white ones, there are smaller ones and larger ones. We sorted the marshmallows into 3 piles - the smallest ones (left) tend to double-fire and the largest ones (right) tend to jam the machine, hence, we are using the medium sized ones (middle). We determined the size by sliding marshmallows down different sized tubes manually. The smallest ones slid through a tube that is slightly smaller than the one in the actual machine and the medium ones slid through one of the same dimensions as the one used in the actual machine.

![Image](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/17.jpeg)


## Videos

**Click the image to play the demo**

[![Watch the demo](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/18.png)](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/18.mp4)

[![Watch the demo](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/19.png)](https://github.com/huhuzou/marshmallow-shooter/raw/main/marshmallow_feeder_images/19.mp4)
