# qlearn

This code is based on the Q-Learning tutorial originally published by MNEMSTUDIO.ORG

Step-By-Step Tutorial

This tutorial introduces the concept of Q-learning through a simple but comprehensive numerical example. 
The example describes an agent which uses unsupervised training to learn about an unknown environment. 
You might also find it helpful to compare this example with the accompanying source code examples.


Suppose we have 5 rooms in a building connected by doors as shown in the figure below. 
We'll number each room 0 through 4. The outside of the building can be thought of as one big room (5). 
Notice that doors 1 and 4 lead into the building from room 5 (outside).


                                                                                
   *************************************                                        
   *                        *          *                                      
   *                        *          *              5                        
   *                        *          *                                        
   *          0             *          ****     ******************************* 
   *                        *                        *                        * 
   *                        *         1              *                        * 
   *                        *                        *                        * 
   * ***************        *                        *                        * 
   *                        * * *    *****************           2            * 
   *                        *                                                 * 
   *                        *                                                 * 
   *           4            *      3                 *                        * 
   *                                                 *                        * 
   *                                    *************************************** 
   *                        *           *                                       
   *                        *           *                                       
   *      *******************************                                     

      5
      
  
  
 
