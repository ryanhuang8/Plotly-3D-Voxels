# Plotly-3D-Voxels

Plotly doesn't have its own grapher/viewer for voxel data (see in references below), which causes issues for visualization. This repo addresses that and provides a fast, visualization tool (takes ~2-5 seconds to render) by converting voxel data into plottable meshes in Plotly.

## Usage

1. Open the `chair.npy.gz` file, which contains a list of chair voxels from ModelNet10. Alternatively, get the path to your .npy/voxel data file
2. In `run.py`, either change the voxel data or keep it as is for demo purposes
3. Run the `run.py` file and navigate to http://127.0.0.1:8050/ on your browser

## Alternative methods/limitations

The plot is a nice approximation as shown here:
![Alt text](example.png?raw=true "Chair")

If you want a better plotting, perhaps check out (takes longer/approx ~5 mins to render): https://github.com/olive004/Plotly-voxel-renderer

## References

- Plotly 3D Mesh Plots: https://plotly.com/python/3d-mesh/
- Inspired by: https://github.com/olive004/Plotly-voxel-renderer
- Chair voxels example obtained from: https://github.com/SomTambe/ModelNet10-dataset
