from utils import *

def run():
    model = get_model()

    drone = connect_drone()
    drone.streamon()

    drone.takeoff()
    drone.move_up(50)
    
    while True:
        image = segment(drone, model)
        drone_stream(image, drone)
        
        key = cv2.waitKey(5000)
        if key & 0xFF == ord('q'):
            break


if __name__ == "__main__":    
    run()