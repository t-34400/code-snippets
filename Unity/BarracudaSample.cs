using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using Unity.Barracuda;

public class BarracudaSample : MonoBehaviour
{
    private const int BATCH_SIZE = 1;
    private const int NUM_CHANNELS = 1;
    private const int WIDTH = 10;
    private const int HEIGHT = 3;

    private const string INPUT_LABEL = "input_label";

    [SerializeField] private NNModel modelAsset;
    private IWorker worker;

    public BarracudaSample()
    {
        var model = ModelLoader.Load(modelAsset);
        // GPU
        worker = WorkerFactory.CreateWorker(WorkerFactory.Type.ComputePrecompiled, model);
        // CPU
        // worker = WorkerFactory.CreateWorker(WorkerFactory.Type.CSharpBurst, model);
    }

    public float[] Estimate(float[] input_a, float[] input_b)
    {
        var inputs = new Dictionary<string, Tensor>();
        var input_tensor = new Tensor(BATCH_SIZE, WIDTH, HEIGHT, NUM_CHANNELS, InterleaveArray(input_a, input_b));
        inputs[INPUT_LABEL] = input_tensor;

        worker.Execute(inputs);

        var output = worker.PeekOutput();

        float[] result = output.ToReadOnlyArray();

        input_tensor.Dispose();
        inputs.Clear();

        return Softmax(result);
    }

    public void OnDestroy()
    {
        worker?.Dispose();
    }

    private static float[] InterleaveArray(float[] array1, float[] array2)
    {
        if(array1.Length != array2.Length)
        {
            throw new ArgumentException("Arrays must be same length.");
        }

        var length = array1.Length;
        var interleavedArray = new float[length * 2];
        foreach(var i in Enumerable.Range(0, length))
        {
            interleavedArray[i * 2] = array1[i];
            interleavedArray[i * 2 + 1] = array2[i];
        }
        return interleavedArray;
    }

    private static float[] Softmax(float[] input)
    {
        float[] result = new float[input.Length];
        float max = input.Max();

        float sum = 0.0f;
        foreach (int i in Enumerable.Range(0, input.Length))
        {
            result[i] = (float)Math.Exp(input[i] - max);
            sum += result[i];
        }

        foreach (int i in Enumerable.Range(0, input.Length))
        {
            result[i] /= sum;
        }

        return result;
    }
}
