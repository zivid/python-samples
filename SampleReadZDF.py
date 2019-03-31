""" 
Copyright (c) 2019, Zivid AS

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

3. Neither the name of Zivid AS nor the names of its contributors may
   be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY ZIVID AS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ZIVID AS OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""" 

""" 
This example shows how to import a Zivid point cloud from a .ZDF file.

"""

from netCDF4 import Dataset
from matplotlib import pyplot as plt

# Read a .ZDF point cloud. The "Zivid3D.zdf" file has to be in the same folder
# as the "SampleReadZDF" file.
FilenameZDF = 'Zivid3D.zdf'
data = Dataset(FilenameZDF,'r')

# Extract the point cloud
pc = data['data']['pointcloud'][:,:,:]

# Extract the RGB image
image = data['data']['rgba_image'][:,:,:]

# Extract the contrast image
contrast = data['data']['contrast'][:,:]

# Display the RGB image
plt.imshow(image)
plt.show()

# Display the Depth Image
plt.imshow(pc[:,:,2], vmin=0, vmax=1500)
plt.show()

# Close the ZDF file
data.close()