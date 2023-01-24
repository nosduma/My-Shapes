

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    
    shape = input('Shape?: ').lower()
    if shape=='square' or shape=='pyramid' or shape=='triangle' or shape=='heart':
       return shape
    else:
       return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    height = input('Height?: ')
    if height.isnumeric():
        if int(height) >= 0 or int(height) <80:
            return int(height)
    else:
        return get_height()



# TODO: Step 2
def draw_pyramid(height, outline):
    b=2
    if outline==True:
        for i in range(1,height+1):
            if i == 1 or i + 1 == height+1:
                print(' '*(height-i)+'*'*(i*2-1 ))
                continue
            print(' '*(height-i)+'*' + ' '*(i*2-1-1-1) + '*')
            

    elif outline== False:
        for i in range(1,height+1):
            print(' '*(height-i)+'*'*(i*2-1 ))
    




# TODO: Step 3
def draw_square(height, outline):
    if outline==True:
        for r in range(height):
            for c in range(height):            
                if r==0 or r==height-1 or c==0 or c==height-1:
                    print('*',end='')
                else:
                    print(' ',end='')           
            print()

    elif outline==False:
        for m in range(height):
            print('*'*height)
    

    
    

# TODO: Step 4
def draw_triangle(height, outline):
    if outline==True:
        for r in range(height):
            for c in range(r+1):
                if r==0 or r==height-1 or c==0 or c == height+1 or c==r or c==r+1:
                    print('*',end='')
                else:
                    print(' ',end='')
            print()


    elif outline==False:
        for p in range(height):
            for m in range(p+1):
                print('*',end='')

            print()

    


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape=='pyramid':
        draw_pyramid(height, outline)
    elif shape=='square':
        draw_square(height, outline)
    elif shape=='rectangle':
        draw_rectangle(height, outline)
    elif shape=='heart':
        draw_heart(height, outline)
    elif shape=='nabia':
        draw_nabia(height, outline)
    elif shape=='triangle':
        draw_triangle(height, outline)


    
def draw_heart(shape, height, outline):
    if outline==True:
     a = 6
     b = 7
     for a in range(6):
        for b in range(7):
          if (a==0) and (b%3!=0) or (a==1) and (b%3==0) or (a-b==2) or (a+b==8):
            print('*',end=' ')
        else:
            print(' ',end=' ')
        print()

    elif outline==False:
        print()





def draw_nabia(shape, height, outline):

    for r in range(height):
       for c in range(height-1):
          print('*',end='')
    
    print()





def draw_rectangle(shape, height, outline):
    
    for r in range(height): 
        for c in range(height-3):
            print('*',end='')

    print()



# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline = input("Outline only? (y/N): ").lower()



    if outline=='y': 
        return True
    elif outline== 'n':
        return False
    
    
                                                                                                                                                                                                                                                                                                                                                                             

if __name__ == "__main__":     
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

