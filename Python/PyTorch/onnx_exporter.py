import torch
import torch.onnx

def export_onnx(model, output_filepath):
    model.eval()

    dummy_input_1 = torch.randn(channel, kernel, requires_grad=True).unsqueeze(0).cuda()
    dummy_input_2 = torch.randn(channel, kernel, requires_grad=True).unsqueeze(0).cuda()

    torch.onnx.export(
        model,
        (dummy_input_1, dummy_input_2),
        output_filepath,
        export_params=True,
        opset_version=10,
        do_constant_folding=True,
        input_names=['input_label_1', 'input_label_2'],
        output_names=['output_label_1', 'output_label_2', 'output_label_3'],
        dynamic_axes={
            'input_label_1' : {0 : 'batch_size'},
            'input_label_2' : {0 : 'batch_size'},
            'output_label_1' : {0 : 'batch_size'},
            'output_label_2' : {0 : 'batch_size'},
            'output_label_3' : {0 : 'batch_size'},
        }
    )

    print(" ") 
    print('Model has been successfully converted to ONNX') 
