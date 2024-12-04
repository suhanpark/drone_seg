import cv2
from djitellopy import tello
from ultralytics import YOLO

def make_onnx():
    model = YOLO("yolo11n-seg.pt")
    model.export(format="onnx")
    
def get_model():
    model = YOLO("yolo11n-seg.onnx")
    return model

def connect_drone():
    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())
    return drone

def segment(drone, model):
    img = drone.get_frame_read().frame
    results = model(img)
    return results

def drone_stream(img, drone):
    drone.send_rc_control(0, 0, 0, 0)
    cv2.imshow("Scene", img)