// create a basic arc (the foundation of a petal)
to arc(:size, :deg) [
  repeat :deg [
    forward (:size)
    right (1)
  ]
]

// combine two arcs to make a pointed petal
to petal(:size) [
  repeat 2 [
    arc(:size, 60)
    right (120)
  ]
]

// function to draw a full flower of petals
to flower(:size, :petals) [
  repeat :petals [
    petal(:size)
    right (360 / :petals)
  ]
]

to rangoli(:size, :count) [
  if :count == 0 [ return void ] 
    
  flower(:size, 3)     
  right (15)               
  
  rangoli(:size * 2, :count - 1) 
]

rangoli(2, 3)