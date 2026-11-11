expected = """Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g    """

for i, line in enumerate(expected.split('\n')):
    print(f"Line {i:2d}: '{line}'")
    for j, c in enumerate(line):
        print(f"  {j:2d}: '{c}'")
    print()
