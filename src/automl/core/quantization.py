# src/automl/core/quantization.py  
import onnxruntime as ort  
import torch.onnx  

class ModelQuantizer:  
    def __init__(self, model, sample_input):  
        self.model = model  
        self.sample_input = sample_input  

    def export_onnx(self, path="model.onnx"):  
        torch.onnx.export(  
            self.model,  
            self.sample_input,  
            path,  
            opset_version=17,  
            dynamic_axes={"input": {0: "batch_size"}}  
        )  

    def optimize_with_tensorrt(self):  
        sess_options = ort.SessionOptions()  
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL  
        return ort.InferenceSession("model.onnx", sess_options)  