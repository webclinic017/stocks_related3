import pandas as pd


def pp(gft,gft2):
    import pandas as pd
    
##    gft2v=pd.concat([gft2,gft],axis=0)
##    pz=gft2v
##    return(pz)
    print(gft2,'33')

    if gft2.shape[0] < 1:
        gft2=gft
        print('babu khan gft2 is 0')
        print(gft2,'34')

    if gft2.shape[0] >= 1:
        gft2=pd.concat([gft2,gft],axis=0)
##        print(gft2,'nn')
        print('bibi')
        print(gft2,'35')
        pz=gft2

