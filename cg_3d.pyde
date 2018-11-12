ry = 0





def setup():

    size(800, 800, P3D)

    global obj, texture1

    texture1 = loadImage("Wolf_Body.jpg")

    obj = loadShape("Wolf_obj.obj")



def draw():

    global ry

    background(10, 10, 10)

    lights()



    translate(width / 2, height / 2 + 200, -200)

    rotateZ(PI)

    rotateY(ry)

    scale(400)

    


    directionalLight(0, 102, 255,  # Color

                     1, 0, 0)      # The x-, y-, z-axis direction


    ambientLight(255, 0, 0);

    
    texture(texture1)

    shape(obj)
    texture(texture1)



    ry += 0.02
