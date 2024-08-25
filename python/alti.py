""" SwissAlti pymesh processing """

import numpy as np
import pymesh
import pymeshlab

# v = np.ndarray(shape=(3,3))
# f = np.zeros(shape=(1,3))
# v[0][:] = (0,0,0)
# v[1][:] = (1,1,1)
# v[2][:] = (2,2,0)
# f[0][:] = (0,1,2)
# print(v,f)
# m = pymesh.form_mesh(v,f)
# m.add_attribute("vertex_area")
# print(m.get_attribute_names())
# print(m.get_attribute("face_area"))

# pymesh.save_mesh("/tmp/test.obj", m, ascii=True)

def build_mesh_from_obj_lines(ms, skipped_v, mv, mf):
    if not mv:
        return []
    v = np.zeros(shape=(len(mv),3), dtype=np.float32)
    f = np.zeros(shape=(len(mf),3), dtype=np.int32)
    for vi in range(len(mv)):
        v[vi][:] = [n for n in mv[vi].split(' ')[1:]]
        #print(v[vi])
    for fi in range(len(mf)):
        f[fi][:] = [n for n in mf[fi].split(' ')[1:]]
        f[fi] -= skipped_v + 1
        #print(f[fi])
    #ms.add_mesh(pymeshlab.Mesh(v,f), set_as_current=False)
    return [pymesh.form_mesh(v,f)]

def read_meshes_from_obj(ms, fn):
    f = open(fn, 'r')
    mv = []
    mf = []
    skipped_v = 0
    added_obj = 0
    res = []
    while True:
        line = f.readline()
        if not line:
            break
        #print(line)
        if line.startswith('g '):
            res += build_mesh_from_obj_lines(ms, skipped_v, mv, mf)
            if len(res) >= 1000:
                return res
            added_obj += 1
            if added_obj % 100 == 0:
                print(added_obj)
            skipped_v += len(mv)
            mv = []
            mf = []
            continue
        if line.startswith('v '):
            mv.append(line)
        if line.startswith('f '):
            mf.append(line)
    res += build_mesh_from_obj_lines(ms, skipped_v, mv, mf)
    f.close()
    return res

ml = read_meshes_from_obj("", '/mnt/n/3d/build/zurich_build.obj')
print (len(ml))
while len(ml) > 1:
    ml2 = []
    for i in range(len(ml)):
        if i == len(ml) - 1:
            ml2.append(ml[i])
            break
        if i % 2 == 1:
            continue
        ml2.append(pymesh.boolean(ml[i], ml[i+1], operation="union", engine='igl'))
        print(len(ml), len(ml2))
    ml = ml2
pymesh.save_mesh("/tmp/test.obj", ml[0], ascii=True)

# pymeshlab.print_pymeshlab_version()
# #pymeshlab.print_filter_list()

# def main ():
#     ms = pymeshlab.MeshSet()
#     #ms.load_new_mesh('/mnt/n/3d/build/zurich_build.fbx')
#     #add_meshes_from_obj(ms, '/mnt/n/3d/build/zurich_build.obj')
#     print(ms.mesh_number())
#     #ms.add_mesh(pymeshlab.Mesh(v,f))
#     #ms.generate_convex_hull()
#     #ms.save_current_mesh('/tmp/test2.obj', save_vertex_normal=False, save_vertex_color=False)

# meshing_decimation_quadric_edge_collapse

# main()
