from reduceWidth import reduceWidth

def resizeImage(img, params):
#resizes the image
#
#input: img - initial image
#       params - the structure with the needed rules for resizing
#
# output: imgResized - the resized image

    optionResize = params.optionResize

    if optionResize == 'reduceWidth':
        imgResized = reduceWidth(img,params)
            
    elif optionResize == 'reduceHeight':
        #completati aici codul vostru
        print 1
        
    elif optionResize == 'increaseWidth' :
        #completati aici codul vostru
        print 2
        
    elif optionResize == 'increaseHeight':
        #completati aici codul vostru
        print 3
    
    elif optionResize == 'removeObject':
        #completati aici codul vostru 
        print 4

    return imgResized