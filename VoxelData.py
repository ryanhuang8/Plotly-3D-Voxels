import numpy as np

class VoxelData:
    def __init__(self, voxel_grid):
        self.voxel_grid = voxel_grid
    
    def get_vertices_and_faces(self):
        surface_voxels = self.get_surface_voxels()
        vertices = []
        faces = []
        
        for voxel in surface_voxels:
            x, y, z = voxel
            # Add 8 vertices of the cube
            vertices.extend([
                [x, y, z],
                [x + 1, y, z],
                [x, y + 1, z],
                [x, y, z + 1],
                [x + 1, y + 1, z],
                [x + 1, y, z + 1],
                [x, y + 1, z + 1],
                [x + 1, y + 1, z + 1]
            ])
            # Add 6 faces of the cube
            faces.extend([
                [len(vertices) - 8, len(vertices) - 7, len(vertices) - 5, len(vertices) - 6],
                [len(vertices) - 8, len(vertices) - 7, len(vertices) - 3, len(vertices) - 4],
                [len(vertices) - 8, len(vertices) - 6, len(vertices) - 2, len(vertices) - 4],
                [len(vertices) - 5, len(vertices) - 7, len(vertices) - 3, len(vertices) - 1],
                [len(vertices) - 6, len(vertices) - 5, len(vertices) - 1, len(vertices) - 2],
                [len(vertices) - 4, len(vertices) - 3, len(vertices) - 1, len(vertices) - 2]
            ])
        
        vertices = np.array(vertices)
        faces = np.array(faces)
        
        return vertices, faces
    
    def get_surface_voxels(self):
        surface_voxels = []
        for x in range(0, self.voxel_grid.shape[0] - 1):
            for y in range(0, self.voxel_grid.shape[1] - 1):
                for z in range(0, self.voxel_grid.shape[2] - 1):
                    if self.voxel_grid[x, y, z] == 1:
                        if (self.voxel_grid[x-1, y, z] == 0 or self.voxel_grid[x+1, y, z] == 0 or
                            self.voxel_grid[x, y-1, z] == 0 or self.voxel_grid[x, y+1, z] == 0 or
                            self.voxel_grid[x, y, z-1] == 0 or self.voxel_grid[x, y, z+1] == 0):
                            surface_voxels.append((x, y, z))
        return surface_voxels
