from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n-cls.pt")  # load a pretrained model

# Train the model
results = model.train(data="./datasets/caltech256", epochs=100, imgsz=416)
